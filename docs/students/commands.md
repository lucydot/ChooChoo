!!! note

    The ChooChoo command line interface is currently fragile. The commands must be written exactly as listed; capitalisation and whitespace matters. 
    Making the interface more robust is on the developer-todo.

**`choochoo list commands`**

:   List all commands available to the user type (either student, instructor or admin).

**`choochoo list people`**

:   List all students, instructors and admins by github username. The list is parsed from. `./instructor/settings.yml`.

**`choochoo check [@handle] is [student/instructor/admin]`**    
*e.g.* `choochoo check @lucydot is instructor`

:    Check if github username `@handle` is listed as a student, instructor or admin in `./instructor/settings.yml`.

**`choochoo vote up`**

:    *`question` issues only*  
    Add an up-vote to the proposed question. Once a pre-specified number of votes is met an admin will be invited to add the question to the question bank.

**`choochoo generate [positive integer] questions`**    
*e.g.* `choochoo generate 5 questions`

:    *`student` issues only*  
     Generate a webpage containing [positive integer] questions from the question bank. **The questions correspond to the objectives which have not been ticked in the issue thread.** Unless otherwise specified the webpage can be found at `username.github.io/repo_name/questions/handle` where `handle` is the github username of the person issuing the command.

**`choochoo generate [positive integer] questions for objectives [positive integers with spaces]`**     
*e.g.* `choochoo generate 5 questions for objectives 1 2 4`

:   *`student` issues only*  
     Generate a webpage containing [positive integer] questions from the question bank. **The questions correspond to the specified objectives.** Unless otherwise specified the webpage can be found at `username.github.io/repo_name/questions/handle` where `handle` is the github username of the person issuing the command.
