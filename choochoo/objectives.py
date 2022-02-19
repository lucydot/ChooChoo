"""
A module for converting a choochoo objectives yaml file into a 
github issues template markdown file.
"""

import yaml
#from markdownTable import markdownTable

with open("./instructor/objectives.yml", "r") as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)