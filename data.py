import re
from collections import defaultdict
from string_describe import StringDescribe
from sentence_describe import SentenceDescribe


class stringsData:
    def __init__(self):
        self.__dict = defaultdict(list)

    def find(self, string):
        list_ = self.__dict.get(string)
        if not list_:
            return list()
        return list_

    def insert(self, key, value, id_):
        list_ = []
        string_describe = StringDescribe(id_, value)
        self.__dict[key] = list_.append(string_describe)


class SentenceData:
    def __init__(self):
        self.__list = []

    def insert(self, value):
        self.__list.append(value)
        return len(self.__list)-1

    def get_sentence(self, id_):
        return self.__list[id_].get_string()


class Data:
    def __init__(self):
        self.__string_data = stringsData()
        self.__sentences_data = SentenceData()

    def insert(self,  url, sentence):
        sentence_describe = SentenceDescribe(url, sentence)
        id_ = self.__sentences_data.insert(sentence_describe)
        for i in range(len(sentence)):
            for j in range(i):
                self.__string_data.insert(sentence[j:i], j, id_)

    def find(self, string: str):
        return self.__string_data.find(string)

    def get_sentence(self, id_):
        return self.__sentences_data.get_sentence(id_)


# class AutoCompleteData:
#     completed_sentence: str
#     source_text: str
#     offset: int
#     score: int


class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.__completed_sentence: str = completed_sentence
        self.__source_text: str = source_text
        self.__offset: int = offset
        self.__score: int = score


data = Data()


# def get_best_k_completions(prefix: str):  # ->
#     list_ = data.find(prefix)
#     auto_complate = []
#     for item in list_:
#         auto = AutoCompleteData()
#         auto.source_text = (data.get_sentence(item.get_id()))
#         auto_complate.append(item)
#     return auto_complate[:5]


def get_best_k_completions(prefix: str):
    list_ = list(data.find(prefix))
    list_auto_completeData = []
    for i in list_:
        auto = AutoCompleteData(prefix, data.get_sentence(i.get_id()), i.get_offset, len(prefix) * 2)
        list_auto_completeData.append(auto)
    return list_auto_completeData[:5]


def clear_string(string):
    wordLower = string.lower()
    wordLower = re.sub(r'[^a-z]', '', wordLower)
    return wordLower


def get_input():
    string = ""
    new_input = input()
    while new_input == "":
        new_input = input()
    while new_input == "" or new_input[len(new_input) - 1] != '#':
        string += clear_string(new_input)
        yield string
        new_input = input()

    # string = ""
    # new_input = input()
    # while new_input == "" or new_input[len(new_input)-1] != '#':
    #     new_input = input()
    #     print("pppp")
    #
    # while new_input[len(new_input) - 1] != '#':
    #     print("iiii")
    #     string += new_input
    #     print("iiii")
    #     yield string
    #     new_input = input()


def print_best_k_completions(list_):
    for item in list_:
        print(item.completed_sentence)  # צריך להוסיף הדפסה של url


def terminal():
    while 1:
        for string in get_input():
            the_best = get_best_k_completions(string)
            print_best_k_completions(the_best)


def manager():
    load_data()
    terminal()


def load_data():
    list_ = [["To be or not to be, that's the question", "dir1/dir2/file1"]
        , ["We are waiting for it to work...", "dir3/file2"]]
    for item in list_:
        data.insert(item[1], item[0])


manager()
