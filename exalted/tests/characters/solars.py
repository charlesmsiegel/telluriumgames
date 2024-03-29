from django.contrib.auth.models import User
from django.test import TestCase

from exalted.models.characters.charms import (
    MartialArtsCharm,
    MartialArtsStyle,
    SolarCharm,
)
from exalted.models.characters.mortals import ExMerit
from exalted.models.characters.solars import Solar
from exalted.models.characters.utils import ABILITIES
from exalted.tests.characters.mortals import ex_setup


def solar_setup():
    ex_setup()
    MartialArtsStyle.objects.create(name="Snake")
    MartialArtsStyle.objects.create(name="Weasel")
    for i in range(10):
        for ability in ABILITIES:
            SolarCharm.objects.create(
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
class TestSolar(TestCase):
    def setUp(self):
        self.solar = Solar.objects.create(name="Test Solar")
        solar_setup()

    def test_set_caste(self):
        self.assertFalse(self.solar.has_caste())
        self.assertTrue(self.solar.set_caste("dawn"))
        self.assertTrue(self.solar.has_caste())

    def test_has_caste(self):
        self.assertFalse(self.solar.has_caste())
        self.solar.set_caste("dawn")
        self.assertTrue(self.solar.has_caste())

    def test_set_caste_abilities(self):
        abilities = ["brawl", "awareness", "melee", "dodge", "resistance"]
        self.assertTrue(self.solar.set_caste_abilities(abilities))
        self.assertEqual(self.solar.caste_abilities, abilities)

    def test_add_caste_ability(self):
        abilities = ["brawl", "awareness", "melee", "dodge"]
        self.solar.set_caste_abilities(abilities)
        self.assertTrue(self.solar.add_caste_abilites("resistance"))
        self.assertEqual(self.solar.caste_abilities, abilities + ["resistance"])
        self.assertFalse(self.solar.add_caste_abilites("resistance"))

    def test_has_caste_abilities(self):
        self.assertFalse(self.solar.has_caste_abilities())
        self.solar.set_caste_abilities(
            ["brawl", "awareness", "melee", "dodge", "resistance"]
        )
        self.assertTrue(self.solar.has_caste_abilities())

    # def test_caste_abilities(self):
    #     self.solar.set_caste("dawn")
    #     self.assertEqual(
    #         self.solar.caste_ability_dict[self.solar.caste],
    #         [
    #             "archery",
    #             "awareness",
    #             "brawl",
    #             "martial_arts",
    #             "dodge",
    #             "melee",
    #             "resistance",
    #             "thrown",
    #             "war",
    #         ],
    #     )
    #     self.solar.set_caste("zenith")
    #     self.assertEqual(
    #         self.solar.caste_ability_dict[self.solar.caste],
    #         [
    #             "athletics",
    #             "integrity",
    #             "performance",
    #             "lore",
    #             "presence",
    #             "resistance",
    #             "survival",
    #             "war",
    #         ],
    #     )
    #     self.solar.set_caste("twilight")
    #     self.assertEqual(
    #         self.solar.caste_ability_dict[self.solar.caste],
    #         [
    #             "bureaucracy",
    #             "craft",
    #             "integrity",
    #             "investigation",
    #             "linguistics",
    #             "lore",
    #             "medicine",
    #             "occult",
    #         ],
    #     )
    #     self.solar.set_caste("night")
    #     self.assertEqual(
    #         self.solar.caste_ability_dict[self.solar.caste],
    #         [
    #             "athletics",
    #             "awareness",
    #             "dodge",
    #             "investigation",
    #             "larceny",
    #             "ride",
    #             "stealth",
    #             "socialize",
    #         ],
    #     )
    #     self.solar.set_caste("eclipse")
    #     self.assertEqual(
    #         self.solar.caste_ability_dict[self.solar.caste],
    #         [
    #             "bureaucracy",
    #             "larceny",
    #             "linguistics",
    #             "occult",
    #             "presence",
    #             "ride",
    #             "sail",
    #             "socialize",
    #         ],
    #     )

    def test_add_favored_ability(self):
        self.solar.add_favored_ability("occult")
        self.assertEqual(self.solar.favored_abilities, ["occult"])
        self.assertGreaterEqual(self.solar.occult, 1)

    def test_has_favored_abilities(self):
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("occult")
        self.assertGreaterEqual(self.solar.occult, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("awareness")
        self.assertGreaterEqual(self.solar.awareness, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("war")
        self.assertGreaterEqual(self.solar.war, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("athletics")
        self.assertGreaterEqual(self.solar.athletics, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("brawl")
        self.assertGreaterEqual(self.solar.brawl, 1)
        self.assertTrue(self.solar.has_favored_abilities())

    def test_set_supernal_ability(self):
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.set_caste("dawn")
        self.assertFalse(self.solar.has_supernal_ability())
        self.assertFalse(self.solar.set_supernal_ability("occult"))
        self.solar.set_caste_abilities(["archery"])
        self.assertTrue(self.solar.set_supernal_ability("archery"))
        self.assertTrue(self.solar.has_supernal_ability())

    def test_has_supernal_ability(self):
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.set_caste("dawn")
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.set_caste_abilities(["archery"])
        self.solar.set_supernal_ability("archery")
        self.assertTrue(self.solar.has_supernal_ability())

    def test_add_charm(self):
        c1 = SolarCharm.objects.get(name="War Charm 0")
        c2 = SolarCharm.objects.get(name="War Charm 1")
        c3 = SolarCharm.objects.create(
            name="Advanced War Charm",
            statistic="war",
            min_statistic=2,
            min_essence=1,
            prereqs=[[("War Charm 0", 1)]],
        )
        count = self.solar.charms.count()
        self.assertFalse(self.solar.add_charm(c2))
        self.solar.war = 2
        self.solar.essence = 1
        self.assertFalse(self.solar.add_charm(c3))
        self.assertTrue(self.solar.add_charm(c1))
        self.assertEqual(self.solar.charms.count(), count + 1)
        self.assertTrue(self.solar.add_charm(c3))
        self.assertEqual(self.solar.charms.count(), count + 2)
        self.assertFalse(
            self.solar.add_charm(MartialArtsCharm.objects.get(name="Snake Charm 0"))
        )
        self.solar.add_merit(ExMerit.objects.create(name="Martial Artist", ratings=[4]))
        self.solar.martial_arts = 3
        self.assertTrue(
            self.solar.add_charm(MartialArtsCharm.objects.get(name="Snake Charm 0"))
        )

    def test_total_charms(self):
        self.assertEqual(self.solar.total_charms(), 0)
        self.solar.charms.create(name="Test Charm")
        self.assertEqual(self.solar.total_charms(), 1)

    def test_has_charms(self):
        self.assertFalse(self.solar.has_charms())
        self.solar.essence = 5
        self.solar.war = 5
        self.solar.archery = 5
        self.solar.melee = 5
        self.solar.brawl = 1
        self.solar.add_merit(ExMerit.objects.create(name="Martial Artist", ratings=[4]))
        self.solar.martial_arts = 5
        for i in range(5):
            c = SolarCharm.objects.get(name=f"Archery Charm {i}")
            self.assertTrue(self.solar.add_charm(c))
            c = SolarCharm.objects.get(name=f"War Charm {i}")
            self.assertTrue(self.solar.add_charm(c))
            c = MartialArtsCharm.objects.get(name=f"Snake Charm {i}")
            self.assertTrue(self.solar.add_charm(c))
        self.assertTrue(self.solar.has_charms())

    def test_filter_charms(self):
        self.assertEqual(len(self.solar.filter_charms()), 50)
        self.solar.war = 2
        self.solar.essence = 1
        self.assertEqual(len(self.solar.filter_charms()), 52)
        self.solar.essence = 2
        self.assertEqual(len(self.solar.filter_charms()), 54)
        ma, _ = ExMerit.objects.get_or_create(name="Martial Artist", ratings=[4])
        self.solar.merits.add(ma)
        self.assertEqual(len(self.solar.filter_charms()), 60)

    def test_set_limit_trigger(self):
        self.assertFalse(self.solar.has_limit_trigger())
        self.assertTrue(self.solar.set_limit_trigger("Test"))
        self.assertTrue(self.solar.has_limit_trigger())

    def test_has_limit_trigger(self):
        self.assertFalse(self.solar.has_limit_trigger())
        self.solar.set_limit_trigger("Test")
        self.assertTrue(self.solar.has_limit_trigger())

    def test_has_finishing_touches(self):
        self.assertFalse(self.solar.has_finishing_touches())
        self.solar.willpower = 5
        self.solar.health_levels = 7
        self.solar.essence = 1
        self.assertTrue(self.solar.has_finishing_touches())

    def test_bonus_cost(self):
        self.assertEqual(self.solar.bonus_cost("primary attribute"), 4)
        self.assertEqual(self.solar.bonus_cost("secondary attribute"), 4)
        self.assertEqual(self.solar.bonus_cost("tertiary attribute"), 3)
        self.assertEqual(self.solar.bonus_cost("ability"), 2)
        self.assertEqual(self.solar.bonus_cost("caste ability"), 1)
        self.assertEqual(self.solar.bonus_cost("favored ability"), 1)
        self.assertEqual(self.solar.bonus_cost("specialty"), 1)
        self.assertEqual(self.solar.bonus_cost("merit"), 1)
        self.assertEqual(self.solar.bonus_cost("willpower"), 2)
        self.assertEqual(self.solar.bonus_cost("caste charm"), 4)
        self.assertEqual(self.solar.bonus_cost("favored charm"), 4)
        self.assertEqual(self.solar.bonus_cost("charm"), 5)
        self.assertEqual(self.solar.bonus_cost("spell"), 5)
        self.solar.add_favored_ability("occult")
        self.assertEqual(self.solar.bonus_cost("spell"), 4)
        self.assertEqual(self.solar.bonus_cost("evocation"), 4)

    def test_random_bonus_functions(self):
        functions = self.solar.random_bonus_functions()
        self.assertIn("charm", functions)

    def test_spend_bonus_points(self):
        self.solar.bonus_points = 10
        self.solar.set_caste_abilities(["brawl", "awareness"])
        self.solar.favored_abilities = ["athletics"]
        self.solar.add_ability("brawl")
        self.solar.add_ability("athletics")
        self.assertEqual(self.solar.bonus_points, 10)
        self.assertTrue(self.solar.spend_bonus_points("brawl"))
        self.assertEqual(self.solar.bonus_points, 9)
        self.assertEqual(self.solar.brawl, 2)
        self.assertTrue(self.solar.spend_bonus_points("brawl"))
        self.assertEqual(self.solar.bonus_points, 8)
        self.assertEqual(self.solar.brawl, 3)

    def test_xp_cost(self):
        self.assertEqual(self.solar.xp_cost("attribute"), 4)
        self.assertEqual(self.solar.xp_cost("new ability"), 3)
        self.assertEqual(self.solar.xp_cost("ability"), 2)
        self.assertEqual(self.solar.xp_cost("specialty"), 3)
        self.assertEqual(self.solar.xp_cost("merit"), 3)
        self.assertEqual(self.solar.xp_cost("willpower"), 8)

        self.assertEqual(self.solar.xp_cost("evocation"), 10)

        self.assertEqual(self.solar.xp_cost("spell"), 10)
        self.solar.add_favored_ability("occult")
        self.assertEqual(self.solar.xp_cost("spell"), 8)

        self.assertEqual(self.solar.xp_cost("martial arts charm"), 10)
        self.solar.add_favored_ability("brawl")
        self.assertEqual(self.solar.xp_cost("martial arts charm"), 8)

        self.assertEqual(self.solar.xp_cost("caste charm"), 8)
        self.assertEqual(self.solar.xp_cost("favored charm"), 8)
        self.assertEqual(self.solar.xp_cost("charm"), 10)

    def test_random_xp_functions(self):
        functions = self.solar.random_xp_functions()
        self.assertIn("charm", functions)

    def test_spend_xp(self):
        self.solar.xp = 100
        self.solar.spend_xp("archery")
        self.assertEqual(self.solar.archery, 1)
        self.assertEqual(self.solar.xp, 97)

    def test_charm_dict(self):
        self.assertEqual(len(self.solar.charm_dict()), 25)
        self.solar.add_charm(self.solar.filter_charms()[0])
        self.assertEqual(len(self.solar.charm_dict()), 25)


class TestRandomSolar(TestCase):
    def setUp(self):
        self.solar = Solar.objects.create(name="Test Solar")
        solar_setup()

    def test_random_name(self):
        solar = Solar.objects.create()
        solar.random_name()
        self.assertNotEqual(solar.name, "")

    def test_random_caste(self):
        self.assertFalse(self.solar.has_caste())
        self.solar.random_caste()
        self.assertTrue(self.solar.has_caste())

    def test_random_favored_ability(self):
        self.solar.random_caste()
        self.solar.random_caste_abilities()
        self.solar.random_favored_ability()
        self.assertNotIn(self.solar.favored_abilities[0], self.solar.caste_abilities)

    def test_random_favored_abilities(self):
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.random_favored_abilities()
        self.assertTrue(self.solar.has_favored_abilities())

    def test_random_supernal_ability(self):
        self.solar.set_caste("dawn")
        self.solar.random_caste_abilities()
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.random_supernal_ability()
        self.assertTrue(self.solar.has_supernal_ability())

    def test_random_charm(self):
        num_charms = self.solar.charms.count()
        self.assertTrue(self.solar.random_charm())
        self.assertEqual(self.solar.charms.count(), num_charms + 1)

    def test_random_charms(self):
        self.assertFalse(self.solar.has_charms())
        self.solar.random_charms()
        self.assertTrue(self.solar.has_charms())

    def test_random_limit_trigger(self):
        self.assertFalse(self.solar.has_limit_trigger())
        self.solar.random_limit_trigger()
        self.assertTrue(self.solar.has_limit_trigger())

    def test_random_bonus_charm(self):
        self.solar.random_caste()
        self.solar.random_caste_abilities()
        self.solar.random_supernal_ability()
        self.solar.random_favored_abilities()
        self.solar.random_charms()
        self.solar.bonus_points = 10
        self.solar.random_bonus_charm()
        self.assertGreater(self.solar.total_charms(), 15)

    def test_random_xp_charm(self):
        self.solar.random_caste()
        self.solar.random_caste_abilities()
        self.solar.random_supernal_ability()
        self.solar.random_favored_abilities()
        self.solar.random_charms()
        self.solar.xp = 10
        self.solar.random_xp_charm()
        self.assertGreater(self.solar.total_charms(), 15)

    def test_random(self):
        self.solar.name = ""
        self.assertFalse(self.solar.has_name())
        self.assertFalse(self.solar.has_concept())
        self.assertFalse(self.solar.has_caste())
        self.assertFalse(self.solar.has_attributes())
        self.assertFalse(self.solar.has_abilities())
        self.assertFalse(self.solar.has_favored_abilities())
        self.assertFalse(self.solar.has_supernal_ability())
        self.assertFalse(self.solar.has_specialties())
        self.assertFalse(self.solar.has_charms())
        self.assertFalse(self.solar.has_merits())
        self.assertFalse(self.solar.has_intimacies())
        self.assertFalse(self.solar.has_limit_trigger())
        self.assertEqual(self.solar.bonus_points, 21)
        self.assertFalse(self.solar.has_finishing_touches())
        self.solar.random(bonus_points=0, xp=0)
        self.assertTrue(self.solar.has_caste())
        self.assertTrue(self.solar.has_name())
        self.assertTrue(self.solar.has_concept())
        self.assertTrue(self.solar.has_attributes(primary=8, secondary=6, tertiary=4))
        self.assertTrue(self.solar.has_abilities())
        self.assertTrue(self.solar.has_favored_abilities())
        self.assertTrue(self.solar.has_supernal_ability())
        self.assertTrue(self.solar.has_specialties())
        self.assertTrue(self.solar.has_charms())
        self.assertTrue(self.solar.has_merits(target_num=10))
        self.assertTrue(self.solar.has_intimacies())
        self.assertTrue(self.solar.has_limit_trigger())
        self.assertEqual(self.solar.bonus_points, 0)
        self.assertTrue(self.solar.has_finishing_touches())
