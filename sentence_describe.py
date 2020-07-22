class SentenceDescribe:
    def __init__(self, url, string):
        self.__url = url
        self.__string = string

    def get_url(self):
      return self.__url

    def get_string(self):
        return self.__string
