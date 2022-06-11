from random import choice, randint


def check_floor_ceiling(x, floor, ceiling):
    if x < floor:
        return floor
    if x > ceiling:
        return ceiling
    return x

def weighted_choice(dictionary, floor=0, ceiling=5):
    d = {k: check_floor_ceiling(v, floor=floor, ceiling=ceiling) for k, v in dictionary.items()}
    l = []
    for key, value in d.items():
        for _ in range(value + 1):
            for __ in range(value + 1):
                l.append(key)
    return choice(l)


def cod_dice(number_of_dice, again_minimum=10):
    if number_of_dice < 0:
        chance_die = randint(1, 10)
        if chance_die == 1:
            return chance_die, -1
        if chance_die == 10:
            return chance_die, 1
        return chance_die, 0
    roll = [randint(1, 10) for _ in range(number_of_dice)]
    num_agains = sum(x >= again_minimum for x in roll)
    while num_agains > 0:
        new_dice = [randint(1, 10) for _ in range(num_agains)]
        roll.extend(new_dice)
        num_agains = sum(x >= again_minimum for x in new_dice)
    return roll, sum(x >= 8 for x in roll)


def add_dot(character, trait, maximum):
    if getattr(character, trait) < maximum:
        setattr(character, trait, getattr(character, trait) + 1)
        character.save()
        return True
    return False
