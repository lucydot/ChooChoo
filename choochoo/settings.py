"""
A module for reading and writing to the settings yml file.
"""

import yaml  # Pyyaml
from typing import List # this is not needed for Python3.9+
from choochoo import management
from choochoo import settings_path

class Settings:
    """Class for reading and writing to the settings yml file.

      The settings file is downloaded from the online repository
      (rather than a local installed copy).
    """
    def __init__(self):

        self.repository = management.Repository()
        self.path = settings_path
        self._dictionary = self.load_dictionary()  
        self._project_title = self.dictionary["project_title"]
        self._admins = self.dictionary["admins"]
        self._instructors = self.dictionary["instructors"]
        self._students = self.dictionary["students"]


    @property
    def dictionary(self):
        return self._dictionary

    def load_dictionary(self):  
        settings_file = self.repository.pygh_repo.get_contents(self.path, ref="main")
        settings_string = settings_file.decoded_content.decode()
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
        self.write_dictionary

    @property
    def instructors(self):
        return self._instructors

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
        """returns true if handle (without the @ prefix) is listed
        under instructors in the settings file"""
        return handle in self.instructors

    def check_admin(self, handle: str) -> bool:
        return handle in self.admins 

    def check_student(self, handle: str) -> bool:
        return handle in self.students


