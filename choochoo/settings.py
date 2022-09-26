"""
A module for reading and writing to the settings yml file.
"""

import yaml  # Pyyaml
from typing import List # this is not needed for Python3.9+
from choochoo import settings_path

class Settings:
    """Class for reading and writing to the settings yml file.

      The settings file is downloaded from the online repository
      (rather than a local installed copy).
    """
    def __init__(self,repository):

        self.repository = repository
        self.path = settings_path
        self._dictionary = self.load_dictionary()  
        self._project_title = self.dictionary["project_title"]
        self._admins = self.dictionary["admins"]
        self._instructors = self.dictionary["instructors"]
        self._students = self.dictionary["students"]
        self.gh_pages_branch = self.dictionary["gh-pages_branch"]
        self.gh_pages = self.dictionary["gh-pages"]
        self.questions = self.dictionary["questions"]
        self.votes_required = self.dictionary["votes_required"]
        self.web_address = self.dictionary["web_address"]

    @property
    def dictionary(self):
        return self._dictionary

    def load_dictionary(self):  
        settings_string = self.repository.file_content(self.path)
        return yaml.safe_load(settings_string)
  
    def write_dictionary(self):   
        with open(self.path, 'w') as stream:
            yaml.dump(self._dictionary, stream)

    @property
    def project_title(self):
        return self._project_title 

    @project_title.setter
    def project_title(self, new_project_title: str) -> None:
        self._project_title = new_project_title
        self._dictionary["project_title"] = self._project_title
        self.write_dictionary()
 
    @property
    def admins(self):
        return self._admins

    def at_admins(self):
        "a list of admins with @ signs included"
        return ["@"+item for item in self.admins]

    @admins.setter
    def admins(self, new_admin_handles: List[str]) -> None:  
        self._admins = new_admin_handles
        self._dictionary["admins"] = self._admins
        self.write_dictionary()
  
    def add_admins(self, new_admin_handles: List[str]) -> None:  # include check to see if admin already in list?
        self._admins = self._admins + new_admin_handles
        self._dictionary["admins"] = self._admins
        self.write_dictionary()
      
    def remove_admins(self, old_admin_handles: List[str]) -> None:
        self._admins = [handle for handle in self._admins if handle not in old_admin_handles]
        self._dictionary["admins"] = self._admins
        self.write_dictionary()

    @property
    def instructors(self):
        return self._instructors
    
    def at_instructors(self):
        "a list of instructors with @ signs included"
        return ["@"+item for item in self.instructors]

    @instructors.setter
    def instructors(self, new_instructor_handles: List[str]) -> None:  
        self._instructors = new_instructor_handles
        self._dictionary["instructors"] = self._instructors
        self.write_dictionary()
  
    def add_instructors(self, new_instructor_handles: List[str]) -> None:  # include check to see if admin already in list?
        self._instructors = self._instructors + new_instructor_handles
        self._dictionary["instructors"] = self._instructors
        self.write_dictionary()
      
    def remove_instructors(self, old_instructor_handles: List[str]) -> None:
        self._instructors = [handle for handle in self._instructors if handle not in old_instructor_handles]
        self._dictionary["instructors"] = self._instructors
        self.write_dictionary()

    @property
    def students(self):
        return self._students
    
    def at_students(self):
        "a list of students with @ signs included"
        return ["@"+item for item in self.students]

    @students.setter
    def students(self, new_student_handles: List[str]) -> None:  
        self._students = new_student_handles
        self._dictionary["students"] = self._students
        self.write_dictionary()
  
    def add_students(self, new_student_handles: List[str]) -> None:  # include check to see if admin already in list?
        self._students = self._students + new_student_handles
        self._dictionary["students"] = self._students
        print(self._dictionary["students"])
        self.write_dictionary()
      
    def remove_students(self, old_student_handles: List[str]) -> None:
        self._students = [handle for handle in self._students if handle not in old_student_handles]
        self._dictionary["students"] = self._students
        self.write_dictionary()
  
    def check_instructor(self, handle: str) -> bool:
        """returns true if handle (with the @ prefix) is listed
        under instructors in the settings file"""
        return handle in self.at_instructors()

    def check_admin(self, handle: str) -> bool:
        return handle in self.at_admins()

    def check_student(self, handle: str) -> bool:
        return handle in self.at_students()


