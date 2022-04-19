"""A simple command line interface for choochoo.

Contains the single function `issue_interface`.
"""
import github
import re
from sys import argv

from choochoo import repository, issue, settings, env, plot, objectives

def issue_interface():
  """ This function interfaces between the user and the choochoo package.
  Choochoo receives and sends messages using comments on a Github issue thread.
  
  It takes a user sub-command and parses it as a complete sentence. 
  It matches this sentence to one within a pre-defined list, 
  and then calls other choochoo functions as appropriate. 
  If it cannot find a match then an error message is returned to the user.
  """

  no_permission_message = "**[checks ticket]** You do not have permission to run this command."
  wrong_command_message = """I'm sorry I don't recognise the command `{0}`.
      To list all available choochoo commands use `choochoo print commands`."""

  repo = repository.Repository()
  issue_number = env.issue_number()
  issue_thread = issue.Issue(repo,issue_number)
  
  user_settings = settings.Settings()
  
  user_input_list = argv[1:]
  user_input = ' '.join(argv[1:])
  author = env.github_actor()
  
  student_commands = []
  
  # returns true if the command string matches the argument string
  input_matches = lambda string: bool(re.match(string, user_input))
  
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
    else:
      issue_thread.make_comment(no_permission_message)

  elif input_matches("add (@[\w-]+) as instructor"):
    handle = user_input_list[1]
    if user_settings.check_instructor(author) \
    or user_settings.check_admin(author):
      user_settings.add_instructors([handle[1:]])
    else:
      issue_thread.make_comment(no_permission_message)

  elif input_matches("add (@[\w-]+) as admin"):
    handle = user_input_list[1]
    if user_settings.check_admin(author):
      user_settings.add_admins([handle[1:]])
    else:
      issue_thread.make_comment(no_permission_message)

  elif input_matches("remove (@[\w-]+) as student"):
    handle = user_input_list[1]
    if user_settings.check_instructor(author) \
    or user_settings.check_admin(author):
      user_settings.remove_students([handle[1:]])
    else:
      issue_thread.make_comment(no_permission_message)

  elif input_matches("remove (@[\w-]+) as instructor"):
    handle = user_input_list[1]
    if user_settings.check_instructor(author) \
    or user_settings.check_admin(author):
      user_settings.remove_instructors([handle[1:]])
    else:
      issue_thread.make_comment(no_permission_message)

  elif input_matches("remove (@[\w-]+) as admin"):
    handle = user_input_list[1]
    if user_settings.check_admin(author):
      user_settings.remove_admins([handle[1:]])
    else:
      issue_thread.make_comment(no_permission_message)
      
  elif input_matches("list people"):
    """ prints out a list of all admins, instructors and students """
    issue_thread.make_comment("Choochoo admins: ", user_settings.admins, 
      "\n", "Choochoo instructors: ", user_settings.instructors, 
      "\n", "Choochoo students: ", user_settings.students)
    
  elif input_matches("build checklist"):
    """Convert objectives.yml into the choochoo-student-thread.md.
    Bonus would be if it checks for broken links when building."""
    if user_settings.check_admin(author):
      objectives.generate_student_thread()
      issue_thread.make_comment("ChooChoo! Checklist has been built")
    else:
      issue_thread.make_comment(no_permission_message)

  elif input_matches("summarise class progress"):
    """Update a webpage displaying class progress. 
    Print a link to this webpage on the thread.
    Also print summary data useful for teaching to issue thread"""
    if user_settings.check_instructor(author) \
    or user_settings.check_admin(author):
      tick_count = repo.parse_tickboxes()
      plot.create_plot(tick_count)
      issue_thread.make_comment("The summary plot has been generated:","\n",
        "![](../raw/{}/plots/summary_plot.png)".format(user_settings.choochoo_branch))
    else:
      issue_thread.make_comment(no_permission_message)

  elif input_matches("generate (@[0-9]+) questions"):
    """Generate a webpage with a random selection of X
    questions from the unticked boxes.
    Print a link to the webpage on the thread."""
    # number_of_questions = 
    pass

  elif input_matches("generate (@[0-9]+) questions for objectives (@[0-9]+)"):
    """Generate a webpage with a random selection of X
    questions from a given subset of objectives.
    Print a link to the webpage on the thread."""
    # number_of_questions = 
    pass

  elif input_matches("vote yes for question ([\w]+.yml)"):
    """Add a yes vote to one of the proposed questions"""
    pass
  
  elif input_matches("bank question"):
    """Append question from the thread number specified to the question bank"""
    if user_settings.check_admin(author):
        pass
    else:
        issue_thread.make_comment(no_permission_message)

  elif input_matches("summarise voting"):
    """Generate a webpage with a list of proposed questions
    and the votes for/against.
    Print a link to the webpage on the thread."""
    pass

  elif input_matches("add question ([\w]+.yml) to objective (@[0-9]+)"):
    """If question still proposed then move it to accepted.
    Add question to the specified objective."""
    pass

  elif input_matches("add link ([\w]+.ipynb) to objective (@[0-9]+)"):
    """Add link to the specified objective."""
    pass

  elif input_matches("add tutorial ([\w]+.ipynb) to objective (@[0-9]+)"):
    """Add tutorial to the specified objective."""
    pass

  elif command_matches("print commands"):
    pass
    
  else:
    issue_thread.make_comment(wrong_command_message.format(command))
 
def check_instructor():
    handle = argv[1]
    if settings.Settings().check_instructor(handle) is False:
        repo = repository.Repository()
        number = env.issue_number()
        issue_thread = issue.Issue(repo,number)
        issue_thread.make_comment("[Checks ticket] I'm closing this issue as",handle,"is not listed as an instructor in settings.yml.")
        issue_thread.close_issue()

def check_student():
    handle = argv[1]
    if settings.Settings().check_student(handle) is False:
        repo = repository.Repository()
        number = env.issue_number()
        issue_thread = issue.Issue(repo,number)
        issue_thread.make_comment("[Checks ticket] I'm closing this issue as",handle, \
                       "is not listed as an student in settings.yml.")
        issue_thread.close_issue()
