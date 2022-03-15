from choochoo import repository
from choochoo import question_bank_path

class Question_bank():

	def __init__(self):

		self.repository = repository.Repository()

	def get_dictionary(self):

		bank_file = self.repository.pygh_repo.get_contents(question_bank_path, ref="main")
        question_bank_string = bank_file.decoded_content.decode()
        return yaml.safe_load(question_bank_string)
