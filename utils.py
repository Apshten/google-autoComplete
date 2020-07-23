import re


def clear_string(string):
    string = re.sub(" +", " ", string.lower())
    return re.sub(r'[^a-z0-9 ]', '', string)
