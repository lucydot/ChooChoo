from choochoo import settings

env = environment.Env()
repo = repository.Repository(env)
user_settings = settings.Settings(repo)

choochoo_path = user_settings.choochoo_path

env_path = None # defaults to project root when set to None
settings_path = choochoo_path+"./instructor/settings.yml"

student_issue_template_path = choochoo_path+"./.github/ISSUE_TEMPLATE/choochoo-student-thread.md"
question_issue_template_path = choochoo_path+"./.github/ISSUE_TEMPLATE/choochoo-questions.yml"

objectives_header_path = choochoo_path+"./instructor/objectives_header.md"
objectives_yml_path = choochoo_path+"./instructor/objectives.yml"

question_folder_path = choochoo_path+"./questions/"
question_bank_path = choochoo_path+question_folder_path+"question_bank"
question_bank_yml_path = choochoo_path+question_folder_path+"question_bank.yml"
question_bank_markdown_path = choochoo_path+question_folder_path+"question_bank.md"

output_plot_path = choochoo_path+"./plots/summary_plot.png"
