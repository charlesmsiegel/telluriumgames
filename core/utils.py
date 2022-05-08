from random import choice, randint


def weighted_choice(dictionary, ceiling=3):
    d = {k: min(v, ceiling) for k, v in dictionary.items()}
    l = []
    for key, value in d.items():
        for _ in range(value + 1):
            l.append(key)
    return choice(l)


def cod_dice(number_of_dice, again_minimum=10):
    if number_of_dice < 0:
        chance_die = randint(1, 11)
        if chance_die == 1:
            return chance_die, -1
        if chance_die == 10:
            return chance_die, 1
        return chance_die, 0
    roll = [randint(1, 11) for _ in range(number_of_dice)]
    num_agains = sum([x >= again_minimum for x in roll])
    while num_agains > 0:
        new_dice = [randint(1, 11) for _ in range(num_agains)]
        roll.extend(new_dice)
        num_agains = sum([x >= again_minimum for x in new_dice])
    return roll, sum([x >= 8 for x in roll])


def add_dot(character, trait, maximum):
    if getattr(character, trait) < maximum:
        setattr(character, trait, getattr(character, trait) + 1)
        character.save()
