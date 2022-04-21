"""
A module for storing and editing choochoo checklist objectives.

Contains the Objectives class.
"""

import shutil
import yaml
import re
from choochoo import utilities, objectives_header_path, objectives_path, issue_template_path, question_issue_template_path

def string_generator(section,long_name, short_name, table=False):
    string_list = []

    if len(section[long_name]) == 1:
        string_list.extend(("[",long_name,"](",section[long_name][0],") "))
    else:
        for index,link in enumerate(section[long_name]):
            string_list.extend(("[",short_name,str(index+1),"](",link,") "))

    string_list.append(" | ")

    if len(section[long_name]) ==  0 and table is True:
        return "| "
    elif len(section[long_name]) ==  0 and table is False:
        return " "
    else:
        return ''.join(string_list)

class Objectives:

    def __init__(self, repository):

        self.repository = repository
        self.dict_from_yaml = utilities.read_yaml(objectives_path)
        self.names_from_yaml = self.names_from_yaml()
        self.dict_from_template = self.dict_from_template()

    def dict_from_template(self):
        """This is from the student issue template in contrast to `names_from_yaml` 
        which is built from the objectives yaml file.

        It returns a dictionary in which each value is itself a dictionary....
        lovely, messy nests"""

        issue_template_content = self.repository.file_content(issue_template_path)
        objectives = re.findall(r'\[ ] (.*?)\|', issue_template_content)

        objectives_dict = dict.fromkeys(objectives,{'id':0,'select':0})
        # instead of count could parse id from the template - 
        # this would be more robust code

        
        # After lots of faffing!....eventually correct....here be dragons
        for i,key in enumerate(objectives_dict):
            objectives_dict[key] = {'id' : i+1, 'select' : 0}

        return objectives_dict

    def objectives_list_by_id(self,id_list):
        """ return a list of objectives which have been selected by id number"""

        return [item[0] for item in self.dict_from_template.items() if item[1]["id"] in id_list]

    def names_from_yaml(self):

        objectives_dictionary = self.dict_from_yaml
        objectives_name_list = []

        for section in objectives_dictionary['sections']:
            for objective in section['objectives']:
                objectives_name_list.append(objective['name'])

        return objectives_name_list

    def generate_student_thread(self):

        shutil.copyfile(objectives_header_path,
            issue_template_path)

        objectives_dictionary = self.dict_from_yaml

        count = 0

        with open(issue_template_path,"a") as stream:

            for section in objectives_dictionary['sections']:
                print("\n\n### "+ section['name']+string_generator(section,'tutorials','T',table=False)
                         +string_generator(section,'questions','Q',table=False)
                         +string_generator(section,'links','L',table=False),file=stream)

                for objective in section['objectives']:

                    count += 1

                    # note that the pipe below is important for the regex to find objectives
                    print(str(count)+") - [ ] "+objective['name']+" | "
                        +string_generator(objective,'tutorials','T',table=False)
                        +string_generator(objective,'questions','Q',table=False)
                        +string_generator(objective,'links','L',table=False),file=stream)

    def generate_question_thread(self):

        question_template_dictionary = utilities.read_yaml(question_issue_template_path)

        objectives_list = self.names_from_yaml

        # depends on the checklist being the final element of the body list
        question_template_dictionary["body"][-1]["attributes"]["options"] = []
        
        for objective in objectives_list:
            question_template_dictionary["body"][-1]["attributes"]["options"].append({"label":objective})

        with open(question_issue_template_path, "w") as stream:
            yaml.dump(question_template_dictionary,stream)


