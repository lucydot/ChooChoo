import os

__version__ = "0.0.1"

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
settings_path = "./instructor/settings.yml"
issue_template_path = os.path.join(ROOT_DIR, "./.github/ISSUE_TEMPLATE/choochoo-student-thread.md")
objectives_header_path = os.path.join(ROOT_DIR, "./instructor/objectives_header.md")
objectives_path = os.path.join(ROOT_DIR, "./instructor/objectives.yml")
