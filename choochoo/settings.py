"""
A module for reading and writing to the settings yml file.
"""
import os
from choochoo import definitions, ROOT_DIR

def get_settings_path():
  return os.path.join(ROOT_DIR, 'instructor', 'settings.yml')

def get_project_repo():
  pass

