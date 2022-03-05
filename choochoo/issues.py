"""
A module for interacting with an Github repo issue thread.
Contains the Issue class.
"""

import github

class Issue:
    """Class for interacting with an Github repo issue thread.
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
