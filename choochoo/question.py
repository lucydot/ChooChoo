import re
import yaml
from choochoo import repository, issue, env, question_bank
from choochoo import question_bank_path

class Question():
  
    def __init__(self,dictionary):
    
        self.repository = repository.Repository()
        self.dictionary = dictionary
        self.authors = self.dictionary["authors"]
        # the title needs to be unique
        self.title = self.dictionary["title"]
        self.question = self.dictionary["question"]
        self.answer = self.dictionary["answer"]
        self.checklist_items = self.dictionary["checklist_items"]
        self.votes = 0

    def upvote(self):
        self.votes += 1
        # edit the issue thread so that vote count increases by 1
        votes_required = settings.Setttings().votes_required
        if self.votes == votes_required:
            # ping the admins in the issue thread asking them to accept the question
            pass
    
    @classmethod
    def from_issue(cls,issue_number):
        issue_body = issue.Issue(repository.Repository(),issue_number).pygh_issue.body
        dictionary = dict()
        dictionary["question"] = re.search("Question\\r\\n\\r\\n(?s)(.*)\\r\\n\\r\\n### Answer",issue_body).group(1).replace('\r', '')
        dictionary["answer"] = re.search("Answer\\r\\n\\r\\n(?s)(.*)\\r\\n\\r\\n### Checklist",issue_body).group(1).replace('\r', '')
        dictionary["title"] = re.search("Title\\r\\n\\r\\n(?s)(.*)\\r\\n\\r\\n### Question",issue_body).group(1)
        dictionary["authors"] = re.search("Authors\\r\\n\\r\\n(?s)(.*)\\r\\n\\r\\n### Title",issue_body).group(1).split()
        dictionary["checklist_items"] = re.findall("\[X\] (?s)(.*?)\\r\\n",issue_body)
        return cls(dictionary)
      
    @classmethod
    def from_question_bank(cls,title):
        question_bank_dictionary = question_bank.Question_bank().get_dictionary()
        dictionary = next((item for item in question_bank_dictionary if item["title"] == title), None)
        dictionary['question'] = dictionary['question'][:-1]
        dictionary['answer'] = dictionary['answer'][:-1]
        return cls(dictionary)

    def in_bank(self):
        question_bank_dictionary = question_bank.Question_bank().get_dictionary()
        return 'title' in question_bank_dictionary and self.title == question_bank_dictionary['title']
                                                                        
    def bank_question(self):

        # move the question to the question bank
        # change the tag on the issue thread to say "accepted question"
        pass
      
