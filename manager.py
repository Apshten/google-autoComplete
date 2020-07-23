from terminals import terminal
from data import data


def manager():
    load_data()
    print("begin")
    terminal()


def load_data():
    # list_ = [
    #     ["To be or not to be, that's the question", "dir1/dir2/file1", 0]
    #     , ["We are waiting for it to work...", "dir3/file2", 1]
    #     , ["To be or not to be, that's the question1", "dir1/dir2/file1", 2]
    #     , ["We are waiting for it to work...1", "dir3/file2", 3]
    #     , ["We are waiting for it to work...2", "dir3/file2", 4]
    #     , ["ae are waiting for it to work...2", "dir3/file2", 5]
    #     , ["for it to work", "dir3/file2", 6]
    #     , ["Hello", "dir3/file2", 7]
    #
    # ]
    list_ = [
        ("We are waiting for it to work...", "dir3/file2", 0),
        ("To be or not to be, that's the question", "dir1/dir2/file1", 1),
        ("hello world1", "dir1/dir2/file1", 2),
        ("hello world2", "dir1/dir2/file1", 3),
        ("hello world3", "dir1/dir2/file1", 4),
        ("hello world4", "dir1/dir2/file1", 5)
    ]
    list_ = sorted(list_, key=lambda x: x[0].lower())
    for item in list_:
        data.insert(item[1], item[0], item[2])
