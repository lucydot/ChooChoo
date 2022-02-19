"""
this script is called by .github/.workflows/fat_controller.yml when someone applies the 
'instructor' issue label (automatic when the instructor issue template is used).

It checks to see the instructor is listed as such in the settings.yml. If not, then the issue is closed.
"""

from sys import argv
from choochoo import management, issues, env

handle = argv[1]

if management.check_instructor(handle) is False:

  repository = management.Repository()
  number = env.issue_number()
  issue = issues.Issue(repository,number)
  issue.make_comment("Choochoo is closing this issue as",handle,"is not listed as an instructor in settings.yml.")
  issue.close_issue()
