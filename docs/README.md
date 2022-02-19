
### Notes:
- Assumes that the repo is public
- for local testing need a .env file that should not be version controlled!
- the locomotive emoji is from: https://creazilla.com/nodes/54585-locomotive-emoji-clipart (creative commons with attribution, from Twitter)
- People management: the issue labels determine permissions for particular choochoo commands. Any thread with 'instructor' label can issue instructor commands, any thread with 'student' label can issue student commands. To see available commands....To add instructors or students to a project you can edit the settings.yml. Alternatively, instructors can use the choochoo commands: ....


### TODO:

[ ] allow parsing of multiple usernames in the CLI. Allow multiple users to be added as students, instructors etc: so instead of finding handles by positions, search by words starting with @ and then form into a list of strings. Regex will do this task quite nicely!
[ ] separate out the choochoo repo from the project repo. Install choochoo in the repo. This separates out what a choochoo admin and what a choochoo developer needs. There will then be the choochoo repo, the choochoo-template repo and the choochoo-physics repo and so on.
[ ] whenever anything is committed to main in questions, tutorials or proposed_questions then automatically compile into html on gh-pages (jekyll, markdown or pandoc type thing?)