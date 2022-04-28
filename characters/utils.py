from random import choice


def weighted_choice(dictionary):
    """
    Takes a dictionary of strings -> int and chooses a key at random based on the values
    """
    choice_list = []
    for key in dictionary.keys():
        for _ in range(dictionary[key] + 1):
            choice_list.append(key)

    return choice(choice_list)
