"""
this script is called by .github/.workflows/fat_controller.yml when someone opens an issue with the 
student label (automatic when the student template is used).

It checks to see the student is listed as such in the settings.yml. If not, then the issue is closed.
"""

from sys import argv
from choochoo import management, issues

handle = argv[1]

if management.check_student(handle) is False:

  repository = management.Repository()
  number = env.issue_number()
  issue = issues.Issue(repository,number)
  issues.make_comment("Choochoo is closing this issue as",handle, \
                       "is not listed as an student in settings.yml.")
  issues.close_issue()
