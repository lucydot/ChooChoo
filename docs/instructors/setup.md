## All aboard! Setting up ChooChoo

The typical ChooChoo setup should take roughly one hour. The exact time depends on whether you are using an existing ChooChoo project (in which case setup should be quicker) or creating a ChooChoo project from scratch (in which case setup time will partly depend on how many objectives you are specifying). It will also depend on how familiar you are with the underlying tools: Github, yaml and markdown. If you are stuck, please get in contact using the [Github discussions board](https://github.com/lucydot/ChooChoo/discussions) or via email ([see here](https://lucydot.github.io/about/)).


``` mermaid
graph LR
  A[1. Get ChooChoo files] --> B[4. Set objectives];
  A --> D[2. Set repository options];
  A --> C[3. Specify settings];
  D --> E[5. Generate templates];
  C --> E;
  B --> E;
  E --> F[6. Test setup];
  F --> G[7. Share documentation];
```

## 1. Get ChooChoo files

There are two ways to get the files required to run ChooChoo:

1. Copy the [choochoo-template repository](https://github.com/lucydot/ChooChoo-template/) and specify the objectives/questions/tutorials for your course.
2. Integrate ChooChoo into an existing Github repository.

The second option requires a solid understanding of Github. If you are new to Github we recommend copying the [choochoo-template](https://github.com/lucydot/ChooChoo-template/). For more setup details please select a tab below.

=== "Copy template"

    1. Visit [github.com/lucydot/ChooChoo-template](https://github.com/lucydot/ChooChoo-template/)
    2. Click on the green `Use this template` button towards the top-right hand corner and select `Create a new repository`
    3. Specify the owner, repository name and description
    4. Click on `Create repository`
    
=== "Integrate"

    This option requires a good understanding of Github. Please use with caution.
    If you are new to Github we recommend forking an existing choochoo repository or the template repository.

    1. Copy/clone the contents of [https://github.com/lucydot/ChooChoo-template/](https://github.com/lucydot/ChooChoo-template/) into the root of your existing repository on the `main` branch. 
    
        - You **do not** need the ChooChoo-template `.git` folder -  this can be safely ignored/removed.
        - Merge the contents of `.github/` into any existing folder of the same name.

!!! Note

    - Your ChooChoo repo should be public if you have standard (free) Github account and want to publish tutorials, questions and summary plots online.
    - You are advised to create one ChooChoo repository for each class group. This will allow you to track the progress of each individual class rather than all classes combined. 
    
## 2. Update Github labels and settings

!!! Note

    The Github web interface does seem to change on a fairly frequent basis. We will try to keep instructions up-to-date, but please do let us know if they need updating. `Issues` and `Workflows` (under `Actions`) both need to be enabled, this is the current default.

#### Add Issue labels

You need to add Issue labels to the repository. To do this:

1. Click on the `Issues` tab
2. Click on the `Labels` button
3. Click on the `New label` button
4. Type `student` into `Label name` and click `Create label`.
5. Type `instructor` into `Label name` and click `Create label`.
6. Type `question proposal` into `Label name` and click `Create label`.
7. Type `accepted question` into `Label name` and click `Create label`.

#### Enable Github Pages

You may need to enable Github to publish your gh-pages branch. To do this:

1. Visit your repository (most likely at github.com/username/repo_name/) 
2. Click on `main` towards the top left hand corner
3. In the box with `find or create a branch` type `gh-pages`
4. Click on `Create branch: gh-pages from main`

#### Optional: Customise your bot

Commands to `choochoo` trigger a Github Action workflow. By default the action responds to issue comments using `secrets.GITHUB_TOKEN` which is automatically generated during any workflow run.  The disadvantage of this approach is that the display name for issue comments is the less charming `gh-actions bot`. To use `choochoo-bot` as the display name you can follow these **optional** steps:

1. Go to `Settings` -> `Collaborators` -> `Add people`.
2. Type `choochoo-bot` 
3. Click `Add collaborator`.
4. Contact us through the [ChooChoo discussion page](https://github.com/lucydot/ChooChoo/discussions/) or [email](https://lucydot.github.io/about/) and we will send a `BOT_ACCESS_TOKEN`
5. Add the BOT_ACCESS_TOKEN as a repository secret.
6. In `.github/workflows/choochoo-fat-controller.yml` replace all instances of `secrets.GITHUB_TOKEN` with `secrets.BOT_ACCESS_TOKEN`.

## 3. Specify ChooChoo settings

All ChooChoo settings are contained within `./instructor/settings.yml`. This is a yaml file;  if you are unfamiliar with yaml you can read more about the syntax on the [Tools page](./tools.md). You can edit plain text files (yaml or Markdown) directly in the Github interface on your web browser without downloading anything.

!!! Important

    Remember to add your own Github username to the list of `admins`.

#### Key settings (must edit)
`project_title`: The project title.    
`project_repo`: In the format `username/repo_name`.       
`admins`: A list of Github usernames without the `@` sign.           
`instructors`: A list of Github usernames without the `@` sign.  
`students`: A list of Github usernames without the `@` sign.
`web_address`: The web address for this ChooChoo project. In most cases this will be `https://username.github.io/repo_name`.     

#### User options (may edit)
`questions`: If set to `true` students can propose their own questions for the question bank.     
`votes_required`: The number of votes required before an admin is asked to add a question to the question bank.    
`gh-pages`: If set to true then the question bank, tutorials and summary plot will be published on the `gh-pages_branch`. 
`gh-pages_branch`: The branch used to publish web content. This is most commonly `gh-pages`. For more information on Github Pages please see the [Tools page](./tools.md).     

## 4. Set ChooChoo objectives

The ChooChoo checklist is generated from `./instructor/objectives.yml`. This is a yaml file;  if you are unfamiliar with yaml you can read more about the syntax on the [Tools page](./tools.md).

!!! Note

    - All web links must be given using the full web address including `https://`.
    - You do not need to provide links for all fields. If there are no links you must use empty square brackets `[]`.

Each ChooChoo checklist contains one or more sections. Each section contains:

`name`: Section name.     
`questions`: A list of links to questions associated with this section.    
`tutorials`: A list of links to tutorials associated with this section.    
`links`: A list of other links associated with this section.    
`objectives`: A list of objectives (see below).

Each objective contains:

`name`: Objective name/description.     
`questions`: A list of links to questions associated with this objective.    
`tutorials`: A list of links to tutorials associated with this objective.    
`links`: A list of other links associated with this objective.  

## 5. Generate templates

1. Visit your choochoo repository (most likely github.com/username/repo_name)
2. Click on  the `Issues` tab towards the top of the page    
3. Click on `New Issue`
4. Click `Get Started` next to `ChooChoo instructor thread`
5. Click `Submit new issue`
6. In the comment box type `choochoo build checklists`

!!! Note

    Each `choochoo` command takes a couple of minutes to run.
    If the `choochoo` command is a success you will see a reply in the issue thread.

## 6. Test setup

1. Visit your choochoo repository (most likely github.com/username/repo_name)
2. Click on  the `Issues` tab towards the top of the page
3. Click on `New Issue`
4. Click `Get Started` next to `ChooChoo instructor thread`
5. Click on `Preview` to check the formatting looks correct
6. Repeat steps 1 through 5 for `ChooChoo student thread` 
7. Click `Submit new issue` to automatically generate a checklist
8. Read through the checklist and double check formatting, spelling, links etc

*If `questions` are enabled:*  

9. Repeat steps 1 through 4 for `Question thread` (if questions are enabled)    
10. Read through `Checklist items` at the bottom of the form and double check formatting, spelling etc.   

*If `gh-pages` is enabled:*    

11. Visit the repository website (most likely username.github.io/repo_name) to verify that a page exists

## 7. Share documentation

!!! Important

    The objective list should not be adjusted once your class is in progress. 
    Strange things will happen if `student` or `question` issues are raised for different objectives - 
    this includes objective lists that are changed, re-ordered or re-worded. 

Although some students will be comfortable using ChooChoo with minimal support or documentation, some may benefit from a walkthrough tutorial. We suggest sharing the link to the [student documentation](./student/setup.md) on your course webpage(s) and communication channels. In addition, we encourage you to do a live walkthrough of the steps contained in [student setup](./student/setup.md) and [student basic usage](./student/basic.md).
