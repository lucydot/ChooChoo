"""
A module for choochoo project management.

A collection of admin functions.
"""
import github
import dotenv 

from choochoo import settings


def get_token():
  "Get gh token, needed for the PyGithub API"
  
  dotenv.load_dotenv()
  return os.getenv("GH_TOKEN")

def get_repo(GH_TOKEN):
  "Get a repo object using PyGithubAPI"
  
  project_repo = settings.get_project_repo()
  g = github.Github(GH_TOKEN)
  return g.get_repo(project_repo)
  
def check_instructor(handle):
  pass

def check_admin(handle):
  pass

def check_student(handle):
  pass
