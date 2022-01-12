"""
A module for reading and writing to the settings yml file.
"""
import os
import yaml  # Pyyaml
from choochoo import definitions, ROOT_DIR

def get_settings():
  settings_path = os.path.join(ROOT_DIR, "instructor", "settings.yml")
  with open(settings_path, "r") as stream:
    return yaml.safe_load(stream)
  
def write_settings(settings_dict):
  settings_path = os.path.join(ROOT_DIR, "instructor", "settings.yml")
  with open('file_to_edit.yaml', 'w') as stream:
    yaml.dump(settings_dict, stream)
  
def get_project_repo():
  settings = get_settings()
  return settings["project_repo"]

def set_project_repo(project_repo):
  settings = get_settings()
  settings["project_repo"] = project_repo
  write_settings(settings)

def get_project_title():
  settings = get_settings()
  return settings["project_title"]

def set_project_title(project_title):
  settings = get_settings()
  settings["project_title"] = project_title
  write_settings(settings)

def get_admins():
  settings = get_settings()
  return settings["admins"]

def set_admins(handles: list[str]) -> None:  
  settings = get_settings()
  settings["admins"] = handles
  write_settings(settings)
  
def add_admins(handles: list[str]) -> None:  # include check to see if admin already in list?
  settings = get_settings()
  settings["admins"] = settings["admins"] + handles
  write_settings(settings)
  
def remove_admins(handles: list[str]) -> None:
  settings = get_settings()
  settings["admins"] = [handle for handle in settings["admins"] if handle not in handles]
  write_settings(settings)

def get_instructors():
  settings = get_settings()
  return settings["instructors"]

def set_instructors(handles: list[str]) -> None:  
  settings = get_settings()
  settings["instructors"] = handles
  write_settings(settings)
  
def add_instructors(handles: list[str]) -> None:  # include check to see if admin already in list?
  settings = get_settings()
  settings["instructors"] = settings["instructors"] + handles
  write_settings(settings)
  
def remove_instructors(handles: list[str]) -> None:
  settings = get_settings()
  settings["instructors"] = [handle for handle in settings["instructors"] if handle not in handles]
  write_settings(settings)

def get_students():
  settings = get_settings()
  return settings["students"]

def set_students(handles: list[str]) -> None:  
  settings = get_settings()
  settings["students"] = handles
  write_settings(settings)
  
def add_students(handles: list[str]) -> None:  # include check to see if admin already in list?
  settings = get_settings()
  settings["students"] = settings["students"] + handles
  write_settings(settings)
  
def remove_students(handles: list[str]) -> None:
  settings = get_settings()
  settings["students"] = [handle for handle in settings["students"] if handle not in handles]
  write_settings(settings)
  
  

