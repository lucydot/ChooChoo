"""
this script is called by .github/.workflows/fat_controller.yml when someone calls choochoo
in an issue thread that is not labelled as "instructor" or "teacher".
"""

### NOTE: we don't need this script. Can make a comment from within the action: 
# https://stackoverflow.com/questions/58066966/commenting-a-pull-request-in-a-github-action

from choochoo import issues

issues.make_comment("""Choochoo is ignoring this command as this is not an 
                   Instructor or Student issue thread.
                   
                   Instructors: add your name to the settings.yml file and then raise an Instructor issue.
                   Students: ask an instructor to add your name to the settings.yml file.""")
