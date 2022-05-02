## All aboard! The ChooChoo journey

``` mermaid
graph LR
  A[Fork/copy ChooChoo files] --> B[Set repository permissions];
  B --> C[Specify settings];
  B --> D[Specify objectives];
  C --> E[Build student checklists];
  D --> E;
  E --> G[Extend the question bank];
  E --> F[Monitor class progress];
  G --> H[Target your teaching];
  F --> H;
```

## Getting the ChooChoo files

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
    
## Permissions

Commands to `choochoo-bot` trigger a Github Action workflow. Permissions are needed to edit the repository during the workflow run. By default the workflow uses `secrets.BOT_ACCESS_TOKEN`,  which requires a `BOT_ACCESS_TOKEN` to be added to your repository secrets. To do this please get in contact through the [ChooChoo discussion page](https://github.com/lucydot/ChooChoo/discussions/) or [email](https://lucydot.github.io/about/).

Alternatively you can use the `secrets.GITHUB_TOKEN` which is automatically generated during any workflow run. To do this replace all instances of `secrets.BOT_ACCESS_TOKEN` with `secrets.GITHUB_TOKEN` in the `.github/workflows/` directory. The disadvantage of this approach is that `choochoo-bot` is replaced by the less charming `gh-actions` bot.

## ChooChoo settings

All ChooChoo settings are contained within `./instructor/settings.yml`. This is a yaml file;  if you are unfamiliar with yaml you can read more about the syntax on the [Tools page](./tools.md).

#### Key settings (must edit)
`project_title`: The project title.    
`project_repo`: In the format `username/repo_name`.       
`admins`: A list of Github usernames without the `@` sign.           
`instructors`: A list of Github usernames without the `@` sign.  
`students`: A list of Github usernames without the `@` sign.

#### User options (may edit)
`questions`: If set to `true` students can propose their own questions for the question bank.     
`votes_required`: The number of votes required before an admin is asked to add a question to the question bank.    

#### Advanced options (expert users only)
`gh-pages`: If set to true then the question bank, tutorials and summary plot will be published on the `gh-pages_branch`.  
`choochoo_branch`: The branch where ChooChoo is installed. In most cases this will be the default `main` or `master` branch. 
`gh-pages_branch`: The branch used to publish web content. This is most commonly `gh-pages`. For more information on Github Pages please see the [Tools page](./tools.md).     
`web_address`: The web address for this ChooChoo project. In most cases this will be `https://username.github.io/repo_name`.     

## ChooChoo objectives

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


