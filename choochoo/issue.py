"""
A module for interacting with an Github repo issue thread.
Contains the Issue class.
"""

import github
from choochoo import objectives

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

    def add_label(self,label):
        #self.pygh_issue.edit(labels=pygh_issue.labels+[github.Label.Label(name=label)])
        self.pygh_issue.add_to_labels(label)

    def remove_label(self, label):
        #self.pygh_issue.edit(pygh_issue.labels.remove(github.Label.Label(name=label)))
        # or use the delete method here? https://pygithub.readthedocs.io/en/latest/github_objects/Label.html#github.Label.Label.delete
        self.pygh_issue.remove_from_labels(label)

    def close_issue(self):
        self.pygh_issue.edit(state='closed')

    def edit_issue_bottom(self,*message):
        message = " ".join(message)
        self.pygh_issue.edit(body=self.pygh_issue.body+"\n"+message)

    def check_label(self,label):
        return label in [label.name for label in self.pygh_issue.get_labels()]

    def tick_log(self):
        """Parse issue data and record which objectives are ticked.
        Return as a dictionary with each objective as the key and a bool value - true for ticked, false for not ticked."""
        
        obj = objectives.Objectives(self.repository)
        tick_log = obj.dict_from_template

        body = self.pygh_issue.body
        for objective in tick_log.keys():
            if objective in body:
                  splits = body.split(objective,maxsplit=2)
                  if splits[0][-4:-1] == '[x]':
                      tick_log[objective]["select"] = True
            else:
                print("problem: '{}' not in string in issue # {}".format(objective, issue.number))

        return tick_log

    def unticked_objectives_list(self):

        return [item[0] for item in self.tick_log.items() if item[1]["select"] == False]



