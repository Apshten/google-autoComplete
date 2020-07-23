from terminals import terminal
from data import data


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
        , ["Hello", "dir3/file2"]

    ]

    list_ = sorted(list_, key=lambda x: x[0].lower())

    for item in list_:
        data.insert(item[1], item[0])


