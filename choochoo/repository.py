"""
A module for choochoo project repository management.

Includes the Repository class.
"""
import github
from choochoo import settings, env
from choochoo import issue_template_path
import re

class Repository:
    """ Class for reading repository information.

    It requires a dotenv file which specifies the
    Github Token (as "GH_TOKEN") and Github repository
    (as "GITHUB_REPOSITORY"). 
    """

    def __init__(self):
        self.repo_name = env.repo_name()
        self._token = env._token()
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

    def parse_tickboxes(self):
        """Parse issue data and sum up the number of ticked boxes for each objective.
        Return as a dictionary with each objective as the key and number of ticks as the value."""

        issue_template_content = self.file_content(issue_template_path)
        objectives = re.findall(r'\[ ] (.*?)\|', issue_template_content)
        student_issues = self.student_issues()
        tick_count = dict.fromkeys(objectives,0)

        for issue in student_issues:
            body = issue.body
            for objective in tick_count.keys():
                if objective in body:
                    splits = body.split(objective,maxsplit=2)
                    if splits[0][-4:-1] == '[x]':
                        tick_count[objective] += 1
                else:
                    print("problem: '{}' not in string in issue # {}".format(objective, issue.number))

        return tick_count
