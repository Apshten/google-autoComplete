from utils import clear_string
from collections import defaultdict


class stringsData:
    def __init__(self):
        self.__dict = defaultdict(list)
        self.__max_list_value_dict = 5

    def find(self, string):
        list_ = self.__dict.get(string)
        if not list_:
            return list()
        return list_[:]

    def __push_item(self, new_item, list_):
        # temp = [item.get_id() for item in list_]
        # id_ = new_item.get_id()
        if new_item in list_ or len(list_) == self.__max_list_value_dict:
            return list_
        list_.append(new_item)

    def insert(self, string, id_):
        list_ = self.find(string)
        if len(list_) == 0:
            self.__dict[clear_string(string)].append(id_)
        else:
            self.__push_item(id_, self.__dict[clear_string(string)])


class SentenceData:
    def __init__(self):
        self.__list = []

    def insert(self, value):
        self.__list.append(value)
        return len(self.__list) - 1

    def get_sentence(self, id_):
        return self.__list[id_][0]

    def get_url(self, _id):
        return self.__list[_id][1]

    def get_offset(self, _id):
        return self.__list[_id][2]

    def sort(self):
        self.__list = sorted(self.__list, key=lambda x: x[0].lower())


class Data:
    def __init__(self):
        self.__string_data = stringsData()
        self.__sentences_data = SentenceData()

    def insert(self, url, sentence, offset):
        sentence_describe = clear_string(sentence)
        id_ = self.__sentences_data.insert((sentence, url, offset))
        for i in range(len(sentence_describe)):
            for j in range(i):
                self.__string_data.insert(sentence_describe[j:i], id_)

    def find(self, string: str):
        return self.__string_data.find(string)

    def get_sentence(self, id_):
        return self.__sentences_data.get_sentence(id_)

    def get_url(self, _id):
        return self.__sentences_data.get_url(_id)

    def get_offset(self, _id):
        return self.__sentences_data.get_offset(_id)

    def get_sentences(self):
        return self.__sentences_data


data = Data()
