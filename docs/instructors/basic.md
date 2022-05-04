## Instructor workflow

``` mermaid
graph LR
  A(1. <a href='https://lucydot.github.io/ChooChoo/instructors/setup/'>Setup ChooChoo</a>) --> B(<b>Basic usage</b> <br> 2. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#2-monitor-class-progress'>Monitor class progress</a> <br> 3. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#3-manage-class-participants'>Manage class participants</a> <br> 4. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#4-add-links-to-the-objectives'>Add links to the objectives</a> </br> 5. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#5-publish-tutorials'>Publish tutorials</a> ); 
  B --> C(<b>Advanced usage</b> <br> 6. <a href='https://lucydot.github.io/ChooChoo/instructors/advanced#6-add-questions-to-the-question-bank'>Add questions to the question bank</a> <br> 7. <a href='https://lucydot.github.io/ChooChoo/instructors/advanced#7-accept-student-contributions'>Accept student contributions</a> </br> 8. <a href='https://lucydot.github.io/ChooChoo/instructors/advanced#8-generate-personalised-question-sets'>Generate personalised question sets</a>);
  style A stroke:#333,stroke-width:4px
  style B fill:#bbf,stroke:#333,stroke-width:4px,text-align:left
  style C fill:#f9f,stroke:#333,stroke-width:4px,text-align:left
```

## 1. Setup ChooChoo

Please see the [Setup page](./setup.md).

## 2. Monitor class progress

1. Open any issue in the ChooChoo repository (or create a new one)
2. Create a comment with the command `choochoo summarise class progress`
3. A plot summarising class progress will be displayed in the issue thread. This may take a few minutes to appear.

!!! Note

    Do not re-edit an existing ChooChoo issue comment -`choochoo-bot` will not pick this up. 
    If you make a mistake it is best to create a new comment in the issue thread.
    You can always delete comments if you would like the issue thread to look less cluttered.
    
## 3. Manage class participants

1. You can add students and instructors using `choochoo add [@handle] as student` or `choochoo add [@handle] as instructor`. `@handle` is the Github username of the student/instructor.
2. You can remove students and instructors using `choochoo remove [@handle] as student` or `choochoo remove [@handle] as instructor`.
3. If you are an admin you can add and remove other admins using `choochoo add [@handle] as admin` or `choochoo remove [@handle] as admin`.
4. To list all students, instructors and admins use `choochoo list people`.

!!! Hint

    There is often more than one way to do something in ChooChoo. For example:
    to add a student to the repo an instructor or admin could use the command `choochoo add @handle as instructor`. 
    Alternatively, they could edit `./instructor/settings.yml` directly. In this sense, many of the ChooChoo instructor commands 
    can be seen as convenience functions.

## 4. Add links to the objectives

1. You can add any link (an external tutorial, Youtube video etc) to a particular objective using the command `choochoo add link [webpage address] to objective [positive integer]`. The objective number can be found in any `student` issue thread.  Alternatively, you can also add a link by directly editing `./instructor/objectives.yml`.   
2. To build a checklist containing this new link run `choochoo build checklists`.      

!!! Important

    All web links must be given using the full web address including `https://`.

!!! Important

    Commands to `choochoo-bot` trigger a Github Action workflow. 
    Each workflow can take a couple of minutes to run, and they do not run sequentially.
    In a small handful of use cases his can have some unwanted effects. For example, you may add a link using 
    `choochoo add link [web-address] to objective 2` and then build the checklist using `choochoo build checklist`.
    There is a chance that the second workflow will complete before the first workflow,
    so that the new checklist will not include the new link. 
    To avoid this problem it is best to double check the generated student issue template by raising an issue.

## 5. Publish tutorials

1. Copy/extend/write a class tutorial using Jupyter Notebooks (`.ipynb`) or Markdown (`.md`).
2. Commit your `.ipynb` or `.md` file to `./tutorials/`.
3. This will automatically trigger a build. After a few minutes your tutorial will be available to view at `username.github.io/repo_name/tutorials/filename`.
4. You can link your new tutorials to a particular objective using the command `choochoo add tutorial [webpage address] to objective [positive integer]`. The objective number can be found in any `student` issue thread.
5. To build a checklist containing this new link run `choochoo build checklists`.
    
--8<-- "includes/glossary.md"



