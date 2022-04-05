
### Notes:

- Choochoo assumes that the repo is public
- for local testing need a .env file that should not be version controlled!
- the locomotive emoji is from: https://creazilla.com/nodes/54585-locomotive-emoji-clipart (creative commons with attribution, from Twitter)
- People management: the issue labels determine permissions for particular choochoo commands. Any thread with 'instructor' label can issue instructor commands, any thread with 'student' label can issue student commands. To add instructors or students to a project you can edit the settings.yml. Alternatively, instructors can use the choochoo command.
- Instructors are advised to create one repo for each class group

### TODO:

- [ ] allow parsing of multiple usernames in the CLI. Allow multiple users to be added as students, instructors etc: so instead of finding handles by positions, search by words starting with @ and then form into a list of strings. Regex will do this task quite nicely!
- [ ] the cli is clunky: perhaps use switch instead (Python 3.9+ only). Or create my own simple parser (command class).
- [x] separate out the choochoo repo from the project repo. Install choochoo in the repo. This separates out what a choochoo admin and what a choochoo developer needs. There will then be the choochoo repo, the choochoo-template repo and the choochoo-physics repo and so on.
- [x] whenever anything is committed to main in questions, tutorials or proposed_questions then automatically compile into html on gh-pages (jekyll, markdown or pandoc type thing?)
- [ ] Choochoo returns update messages when something succesfully done
- [ ] Assign the issues to appropriate people (the people who raised them?)
- [ ] Use yaml + python dictionaries to do the many:many mapping between objectives and questions? OR play around with a mysql database which would be fun but prob overkill
- [ ] Stop students from creating more than one checklist per person
- [ ] Think about how to handle testing 
