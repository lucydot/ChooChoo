!!! note

    The ChooChoo command line interface is currently fragile. The commands must be written exactly as listed; capitalisation and whitespace matters. 
    Making the interface more robust is on the developer-todo.

==`choochoo list commands`==

:   List all commands available to the user type (either student, instructor or admin).

`==choochoo list people==`

:   List all students, instructors and admins by github username. The list is parsed from. `./instructor/settings.yml`.

<mark>`choochoo build checklists`</mark>
    
!!! Warning

    This command should not be used once your class is in progress. Strange things will happen if `student` and `question` issues are raised for different checklist builds. 

:   *Admin-only command*  
    Build the `student` and `question` issue templates using the objectives listed in `./instructor/settings.yml`.

`choochoo build question bank`

!!! note " "

    Admin-only command.
    
:   Build and publish a webpage containing all questions in the question bank. Unless otherwise specified the web address is `username.github.io/repo_name/questions/question_bank`. The question bank file is located at `./questions/question_bank.yml`. This yaml file is converted to markdown before being published.

`choochoo summarise class progress`

:   Generate a bar chart summarising class progress through the checklist. Unless otherwise specified the bar chart will be published at `username.github.io/repo_name/`. 

`choochoo check [@handle] is [student/instructor/admin]`

!!! Example "`choochoo check @lucydot is instructor`"

:    Check if github username `@handle` is listed as a student, instructor or admin in `./instructor/settings.yml`.

`choochoo add [@handle] as [student/instructor]`

!!! Example "`choochoo add @lucydot as instructor`"

:    Add github username `@handle` as a student or instructor in `./instructor/settings.yml`.

`choochoo remove [@handle] as [student/instructor]`

!!! Example "`choochoo remove @lucydot as instructor`"

:    Remove github username `@handle` as a student or instructor in `./instructor/settings.yml`.

`choochoo add [@handle] as admin`

!!! note " "

    Admin-only command.

!!! Example "`choochoo add @lucydot as admin`"

:    Add github username `@handle` as an admin in `./instructor/settings.yml`.

`choochoo remove [@handle] as admin`

!!! note " "

    Admin-only command.

!!! Example "`choochoo remove @lucydot as admin`"

:    Remove github username `@handle` as an admin in `./instructor/settings.yml`.
    
`choochoo add question [web address] to objective [positive integer]`

!!! note " "

    Admin-only command.

!!! Example "`choochoo add question https://lucydot.github.io/ChooChoo-template/questions/question_bank#markdown to objective 2`"

:    Add a question to an objective in the checklist. The question is specified using a full web address (including `https://`). Anchor links can be used to link to particular question within the published question bank (as in the example above). The objective is referenced using the number given in the `student` issue template.

`choochoo add link [web address] to objective [positive integer]`

!!! note " "

    Admin-only command.

!!! Example "`choochoo add link https://www.markdownguide.org/basic-syntax/ to objective 2`"

:    Add a link to an objective in the checklist. The link is specified using a full web address (including `https://`). The objective is referenced using the number given in the `student` issue template.

`choochoo add tutorial [web address] to objective [positive integer]`

!!! note " "

    Admin-only command.

!!! Example "`choochoo add tutorial https://lucydot.github.io/ChooChoo-template/tutorials/lists to objective 3`"

:    Add a tutorial to an objective in the checklist. The link is specified using a full web address (including `https://`). This (of-course!) allows the possibility to add any tutorials that are contained within `https://username.github.io/repo_name/tutorials/`. The objective is referenced using the number given in the `student` issue template.

`choochoo vote up`

!!! note " "

    `question` issues only.

!!! note " "

    Admin-only command.

:    Add an up-vote to the proposed question. Once a pre-specified number of votes is met an admin will be invited to add the question to the question bank.

`choochoo bank question`

!!! note " "

    `question` issues only.

!!! note " "

    Admin-only command.

:   Add the proposed question to the question bank. `choochoo build question bank` is required to publish the question online.

`choochoo generate [positive integer] questions`

!!! note " "

    `student` issues only.
    
!!! Example "`choochoo generate 5 questions`"

:   Generate a webpage containing [positive integer] questions from the question bank. **The questions correspond to the objectives which have not been ticked in the issue thread.** Unless otherwise specified the webpage can be found at `username.github.io/repo_name/questions/handle` where `handle` is the github username of the person issuing the command.

`choochoo generate [positive integer] questions for objectives [positive integers with spaces]`

!!! note " "

    `student` issues only.
    
!!! Example "`choochoo generate 5 questions for objectives 1 2 4`"

:   Generate a webpage containing [positive integer] questions from the question bank. **The questions correspond to the specified objectives.** Unless otherwise specified the webpage can be found at `username.github.io/repo_name/questions/handle` where `handle` is the github username of the person issuing the command.

