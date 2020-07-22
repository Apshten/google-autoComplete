from data import Data, stringsData, clear_string


class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.__completed_sentence: str = completed_sentence
        self.__source_text: str = source_text
        self.__offset: int = offset
        self.__score: int = score

    def get_source_text(self):
        return self.__source_text

    def get_completed_sentence(self):
        return self.__completed_sentence


data = Data()


def get_best_k_completions(prefix: str):
    list_ = list(data.find(prefix))
    list_auto_completeData = []
    for item in list_:
        auto = AutoCompleteData(data.get_sentence(item.get_id()), data.get_url(item.get_id()), item.get_offset(),
                                len(prefix) * 2)
        list_auto_completeData.append(auto)
    return list_auto_completeData


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


def print_best_k_completions(list_):
    for i, item in enumerate(list_):
        print(f'{i+1}) {item.get_completed_sentence()} ( {item.get_source_text()} ) ')


def terminal():
    while 1:
        print(">>> ", end=" ")
        for string in get_input():
            the_best = get_best_k_completions(string)
            # if len(the_best) < 5:
            # Corrections(string, the_best)
            print_best_k_completions(the_best)
            print(">>> ", end=" ")


def manager():
    load_data()
    terminal()


def load_data():
    list_ = [
        ["To be or not to be, that's the question", "dir1/dir2/file1"]
        , ["We are waiting for it to work...", "dir3/file2"]
        , ["To be or not to be, that's the question1", "dir1/dir2/file1"]
        , ["We are waiting for it to work...1", "dir3/file2"]
        , ["We are waiting for it to work...2", "dir3/file2"]
        , ["ae are waiting for it to work...2", "dir3/file2"]
        , ["for it to work", "dir3/file2"]

    ]

    list_ = sorted(list_, key=lambda x: x[0].lower())

    for item in list_:
        data.insert(item[1], item[0])


# def Corrections(string, list_):
#     i = len(string) - 1
#     while len(list_) < 5:
#         list_1 = deleting_character(string, i)
#         for item in list_:
#             if item
#
#
# def deleting_character(string: str, index):
#     string = string[:index]
#     return get_best_k_completions(string)


manager()
