"""
A module for choochoo project repository management.

Includes the Repository class.
"""
import github
from choochoo import issue, objectives


class Repository:
    """ Class for reading repository information.

    It requires an env which specifies the
    Github Token (as "GH_TOKEN") and Github repository
    (as "GITHUB_REPOSITORY"). 

    It uses pygithub to create a pygithub repository object.
    """

    def __init__(self,env):
        self.repo_name = env.repo_name
        self._token = env._token
        self.pygh_repo = self.pygh_repo()

    def pygh_repo(self):
        "Get a repo object using PyGithubAPI"
        g = github.Github(self._token)
        return g.get_repo(self.repo_name)

    def student_issues(self):
        "Find open student issues in the repo"
        return self.pygh_repo.get_issues(labels=['student'],state='open')

    def issue(self,number=None,creator=None):
        "Find an issue by number or issue creator"
        return self.pygh_repo.get_issues(number=number,
            creator=creator)
    
    def file_content(self,filepath):
        "return content of specified file"
        return self.pygh_repo.get_contents(filepath).decoded_content.decode()

    def total_tick_count(self):
        """Parse all issue data and sum up the number of ticked boxes for each objective.
        Return as a dictionary with each objective as the key and number of ticks as the value."""

        student_issues = self.student_issues()

        obj = objectives.Objectives(self)

        total_tick_count = obj.dict_from_template

        for student_issue in student_issues:

            student_issue = issue.Issue(self,student_issue.number)

            tick_log = student_issue.tick_log()

            for objective, value in tick_log.items():
                if value["select"] is True:
                    total_tick_count[objective]["select"] += 1

        return total_tick_count
