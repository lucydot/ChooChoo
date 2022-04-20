#import os

__version__ = "0.0.1"

#ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
settings_path = "./instructor/settings.yml"
issue_template_path = "./.github/ISSUE_TEMPLATE/choochoo-student-thread.md"
question_issue_template_path = "./github/ISSUE_TEMPLATE/choochoo-questions.yml"
objectives_header_path = "./instructor/objectives_header.md"
objectives_path = "./instructor/objectives.yml"
env_path = None # defaults to project root when set to None
question_bank_path = "./questions/question_bank.yml"
question_bank_markdown_path = "./questions/question_bank.md"
output_plot_path = "./plots/summary_plot.png"
question_folder_path = "./folders/"