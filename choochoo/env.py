"""
A module for reading environment variables
"""
import os
import dotenv
import sys

def getenv(variable,filepath=None):
    dotenv.load_dotenv(filepath)  
    if os.getenv(variable) is None:
    	sys.exit("Environment variable {} not found.".format(variable))
    else:
    	return os.getenv(variable)

def issue_number():
	"Get issue number"
	return int(getenv("ISSUE_NUMBER"))
    
def _token():
	"Get gh token, needed for the PyGithub API"
	return getenv("GH_TOKEN")

def repo_name():
	"Get repository in name/repo format"
	return getenv("GITHUB_REPOSITORY")

def github_actor():
	"Get the user who triggered the action"
	return getenv("GITHUB_ACTOR")

