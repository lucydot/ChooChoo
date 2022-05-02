## All aboard! The ChooChoo journey



## Getting ChooChoo

There are three ways to get setup with ChooChoo:

1. Fork the [choochoo-template repository]() and specify the objectives/questions/tutorials for your course.
2. Fork an [existing choochoo repository]() and use or extend objectives/questions/tutorials from an existing ChooChoo project.
3. Integrate choochoo into an existing Github repository.

The third option (integrate) requires a better understanding of Github. If you are new to Github we recommend Forking the [choochoo-template]() or an [existing choochoo repository](). For more setup details please select a tab below.

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

    1. Automatically assumes branch names but this can be edited
    2.
    

!!! Note

    - Your ChooChoo repo should be public if you have standard (free) Github account and want to publish tutorials, questions and summary plots online.
    - You are advised to create one ChooChoo repository for each class group. This will allow you to track the progress of each individual class rather than all classes combined.

## ChooChoo settings

All ChooChoo settings are contained within `./instructor/settings.yml`. This is a yaml file;  if you are unfamiliar with yaml you can read more about the syntax on the [Tools page](./tools.md).

`project_title`: The project title.    
`project_repo`: In the format `username/repo_name`.       
`admins`: A list of Github usernames without the `@` sign.           
`instructors`: A list of Github usernames without the `@` sign.  
`students`: A list of Github usernames without the `@` sign.  

`choochoo_branch`: The branch where ChooChoo is installed. In most cases this will be the default `main` or `master` branch.      
`gh-pages`: If set to true then the question bank, tutorials and summary plot will be published on the `gh-pages_branch`.    
`gh-pages_branch`: The branch used to publish web content. This is most commonly `gh-pages`. For more information on Github Pages please see the [Tools page](./tools.md).     
`web_address`: The web address for this ChooChoo project. In most cases this will be `https://username.github.io/repo_name`.     

`questions`: If set to `true` students can propose their own questions for the question bank.     
`votes_required`: The number of votes required before an admin is asked to add a question to the question bank.     


## ChooChoo objectives

The ChooChoo checklist is generated from `./instructor/objectives.yml`. This is a yaml file;  if you are unfamiliar with yaml you can read more about the syntax on the [Tools page](./tools.md).
