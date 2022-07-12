from time import time

from django.contrib.auth.models import User

player, _ = User.objects.get_or_create(username="Test")

from wod.models.characters.mage import Mage
from wod.models.characters.werewolf import Werewolf
from wod.models.items.mage import Grimoire
from wod.models.locations.mage import Node

mage_start = time()
for i in range(10):
    mage = Werewolf.objects.create(
        name=f"Werewolf {Werewolf.objects.count()}", player=player
    )
    mage.random()
    mage.save()
print("Average Random Werewolf Time:", (time() - mage_start) / 10)

mage_start = time()
for i in range(10):
    mage = Mage.objects.create(
        name=f"Mage {Mage.objects.count()}", player=player
    )
    mage.random()
    mage.save()
print("Average Random Mage Time:", (time() - mage_start) / 10)


node_start = time()
for i in range(10):
    node = Node.objects.create(name=f"Node {Node.objects.count()}")
    node.random(rank=(i % 5) + 1)
    node.save()
print("Average Random Node Time:", (time() - node_start) / 10)


grimoire_start = time()
for i in range(10):
    grimoire = Grimoire.objects.create(name=f"Grimoire {Grimoire.objects.count()}")
    grimoire.random(rank=(i % 5) + 1)
    grimoire.save()
print("Average Random Grimoire Time:", (time() - grimoire_start) / 10)

from cod.models.characters.mage import Mage, Proximi, ProximiFamily
from cod.models.characters.mortal import Mortal

mortal_start = time()
for i in range(10):
    mortal = Mortal.objects.create(
        name=f"Mortal {Mortal.objects.count()}", player=player
    )
    mortal.random()
    mortal.save()
print("Average CoD Mortal Time:", (time() - mortal_start) / 10)

mortal_start = time()
for i in range(10):
    mortal = Mage.objects.create(
        name=f"Mage {Mage.objects.count()}", player=player
    )
    mortal.random()
    mortal.save()
print("Average CoD Mage Time:", (time() - mortal_start) / 10)

mortal_start = time()
for i in range(10):
    mortal = ProximiFamily.objects.create(
        name=f"Proximi Family {ProximiFamily.objects.count()}"
    )
    mortal.random()
    mortal.save()
print("Average CoD Proximi Family Time:", (time() - mortal_start) / 10)

mortal_start = time()
for i in range(10):
    mortal = Proximi.objects.create(
        name=f"Proximi {Proximi.objects.count()}", player=player
    )
    mortal.random()
    mortal.save()
print("Average CoD Proximi Time:", (time() - mortal_start) / 10)

from tc.models.characters.aberrant import Aberrant
from tc.models.characters.human import Human
from tc.models.characters.talent import Talent

human_start = time()
for i in range(10):
    human = Human.objects.create(
        name=f"Human {Human.objects.count()}", player=player
    )
    human.random(xp=0)
    human.save()
print("Average Random TC Human Time:", (time() - human_start) / 10)
talent_start = time()
for i in range(10):
    talent = Talent.objects.create(
        name=f"Talent {Talent.objects.count()}", player=player
    )
    talent.random(xp=50)
    talent.save()
print("Average Random Talent Time:", (time() - talent_start) / 10)
aberrant_start = time()
for i in range(10):
    aberrant = Aberrant.objects.create(
        name=f"Aberrant {Aberrant.objects.count()}", player=player
    )
    aberrant.random(xp=150)
    aberrant.save()
print("Average Random Aberrant Time:", (time() - aberrant_start) / 10)

from exalted.models.characters.mortals import Mortal

mortal_start = time()
for i in range(10):
    mortal = Mortal.objects.create(name="", player=player)
    mortal.random()
    mortal.save()
print("Average Exalted Mortal Time:", (time() - mortal_start) / 10)
