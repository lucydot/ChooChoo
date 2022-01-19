"""
A module for choochoo project repository management.

A collection of admin functions and the Repository class.
"""
import github
import dotenv 

from choochoo import settings

class Repository:
    """ Class for reading repository information.

    It requires a dotenv file which specifies the
    Github Token (as "GH_TOKEN") and Github repository
    (as "GITHUB_REPOSITORY"). 
    """

    def __init__(self):
        self.repo_name = self.repo_name
        self.pygh_repo = self.pygh_repo()

    def _token(self):
        "Get gh token, needed for the PyGithub API"
        dotenv.load_dotenv()
        return os.getenv("GH_TOKEN")

    def repo_name(self):
        "Get repository in name/repo format"
        dotenv.load_dotenv()
        return os.dotenv("GITHUB_REPOSITORY")

    def pygh_repo(self):
        "Get a repo object using PyGithubAPI"
        token = self._token()
        repo_name = self.repo_name()
        g = github.Github(token)
        return g.get_repo(repo_name)

    def student_issues(self,since=None):
        "Find student issues in the repo"
        return self.pygh_repo.get_issues(labels=
            [student],since=since)

    def issue(number=None,creator=None):
        "Find an issue by number or issue creator"
        return self.pygh_repo.get_issues(number=number,
            creator=creator)
        
def check_instructor(handle: str) --> bool:
    return handle in settings.Settings.instructors 

def check_admin(handle: str) --> bool:
    return handle in settings.Settings.admins 

def check_student(handle: str) --> bool:
    return handle in settings.Settings.students
