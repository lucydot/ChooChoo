ChooChoo is a Checklist tool for educators. ChooChoo encourages learning through self-assessment, collaboration and diagnostic teaching. If you would like to know more about the pedagogy underlying ChooChoo please read the [Pedagogy page](./pedagogy.md).

If you use ChooChoo as part of any published work, please [cite accordingly](./citation.md).

# ChooChoo target audience
ChooChoo is domain agnostic. It is primarily aimed at people who already use Github for their teaching, and who would like a straight-forward way to assess the progress of their students. It can be integrated into an existing Github repository, or exist as a standalone project.

We strongly encourage people to share their ChooChoo repositories so that others can use and adapt existing checklists and question sets. For example, the [ChooChoo-physics]() repository can be easily adapted for use in other undergraduate computational physics courses. A full list of ChooChoo projects is maintained [here]().

### Which skills are needed to use ChooChoo?
ChooChoo is based around Github and, in particular, Github Issues. Self-assessment questions (an optional feature) are written using Markdown syntax. In addition, instructors use yaml to set the ChooChoo checklists and settings. All three tools (Github, Markdown, yaml) are *very* widely used within the programming community. Learning these skills will, in many cases, be a worthwhile time investment for those who continue to work in technology-related fields. To learn more about the tools that ChooChoo is built on top of please read the [Tools page].

# ChooChoo-bot 
Students and instructors interact with the ChooChoo-bot helper using comments in a Github issue thread. All comments starting with `choochoo` will be received by ChooChoo-bot. 

# ChooChoo roles and issue types
There are three roles within a ChooChoo project: `admin`, `instructor` and `student`:

- **Students** can generate personal checklists to work through, propose self-assessment questions and vote on proposed questions. 
- **Instructors** can add or remove students, summarise class progress as a bar chart, and add questions to the question bank. 
- **Admins** can do the same as instructors, in addition they are able to generate the student checklist template and add/remove instructors. 

Documentation for students can be found in the [student section](./students/). **We suggest linking to this from any associated course pages.** Documentation for admins and instructors can be found in the [instructor section](./instructors/).

There are also three ChooChoo issue types: `student`, `instructor` and `question_proposal`. 

- **`student` issues** can by a student, instructor or admin. They contain an automatically generated, personal checklist for the student to work through. They also contain links to any associated tutorials, questions or external websites.
- **`instructor` issues** can be created by an instructor or admin. They are used to monitor class progress (generate plots) and add/remove students.
- **`question_proposal` issues** can be created by a student, instructor or admin. They contain the proposed question. They also contain any discussion about the question and the votes in support of the question.

The table below summarises the `choochoo-bot` commands, who can use each command, and where each command can be used. A summary of the available student commands is available [here](./students/commands). A summary of the available instructor commands is available [here](./instructors/commands).

| Command | `student` role | `instructor` role | `admin` role | `student` issue | `instructor` issue | `question_proposal` issue |
| ------ | :----:  | :----:  | :----:  | :----:  | :----:  | :----: |
| `choochoo` add student |❌ | ✅ | ✅ |❌ |✅ |❌ |





