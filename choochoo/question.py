import re
from choochoo import repository, issue
from choochoo import question_bank_path

class Question():
  
  def __init__(self,dictionary):
    
    self.repository = repository.Repository()
    self.dictionary = dictionary
    self.authors = self.dictionary["authors"]
    self.title = self.dictionary["title"]
    self.question = self.dictionary["question"]
    self.answer = self.dictionary["answer"]
    self.checklist_items = self.dictionary["checklist_items"]
    
    @classmethod
    def from_issue(cls,issue_number):
        issue_body = issue.Issue(self.repository,issue_number).pygh_issue.body
        dictionary = dict()
        dictionary["question"] = re.match("Question\\n\\n(?s)(.*)\\n\\n### Answer",issue_body)
        dictionary["answer"] = re.match("Answer\\n\\n(?s)(.*)\\n\\n### Checklist",issue_body)
        dictionary["title"] = re.match("Title\\n\\n(?s)(.*)\\n\\n### Question",issue_body)
        dictionary["authors"] = re.match("Authors\\n\\n(?s)(.*)\\n\\n### Title",issue_body)
        dictionary["checklist_items"] = re.findall("\[X\] (?s)(.*?)\\r\\n",issue_body)
        return cls(dictionary)
      
    @classmethod
    def from_question_bank(cls,title):
        bank_file = self.repository.pygh_repo.get_contents(question_bank_path, ref="main")
        question_bank_string = bank_file.decoded_content.decode()
        question_bank_dictionary = yaml.safe_load(question_bank_string)
        dictionary = next((item for item in question_bank_dictionary if item["title"] == title), None)
        return cls(dictionary)
                                                                        
    def bank_question(self):
        # check name not already in dict
        pass
      
