""" A module containing the Question class.
"""

import re
import yaml
from choochoo import question_bank, question_bank_yml_path
from choochoo import settings

class Question:
    """ A class for holding and editing information about a Choochoo question.

    Note that the title of each choochoo question must be unique or it cannot be added to the bank.

    Can be initialised using the class methods `from_question_bank` or
    'from_issue'.

    Proposed questions have an associated open issue thread.

    Accepted questions are in the questions bank and have an associated closed issue thread.
    """
  
    def __init__(self,dictionary):
    
        
        self.dictionary = dictionary
        self.repository = self.dictionary["repository"]
        self.authors = self.dictionary["authors"]
        self.title = self.dictionary["title"]
        self.question = self.dictionary["question"]
        self.answer = self.dictionary["answer"]
        self.checklist_items = self.dictionary["checklist_items"]
        self.status = self.dictionary["status"]
        if self.status == 'proposed':
            # assuming here that if the question is proposed it is created via issue thread
            self.votes = self.dictionary["votes"]
            self.issue = self.dictionary["issue"]

    def upvote(self,voter):
        user_settings = settings.Settings(self.repository)
        self.votes += 1
        if self.votes == 1:
            self.issue.edit_issue_bottom("\n \n")
        self.issue.edit_issue_bottom("✨ @{} has up-voted! **Total votes:** {}".format(voter,self.votes))
        votes_required = user_settings.votes_required
        if self.votes == votes_required:
            self.issue.make_comment("📢 Calling all admins! This question may be ready for acceptance 📢", "\n",
                " ".join(user_settings.at_admins()))
    
    @classmethod   
    def from_issue(cls,issue):  # this shouldn't be used if the question is in the bank as assumes it is proposed
        dictionary = dict()
        dictionary["issue"] = issue
        dictionary["repository"] = issue.repository
        issue_body = dictionary["issue"].pygh_issue.body
        dictionary["question"] = re.search("Question(?s)(.*)### Answer",issue_body).group(1).strip()
        dictionary["answer"] = re.search("Answer(?s)(.*)### Checklist",issue_body).group(1).strip()
        dictionary["title"] = re.search("Title(?s)(.*)### Question",issue_body).group(1).strip()
        dictionary["authors"] = re.search("Authors(?s)(.*)### Title",issue_body).group(1).strip().split()
        dictionary["checklist_items"] = [item.strip() for item in re.findall("\[X\](.*?)\\n",issue_body)]
        dictionary["status"] = 'proposed'
        try:
            dictionary["votes"] = int(re.findall("votes:.*([1-9]\d*)",issue_body)[-1]) # find final value
        except IndexError:
            dictionary["votes"] = 0

        return cls(dictionary)
      
    @classmethod
    def from_question_bank(cls,title,repository):
        dictionary_list = question_bank.QuestionBank(repository).get_dictionary_list()
        dictionary = next((item for item in dictionary_list if item["title"] == title), None)
        dictionary["status"] = 'accepted'
        dictionary["repository"] = repository

        return cls(dictionary)

    def in_bank(self):

        return self.title in question_bank.QuestionBank(self.repository).get_question_titles()
                                                                        
    def bank_question(self):

        dictionary_list = question_bank.QuestionBank(self.repository).get_dictionary_list()
        dictionary_list.append({"authors":self.authors,"title":self.title,"question":self.question,"answer":self.answer,"checklist_items":self.checklist_items})
        with open(question_bank_path, 'w') as stream:
            yaml.dump(dictionary_list, stream)
      
