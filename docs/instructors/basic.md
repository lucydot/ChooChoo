## Instructor workflow

``` mermaid
graph LR
  A[1. <a href='./setup.md'>Setup ChooChoo</a>] --> B[2. Monitor class progress];
  A --Add--> C[3. questions];
  A --Add--> D[4. tutorials];
  A --Add--> E[5. links]
  A --> F[6. Accept student contributions];
```


!!! Note

    Do not re-edit an existing ChooChoo issue comment -`choochoo-bot` will not pick this up. 
    If you make a mistake it is best to create a new comment in the issue thread.
    You can always delete comments if you would like the issue thread to look less cluttered.
    
!!! Important

    Commands to `choochoo-bot` trigger a Github Action workflow. 
    Each workflow can take a couple of minutes to run, and they do not run sequentially.
    In a small handful of use cases his can have some unwanted effects. For example, you may add a link using 
    `choochoo add [web-address] to objective 2` and then build the checklist using `choochoo build checklist`.
    There is a chance that the second workflow will complete before the first workflow,
    so that the new checklist will not include the new link. To avoid this problem it is best to double check the generated issue templates.

!!! Hint

    There is often more than one way to do something in ChooChoo. For example:
    - to add a student to the repo an instructor or admin could use the command `choochoo add @handle as instructor`. 
    Alternatively, they could edit `./instructor/settings.yml` directly. 
    - to add a question to the question bank the instructor could raise a `question` issue and then use the command `choochoo bank question`.
    Alternatively, they could edit `./questions/question_bank.yml` directly. 
    In this sense, many of the ChooChoo instructor commands can be seen as convenience functions.





    
--8<-- "includes/glossary.md"



