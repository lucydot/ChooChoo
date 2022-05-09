"""
A module for reading environment variables
"""
import os
import dotenv
import sys
from choochoo import paths

class Env:

	def __init__(self):

		try:
			self.issue_number = self.issue_number()
		except BaseException as error:
			pass
		try:
			self._token = self._token()
		except BaseException as error:
			pass
		try:
			self.repo_name = self.repo_name()
		except BaseException as error:
			pass
		try:
			self.github_actor = self.github_actor()
		except BaseException as error:
			pass


	def getenv(self,variable):
	    dotenv.load_dotenv(paths.env_path)  
	    if os.getenv(variable) is None:
	    	sys.exit("Environment variable {} not found.".format(variable))
	    else:
	    	return os.getenv(variable)

	def issue_number(self):
		"Get issue number"
		return int(self.getenv("ISSUE_NUMBER"))
	    
	def _token(self):
		"Get gh token, needed for the PyGithub API"
		return self.getenv("GH_TOKEN")

	def repo_name(self):
		"Get repository in name/repo format"
		return self.getenv("GITHUB_REPOSITORY")

	def github_actor(self):
		"Get the user who triggered the action"
		return self.getenv("GITHUB_ACTOR")

