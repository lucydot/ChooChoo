"""A simple command line interface for choochoo.

Contains the single function `interface`.
"""
import re
from sys import argv

from choochoo import management, delivery

def interface():
  """ This function interfaces between the user and the choochoo package.
  
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
    management.check_instructor(handle)
    
  elif command_matches("check (@\w+) is admin"):
    handle = argv[2]
    management.check_admin(handle)
    
  elif command_matches("check (@\w+) is student"):
    handle = argv[2]
    management.check_student(handle)
    
    
  
