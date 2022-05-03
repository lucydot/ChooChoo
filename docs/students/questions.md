## Student contributions to the question-bank


!!! Question "Why should I bother writing a question for the question bank?"

  



!!! Info "Contributing to ChooChoo"

  Your course repository is powered by ChooChoo, which is an open-source project. This means ChooChoo can be modified and shared freely as it is publically accessible. This also means that ChooChoo relies on a community of people (that includes you!) to make contributions and improvements. You do not need to be a programmer to make contributions to the ChooChoo code. It may be that you have spotted a mistake in the documentation, or you have a suggestion for how the software could be improved. If you are interested in improving ChooChoo (no matter how small the contribution), please visit the [Contributing docs](./contributing/welcome.md). All contributions will be recognised on the ChooChoo [README page](https://github.com/lucydot/ChooChoo/README#contributions).

## Proposing a question

1. Open a `Question thread` issue in the ChooChoo repository
3. Complete the fields in the form:

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


!!! Info "Writing in Markdown"

!!! Question "What makes a good question?"

    Writing questions for self-assessment is not always easy. 
    A good rule of thumb is to have a variety of questions: some which are open-ended (for example, "write a piece of code that does X,Y and Z"),
    and some which are closed (for example, "fill the blank" type questions).
    Take a look at [existing ChooChoo question banks](./existing.md) for inspiration.

    
## Voting for a question

- Students are also allowed to propose questions using the `Question thread` issue form. 
- ChooChoo participants can then vote their support for a question using the command `choochoo vote up` in the corresponding issue thread. 
- When a certain number of votes are reached (determined by the `votes_required` option in `./instructor/settings.yml`), the admins will be mentioned in the issue thread. 
- To accept and publish this student contribution follow steps 4 to 9 in [Step 6](#6-add-questions-to-the-question-bank) above.

!!! Note "Course chit-chat"

    Feel free to use the Github issue comments to discuss the question. The comment boxes aren't only for `choochoo` commands. If you have a question for a fellow student, try mentioning them (with an `@` sign before their username) in the issue thread - they will receive a notification when you do.
    
    
    
   


