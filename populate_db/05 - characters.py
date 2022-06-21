from time import time

from django.contrib.auth.models import User

player = User.objects.create_user(username="Test")

from wod.models.characters.mage import Mage
from wod.models.characters.werewolf import Werewolf
from wod.models.items.mage import Grimoire
from wod.models.locations.mage import Node

mage_start = time()
for i in range(10):
    mage = Werewolf.objects.create(name="", player=player.wod_profile)
    mage.random()
    mage.save()
print("Average Random Werewolf Time:", (time() - mage_start) / 10)

mage_start = time()
for i in range(10):
    mage = Mage.objects.create(name="", player=player.wod_profile)
    mage.random()
    mage.save()
print("Average Random Mage Time:", (time() - mage_start) / 10)


node_start = time()
for i in range(10):
    node = Node.objects.create(name=f"Node {i}")
    node.random(rank=(i % 5) + 1)
    node.save()
print("Average Random Node Time:", (time() - node_start) / 10)


grimoire_start = time()
for i in range(10):
    grimoire = Grimoire.objects.create(name=f"Grimoire {i}")
    grimoire.random(rank=(i % 5) + 1)
    grimoire.save()
print("Average Random Grimoire Time:", (time() - grimoire_start) / 10)

from cod.models.characters.mortal import Mortal

mortal_start = time()
for i in range(10):
    mortal = Mortal.objects.create(name=f"Mortal {i}", player=player.cod_profile)
    mortal.random()
    mortal.save()
print("Average CoD Mortal Time:", (time() - mortal_start) / 10)

from tc.models.characters.aberrant import Aberrant
from tc.models.characters.human import Human
from tc.models.characters.talent import Talent

human_start = time()
for i in range(10):
    human = Human.objects.create(name=f"Human {i}", player=player.tc_profile)
    human.random(xp=0)
    human.save()
print("Average Random TC Human Time:", (time() - human_start) / 10)
talent_start = time()
for i in range(10):
    talent = Talent.objects.create(name=f"Talent {i}", player=player.tc_profile)
    talent.random(xp=50)
    talent.save()
print("Average Random Talent Time:", (time() - talent_start) / 10)
aberrant_start = time()
for i in range(10):
    aberrant = Aberrant.objects.create(name=f"Aberrant {i}", player=player.tc_profile)
    aberrant.random(xp=150)
    aberrant.save()
print("Average Random Aberrant Time:", (time() - aberrant_start) / 10)
