from django.contrib.auth.models import User
from django.test import TestCase

from exalted.models.characters.charms import (
    DragonBloodedCharm,
    MartialArtsCharm,
    MartialArtsStyle,
)
from exalted.models.characters.dragonblooded import DragonBlooded
from exalted.models.characters.mortals import ExMerit, ExSpecialty
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
        self.db = DragonBlooded.objects.create()
        dragonblooded_setup()

    def test_has_aspect(self):
        self.assertFalse(self.db.has_aspect())
        self.db.set_aspect("fire")
        self.assertTrue(self.db.has_aspect())

    def test_set_aspect(self):
        self.assertFalse(self.db.has_aspect())
        self.assertTrue(self.db.set_aspect("air"))
        self.assertTrue(self.db.has_aspect())
        self.assertEqual(self.db.aspect, "air")
        self.assertEqual(
            self.db.aspect_abilities,
            ["linguistics", "lore", "occult", "stealth", "thrown",],
        )

    def test_has_origin(self):
        self.assertFalse(self.db.has_origin())
        self.db.set_origin("dynast")
        self.assertTrue(self.db.has_origin())

    def test_set_origin(self):
        self.assertFalse(self.db.has_origin())
        self.assertTrue(self.db.set_origin("dynast"))
        self.assertTrue(self.db.has_origin())
        self.assertEqual(self.db.origin, "dynast")

    def test_set_house(self):
        self.assertEqual(self.db.house, "")
        self.assertTrue(self.db.set_house("cathak"))
        self.assertEqual(self.db.house, "cathak")

    def test_set_school(self):
        self.assertEqual(self.db.school, "")
        self.assertTrue(self.db.set_school("heptagram"))
        self.assertEqual(self.db.school, "heptagram")

    def test_has_favored_abilities(self):
        self.assertFalse(self.db.has_favored_abilities())
        self.db.add_favored_ability("athletics")
        self.db.add_favored_ability("dodge")
        self.db.add_favored_ability("melee")
        self.db.add_favored_ability("presence")
        self.db.add_favored_ability("socialize")
        self.assertTrue(self.db.has_favored_abilities())

    def test_add_favored_ability(self):
        self.db.add_favored_ability("athletics")
        self.db.add_favored_ability("dodge")
        self.db.add_favored_ability("melee")
        self.db.add_favored_ability("presence")
        self.assertTrue(self.db.add_favored_ability("socialize"))
        self.assertEqual(
            self.db.favored_abilities,
            ["athletics", "dodge", "melee", "presence", "socialize",],
        )

    def test_finishing_touches(self):
        self.fail()

    def test_total_charms(self):
        self.assertEqual(self.db.total_charms(), 0)
        charm = DragonBloodedCharm.objects.create(name="Test Charm")
        self.db.charms.add(charm)
        self.assertEqual(self.db.total_charms(), 1)

    def test_total_excellencies(self):
        self.assertEqual(self.db.total_excellencies(), 0)
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency of Fire", keywords=["excellency"]
            )
        )
        self.assertEqual(self.db.total_excellencies(), 1)
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency of Water", keywords=["excellency"]
            )
        )
        self.assertEqual(self.db.total_excellencies(), 2)

    def test_has_excellencies(self):
        self.assertFalse(self.db.has_excellencies())
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 1", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 2", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 3", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 4", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 5", keywords=["excellency"]
            )
        )
        self.assertTrue(self.db.has_excellencies())

    def test_has_charms(self):
        self.assertFalse(self.db.has_charms())
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 1", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 2", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 3", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 4", keywords=["excellency"]
            )
        )
        self.db.charms.add(
            DragonBloodedCharm.objects.create(
                name="Excellency 5", keywords=["excellency"]
            )
        )
        for i in range(15):
            self.db.charms.add(
                DragonBloodedCharm.objects.create(
                    name=f"Fireball {i}", statistic="melee", min_statistic=0
                )
            )
        self.assertTrue(self.db.has_charms())

    def test_filter_excellencies(self):
        self.fail()

    def test_filter_charms(self):
        self.fail()

    def test_add_charm(self):
        charm = DragonBloodedCharm.objects.create(
            name="Fireball", statistic="melee", min_statistic=0
        )
        self.assertNotIn(charm, self.db.charms.all())
        self.db.add_charm(charm)
        self.assertIn(charm, self.db.charms.all())

    def test_has_specialties(self):
        self.assertFalse(self.db.has_specialties())
        self.db.melee = 1
        self.db.athletics = 1
        self.db.presence = 1
        self.db.add_specialty(
            ExSpecialty.objects.create(name="Excellent Strike", ability="melee")
        )
        self.db.add_specialty(
            ExSpecialty.objects.create(name="Sprinting", ability="athletics")
        )
        self.db.add_specialty(
            ExSpecialty.objects.create(name="Intimidation", ability="presence")
        )
        self.db.save()
        self.assertTrue(self.db.has_specialties())

    def test_bonus_cost(self):
        self.assertEqual(self.db.bonus_cost("charm"), 5)
        self.assertEqual(self.db.bonus_cost("aspect ability"), 1)
        self.assertEqual(self.db.bonus_cost("favored ability"), 1)
        self.assertEqual(self.db.bonus_cost("aspect charm"), 4)
        self.assertEqual(self.db.bonus_cost("favored charm"), 4)
        self.assertEqual(self.db.bonus_cost("spell"), 5)
        self.db.add_favored_ability("occult")
        self.assertEqual(self.db.bonus_cost("spell"), 4)
        self.assertEqual(self.db.bonus_cost("evocation"), 4)

    def test_random_bonus_functions(self):
        random_functions = self.db.random_bonus_functions()
        self.assertIn("charm", random_functions)

    def test_spend_bonus_points(self):
        self.fail()

    def test_xp_cost(self):
        self.assertEqual(self.db.xp_cost("charm"), 10)
        self.assertEqual(self.db.xp_cost("aspect charm"), 8)
        self.assertEqual(self.db.xp_cost("favored charm"), 8)
        self.assertEqual(self.db.xp_cost("martial arts charm"), 10)
        self.db.add_favored_ability("brawl")
        self.assertEqual(self.db.xp_cost("martial arts charm"), 8)
        self.assertEqual(self.db.xp_cost("spell"), 12)
        self.db.add_favored_ability("occult")
        self.assertEqual(self.db.xp_cost("spell"), 10)
        self.assertEqual(self.db.xp_cost("evocation"), 12)

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
