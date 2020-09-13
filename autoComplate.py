from Data import data


class AutoCompleteData:

    def __init__(self, complated_sentences, source_text, offset, score):
        self.completed_sentence: str = complated_sentences
        self.source_text: str = source_text
        self.offset: int = offset
        self.score: int = score

    def __eq__(self, other):
        if self.completed_sentence != other.completed_sentence:
            return False
        if self.source_text != other.source_text:
            return False
        if self.offset != other.offset:
            return False
        return True


alphabet = "abcdefghijklmnopqrstuvwxyz "


def push_list_to_list(auto_complete_list, new_list):
    for item in new_list:
        if item not in auto_complete_list:
            auto_complete_list.append(item)

        if len(auto_complete_list) == 5:
            return auto_complete_list

    return auto_complete_list


def get_with_change(substring, index):
    for char in alphabet:
        new_substring = substring[:index] + str(char) + substring[index + 1:]
        yield new_substring

    yield StopAsyncIteration


def get_with_add(substring, index):
    substring = substring[:index + 1] + "$" + substring[index + 1:]
    return iter(get_with_change(substring, index + 1))


def get_with_delete(substring, index):
    yield substring[:index] + substring[index + 1:]


def get_auto_completions_list(substring, score):
    completed_sentences_id = list(data.find(substring))
    auto_complete = []
    for id in completed_sentences_id:
        auto = AutoCompleteData(data.get_sentence(id),
                                data.get_url(id),
                                data.get_offset(id), score)
        auto_complete.append(auto)
    return auto_complete


def next_substring(substring):
    start = 0
    end = len(substring)
    index = 0
    while index < end:
        if len(data.find(substring[:index])) == 0:
            end = index
        if len(data.find(substring[index + 1:])) == 0:
            start = index
        index += 1

    functions_list = [
        {"score_to_sub": 2, "indexes": (i for i in range(max(start, 4), end)), "func": get_with_add},
        {"score_to_sub": 3, "indexes": (i for i in range(max(start, 4), end)), "func": get_with_change},
        {"score_to_sub": 4, "indexes": (i for i in range(max(start, 4), end)), "func": get_with_delete},

    ]

    for type_substring in functions_list:
        for index in type_substring["indexes"]:
            for new_substring in type_substring["func"](substring, index):
                yield new_substring, type_substring["score_to_sub"]

    functions_list = [
        {"score": 4, "indexes": (3, 3), "func": (get_with_change, get_with_add)},
        {"score": 5, "indexes": (2,), "func": (get_with_change,)},
        {"score": 6, "indexes": (3, 2, 1), "func": (get_with_delete, get_with_add, get_with_change)},
        {"score": 7, "indexes": (0,), "func": (get_with_change,)},
        {"score": 8, "indexes": (2, 1), "func": (get_with_delete, get_with_add)},
        {"score": 10, "indexes": (1, 0), "func": (get_with_delete, get_with_add)},
        {"score": 12, "indexes": (0,), "func": (get_with_delete,)}
    ]

    for list_ in functions_list:
        for index, func_ in zip(list_["indexes"], list_["func"]):
            for new_substring in func_(substring, index):
                yield new_substring, list_["score"]


def get_best_k_completions(prefix):  # ->
    score = len(prefix) * 2
    auto_complete_sentences = get_auto_completions_list(prefix, score)
    if len(auto_complete_sentences) == 5:
        return auto_complete_sentences
    for new_substring, score_to_sub in next_substring(prefix):
        completed_sentences = get_auto_completions_list(new_substring, score - score_to_sub)
        auto_complete_sentences = push_list_to_list(auto_complete_sentences, completed_sentences)
        if len(auto_complete_sentences) == 5:
            return auto_complete_sentences
    return auto_complete_sentences


def print_best_k_completions(list_: AutoCompleteData):
    for i, item in enumerate(list_):
        print(f"{i + 1}) ", item.completed_sentence, f"( {item.source_text} )", item.offset,
              item.score)  # צריך להדפיס URL
