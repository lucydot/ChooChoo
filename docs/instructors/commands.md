`choochoo list commands`

:   List all commands available to the user type (either student, instructor or admin).

`choochoo list people`

:   List all students, instructors and admins by github username. The list is parsed from. `./instructor/settings.yml`.

`choochoo build checklists`

!!!  Note ""

    Admin-only command.
    
!!! Warning

    This command should not be used once your class is in progress. Strange things will happen if `student` and `question` issues are raised for different checklist builds. 

:   Build the `student` and `question` issue templates using the objectives listed in `./instructor/settings.yml`.

`
    
    

