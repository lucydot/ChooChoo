"""
this script is called by .github/.workflows/fat_controller.yml when someone calls choochoo
in an issue thread they did not author (create).
"""

from choochoo import issues

issues.make_comment("Choochoo is ignoring this command as you are not the \
                   issue author.")
