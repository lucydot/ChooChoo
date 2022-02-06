"""
A module for reading from, and writing to, the issues tracker on a choochoo repo.
"""
import github
from choochoo import management



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

    def make_comment(self,*message):
        message = " ".join(message)
        self.pygh_issue.create_comment(message)

    def close_issue(self):
        self.pygh_issue.edit(state='closed')