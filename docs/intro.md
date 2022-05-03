ChooChoo is a checklist tool for educators. ChooChoo encourages learning through self-assessment, collaboration and diagnostic teaching. If you would like to know more about the pedagogy underlying ChooChoo please read the [Pedagogy page](./pedagogy.md).

!!! warning

    If you use ChooChoo as part of any published work, please [cite accordingly](./citation.md).

## ChooChoo target audience
ChooChoo is domain agnostic. It is primarily aimed at people who already use Github for their teaching, and who would like a straight-forward way to assess the progress of their students. It can be integrated into an existing Github repository, or exist as a standalone project. A list of ChooChoo projects is maintained [here](./projects.md).

!!! note "Sharing is caring"

    Users are strongly encouraged to share their ChooChoo repositories. This will enable other people to start from existing checklists and question 
    sets and will make setup quicker over time. Sharing can also incentivise student participation in building the question bank, as their work will have impact 
    beyond a single institution. 

### Which skills are needed to use ChooChoo?
ChooChoo is based around Github and, in particular, Github Issues. Self-assessment questions (an optional feature) are written using Markdown syntax. In addition, instructors use yaml to specify the ChooChoo checklists and settings. All three tools (Github, Markdown, yaml) are *very* widely used within the programming community. Learning these skills will, in many cases, be a worthwhile time investment for those who continue to work in technology-related fields. To learn more about the tools that ChooChoo is built on top of please read the [Tools page](./tools.md).

## choochoo-bot
Students and instructors interact with the `choochoo-bot` helper using comments in a Github issue thread. All comments starting with `choochoo` will be received by `choochoo-bot`. 

## ChooChoo roles 
There are three roles within a ChooChoo project: `student`, `instructor` and  `admin`:

- A **`student`** can generate personal checklists to work through, propose self-assessment questions and vote on proposed questions. 
- An **`instructor`** can do the same as a student, plus summarise class progress as a bar chart and add/remove students.
- An **`admin`** can do the same as an instructor, plus generate the Github issue templates, add questions to the question bank and add/remove instructors. 

## ChooChoo issue types
There are three ChooChoo issue types: `student`, `instructor` and [optional] `question`. 

- A **`student`** issue can be created by a student, instructor or admin. It contains an automatically generated, personal checklist to work through. It also contains links to any associated tutorials, questions or external websites.
- An **`instructor`** issue can be created by an instructor or admin. It is used for general ChooChoo management: for example, to monitor class progress (generate plots), add/remove students or generate the Github issue templates.
- [optional] A **`question`** issue can be created by a student, instructor or admin. Its contain a proposed question for the question bank. It also contains any discussion about the question and tracks the votes in support of accepting the question to the question bank.

## Get started
Setup steps for course leaders and instructors can be found in the [instructor section](./instructors/setup.md).

