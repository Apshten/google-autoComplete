
class StringDescribe:
    def __init__(self, id_sentence, offset):
        self.__id_sentence = id_sentence
        self.__offset = offset

    def get_id(self):
        return self.__id_sentence

    def get_offset(self):
        return self.__offset
