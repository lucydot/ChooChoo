""" A module containing helper functions used by the other choochoo modules
"""

def read_yaml(self,pathname):

    with open(pathname, "r") as stream:
        try:
                dictionary = yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
                print(exc)

    return dictionary

def string_to_anchor_link(input_string):

    s = input_string.translate(str.maketrans('', '', string.punctuation))
    anchor_string = "-".join(s.lower().split())
    return "(#"+anchor_string+")"

