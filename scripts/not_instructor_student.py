"""
this script is called by .github/.workflows/fat_controller.yml when someone calls choochoo
in an issue thread that is not labelled as "instructor" or "teacher".
"""

from choochoo import issues

issues.issue_reply("""Choochoo is ignoring this command as this is not an 
                   Instructor or Student issue thread.
                   
                   Instructors: add your name to settings.yml and then raise an Instructor issue.
                   Students: ask an instructor to create a Student thread for you.""")
