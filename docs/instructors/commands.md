!!!  Note

    The ChooChoo command line interface is currently fragile. The commands must be written exactly as listed; capitalisation and whitespace matters. 
    Making the interface more robust is on the developer-todo.

`choochoo list commands`

:   List all commands available to the user type (either student, instructor or admin).

`choochoo list people`

:   List all students, instructors and admins by github username. The list is parsed from. `./instructor/settings.yml`.

`choochoo build checklists`

!!!  Note " "

    Admin-only command.
    
!!! Warning

    This command should not be used once your class is in progress. Strange things will happen if `student` and `question` issues are raised for different checklist builds. 

:   Build the `student` and `question` issue templates using the objectives listed in `./instructor/settings.yml`.

`choochoo build question bank`

!!!  Note ""

    Admin-only command.
    
:   Build and publish a webpage containing all questions in the question bank. Unless otherwise specified the web address is `username.github.io/repo_name/questions/question_bank`. The question bank file is located at `./questions/question_bank.yml`. This yaml file is converted to markdown before being published.

`choochoo summarise class progress`

:   Generate a bar chart summarising class progress through the checklist. Unless otherwise specified the bar chart will be published at `username.github.io/repo_name/`. 

`choochoo check [@handle] is [student/instructor/admin]`

!!! Example "`choochoo check @lucydot is instructor`"

:    Check if github username `@handle` is listed as a student, instructor or admin in `./instructor/settings.yml`.

`choochoo add [@handle] as [student/instructor/admin]`

!!! Example "`choochoo add @lucydot as instructor`"

:    Add github username `@handle` as a student, instructor or admin in `./instructor/settings.yml`.

`choochoo remove [@handle] as [student/instructor/admin]`

!!! Example "`choochoo remove @lucydot as instructor`"

:    Remove github username `@handle` as a student, instructor or admin in `./instructor/settings.yml`.
    

