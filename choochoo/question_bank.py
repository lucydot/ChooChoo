import yaml
from choochoo import question_bank_path, question_bank_markdown_path, question_folder_path, utilities

class QuestionBank:
    """ A class for manipulating the question_bank and converting between yaml (for data storage)
                                and markdown (for web publication).

    Note that individual questions are read and edited using the class `choochoo.question.Question`."""


    def __init__(self,repository):

        self.repository = repository
        self.path = question_bank_path
        self.dictionary_list = self.get_dictionary_list()

    def get_dictionary_list(self):

        dictionary_string = self.repository.file_content(self.path)
        return yaml.safe_load(dictionary_string)  # could this be done as in objectives.get_objective_dict?

    def get_question_titles(self):

        return [entry["title"] for entry in self.dictionary_list]

    def build_bank_markdown(self):
        """convert the question bank yml file into markdown"""

        dictionary_list = self.get_dictionary_list()

        import matplotlib.pyplot as plt
        plt.plot([2,3],[3,7])
        plt.savefig("./plots/test.png")

        with open(question_bank_markdown_path, 'w') as f:
            for question_dict in dictionary_list:
                f.write("## "+question_dict["title"]+utilities.string_to_anchor_link(question_dict["title"])+"\n")
                f.write("#### authors: "+" ".join(question_dict["authors"])+"\n")
                f.write("#### checklist items: "+" ".join(question_dict["checklist_items"])+"\n")
                f.write(question_dict["question"]+"\n")
                f.write("<details>\n<summary>Answer</summary>\n")
                f.write(question_dict["answer"]+"\n</details>")
                f.write("\n\n")

    def question_dict_as_markdown(self, f, question_dict):

        f.write("## "+question_dict["title"]+utilities.string_to_anchor_link(question_dict["title"])+"\n")
        f.write("#### authors: "+" ".join(question_dict["authors"])+"\n")
        f.write("#### checklist items: "+" ".join(question_dict["checklist_items"])+"\n")
        f.write(question_dict["question"]+"\n")
        f.write("<details>\n<summary>Answer</summary>\n")
        f.write(question_dict["answer"]+"\n</details>")
        f.write("\n\n")


    def questions_from_objectives_list(self, objectives_list):
        """return a list of question dictionaries which contain objectives
            in `objectives_list`.
        """

        question_list = []
        for objective in objectives_list:
                for question in self.dictionary_list:
                        if objective in question["checklist_items"]:
                                question_list.append(question)

        return question_list

    def build_user_markdown(self,question_list,author):
        """convert a list of question dictionaries into markdown
        and save as `./questions/username.md`"""

        with open(question_folder_path+author+".md","w") as f:
                for entry in question_list:
                        self.question_dict_as_markdown(f,entry)






