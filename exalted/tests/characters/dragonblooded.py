from django.contrib.auth.models import User
from django.test import TestCase

from exalted.models.characters.charms import (
    DragonBloodedCharm,
    MartialArtsCharm,
    MartialArtsStyle,
)
from exalted.models.characters.dragonblooded import DragonBlooded
from exalted.models.characters.mortals import ExMerit
from exalted.models.characters.utils import ABILITIES
from exalted.tests.characters.mortals import setup


def dragonblooded_setup():
    setup()
    MartialArtsStyle.objects.create(name="Snake")
    MartialArtsStyle.objects.create(name="Weasel")
    for i in range(10):
        for ability in ABILITIES:
            DragonBloodedCharm.objects.create(
                name=f"{ability.title()} Charm {i}",
                statistic=ability,
                min_statistic=i % 5,
                min_essence=i % 5,
            )
        for style in MartialArtsStyle.objects.all():
            MartialArtsCharm.objects.create(
                name=f"{style.name} Charm {i}",
                statistic="martial_arts",
                min_statistic=i % 5,
                min_essence=i % 5,
                style=style,
            )


# Create your tests here.
class TestDragonBlooded(TestCase):
    def setUp(self):
        self.dragon_blooded = DragonBlooded.objects.create(name="Test DragonBlooded")
        dragonblooded_setup()

    def test_has_aspect(self):
        pass

    def test_set_aspect(self):
        pass

    def test_has_origin(self):
        pass

    def test_set_origin(self):
        pass

    def test_set_house(self):
        pass

    def test_set_school(self):
        pass

    def test_has_favored_abilities(self):
        pass

    def test_add_favored_ability(self):
        pass

    def test_finishing_touches(self):
        pass

    def test_total_charms(self):
        pass

    def test_total_excellencies(self):
        pass

    def test_has_excellencies(self):
        pass

    def test_has_charms(self):
        pass

    def test_filter_excellencies(self):
        pass

    def test_filter_charms(self):
        pass

    def test_add_charm(self):
        pass

    def test_has_specialties(self):
        pass

    def test_bonus_cost(self):
        pass

    def test_random_bonus_functions(self):
        pass

    def test_spend_bonus_points(self):
        pass

    def test_xp_cost(self):
        pass

    def test_spend_xp(self):
        pass


class TestRandomDragonBlooded(TestCase):
    def setUp(self):
        self.dragon_blooded = DragonBlooded.objects.create(name="Test DragonBlooded")
        dragonblooded_setup()

    def test_random_aspect(self):
        pass

    def test_random_origin(self):
        pass

    def test_random_favored_ability(self):
        pass

    def test_random_favored_abilities(self):
        pass

    def test_random_name(self):
        pass

    def test_random_excellency(self):
        pass

    def test_random_charm(self):
        pass

    def test_random_charms(self):
        pass

    def test_random_additional_specialties(self):
        pass

    def test_random_bonus_charm(self):
        pass

    def test_random_xp_charm(self):
        pass

    def test_random(self):
        pass
