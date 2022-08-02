import cProfile
import pstats
from pstats import SortKey
from time import time

from django.contrib.auth.models import User

player, _ = User.objects.get_or_create(username="Test")

from wod.models.characters.human import Human
from wod.models.characters.mage import Mage, Rote
from wod.models.characters.werewolf import Werewolf
from wod.models.items.mage import Grimoire
from wod.models.locations.mage import Chantry, Node


def time_test(cls, character=True, xp=0):
    start = time()
    for _ in range(10):
        create_character(cls, character=character, xp=xp)
    print(f"Average Random {cls.__name__} Time:", (time() - start) / 10)


def create_character(cls, character=True, xp=0):
    if character:
        obj = cls.objects.create(
            name=f"{cls.__name__} {cls.objects.count()}", player=player
        )
        obj.random(xp=xp)
    else:
        obj = cls.objects.create(name=f"{cls.__name__} {cls.objects.count()}")
        obj.random()
    obj.save()


def profile(cls, character=True, num_rows=10, xp=0):
    cProfile.run(
        f"create_character({cls.__name__}, character={character}, xp={xp})", "tmp"
    )
    p = pstats.Stats("tmp")
    p.sort_stats(SortKey.CUMULATIVE).print_stats(num_rows)


time_test(Human)
time_test(Werewolf)
time_test(Mage)
time_test(Node, character=False)
time_test(Chantry, character=False)
time_test(Grimoire, character=False)

from cod.models.characters.mage import Mage, Proximi, ProximiFamily
from cod.models.characters.mortal import Mortal

time_test(Mortal)
time_test(Mage)
time_test(ProximiFamily, character=False)
time_test(Proximi)

from tc.models.characters.aberrant import Aberrant
from tc.models.characters.human import Human
from tc.models.characters.talent import Talent

time_test(Human)
time_test(Talent, xp=50)
time_test(Aberrant, xp=150)

from exalted.models.characters.mortals import ExMortal

time_test(ExMortal)
