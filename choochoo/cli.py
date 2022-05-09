"""A simple command line interface for choochoo.

Contains the single function `issue_interface`.
"""
import github
import re
from sys import argv
import random

from choochoo import repository, issue, settings, environment, plot, objectives, question, question_bank, paths

def issue_interface():
    """ This function interfaces between the user and the choochoo package.
    Choochoo receives and sends messages using comments on a Github issue thread.
    
    It takes a user sub-command and parses it as a complete sentence. 
    It matches this sentence to one within a pre-defined list, 
    and then calls other choochoo functions as appropriate. 
    If it cannot find a match then an error message is returned to the user.
    """

    env = environment.Env()
    repo = repository.Repository(env)

    issue_thread = issue.Issue(repo,env.issue_number)
    obj = objectives.Objectives(repo)
    qbank = question_bank.QuestionBank(repo)
    user_settings = settings.Settings(repo)

    author = env.github_actor
    user_input_list = argv[1:]
    user_input = ' '.join(argv[1:])

    check_participant(author=author)  # check again if student, admin or instructor.
    
    # returns true if the command string matches the argument string
    input_matches = lambda string: bool(re.match("^"+string+"$", user_input))
    
    if input_matches("check (@[\w-]+) is instructor"):    
        handle = user_input_list[1]
        if user_settings.check_instructor(handle):
            issue_thread.make_comment(handle," is an instructor")
        else:
            issue_thread.make_comment(handle," is not an instructor")
      
    elif input_matches("check (@[\w-]+) is admin"):
        handle = user_input_list[1]
        if user_settings.check_admin(handle):
            issue_thread.make_comment(handle," is an admin")
        else:
            issue_thread.make_comment(handle," is not an admin")
        
    elif input_matches("check (@[\w-]+) is student"):
        handle = user_input_list[1]
        if user_settings.check_student(handle):
            issue_thread.make_comment(handle," is a student")
        else:
            issue_thread.make_comment(handle," is not a student")

    elif input_matches("add (@[\w-]+) as student"):
        handle = user_input_list[1]
        if user_settings.check_instructor(author) \
        or user_settings.check_admin(author):
            user_settings.add_students([handle[1:]])
            issue_thread.make_comment(handle, " is now a student. Choo-choo!")
        else:
           issue_thread.make_comment(no_permission_message)

    elif input_matches("add (@[\w-]+) as instructor"):
        handle = user_input_list[1]
        if user_settings.check_instructor(author) \
        or user_settings.check_admin(author):
           user_settings.add_instructors([handle[1:]])
           issue_thread.make_comment(handle, " is now an instructor. Choo-choo!")
        else:
           issue_thread.make_comment(no_permission_message)

    elif input_matches("add (@[\w-]+) as admin"):
        handle = user_input_list[1]
        if user_settings.check_admin(author):
            user_settings.add_admins([handle[1:]])
            issue_thread.make_comment(handle, " is now an admin. Choo-choo!")
        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("remove (@[\w-]+) as student"):
        handle = user_input_list[1]
        if user_settings.check_instructor(author) \
        or user_settings.check_admin(author):
            user_settings.remove_students([handle[1:]])
            issue_thread.make_comment(handle, " is no longer a student. Bye-bye!")
        else:
           issue_thread.make_comment(no_permission_message)

    elif input_matches("remove (@[\w-]+) as instructor"):
        handle = user_input_list[1]
        if user_settings.check_instructor(author) \
        or user_settings.check_admin(author):
            user_settings.remove_instructors([handle[1:]])
            issue_thread.make_comment(handle, " is no longer an instructor. Bye-bye!")
        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("remove (@[\w-]+) as admin"):
        handle = user_input_list[1]
        if user_settings.check_admin(author):
            user_settings.remove_admins([handle[1:]])
            issue_thread.make_comment(handle, " is no longer an admin. Bye-bye!")
        else:
            issue_thread.make_comment(no_permission_message)
        
    elif input_matches("list people"):
        """ prints out a list of all admins, instructors and students """
        issue_thread.make_comment("🚂 Admins: ", user_settings.admins, 
          "\n", "🚂 Instructors: ", user_settings.instructors, 
          "\n", "🚂 Students: ", user_settings.students)
        
    elif input_matches("build checklists"):
        """Convert objectives.yml into the choochoo-student-thread.md
        and the choochoo-question-thread.yml.
        Bonus would be if it checks for broken links when building."""
        if user_settings.check_admin(author):
            obj.generate_student_thread()
            if user_settings.questions:
                obj.generate_question_thread()
            issue_thread.make_comment("ChooChoo! Checklist(s) have been built")
        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("summarise class progress"):
        """Update a webpage displaying class progress. 
        Print a link to this webpage on the thread.
        Also print summary data useful for teaching to issue thread"""
        if user_settings.check_instructor(author) \
        or user_settings.check_admin(author):
            total_tick_count = repo.total_tick_count()
            plot.create_plot(repo,total_tick_count)
            issue_thread.make_comment("The summary plot has been generated:","\n",
              "![](../raw/{}/plots/summary_plot.png)".format(user_settings.choochoo_branch))
        else:
           issue_thread.make_comment(no_permission_message)

    elif input_matches("generate ([1-9][0-9]*) questions"):
        """Generate a webpage with a random selection of [positive integer]
        questions from the unticked boxes.

        The name of the webpage corresponds to the username of the author.

        Building this page triggers a github action to deploy on the gh_pages branch.

        On completion a link to the webpage is posted on the thread (there may be a slight delay in deployment)."""

        if issue_thread.check_label("student"):
            number_qs = int(user_input_list[1])
            objectives_list = issue_thread.unticked_objectives_list()
            questions_list = qbank.questions_from_objectives_list(objectives_list)
            random_questions = random.sample(questions_list,number_qs)
            qbank.build_user_markdown(random_questions,author)
            issue_thread.make_comment("All aboard! Your personalised webpage has been generated at "+
                "[{0}]({0})".format(user_settings.web_address+"/"+paths.question_folder_path+author))
          
        else:
            issue_thread.make_comment("Halt! You can only run this command in a choochoo student thread")


    elif input_matches("generate ([1-9][0-9]*) questions for objectives ([0-9 ]+)"):
        """Generate a webpage with a random selection of X
        questions from a given subset of objectives.

        The name of the webpage corresponds to the username of the author.

        Building this page triggers a github action to deploy on the gh_pages branch.

        On completion a link to the webpage is posted on the thread (there may be a slight delay in deployment)."""
        if issue_thread.check_label("student"):
            number_qs = int(user_input_list[1])
            id_list = [int(item) for item in user_input_list[5:]]
            objectives_list = obj.objectives_list_by_id(id_list)
            questions_list = qbank.questions_from_objectives_list(objectives_list)
            if len(questions_list) >= number_qs:
                random_questions = random.sample(questions_list,number_qs)
            else:
                issue_thread.make_comment("""Uh-oh - the number of questions requested exceeds the number 
                    available for these objectives.\n Building a question page with {} questions.""".format(len(questions_list)))
                random_questions = questions_list
            qbank.build_user_markdown(random_questions,author)
            issue_thread.make_comment("All aboard! Your personalised webpage has been generated at "+
                "["+user_settings.web_address+"/"+paths.question_folder_path+author+".md]("+
                user_settings.web_address+"/"+paths.question_folder_path+author+")")

        else:
            issue_thread.make_comment("Halt! You can only run this command in a choochoo student thread")


    elif input_matches("vote up"):
        """Add a yes vote to one of the proposed questions.

        You are not allowed to vote for your own proposed question.
        """
        print(author)
        print(issue_thread.pygh_issue.user.name)
        if issue_thread.check_label("question proposal") and \
          author is not issue_thread.pygh_issue.user.name:
              proposed_question = question.Question.from_issue(issue_thread)
              proposed_question.upvote(author)
              issue_thread.make_comment("Your vote has been registered ☑️")
        else:
              issue_thread.make_comment("""There are two rules for voting: 1) run the `choochoo vote up`
              command in the question proposal issue thread; 2) you can't vote for your own question!
              """)
      
    
    elif input_matches("bank question"):
        """Append question from the thread number specified to the question bank.

        Edit the labels to show that the question has been accepted."""
        if issue_thread.check_label("accepted question"):
            issue_thread.make_comment("Oh dear! You cannot bank a question that has already been accepted.")
        if user_settings.check_admin(author) and issue_thread.check_label("question proposal"):
            if question.Question.from_issue(issue_thread).in_bank is True:
                issue_thread.make_comment("Oh dear! A question with this title is already in the bank")

            else:
                question.Question.from_issue(issue_thread).bank_question()  # change this to initalise from the issue_thread rather than number?
                issue_thread.remove_label("question proposal")
                issue_thread.add_label("accepted question")
                issue_thread.make_comment("The question has been banked 💰")
            
        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("build question bank"):
        """ Build a html page containing all questions in the question bank.

        The page uses anchor links so that individual questions can be accessed. 

        Building this page triggers a github action to deploy on the gh_pages branch."""
        
        if user_settings.check_admin(author):
            qbank.build_bank_markdown()
            issue_thread.make_comment("The question bank is building and will soon be available at [{0}]({0})".format(user_settings.web_address+"/"+paths.question_bank_path))
        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("summarise voting"):
        """Generate a webpage with a list of proposed questions
        and the votes for/against.
        Print a link to the webpage on the thread."""
        pass

    elif input_matches("add question (.+) to objective ([1-9]+)"):
        """If question still proposed then move it to accepted.
        Add question to the specified objective."""
        if user_settings.check_admin(author):
            question_link = user_input_list[2]
            objective_number = int(user_input_list[5])
            objective_name = obj.objectives_list_by_id([objective_number])[0]
            current_dict = obj.dict_from_yaml
            for i, section in enumerate(current_dict['sections']):
                for j, objective in enumerate(section["objectives"]):
                    if objective["name"] == objective_name:
                        current_dict['sections'][i]['objectives'][j]["questions"].append(question_link)
                        obj.dict_to_yaml(current_dict)
                        issue_thread.make_comment("Question link {} has been added to the objective \"{}\"".format(question_link,objective_name))
                        break

        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("add link (.+) to objective ([1-9]+)"):
        """Add link to the specified objective."""
        if user_settings.check_admin(author):
            link = user_input_list[2]
            objective_number = int(user_input_list[5])
            objective_name = obj.objectives_list_by_id([objective_number])[0]
            current_dict = obj.dict_from_yaml
            for i, section in enumerate(current_dict['sections']):
                for j, objective in enumerate(section["objectives"]):
                    if objective["name"] == objective_name:
                        current_dict['sections'][i]['objectives'][j]["links"].append(link)
                        obj.dict_to_yaml(current_dict)
                        issue_thread.make_comment("Link {} has been added to the objective \"{}\"".format(link,objective_name))
                        break
        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("add tutorial (.+) to objective ([1-9]+)"):
        """Add tutorial to the specified objective."""
        if user_settings.check_admin(author):
            tutorial_link = user_input_list[2]
            objective_number = int(user_input_list[5])
            objective_name = obj.objectives_list_by_id([objective_number])[0]
            current_dict = obj.dict_from_yaml
            for i, section in enumerate(current_dict['sections']):
                for j, objective in enumerate(section["objectives"]):
                    if objective["name"] == objective_name:
                        current_dict['sections'][i]['objectives'][j]["tutorials"].append(tutorial_link)
                        obj.dict_to_yaml(current_dict)
                        issue_thread.make_comment("Tutorial link {} has been added to the objective \"{}\"".format(tutorial_link,objective_name))
                        break
        else:
            issue_thread.make_comment(no_permission_message)

    elif input_matches("list commands"):
        if user_settings.check_admin(author):
            issue_thread.make_comment(admin_commands_message)
        elif user_settings.check_instructor(author):
            issue_thread.make_comment(instructor_commands_message)
        elif user_settings.check_student(author):
            issue_thread.make_comment(student_commands_message)
        else:
            issue_thread.make_comment(no_permission_message)
      
    else:
        issue_thread.make_comment(wrong_command_message.format(user_input))

no_permission_message = "**[checks ticket]** You do not have permission to run this command."

wrong_command_message = """I'm sorry I don't recognise the command `{0}`.
    To list all available choochoo commands use `choochoo list commands`."""

student_commands_message = """
`choochoo list people` \n
`choochoo check [@handle] is [student/admin/instructor]` \n
`choochoo generate [positive integer] questions` \n
`choochoo generate [positive integer] questions for objectives [positive integers with spaces]` \n \n
❓ The following command can be used in a issue thread labelled `question proposal`: \n
`choochoo vote up` \n

"""

admin_commands_message = """
🧑‍🤝‍🧑 People management: \n 
`choochoo list people` \n
`choochoo check [@handle] is [student/admin/instructor]` \n
`choochoo add [@handle] as [student/admin/instructor]` \n
`choochoo remove [@handle] as [student/admin/instructor]` \n
☑️ Checklist management and monitoring: \n
`choochoo build checklists` \n
`choochoo add question [web address] to objective [positive integer]` \n
`choochoo add link [web address] to objective [positive integer]` \n
`choochoo add tutorial [web address] to objective [positive integer]` \n
`choochoo summarise class progress` \n \n
`choochoo build question bank` \n \n
❓ The following command can be used in a issue thread labelled `question proposal`: \n
`choochoo vote up` \n
`choochoo bank question` \n \n
👩🏽‍🎓 The following command can be used in a issue thread labelled `student`: \n
`choochoo generate [positive integer] questions` \n
`choochoo generate [positive integer] questions for objectives [positive integers with spaces]` \n
"""

instructor_commands_message = """
🧑‍🤝‍🧑 People management: \n 
`choochoo list people` \n
`choochoo check [@handle] is [student/admin/instructor]` \n
`choochoo add [@handle] as [student/instructor]` \n
`choochoo remove [@handle] as [student/instructor]` \n
☑️ Checklist monitoring: \n
`choochoo summarise class progress` \n \n
❓ The following command can be used in a issue thread labelled `question proposal`: \n
`choochoo vote up` \n \n
👩🏽‍🎓 The following command can be used in a issue thread labelled `student`: \n
`choochoo generate [positive integer] questions` \n
`choochoo generate [positive integer] questions for objectives [positive integers with spaces]` \n
"""
 
def check_instructor(author=None):
    if author:
        handle = author
    else:
        handle = argv[1]
    env = environment.Env()
    repo = repository.Repository(env)
    if settings.Settings(repo).check_instructor(handle) is False and settings.Settings(repo).check_admin(handle) is False:
        issue_thread = issue.Issue(repo,env.issue_number)
        issue_thread.make_comment("[Checks ticket] I'm closing this issue as",handle,"is not listed as an or admin or instructor in settings.yml.")
        issue_thread.close_issue()

def check_participant(author=None):
    if author:
        handle = author
    else:
        handle = argv[1]
    env = environment.Env()
    repo = repository.Repository(env)
    if settings.Settings(repo).check_student(handle) is False and settings.Settings(repo).check_admin(handle) is False and settings.Settings(repo).check_instructor(handle) is False:
        issue_thread = issue.Issue(repo,env.issue_number)
        issue_thread.make_comment("[Checks ticket] I'm closing this issue as",handle, \
                       "is not listed as a student, admin or instructor in settings.yml.")
        issue_thread.close_issue()


