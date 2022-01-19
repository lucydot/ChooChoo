"""
this script is called by .github/.workflows/fat_controller.yml when someone calls choochoo
in an issue thread they did not author (create).
"""

### NOTE: we don't need this script. Can make a comment from within the action: 
# https://stackoverflow.com/questions/58066966/commenting-a-pull-request-in-a-github-action

from choochoo import issues

issues.make_comment("Choochoo is ignoring this command as you are not the \
                   issue author.")
