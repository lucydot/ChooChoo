"""A simple command line interface for choochoo.

Contains the single function `interface`.
"""
import re
from sys import argv

from choochoo import management, delivery

def interface():
  """ This function interfaces between the user and the choochoo package.
  Choochoo receives and sends messages using comments on a Github issue thread.
  
  It takes user sub-commands and parses them as a complete sentence. 
  It matches this sentence to one within a pre-defined list, 
  and then calls other choochoo functions as appropriate. 
  If it does not match the sentence then a message is returned to the user.
  """
  
  command = ' '.join(argv[1:])
  
  # returns true if the command string matches the argument string
  command_matches = lambda string: bool(re.match(string, command))
  
  if command_matches("check (@\w+) is instructor"):
    handle = argv[2]
    if management.check_instructor(handle):
      issues.make_comment(handle," is an instructor")
    else:
      issues.make_comment(handle," is not an instructor")
    
  elif command_matches("check (@\w+) is admin"):
    handle = argv[2]
    if management.check_admin(handle):
      issues.make_comment(handle," is an admin")
    else:
      issues.make_comment(handle," is not an admin")
    
  elif command_matches("check (@\w+) is student"):
    handle = argv[2]
    if management.check_student(handle):
      issues.make_comment(handle," is a student")
    else:
      issues.make_comment(handle," is not a student")
    
    
  
