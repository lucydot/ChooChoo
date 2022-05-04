## Generating personalised question sets

- All ChooChoo participants can generate personalised question sets by typing `choochoo` commands into their issue thread comment boxes. There are two types of personalised question sets to generate:
    1. `choochoo generate [positive integer] questions` will generate a webpage containing [positive integer] questions from the question bank. The questions correspond to the objectives which have not been ticked in the issue thread. 
    2. `choochoo generate [positive integer] questions for objectives [positive integers with spaces]` will generate a webpage containing [positive integer] questions from the question bank. The questions correspond to the specified objectives.
- A link to the question set webpage will be posted in the issue thread.

!!! Note

    - Do not re-edit an existing ChooChoo issue comment -`choochoo-bot` will not pick this up. 
    If you make a mistake it is best to create a new comment in the issue thread.
    - `choochoo` commands can take a few minutes to run...be patient!

## Student contributions to the question-bank

ChooChoo is designed so that instructors *and* students can propose questions for the question bank. Other students then review the proposed questions, and up-vote those which they think should be accepted to the bank.

You may think that this is your instructor passing on the hard work of question-design to their students. Not so! It is now well established that learners construct knowledge when they are actively engaging with content rather than passively taking in education. Teaching is not a one-way process flowing from teacher to student; the best learning takes place when knowledge is co-created. By writing assessment questions you are actively engaging with the subject matter, and developing a deeper understanding of it. In addition you will learn how to use, an extremely popular language that is used across seveal technical domains.

And there is additional benefit for those who have contributions accepted, as your work will have value beyond your own learning. Most ChooChoo repositories are openly licensed and publicly shared with the global community; your work will be used to support the learning of others across the world. 

!!! Question "What makes a good question?"

    Writing effective assessment questions is not always easy. 
    A good rule of thumb is to have a variety of questions: some which are open-ended (for example, "write a piece of code that does X,Y and Z"),
    and some which are closed (for example, "fill the blank" type questions).
    Take a look at [existing ChooChoo question banks](./existing.md) for inspiration.

## Proposing a question

1. Open a `Question thread` issue in the ChooChoo repository
3. Complete the fields in the form:

     - `authors`: Github username(s) of the question author(s)
     - `title`: Question title
     - `Question`: Question. This can be formatted using the webpage icons or Markdown. You can preview your text using the `Preview` tab.
     - `Answer`: Answer. This can be formatted using the webpage icons or Markdown. You can preview your text using the `Preview` tab.
     - `Checklist items`: Select the checklist items this question is designed to assess

3. Click on `submit new issue`
4. Mention your classmates in the issue thread, and ask them to review your question. They will probably (hopefully!) have suggestions for improvement. Once they are happy with the question they can [vote it up](#voting-for-a-question).
    
!!! Info "Writing in Markdown"

    Markdown is a language for creating formatted text using a plain-text editor. For example a `#` in markdown converts text to a heading; `# This is a heading` will be displayed as a bold heading in large font (without the `#`). It used in many technical domains, and is especially popular for software documentation. In addition Github supports Markdown; you can write plain text files in Markdown and then preview the formatted text using the `Preview` tab. For more information about Markdown we suggest you take a look at [one of the many tutorials online](https://www.markdownguide.org/basic-syntax/).
    
## Editing a question

1. Open your Question issue thread
2. Click the button with the three dots (next to the smiley face) and click `Edit`. You will see Markdown text displayed. 
3. Carefully edit the relevant fields. **Do not** edit the headings (starting withh `###`).
4. Click on `Preview` to preview your edits.
5. Once you are happy, click `Update comment`.


!!! Note "Course chit-chat"

    The issue comments aren't only for `choochoo` commands. You can also use this as a place for discussion, for example to suggest improvements to the question. If you have a question for a fellow student, try mentioning them (with an `@` sign before their username) in the issue thread - they will receive a notification when you do.

## Voting for a question

1. Open the `Question thread` issue you would like to vote for
2. Double check that all of the proposed fields are correct  (`authors`, `title`, `question`, `answer`). 
3. Verify that the correct Checklist items have been selected.
4. If improvements can be made, make a comment in the issue thread. Mention (with an `@` sign) the authors of the question in the thread.
5. Once you are happy with the proposed question, show your support with the command `choochoo vote up`.
6. When a certain number of votes are reached (as determined by your instructor), the course admins will be mentioned and asked to add the question to the question bank.

!!! Info "Contributing to ChooChoo"

    Your course repository is powered by ChooChoo, which is an open-source project. This means ChooChoo can be modified and shared freely as it is publically accessible. This also means that ChooChoo relies on a community of people (that includes you!) to make contributions and improvements. You do not need to be a programmer to make contributions to the ChooChoo code. It may be that you have spotted a mistake in the documentation, or you have a suggestion for how the software could be improved. If you are interested in improving ChooChoo (no matter how small the contribution), please visit the [Contributing docs](./contributing/welcome.md). All contributions will be recognised on the ChooChoo [README page](https://github.com/lucydot/ChooChoo/README#contributions).


