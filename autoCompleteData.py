from data import data


class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence: str = completed_sentence
        self.source_text: str = source_text
        self.offset: int = offset
        self.score: int = score

    def get_source_text(self):
        return self.source_text

    def get_completed_sentence(self):
        return self.completed_sentence

    def get_score(self):
        return self.score

    def get_offset(self):
        return self.offset

    def __eq__(self, other):
        if self.completed_sentence != other.completed_sentence:
            return False
        if self.source_text != other.source_text:
            return False
        if self.offset != other.offset:
            return False
        return True


alphabet = "abcdefghijklmnopqrstuvwxuz "


# def get_score_after_exchange(index):
#     if index <= 4:
#         return 12 - 2 * index
#     return 2
#
#
# def get_score_after_add_or_delete(index):
#     if index <= 4:
#         return 6 - index
#     return 1


def push_list_to_list(auto_complete_list, new_list):
    for item in new_list:
        if item not in auto_complete_list:
            auto_complete_list.append(item)
        if len(auto_complete_list) == 5:
            return auto_complete_list
    return auto_complete_list


def get_with_exchange(substring, auto_complete_list, index, reduction_in_score):
    if index != 0 and len(data.find(substring[:index])) == 0:
        return auto_complete_list

    if index != len(substring) - 1 and len(data.find(substring[index + 1:])) == 0:
        return auto_complete_list

    for char in alphabet:
        substring = substring[:index] + str(char) + substring[index + 1:]
        completed_sentences = get_perfect_completions(substring)
        for item in completed_sentences:
            item.score -= reduction_in_score
        auto_complete_list = push_list_to_list(auto_complete_list, completed_sentences)
        if len(auto_complete_list) == 5:
            return auto_complete_list

    return auto_complete_list


def get_with_add(substring, auto_complete_list, index, reduction_in_score):
    if index != 0 and len(data.find(substring[:index])) == 0:
        return auto_complete_list

    if index != len(substring) - 1:
        return auto_complete_list

    for char in alphabet:
        substring = substring[:index + 1] + str(char) + substring[index + 1:]
        completed_sentences = get_perfect_completions(substring)
        for item in completed_sentences:
            item.score -= reduction_in_score
        if len(auto_complete_list) == 5:
            return auto_complete_list

    return auto_complete_list


def get_with_delete(substring, auto_complete_list, index, reduction_in_score):
    if index != 0 and len(data.find(substring[:index])) == 0:
        return auto_complete_list

    if index != len(substring) - 1 and len(data.find(substring[index + 1:])) == 0:
        return auto_complete_list

    substring = substring[:index] + substring[index + 1:]
    completed_sentences = get_perfect_completions(substring)
    for item in completed_sentences:
        item.score -= reduction_in_score
    auto_complete_list = push_list_to_list(auto_complete_list, completed_sentences)
    if len(auto_complete_list) == 5:
        return auto_complete_list
    return auto_complete_list


def get_perfect_completions(substring):
    completed_sentences = list(data.find(substring))
    auto_complete = []
    for item in completed_sentences:
        auto = AutoCompleteData(data.get_sentence(item),
                                data.get_url(item),
                                data.get_offset(item),
                                len(substring) * 2)
        auto_complete.append(auto)
    return auto_complete


# def get_sub_score(add_index, delete_index, exchange_index):
#     return get_score_after_add_or_delete(add_index), \
#            get_score_after_add_or_delete(delete_index), \
#            get_score_after_exchange(exchange_index)


def get_best_k_completions(prefix):
    auto_complete_sentences = get_perfect_completions(prefix)
    length = len(prefix)

    for i in range(4, length):
        if len(auto_complete_sentences) != 5:
            auto_complete_sentences = get_with_exchange(prefix, auto_complete_sentences, i, 1)
        else:
            return auto_complete_sentences

    for i in range(4, length):
        if len(auto_complete_sentences) != 5:
            auto_complete_sentences = get_with_delete(prefix, auto_complete_sentences, i, 2)
        else:
            return auto_complete_sentences

    for i in range(4, length):
        if len(auto_complete_sentences) != 5:
            auto_complete_sentences = get_with_add(prefix, auto_complete_sentences, i, 2)
        else:
            return auto_complete_sentences

    function_tuple = [
        [2, (3,), (get_with_exchange,)],
        [3, (2, 2), (get_with_delete, get_with_add)],
        [4, (3, 1, 1), (get_with_exchange, get_with_delete, get_with_add)],
        [5, (0, 0), (get_with_delete, get_with_add)],
        [6, (2,), (get_with_exchange,)],
        [8, (1,), (get_with_exchange,)],
        [10, (0,), (get_with_exchange,)]
    ]

    for list_ in function_tuple:
        for index, func in zip(list_[1], list_[2]):
            if len(auto_complete_sentences) != 5:
                auto_complete_sentences = func(prefix, auto_complete_sentences, index, list_[0])
            else:
                return auto_complete_sentences
    return auto_complete_sentences


def print_best_k_completions(list_):
    for i, item in enumerate(list_):
        print(f'{i + 1}) {item.get_completed_sentence()} ( {item.get_source_text()} )', item.get_offset())
