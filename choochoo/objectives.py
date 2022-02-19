"""
A module for converting a choochoo objectives yaml file into a 
github issues template markdown file.
"""

import shutil
import yaml

def string_generator(long_name, short_name, table=False):
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

shutil.copyfile('./instructor/objectives_header.md',
    './.github/ISSUE_TEMPLATE/choochoo-student-thread.md')

with open("./instructor/objectives.yml", "r") as stream:
    try:
        objectives_dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print(exc)

with open("./.github/ISSUE_TEMPLATE/choochoo-student-thread.md","a") as f:
    for section in objectives_dictionary['sections']:
        print("\n\n### "+ section['name'],file=f)
        print("|"+string_generator('tutorials','Tutorial')
                 +string_generator('questions','Question')
                 +string_generator('links','Link'),file=f)

        print("\n| objective | tutorials | questions | links |\n|----|----|----|----|",file=f)
        for objective in section['objectives']:
            print("|"+objective['name']+"|"
                +string_generator('tutorials','T',table=True)
                +string_generator('questions','Q',table=True)
                +string_generator('links','L',table=True),file=f)

