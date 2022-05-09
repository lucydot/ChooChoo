from choochoo import environment, repository, settings

env = environment.Env()
repo = repository.Repository(env)
user_settings = settings.Settings(repo)

choochoo_path = user_settings.choochoo_path
instructor_folder_path = choochoo_path+"./instructor/"
question_folder_path = choochoo_path+"./questions/"
plots_folder_path = choochoo_path+"./plots/"

env_path = None # defaults to project root when set to None

student_issue_template_path = ".github/ISSUE_TEMPLATE/choochoo-student-thread.md"
question_issue_template_path = ".github/ISSUE_TEMPLATE/choochoo-questions.yml"

objectives_header_path = instructor_folder_path+"objectives_header.md"
objectives_yml_path = instructor_folder_path+"objectives.yml"
settings_path = instructor_folder_path+"settings.yml"

question_bank_path = question_folder_path+"question_bank"
question_bank_yml_path = question_folder_path+"question_bank.yml"
question_bank_markdown_path = question_folder_path+"question_bank.md"

output_plot_path = plots_folder_path+"summary_plot.png"
