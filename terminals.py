from autoCompleteData import print_best_k_completions, get_best_k_completions
from utils import clear_string
import datetime


def terminal():
    while 1:
        print(">>> ", end=" ")
        for string in get_input():
            print(datetime.datetime.now())
            the_best = get_best_k_completions(string)
            print_best_k_completions(the_best)
            print(datetime.datetime.now())
            print(">>> ", end=" ")


def get_input():
    string = ""
    new_input = input(string)
    while new_input == "":
        new_input = input(string)

    while new_input == "" or new_input[len(new_input) - 1] != '#':
        string += new_input
        yield clear_string(string)
        new_input = input(string)


