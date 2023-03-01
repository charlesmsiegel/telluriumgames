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
from exalted.tests.characters.mortals import ex_setup


def dragonblooded_setup():
    ex_setup()
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
        self.fail()

    def test_set_aspect(self):
        self.fail()

    def test_has_origin(self):
        self.fail()

    def test_set_origin(self):
        self.fail()

    def test_set_house(self):
        self.fail()

    def test_set_school(self):
        self.fail()

    def test_has_favored_abilities(self):
        self.fail()

    def test_add_favored_ability(self):
        self.fail()

    def test_finishing_touches(self):
        self.fail()

    def test_total_charms(self):
        self.fail()

    def test_total_excellencies(self):
        self.fail()

    def test_has_excellencies(self):
        self.fail()

    def test_has_charms(self):
        self.fail()

    def test_filter_excellencies(self):
        self.fail()

    def test_filter_charms(self):
        self.fail()

    def test_add_charm(self):
        self.fail()

    def test_has_specialties(self):
        self.fail()

    def test_bonus_cost(self):
        self.fail()

    def test_random_bonus_functions(self):
        self.fail()

    def test_spend_bonus_points(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()


class TestRandomDragonBlooded(TestCase):
    def setUp(self):
        self.dragon_blooded = DragonBlooded.objects.create(name="Test DragonBlooded")
        dragonblooded_setup()

    def test_random_aspect(self):
        self.fail()

    def test_random_origin(self):
        self.fail()

    def test_random_favored_ability(self):
        self.fail()

    def test_random_favored_abilities(self):
        self.fail()

    def test_random_name(self):
        self.fail()

    def test_random_excellency(self):
        self.fail()

    def test_random_charm(self):
        self.fail()

    def test_random_charms(self):
        self.fail()

    def test_random_additional_specialties(self):
        self.fail()

    def test_random_bonus_charm(self):
        self.fail()

    def test_random_xp_charm(self):
        self.fail()

    def test_random(self):
        self.fail()
