## ChooChoo commands:
ChooChoo commands can be split into three types. Each question type is associated with a ChooChoo issue type(s).

| Icon | Description | Used in |
|:------:|-----------|---------|
👩🏾‍💻 | choochoo-management | any issue |
❓ | choochoo-question | issue labelled 'question' |
📋 | choochoo-student |issue labelled 'student'|

The table below summarises who can run ChooChoo commands. [Student command examples](./students/commands.md) and [instructor command examples](./instructors/commands.md) are also available.

| Type | Command | `student`  | `instructor`  | `admin`  | 
| :-----: | ------ | :----:  | :----:  | :----:  |
| 👩🏾‍💻 |`choochoo list commands` |:material-check: | :material-check: | :material-check: |
| 👩🏾‍💻  | `choochoo list people` |:material-check: | :material-check: | :material-check: |
| 👩🏾‍💻 |`choochoo build checklists` |:material-close: | :material-close: | :material-check: |
| 👩🏾‍💻 |`choochoo build question bank`| :material-close: | :material-close: | :material-check: |
| 👩🏾‍💻 |`choochoo summarise class progress` |:material-close: | :material-check: | :material-check: |
| 👩🏾‍💻  |`choochoo check [@handle] is [student/instructor/admin]` |:material-check: | :material-check: | :material-check: |
| 👩🏾‍💻 |`choochoo add [@handle] as [student/instructor]` |:material-close: | :material-check: | :material-check: |
| 👩🏾‍💻 |`choochoo remove [@handle] as [student/instructor]` |:material-close: | :material-check: | :material-check: |
| 👩🏾‍💻 |`choochoo add [@handle] as admin` |:material-close: | :material-close: | :material-check: |
| 👩🏾‍💻 |`choochoo remove [@handle] as admin` |:material-close: | :material-close: | :material-check: |
| 👩🏾‍💻 |`choochoo add question [web address] to objective [positive integer]` |:material-close: | :material-close: | :material-check: |
| 👩🏾‍💻 |`choochoo add link [web address] to objective [positive integer]` |:material-close: | :material-close: | :material-check: |
| 👩🏾‍💻 |`choochoo add tutorial [web address] to objective [positive integer]` |:material-close: | :material-close: | :material-check: |
| ❓ |`choochoo vote up`| :material-check: | :material-check: | :material-check: |
| ❓ |`choochoo bank question`| :material-close: | :material-close: | :material-check: |
| 📋 |`choochoo generate [positive integer] questions`|:material-check: | :material-check: | :material-check: |
| 📋 |`choochoo generate [positive integer] questions for objectives [positive integers with spaces]`|:material-check: | :material-check: | :material-check: |
