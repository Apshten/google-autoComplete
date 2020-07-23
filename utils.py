import re


def clear_string(string):
    string = string.lower().replace("  ", " ")
    return re.sub(r'[^a-z0-9 ]', '', string)