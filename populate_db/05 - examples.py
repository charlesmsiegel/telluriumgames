import cProfile
import pstats
from pstats import SortKey
from time import time

from django.contrib.auth.models import User

player, _ = User.objects.get_or_create(username="Test")


def time_test(cls, character=True, xp=0, random_name=True):
    start = time()
    for _ in range(10):
        create(cls, character=character, xp=xp, random_name=random_name)
    print(f"Average Random {cls.__name__} Time:", (time() - start) / 10)


def create(cls, character=True, xp=0, random_name=True):
    if random_name:
        name = ""
    else:
        name = f"{cls.__name__} {cls.objects.count()}"
    obj = cls.objects.create(name=name, owner=player)
    if character:
        obj.random(xp=xp)
    else:
        obj.random()
    obj.save()


def profile(cls, character=True, num_rows=10, xp=0):
    cProfile.run(f"create({cls.__name__}, character={character}, xp={xp})", "tmp")
    p = pstats.Stats("tmp")
    p.sort_stats(SortKey.CUMULATIVE).print_stats(num_rows)


from wod.models.characters.changeling import Changeling, Motley
from wod.models.characters.human import Human
from wod.models.characters.mage import Cabal, Mage
from wod.models.characters.werewolf import Fomor, Kinfolk, Pack, Werewolf
from wod.models.items.mage import Artifact, Charm, Grimoire, Talisman
from wod.models.locations.mage import Chantry, Library, Node

time_test(Human)
time_test(Kinfolk)
time_test(Fomor)
time_test(Werewolf)
time_test(Mage)
time_test(Changeling)
time_test(Cabal)
time_test(Pack)
time_test(Motley)
time_test(Node, character=False)
time_test(Chantry, character=False)
time_test(Library, character=False)
time_test(Grimoire, character=False)
time_test(Charm, character=False)
time_test(Artifact, character=False)
time_test(Talisman, character=False)

from cod.models.characters.ephemera import Ephemera
from cod.models.characters.mage import Mage as CoDMage
from cod.models.characters.mage import Proximi, ProximiFamily
from cod.models.characters.mortal import Mortal

time_test(Mortal)
time_test(Ephemera, character=False)
time_test(CoDMage)
time_test(ProximiFamily, character=False)
time_test(Proximi)

from tc.models.characters.aberrant import Aberrant
from tc.models.characters.human import Human as TCHuman
from tc.models.characters.talent import Talent

time_test(TCHuman)
time_test(Talent, xp=50)
time_test(Aberrant, xp=150)

from exalted.models.characters.mortals import ExMortal
from exalted.models.characters.solars import Solar

time_test(ExMortal)
time_test(Solar)
