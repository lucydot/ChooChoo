"""
A module for converting a choochoo objectives yaml file into a 
github issues template markdown file.
"""

import shutil
import yaml
from choochoo import objectives_header_path, objectives_path, issue_template_path

def string_generator(section,long_name, short_name, table=False):
    string_list = []

    if len(section[long_name]) == 1:
        string_list.extend(("[",short_name,"](",section[long_name][0],") "))
    else:
        for index,link in enumerate(section[long_name]):
            string_list.extend(("[",short_name,str(index+1),"](",link,") "))

    string_list.append("|")

    if len(section[long_name]) ==  0 and table is True:
        return "| "
    elif len(section[long_name]) ==  0 and table is False:
        return " "
    else:
        return ''.join(string_list)

def generate_student_thread():

    shutil.copyfile(objectives_header_path,
        issue_template_path)

    with open(objectives_path, "r") as stream:
        try:
            objectives_dictionary = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            print(exc)

    with open(issue_template_path,"a") as f:
        for section in objectives_dictionary['sections']:
            print("\n\n### "+ section['name'],file=f)
            print("|"+string_generator(section,'tutorials','Tutorial')
                     +string_generator(section,'questions','Question')
                     +string_generator(section,'links','Link'),file=f)

            print("\n| | objective | tutorials | questions | links |\n|----|----|----|----|",file=f)
            for objective in section['objectives']:
                print("|[ ]| "+objective['name']+"|"
                    +string_generator(objective,'tutorials','T',table=True)
                    +string_generator(objective,'questions','Q',table=True)
                    +string_generator(objective,'links','L',table=True),file=f)

