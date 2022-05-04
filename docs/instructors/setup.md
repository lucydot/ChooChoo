## All aboard! Setting up ChooChoo

!!! Note "We know you're busy"

    The typical ChooChoo setup should take roughly one hour. The exact time depends on whether you are using an existing ChooChoo project (in which case setup should be quicker) or creating a ChooChoo project from scratch (in which case setup time will partly depend on how many objectives you are specifying). It will also depend on how familiar you are with the underlying tools: Github, yaml and markdown. For more support in using these tools please see the [Tools page](./tools.md). If you are stuck, please [get in contact](https://github.com/lucydot/ChooChoo/discussions).


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

There are three ways to get the files required to run ChooChoo:

1. Fork the [choochoo-template repository](https://github.com/lucydot/ChooChoo-template/) and specify the objectives/questions/tutorials for your course.
2. Fork an [existing choochoo repository](./existing.md) and use or extend objectives/questions/tutorials from an existing ChooChoo project.
3. Integrate ChooChoo into an existing Github repository.

The third option (integrate) requires a good understanding of Github. If you are new to Github we recommend forking the [choochoo-template](https://github.com/lucydot/ChooChoo-template/) or an [existing choochoo repository](./existing.md). For more setup details please select a tab below.

=== "Fork template"

    1. Visit https://github.com/lucydot/ChooChoo-template/
    2. Click on the `fork` icon in the top-right hand corner
    3. Specify the owner, repository name and description
    4. Click on `Create Fork`
    
=== "Fork existing"

    1. Find an [existing ChooChoo repository](./existing.md) in your subject domain
    2. Click on the `fork` icon in the top-right hand corner
    3. Specify the owner, repository name and description
    4. Click on `Create Fork`
    
=== "Integrate"

    !!! Warning
    
        This option requires a good understanding of Github. 
        If you are new to Github we recommend forking an existing choochoo repository or the template repository.
        
    !!! Note
    
        You can copy the ChooChoo files into a dedicated branch if preferred. Just be sure to specify the branch in `./instructor/settings.yml`.

    1. Visit https://github.com/lucydot/ChooChoo-template/
    2. Copy the `./instructor` folder and contents into the root of your repository
    3. Create an empty `./plots` folder in the root your repository
    4. [optional] Create an empty `./questions` folder in the root of your repository
    5. [optional] Create an empty `./tutorials` folder in the root of your repository
    6. Copy the contents of `.github/ISSUE_TEMPLATE/` into your repository. You may need to create this folder if it does not already exist.
    7. Copy the contents of `.github/workflows/` into your repository. You may need to create this folder if it does not already exist.

!!! Note

    - Your ChooChoo repo should be public if you have standard (free) Github account and want to publish tutorials, questions and summary plots online.
    - You are advised to create one ChooChoo repository for each class group. This will allow you to track the progress of each individual class rather than all classes combined.
    
## 2. Set repository permissions

#### Enable Issues

You may need to enable Issues on the repository. To do this:  

1. Visit your repository (most likely at `github.com/username/repo_name/`).   
2. Go to `Settings`-> `General`-> `Features`.
3. Tick the box next to `Issues` to enable Issues.

#### Add Issue labels

You need to add Issue labels to the forked repository. To do this:

1. Click on the `Issues` tab
2. Click on the `Labels` button
3. Click on the `New label` button
4. Type `student` into `Label name` and click `Create label`.
5. Type `instructor` into `Label name` and click `Create label`.
6. Type `question_proposal` into `Label name` and click `Create label`.
7. Type `accepted_question` into `Label name` and click `Create label`.

#### Enable Workflows

You may need to enable workflows on the repository. To do this:      
  
2. Click on the `Actions` tab towards the top of the page.   
3. Click on `I understand my workflows, go ahead and enable them`.   

#### Set repository secrets

Commands to `choochoo-bot` trigger a Github Action workflow. Permissions are needed to edit the repository during the workflow run. By default the workflow uses `secrets.BOT_ACCESS_TOKEN`,  which requires a `BOT_ACCESS_TOKEN` to be added to your repository secrets. To do this please get in contact through the [ChooChoo discussion page](https://github.com/lucydot/ChooChoo/discussions/) or [email](https://lucydot.github.io/about/).

Alternatively you can use the `secrets.GITHUB_TOKEN` which is automatically generated during any workflow run. The disadvantage of this approach is that `choochoo-bot` is replaced by the less charming `gh-actions` bot. To do this nonetheless:   
1. Visit your repository (most likely at github.com/username/repo_name/)   
2. In `.github/workflows/choochoo-fat-controller.yml` replace all instances of `secrets.BOT_ACCESS_TOKEN` with `secrets.GITHUB_TOKEN`.   

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

#### User options (may edit)
`questions`: If set to `true` students can propose their own questions for the question bank.     
`votes_required`: The number of votes required before an admin is asked to add a question to the question bank.    
`gh-pages`: If set to true then the question bank, tutorials and summary plot will be published on the `gh-pages_branch`. 

#### Advanced options (expert users only)
`choochoo_branch`: The branch where ChooChoo is installed. In most cases this will be the default `main` or `master` branch. 
`gh-pages_branch`: The branch used to publish web content. This is most commonly `gh-pages`. For more information on Github Pages please see the [Tools page](./tools.md).     
`web_address`: The web address for this ChooChoo project. In most cases this will be `https://username.github.io/repo_name`.     

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
