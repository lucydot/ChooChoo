## Instructor workflow

``` mermaid
graph LR
  A(1. <a href='https://lucydot.github.io/ChooChoo/instructors/setup/'>Setup ChooChoo</a>) --> B(<b>Basic usage</b> <br> 2. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#2-monitor-class-progress'>Monitor class progress</a> <br> 3. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#3-manage-class-participants'>Manage class participants</a> <br> 4. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#4-add-links-to-the-objectives'>Add links to the objectives</a> </br> 5. <a href='https://lucydot.github.io/ChooChoo/instructors/basic#5-publish-tutorials'>Publish tutorials</a> ); 
  B --> C(<b>The question bank</b> <br> 6. <a href='https://lucydot.github.io/ChooChoo/instructors/advanced#6-add-questions-to-the-question-bank'>Add questions to the question bank</a> <br> 7. <a href='https://lucydot.github.io/ChooChoo/instructors/advanced#7-accept-student-contributions'>Accept student contributions</a> </br> 8. <a href='https://lucydot.github.io/ChooChoo/instructors/advanced#8-generate-personalised-question-sets'>Generate personalised question sets</a>);
  style A stroke:#333,stroke-width:4px
  style B fill:#bbf,stroke:#333,stroke-width:4px,text-align:left
  style C fill:#f9f,stroke:#333,stroke-width:4px,text-align:left
```
## ChooChoo question bank

ChooChoo is designed so that admins, instructors and students can propose questions for the question bank. Other participants then review the proposed questions, and up-vote those which they think should be accepted to the bank.

This process is motivated by the evidenced benefits of co-creation in education. It is now well established that learners construct knowledge when they are actively engaging with content rather than passively taking in information. Teaching is not a one-way process flowing from teacher to student; the best learning takes place when knowledge is created together. By writing assessment questions the students are actively engaging with the subject matter, and developing a deeper understanding of it. In addition to this it is an opportunity to learn basic Markdown. For more about the pedagogy underlying ChooChoo, please see the [Pedagogy page](./pedagogy.md).

!!! Note

    Students can propose questions for the question bank, and vote for the questions they think should be accepted. However only admins can add questions to the question bank; they have ultimate responsibility for quality control.

## 6. Add questions to the question bank

1. Open a `Question thread` issue in the ChooChoo repository
2. Complete the fields in the form:

     - `authors`: Github username(s) of the question author(s)
     - `title`: Question title
     - `Question`: Question. This can be formatted using the webpage icons or Markdown. You can preview your text using the `Preview` tab.
     - `Answer`: Answer. This can be formatted using the webpage icons or Markdown. You can preview your text using the `Preview` tab.
     - `Checklist items`: Select the checklist items this question is designed to assess

3. Click on `submit new issue`
4. If you need to edit a question, see the [steps below](editing-a-question).
5. Once you are happy with the question, you can add it to the question bank using `choochoo bank question`
6. A message will be posted to the issue thread when the question has been successfully banked. 
7. You can build the question bank for online viewing using `choochoo build question bank`
8. A message will be posted to the issue thread which contains a link to the webpage. It may take a few minutes for the webpage to reflect your latest changes.
9. You can link your new question to a particular objective using the command `choochoo add question [webpage address] to objective [positive integer]`. The webpage address could be an anchor link to a question in your question bank. To get the anchor link, hover over the question title - you will see a link icon appear. The objective number can be found in any `student` issue thread.
10. To build a checklist containing this new link run `choochoo build checklists`.

#### Editing a question

1. Open your Question issue thread
2. Click the button with the three dots (next to the smiley face) and click `Edit`. You will see Markdown text displayed. 
3. Carefully edit the relevant fields. **Do not** edit the headings (starting withh `###`).
4. Click on `Preview` to preview your edits.
5. Once you are happy, click `Update comment`.

!!! Important

    - All web links must be given using the full web address including `https://`.

!!! Hint

    There is often more than one way to do something in ChooChoo. For example to add a question to the question bank the instructor 
    could raise a `question` issue and then use the command `choochoo bank question`.
    Alternatively, they could edit `./questions/question_bank.yml` directly. 
    
## 7. Accept student contributions

- Students are also allowed to propose questions using the `Question thread` issue form. 
- ChooChoo participants can then vote their support for a question using the command `choochoo vote up` in the corresponding issue thread. 
- When a certain number of votes are reached (determined by the `votes_required` option in `./instructor/settings.yml`), the admins will be mentioned in the issue thread. 
- To accept and publish this student contribution follow steps 4 to 9 in [Step 6](#6-add-questions-to-the-question-bank) above.

!!! Note

    Students may need extra support to write effective questions. 
    You may like to point them to [existing ChooChoo question banks](./existing.md) for inspiration.

## 8. Generate personalised question sets

- All ChooChoo participants can generate personalised question sets using one of two ways. Whichever way you choose, the command should be used in a `student` issue thread.
- `choochoo generate [positive integer] questions` will generate a webpage containing [positive integer] questions from the question bank. The questions correspond to the objectives which have not been ticked in the issue thread. 
- `choochoo generate [positive integer] questions for objectives [positive integers with spaces]` will generate a webpage containing [positive integer] questions from the question bank. The questions correspond to the specified objectives.
- Unless otherwise specified the webpage can be found at username.github.io/repo_name/questions/handle where handle is the github username of the person issuing the command.


