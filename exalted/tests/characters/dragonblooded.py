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
    for ability in ABILITIES:
        DragonBloodedCharm.objects.create(
            name=f"{ability.title()} Excellency",
            keywords=["excellency"],
            statistic=ability,
            min_statistic=1,
            min_essence=1,
        )
        for i in range(10):
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
    for merit_name in [
        "Backing",
        "Command",
        "Contacts",
        "Followers",
        "Influence",
        "Language",
        "Resources",
        "Retainers",
    ]:
        ExMerit.objects.create(name=merit_name, ratings=[1, 2, 3, 4, 5])


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
        self.db.apply_finishing_touches()
        self.assertEqual(self.db.willpower, 5)
        self.assertEqual(self.db.health_levels, 7)
        self.assertEqual(self.db.essence, 2)

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
        self.db.essence = 1
        self.db.melee = 2
        filtered_charms = self.db.filter_excellencies()
        self.assertEqual(len(filtered_charms), 1)
        self.assertEqual(filtered_charms[0].name, "Melee Excellency")

    def test_filter_charms(self):
        self.db.essence = 2
        ma = ExMerit.objects.create(name="Martial Artist", ratings=[1])
        self.db.add_merit(ma)

        self.db.archery = 3
        DragonBloodedCharm.objects.create(
            name="Test Charm 1", statistic="archery", min_statistic=3, min_essence=1,
        )
        self.db.athletics = 2
        DragonBloodedCharm.objects.create(
            name="Test Charm 2", statistic="athletics", min_statistic=2, min_essence=1,
        )
        self.db.martial_arts = 1
        MartialArtsCharm.objects.create(
            name="Test Charm 3",
            statistic="martial_arts",
            min_statistic=1,
            min_essence=2,
        )
        self.db.bureaucracy = 3
        DragonBloodedCharm.objects.create(
            name="Test Charm 4",
            statistic="bureaucracy",
            min_statistic=3,
            min_essence=3,
        )
        self.db.presence = 4
        DragonBloodedCharm.objects.create(
            name="Test Charm 5", statistic="presence", min_statistic=4, min_essence=4,
        )
        filtered_charms = self.db.filter_charms()
        self.assertEqual(len(filtered_charms), 78)
        charm_names = [charm.name for charm in filtered_charms]
        self.assertIn("Test Charm 1", charm_names)
        self.assertIn("Test Charm 2", charm_names)
        self.assertIn("Test Charm 3", charm_names)

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
        self.db.bonus_points = 10
        self.db.aspect_abilities = ["archery"]
        self.db.favored_abilities = ["melee"]
        self.db.save()
        self.assertTrue(self.db.spend_bonus_points("archery"))
        self.assertEqual(self.db.aspect_abilities, ["archery"])
        self.assertEqual(self.db.bonus_points, 9)

        self.db.bonus_points = 10
        self.db.aspect_abilities = ["archery"]
        self.db.favored_abilities = ["melee"]
        self.db.save()
        self.assertTrue(self.db.spend_bonus_points("melee"))
        self.assertEqual(self.db.favored_abilities, ["melee"])
        self.assertEqual(self.db.bonus_points, 9)

        charm = DragonBloodedCharm.objects.create(
            name="Heavenly Guardian Defense",
            statistic="melee",
            min_statistic=3,
            min_essence=2,
        )
        self.db.bonus_points = 10
        self.db.aspect_abilities = ["archery"]
        self.db.favored_abilities = ["melee"]
        self.db.melee = 4
        self.db.essence = 3
        self.db.save()
        self.assertTrue(self.db.spend_bonus_points("Heavenly Guardian Defense"))
        self.assertEqual(set(self.db.charms.all()), {charm})
        self.assertEqual(self.db.bonus_points, 6)

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
        self.db.xp = 20
        self.db.aspect_abilities = ["archery"]
        self.db.favored_abilities = ["melee"]
        self.db.archery = 1
        self.db.melee = 1
        self.db.save()
        self.assertTrue(self.db.spend_xp("archery"))
        self.assertEqual(self.db.aspect_abilities, ["archery"])
        self.assertEqual(self.db.xp, 19)

        self.db.xp = 20
        self.db.aspect_abilities = ["archery"]
        self.db.favored_abilities = ["melee"]
        self.db.save()
        self.assertTrue(self.db.spend_xp("melee"))
        self.assertEqual(self.db.favored_abilities, ["melee"])
        self.assertEqual(self.db.xp, 19)

        charm = DragonBloodedCharm.objects.create(
            name="Heavenly Guardian Defense",
            statistic="melee",
            min_statistic=3,
            min_essence=2,
        )
        self.db.xp = 20
        self.db.aspect_abilities = ["archery"]
        self.db.melee = 3
        self.db.essence = 2
        self.db.favored_abilities = ["melee"]
        self.db.save()
        self.assertTrue(self.db.spend_xp("Heavenly Guardian Defense"))
        self.assertEqual(set(self.db.charms.all()), {charm})
        self.assertEqual(self.db.xp, 12)


class TestRandomDragonBlooded(TestCase):
    def setUp(self):
        self.db = DragonBlooded.objects.create(name="Test DragonBlooded")
        dragonblooded_setup()

    def test_random_aspect(self):
        self.db.random_aspect()
        self.assertIn(self.db.aspect, [aspect[0] for aspect in self.db.ASPECT_CHOICES])

    def test_random_origin(self):
        self.db.random_origin()
        self.assertIn(self.db.origin, [origin[0] for origin in self.db.ORIGIN_CHOICES])
        if self.db.origin == "dynast":
            self.assertIn(
                self.db.house,
                [
                    "cathak",
                    "cynis",
                    "iselsi",
                    "ledaal",
                    "mnemon",
                    "nellens",
                    "peleps",
                    "ragara",
                    "sesus",
                    "tepet",
                    "vneef",
                ],
            )
        elif self.db.origin == "dynast_outcaste":
            self.assertIn(
                self.db.house,
                [
                    "cathak",
                    "cynis",
                    "iselsi",
                    "ledaal",
                    "mnemon",
                    "nellens",
                    "peleps",
                    "ragara",
                    "sesus",
                    "tepet",
                    "vneef",
                ],
            )
        elif self.db.origin == "cadet":
            self.assertIn(self.db.house, ["ferem", "desai", "yueh"])
        elif self.db.origin == "prasadi":
            self.assertIn(self.db.house, ["burano", "ophris"])
        elif self.db.origin == "lookshyan":
            self.assertIn(
                self.db.house,
                [
                    "amilar",
                    "karal",
                    "maheka",
                    "teresu",
                    "yushoto",
                    "kiriga",
                    "nefvarin",
                    "nerigus",
                    "sirel",
                    "taroketu",
                    "toriki",
                    "yan_tu",
                ],
            )
        elif self.db.origin == "foriegn_outcaste":
            self.assertIn(
                self.db.house,
                [
                    "violet_fangs",
                    "grass_spiders",
                    "heavens_dragons",
                    "khamaseen_battalion",
                    "rogue_legion",
                    "yatanis_children",
                    "forest_witches",
                ],
            )

    def test_random_favored_ability(self):
        self.db.random_favored_ability()
        self.assertIn(self.db.favored_abilities[-1], ABILITIES)

    def test_random_favored_abilities(self):
        self.db.random_favored_abilities()
        self.assertGreaterEqual(len(self.db.favored_abilities), 5)

    def test_random_name(self):
        self.db.random_name()
        self.assertTrue(isinstance(self.db.name, str))

    def test_random_excellency(self):
        self.db.melee = 1
        self.db.essence = 1
        self.assertGreaterEqual(self.db.charms.count(), 0)
        self.db.random_excellency()
        self.assertGreaterEqual(self.db.charms.count(), 1)
        self.assertIn("excellency", self.db.charms.first().keywords)

    def test_random_charm(self):
        self.db.random_charm()
        self.assertGreaterEqual(self.db.charms.count(), 1)

    def test_random_charms(self):
        self.db.random_aspect()
        self.db.random_favored_abilities()
        self.db.random_abilities()
        self.db.essence = 1
        self.db.random_charms()
        self.assertGreaterEqual(self.db.charms.count(), 20)
        self.assertTrue(self.db.has_excellencies())

    def test_random_additional_specialties(self):
        self.db.random_origin()
        self.db.random_aspect()
        self.db.random_favored_abilities()
        self.db.random_abilities()
        self.db.random_additional_specialties()
        specialties = [
            getattr(self.db, ability)
            for ability in ABILITIES
            if getattr(self.db, ability) > 0
        ]
        self.assertGreaterEqual(len(specialties), 2)

    def test_random_bonus_charm(self):
        self.db.bonus_points = 20
        self.db.random_bonus_charm()
        self.assertGreaterEqual(self.db.bonus_points, 0)

    def test_random_xp_charm(self):
        # Create a DragonBlooded object
        dragon_blooded = DragonBlooded.objects.create(
            aspect="fire", origin="dynast", house="cathak", school="heptagram"
        )

        dragon_blooded.melee = 2
        dragon_blooded.essence = 1

        # Test that the random_xp_charm() method returns the expected result
        dragon_blooded.xp = 20
        self.assertTrue(dragon_blooded.random_xp_charm())
        self.assertGreater(dragon_blooded.charms.count(), 0)
        self.assertEqual(dragon_blooded.xp, 10)

    def test_random(self):
        dragon_blooded = DragonBlooded.objects.create()
        dragon_blooded.random(xp=0, bonus_points=0)

        # Check that the object has the expected attributes
        self.assertTrue(dragon_blooded.has_concept())
        self.assertTrue(dragon_blooded.has_aspect())
        self.assertTrue(dragon_blooded.has_origin())
        self.assertTrue(dragon_blooded.has_name())
        self.assertEqual(dragon_blooded.essence, 2)
        self.assertTrue(dragon_blooded.has_favored_abilities())
        self.assertTrue(dragon_blooded.has_abilities())
        self.assertTrue(dragon_blooded.has_merits(target_num=18))
        self.assertGreaterEqual(dragon_blooded.specialties.count(), 4)
        self.assertTrue(dragon_blooded.has_intimacies())
