"""
A module for reading from, and writing to, the issues tracker on a choochoo repo.
"""
import github
from choochoo import management

def issue_number():
    dotenv.load_dotenv()
    return os.getenv("ISSUE_NUMBER")

class Issue:
    """Class for holding, reading from and writing to a
    repository issue.
    """

    def __init__(self,
                 repository,
                 number):

        self.repository = repository
        self.number = number
        self.pygh_issue = self.repository.pygh_repo.get_issue(self.number)


    def make_comment(*message):
        message = " ".join(message)
        self.pygh_issue.create_comment(message)

    def close_issue():
        self.pygh_issue.edit(state=closed)