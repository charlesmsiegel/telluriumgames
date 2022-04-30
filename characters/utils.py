from random import choice

def weighted_choice(dictionary):
    l = []
    for key, value in dictionary.items():
        for _ in range(value+1):
            l.append(key)
    return choice(l)
