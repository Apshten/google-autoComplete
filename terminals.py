from autoCompleteData import print_best_k_completions, get_best_k_completions
from utils import clear_string


def terminal():
    while 1:
        print(">>> ", end=" ")
        for string in get_input():
            the_best = get_best_k_completions(string)
            # if len(the_best) < 5:
            # Corrections(string, the_best)
            print_best_k_completions(the_best)
            print(">>> ", end=" ")


def get_input():
    string = ""
    stringTemp = ""
    new_input = input(stringTemp)
    while new_input == "":
        new_input = input(stringTemp)
    while new_input == "" or new_input[len(new_input) - 1] != '#':
        string += clear_string(new_input)
        stringTemp += new_input
        yield string
        new_input = input(stringTemp)


