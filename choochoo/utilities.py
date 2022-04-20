""" A module containing helper functions used by the other choochoo modules
"""

def read_yaml(self,pathname):

        with open(pathname, "r") as stream:
            try:
                dictionary = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

        return dictionary

