from Data import data
from run import run
import os


def load_data():
    data.load_from_file("data.json")
    count = 0
    for root, dirs, files in os.walk("./technology_texts"):
        for file in files:
            if file.endswith(".txt"):
                count += 1
                print("file ", count)
                data.fill_sentences(os.path.join(root, file))
    # data.fill_substrings_dict()
    # data.load_to_file("data.json")


def manager():
    load_data()
    print("let start:")
    run()

