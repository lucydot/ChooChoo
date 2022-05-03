## Instructor workflow

``` mermaid
graph LR
  A(1. <a href='./setup.md'>Setup ChooChoo</a>) --> B(<b>Basic usage</b> <br> 2. <a href='#2-monitor-class-progress'>Monitor class progress</a> <br> 3. <a href='#3-manage-class-participants'>Manage class participants</a> <br> 4. <a href='#4-add-links-to-the-objectives'>Add links to the objectives</a>); 
  B --> C(<b>Advanced usage</b> <br> 5. <a href='./setup.md'>Publish tutorials</a> <br> 6. <a href='./setup.md'>Add questions to the question bank</a> <br> 7. <a href='./setup.md'>Accept student contributions</a>);
  style A stroke:#333,stroke-width:4px
  style B fill:#bbf,stroke:#333,stroke-width:4px,text-align:left
  style C fill:#f9f,stroke:#333,stroke-width:4px,text-align:left
```

## 5. Publish tutorials

1. Copy/extend/write a class tutorial using Jupyter Notebooks (`.ipynb`) or Markdown (`.md`).
2. Commit your `.ipynb` or `.md` file to `./tutorials/`.
3. This will automatically trigger a build. After a few minutes your tutorial will be available to view at `username.github.io/repo_name/tutorials/filename`.
4. You can link your new tutorials to a particular objective using the command `choochoo add tutorial [webpage address] to objective [positive integer]`. The objective number can be found in any `student` issue thread.
5. To build a checklist containing this new link run `choochoo build checklists`.

## 6. Add questions to the question bank

1. Open a `Question thread` issue in the ChooChoo repository
2. Complete the fields in the form:

     - `authors`: Github username(s) of the question author(s)
     - `title`: Question title
     - `Question`: Question. This can be formatted using the webpage icons or Markdown. You can preview your text using the `Preview` tab.
     - `Answer`: Answer. This can be formatted using the webpage icons or Markdown. You can preview your text using the `Preview` tab.
     - `Checklist items`: Select the checklist items this question is designed to assess

3. Click on `submit new issue`
4. If you are happy with the question, you can add it to the question bank using `choochoo bank question`
5. A message will be posted to the issue thread when the question has been successfully banked. 
6. You can build the question bank for online viewing using `choochoo build question bank`
7. A message will be posted to the issue thread which contains a link to the webpage. It may take a few minutes for the webpage to reflect your latest changes.
8. You can link your new question to a particular objective using the command `choochoo add question [webpage address] to objective [positive integer]`. The webpage address could be an anchor link to a question in your question bank. To get the anchor link, hover over the question title - you will see a link icon appear. The objective number can be found in any `student` issue thread.
9. To build a checklist containing this new link run `choochoo build checklists`.

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

    



