from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.changeling import Changeling, CtDLegacy, House, Kith, Motley
from wod.models.characters.human import MeritFlaw, WoDSpecialty


# Create your tests here.
def changeling_setup(player):
    for i in range(5):
        c = Changeling.objects.create(name=f"Character {i}", owner=player)

    for i in range(10):
        Kith.objects.create(
            name=f"Kith {i}",
            birthrights=["Birthright 1", "Birthright 2"],
            frailty="",
            description="",
        )
        House.objects.create(
            name=f"House {i}",
            court=["seelie", "unseelie"][i % 2],
            boon="",
            flaw="",
            factions=[],
        )
        CtDLegacy.objects.create(
            name=f"Legacy {i}", court=["seelie", "unseelie"][i % 2],
        )
        if i % 2 == 0:
            MeritFlaw.objects.create(
                name=f"Merit {i//2}", ratings=[i // 2 + 1], changeling=True
            )
        else:
            MeritFlaw.objects.create(
                name=f"Flaw {i//2}", ratings=[-i // 2 - 1], changeling=True
            )
        for ability in c.get_abilities():
            WoDSpecialty.objects.create(
                name=f"{ability.title()} Specialty {i}", stat=ability
            )
        for attribute in c.get_attributes():
            WoDSpecialty.objects.create(
                name=f"{attribute.title()} Specialty {i}", stat=attribute
            )


class TestCtDHuman(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")
        changeling_setup(self.player)

    def set_abilities(self):
        self.character.kenning = 3
        self.character.leadership = 2
        self.character.crafts = 3
        self.character.animal_ken = 2
        self.character.larceny = 2
        self.character.enigmas = 2
        self.character.gremayre = 3

    def test_get_talents(self):
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "expression": 0,
                "intimidation": 0,
                "kenning": 0,
                "leadership": 0,
                "streetwise": 0,
                "subterfuge": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "expression": 0,
                "intimidation": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "kenning": 3,
                "leadership": 2,
            },
        )

    def test_get_skills(self):
        self.assertEqual(
            self.character.get_skills(),
            {
                "animal_ken": 0,
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "larceny": 0,
                "melee": 0,
                "performance": 0,
                "stealth": 0,
                "survival": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 3,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 2,
                "larceny": 2,
                "performance": 0,
                "survival": 0,
            },
        )

    def test_get_knowledges(self):
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "enigmas": 0,
                "gremayre": 0,
                "investigation": 0,
                "law": 0,
                "medicine": 0,
                "politics": 0,
                "science": 0,
                "technology": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
                "enigmas": 2,
                "gremayre": 3,
                "law": 0,
                "politics": 0,
                "technology": 0,
            },
        )

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "chimera": 0,
                "contacts": 0,
                "dreamers": 0,
                "holdings": 0,
                "mentor": 0,
                "remembrance": 0,
                "resources": 0,
                "retinue": 0,
                "title": 0,
                "treasure": 0,
            },
        )
        self.character.contacts = 2
        self.character.title = 3
        self.character.dreamers = 4
        self.character.resources = 5
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "contacts": 2,
                "mentor": 0,
                "chimera": 0,
                "dreamers": 4,
                "holdings": 0,
                "remembrance": 0,
                "resources": 5,
                "retinue": 0,
                "title": 3,
                "treasure": 0,
            },
        )


class TestChangeling(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")
        changeling_setup(self.player)

    def test_set_seeming(self):
        self.assertFalse(self.character.has_seeming())
        c = Changeling.objects.create(name="Childling")
        self.assertFalse(c.has_seeming())
        glamour = 4
        willpower = 4
        self.assertTrue(c.set_seeming("childling"))
        self.assertEqual(c.glamour, glamour + 1)
        self.assertTrue(c.has_seeming())
        c = Changeling.objects.create(name="Wilder")
        self.assertFalse(c.has_seeming())
        glamour = 4
        willpower = 4
        self.assertTrue(c.set_seeming("wilder"))
        self.assertEqual(c.glamour + c.willpower, glamour + willpower + 1)
        c = Changeling.objects.create(name="Grump")
        self.assertFalse(c.has_seeming())
        glamour = 4
        willpower = 4
        self.assertTrue(c.set_seeming("grump"))
        self.assertEqual(c.willpower, willpower + 1)

    def test_has_seeming(self):
        self.assertFalse(self.character.has_seeming())
        self.character.set_seeming("childer")
        self.assertTrue(self.character.has_seeming())

    def test_set_court(self):
        self.assertFalse(self.character.has_court())
        self.assertTrue(self.character.set_court("seelie"))
        self.assertTrue(self.character.has_court())

    def test_eligible_for_house(self):
        self.character.kith = Kith.objects.get(name="Kith 0")
        self.assertFalse(self.character.eligible_for_house())
        self.character.title = 1
        self.assertTrue(self.character.eligible_for_house())
        self.character.title = 0
        self.assertFalse(self.character.eligible_for_house())
        self.character.kith = Kith.objects.create(name="Arcadian Sidhe")
        self.assertTrue(self.character.eligible_for_house())

    def test_has_house(self):
        self.character.title = 1
        self.character.court = "seelie"
        self.assertFalse(self.character.has_house())
        self.assertTrue(self.character.set_house(House.objects.get(name="House 0")))
        self.assertTrue(self.character.has_house())
        self.character.title = 0
        self.assertFalse(self.character.has_house())
        self.character.house = None
        self.assertTrue(self.character.has_house())

    def test_set_house(self):
        self.assertTrue(self.character.has_house())
        self.assertFalse(self.character.set_house(House.objects.get(name="House 0")))
        self.character.title = 1
        self.character.court = "seelie"
        self.assertTrue(self.character.set_house(House.objects.get(name="House 0")))
        self.assertTrue(self.character.has_house())
        self.character.title = 0
        self.assertFalse(self.character.has_house())
        self.character.kith = Kith.objects.create(name="Arcadian Sidhe")
        self.assertTrue(self.character.set_house(House.objects.get(name="House 0")))
        self.assertTrue(self.character.has_house())
        self.character.court = "unseelie"
        self.assertFalse(self.character.set_house(House.objects.get(name="House 0")))

    def test_has_court(self):
        self.assertFalse(self.character.has_court())
        self.character.set_court("seelie")
        self.assertTrue(self.character.has_court())

    def test_has_kith(self):
        self.assertFalse(self.character.has_kith())
        self.character.set_kith(Kith.objects.get(name="Kith 0"))
        self.assertTrue(self.character.has_kith())

    def test_set_kith(self):
        self.assertFalse(self.character.has_kith())
        self.assertTrue(self.character.set_kith(Kith.objects.get(name="Kith 0")))
        self.assertTrue(self.character.has_kith())

    def test_set_seelie_legacy(self):
        seelie = CtDLegacy.objects.get(name="Legacy 0")
        unseelie = CtDLegacy.objects.get(name="Legacy 1")
        self.assertFalse(self.character.has_seelie_legacy())
        self.assertFalse(self.character.set_seelie_legacy(unseelie))
        self.assertFalse(self.character.has_seelie_legacy())
        self.assertTrue(self.character.set_seelie_legacy(seelie))
        self.assertTrue(self.character.has_seelie_legacy())

    def test_has_seelie_legacy(self):
        legacy = CtDLegacy.objects.get(name="Legacy 0")
        self.assertFalse(self.character.has_seelie_legacy())
        self.assertTrue(self.character.set_seelie_legacy(legacy))
        self.assertTrue(self.character.has_seelie_legacy())

    def test_set_unseelie_legacy(self):
        seelie = CtDLegacy.objects.get(name="Legacy 0")
        unseelie = CtDLegacy.objects.get(name="Legacy 1")
        self.assertFalse(self.character.has_unseelie_legacy())
        self.assertFalse(self.character.set_unseelie_legacy(seelie))
        self.assertFalse(self.character.has_unseelie_legacy())
        self.assertTrue(self.character.set_unseelie_legacy(unseelie))
        self.assertTrue(self.character.has_unseelie_legacy())

    def test_has_unseelie_legacy(self):
        legacy = CtDLegacy.objects.get(name="Legacy 1")
        self.assertFalse(self.character.has_unseelie_legacy())
        self.assertTrue(self.character.set_unseelie_legacy(legacy))
        self.assertTrue(self.character.has_unseelie_legacy())

    def test_add_art(self):
        self.character.wayfare = 0
        self.assertTrue(self.character.add_art("wayfare"))
        self.assertEqual(self.character.wayfare, 1)

    def test_get_arts(self):
        self.assertEqual(
            self.character.get_arts(),
            {
                "autumn": 0,
                "chicanery": 0,
                "chronos": 0,
                "contract": 0,
                "dragons_ire": 0,
                "legerdemain": 0,
                "metamorphosis": 0,
                "naming": 0,
                "oneiromancy": 0,
                "primal": 0,
                "pyretics": 0,
                "skycraft": 0,
                "soothsay": 0,
                "sovereign": 0,
                "spring": 0,
                "summer": 0,
                "wayfare": 0,
                "winter": 0,
            },
        )
        self.character.add_art("naming")
        self.character.add_art("naming")
        self.character.add_art("naming")
        self.character.add_art("wayfare")
        self.character.add_art("wayfare")
        self.character.add_art("pyretics")
        self.character.add_art("legerdemain")
        self.assertEqual(
            self.character.get_arts(),
            {
                "autumn": 0,
                "chicanery": 0,
                "chronos": 0,
                "contract": 0,
                "dragons_ire": 0,
                "legerdemain": 1,
                "metamorphosis": 0,
                "naming": 3,
                "oneiromancy": 0,
                "primal": 0,
                "pyretics": 1,
                "skycraft": 0,
                "soothsay": 0,
                "sovereign": 0,
                "spring": 0,
                "summer": 0,
                "wayfare": 2,
                "winter": 0,
            },
        )

    def test_has_arts(self):
        self.assertFalse(self.character.has_arts())
        self.character.add_art("naming")
        self.assertFalse(self.character.has_arts())
        self.character.add_art("naming")
        self.assertFalse(self.character.has_arts())
        self.character.add_art("naming")
        self.assertTrue(self.character.has_arts())

    def test_total_arts(self):
        self.assertEqual(self.character.total_arts(), 0)
        self.character.add_art("naming")
        self.assertEqual(self.character.total_arts(), 1)
        self.character.add_art("soothsay")
        self.assertEqual(self.character.total_arts(), 2)
        self.character.add_art("chronos")
        self.assertEqual(self.character.total_arts(), 3)

    def test_filter_arts(self):
        self.character.autumn = 0
        self.character.pyretics = 0
        self.character.chicanery = 1
        self.character.primal = 1
        self.character.skycraft = 1
        self.character.chronos = 2
        self.character.oneiromancy = 2
        self.character.soothsay = 2
        self.character.contract = 3
        self.character.naming = 3
        self.character.winter = 3
        self.character.sovereign = 3
        self.character.dragons_ire = 4
        self.character.spring = 4
        self.character.wayfare = 4
        self.character.metamorphosis = 4
        self.character.legerdemain = 5
        self.character.summer = 5
        self.assertEqual(len(self.character.filter_arts(minimum=0, maximum=5)), 18)
        self.assertEqual(len(self.character.filter_arts(minimum=1, maximum=5)), 16)
        self.assertEqual(len(self.character.filter_arts(minimum=2, maximum=5)), 13)
        self.assertEqual(len(self.character.filter_arts(minimum=3, maximum=5)), 10)
        self.assertEqual(len(self.character.filter_arts(minimum=4, maximum=5)), 6)
        self.assertEqual(len(self.character.filter_arts(minimum=5, maximum=5)), 2)
        self.assertEqual(len(self.character.filter_arts(minimum=0, maximum=4)), 16)
        self.assertEqual(len(self.character.filter_arts(minimum=0, maximum=3)), 12)
        self.assertEqual(len(self.character.filter_arts(minimum=0, maximum=2)), 8)
        self.assertEqual(len(self.character.filter_arts(minimum=0, maximum=1)), 5)
        self.assertEqual(len(self.character.filter_arts(minimum=0, maximum=0)), 2)

    def test_add_realm(self):
        self.character.actor = 0
        self.assertTrue(self.character.add_realm("actor"))
        self.assertEqual(self.character.actor, 1)

    def test_get_realms(self):
        self.assertEqual(
            self.character.get_realms(),
            {
                "actor": 0,
                "fae": 0,
                "nature_realm": 0,
                "prop": 0,
                "scene": 0,
                "time": 0,
            },
        )
        self.character.add_realm("actor")
        self.character.add_realm("actor")
        self.character.add_realm("actor")
        self.character.add_realm("nature_realm")
        self.character.add_realm("nature_realm")
        self.character.add_realm("scene")
        self.character.add_realm("time")
        self.assertEqual(
            self.character.get_realms(),
            {
                "actor": 3,
                "fae": 0,
                "nature_realm": 2,
                "prop": 0,
                "scene": 1,
                "time": 1,
            },
        )

    def test_has_realms(self):
        self.assertFalse(self.character.has_realms())
        self.character.add_realm("actor")
        self.assertFalse(self.character.has_realms())
        self.character.add_realm("actor")
        self.assertFalse(self.character.has_realms())
        self.character.add_realm("actor")
        self.assertFalse(self.character.has_realms())
        self.character.add_realm("fae")
        self.assertFalse(self.character.has_realms())
        self.character.add_realm("fae")
        self.assertTrue(self.character.has_realms())

    def test_total_realms(self):
        self.assertEqual(self.character.total_realms(), 0)
        self.character.add_realm("actor")
        self.assertEqual(self.character.total_realms(), 1)
        self.character.add_realm("time")
        self.assertEqual(self.character.total_realms(), 2)
        self.character.add_realm("fae")
        self.assertEqual(self.character.total_realms(), 3)

    def test_filter_realms(self):
        self.character.actor = 0
        self.character.fae = 1
        self.character.nature_realm = 2
        self.character.prop = 3
        self.character.scene = 4
        self.character.time = 5
        self.assertEqual(len(self.character.filter_realms(minimum=0, maximum=5)), 6)
        self.assertEqual(len(self.character.filter_realms(minimum=1, maximum=5)), 5)
        self.assertEqual(len(self.character.filter_realms(minimum=2, maximum=5)), 4)
        self.assertEqual(len(self.character.filter_realms(minimum=3, maximum=5)), 3)
        self.assertEqual(len(self.character.filter_realms(minimum=4, maximum=5)), 2)
        self.assertEqual(len(self.character.filter_realms(minimum=5, maximum=5)), 1)
        self.assertEqual(len(self.character.filter_realms(minimum=0, maximum=4)), 5)
        self.assertEqual(len(self.character.filter_realms(minimum=0, maximum=3)), 4)
        self.assertEqual(len(self.character.filter_realms(minimum=0, maximum=2)), 3)
        self.assertEqual(len(self.character.filter_realms(minimum=0, maximum=1)), 2)
        self.assertEqual(len(self.character.filter_realms(minimum=0, maximum=0)), 1)

    def test_set_musing_threshold(self):
        self.assertFalse(self.character.has_musing_threshold())
        self.assertTrue(self.character.set_musing_threshold("Inspire Creativity"))
        self.assertTrue(self.character.has_musing_threshold())

    def test_has_musing_threshold(self):
        self.assertFalse(self.character.has_musing_threshold())
        self.character.set_musing_threshold("Inspire Creativity")
        self.assertTrue(self.character.has_musing_threshold())

    def test_set_ravaging_threshold(self):
        self.assertFalse(self.character.has_ravaging_threshold())
        self.assertTrue(self.character.set_ravaging_threshold("Exhaust Creativity"))
        self.assertTrue(self.character.has_ravaging_threshold())

    def test_has_ravaging_threshold(self):
        self.assertFalse(self.character.has_ravaging_threshold())
        self.character.set_ravaging_threshold("Exhaust Creativity")
        self.assertTrue(self.character.has_ravaging_threshold())

    def test_set_antithesis(self):
        self.assertFalse(self.character.has_antithesis())
        self.assertTrue(self.character.set_antithesis("Random Antithesis"))
        self.assertTrue(self.character.has_antithesis())

    def test_has_antithesis(self):
        self.assertFalse(self.character.has_antithesis())
        self.character.set_antithesis("Random Antithesis")
        self.assertTrue(self.character.has_antithesis())

    def test_add_glamour(self):
        g = self.character.glamour
        self.assertTrue(self.character.add_glamour())
        self.assertEqual(self.character.glamour, g + 1)

    def test_add_banality(self):
        b = self.character.banality
        self.assertTrue(self.character.add_banality())
        self.assertEqual(self.character.banality, b + 1)

    # def test_changeling_numbers(self):
    #     # self.assertEqual(self.character.background_points, 5)
    #     # self.assertEqual(self.character.willpower, 4)
    #     # self.assertEqual(self.character.glamour, 4)
    #     # self.assertEqual(self.character.banality, 3)

    def test_freebie_cost(self):
        self.assertEqual(self.character.freebie_cost("attribute"), 5)
        self.assertEqual(self.character.freebie_cost("ability"), 2)
        self.assertEqual(self.character.freebie_cost("background"), 1)
        self.assertEqual(self.character.freebie_cost("willpower"), 1)
        self.assertEqual(self.character.freebie_cost("meritflaw"), 1)
        self.assertEqual(self.character.freebie_cost("art"), 5)
        self.assertEqual(self.character.freebie_cost("glamour"), 3)
        self.assertEqual(self.character.freebie_cost("realm"), 2)

    def test_spend_freebies(self):
        self.assertEqual(self.character.freebies, 15)
        self.assertTrue(self.character.spend_freebies("strength"))
        self.assertEqual(self.character.freebies, 10)
        self.assertTrue(self.character.spend_freebies("larceny"))
        self.assertEqual(self.character.freebies, 8)
        self.assertTrue(self.character.spend_freebies("mentor"))
        self.assertEqual(self.character.freebies, 7)
        self.assertTrue(self.character.spend_freebies("willpower"))
        self.assertEqual(self.character.freebies, 6)
        self.assertTrue(self.character.spend_freebies("Merit 1"))
        self.assertEqual(self.character.freebies, 5)
        self.character.freebies = 15
        self.assertEqual(self.character.freebies, 15)
        self.assertTrue(self.character.spend_freebies("winter"))
        self.assertEqual(self.character.freebies, 10)
        self.assertTrue(self.character.spend_freebies("actor"))
        self.assertEqual(self.character.freebies, 8)
        self.assertTrue(self.character.spend_freebies("glamour"))
        self.assertEqual(self.character.freebies, 5)

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("ability"), 2)
        self.assertEqual(self.character.xp_cost("background"), 3)
        self.assertEqual(self.character.xp_cost("new background"), 5)
        self.assertEqual(self.character.xp_cost("willpower"), 2)
        self.assertEqual(self.character.xp_cost("new ability"), 3)

        self.assertEqual(self.character.xp_cost("art"), 4)
        self.assertEqual(self.character.xp_cost("new art"), 7)
        self.assertEqual(self.character.xp_cost("realm"), 3)
        self.assertEqual(self.character.xp_cost("new realm"), 5)
        self.assertEqual(self.character.xp_cost("glamour"), 3)

    def test_spend_xp(self):
        self.character.willpower = 4
        self.character.glamour = 4
        self.character.xp = 100
        self.assertTrue(self.character.spend_xp("strength"))
        self.assertEqual(self.character.xp, 96)
        self.assertTrue(self.character.spend_xp("larceny"))
        self.assertEqual(self.character.xp, 93)
        self.assertTrue(self.character.spend_xp("larceny"))
        self.assertEqual(self.character.xp, 91)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 86)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 83)
        self.assertTrue(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 75)
        self.assertTrue(self.character.spend_xp("actor"))
        self.assertEqual(self.character.xp, 70)
        self.assertTrue(self.character.spend_xp("actor"))
        self.assertEqual(self.character.xp, 67)
        self.assertTrue(self.character.spend_xp("wayfare"))
        self.assertEqual(self.character.xp, 60)
        self.assertTrue(self.character.spend_xp("wayfare"))
        self.assertEqual(self.character.xp, 56)
        self.assertTrue(self.character.spend_xp("glamour"))
        self.assertEqual(self.character.xp, 44)

    def test_birthright_corrections(self):
        piskey = Kith.objects.create(name="Piskey")
        satyr = Kith.objects.create(name="Satyr")
        troll = Kith.objects.create(name="Troll")
        autumn_sidhe = Kith.objects.create(name="Autumn Sidhe")
        arcadian_sidhe = Kith.objects.create(name="Arcadian Sidhe")
        char1 = Changeling.objects.create(name="Char 1", kith=piskey)
        char2 = Changeling.objects.create(name="Char 2", kith=satyr)
        char3 = Changeling.objects.create(name="Char 3", kith=troll)
        char4 = Changeling.objects.create(name="Char 4", kith=autumn_sidhe)
        char5 = Changeling.objects.create(name="Char 5", kith=arcadian_sidhe)
        char1.birthright_correction()
        char2.birthright_correction()
        char3.birthright_correction()
        char4.birthright_correction()
        char5.birthright_correction()
        self.assertEqual(char1.dexterity, 2)
        self.assertEqual(char2.stamina, 2)
        self.assertEqual(char3.strength, 2)
        self.assertEqual(char3.max_health_levels, 8)
        self.assertEqual(char4.appearance, 3)
        self.assertEqual(char5.appearance, 3)

    def test_has_changeling_history(self):
        self.assertFalse(self.character.has_changeling_history())
        self.character.true_name = "Faerie Name"
        self.assertFalse(self.character.has_changeling_history())
        self.character.date_ennobled = "N/A"
        self.assertFalse(self.character.has_changeling_history())
        self.character.crysalis = "It Happened"
        self.assertFalse(self.character.has_changeling_history())
        self.character.date_of_crysalis = "It Happened"
        self.assertTrue(self.character.has_changeling_history())

    def test_has_changeling_appearance(self):
        self.assertFalse(self.character.has_changeling_appearance())
        self.character.fae_mien = "Magical"
        self.assertTrue(self.character.has_changeling_appearance())

    def test_set_changeling_appearance(self):
        fae_mien = "Beautiful butterfly wings"
        self.character.set_changeling_appearance(fae_mien)
        self.assertEqual(self.character.fae_mien, fae_mien)
        self.assertTrue(self.character.has_changeling_appearance())

    def test_set_changeling_history(self):
        true_name = "John Doe"
        date_ennobled = "01/01/2000"
        crysalis = "A cocoon"
        date_of_crysalis = "01/02/2000"
        self.character.set_changeling_history(
            true_name, date_ennobled, crysalis, date_of_crysalis
        )
        self.assertEqual(self.character.true_name, true_name)
        self.assertEqual(self.character.date_ennobled, date_ennobled)
        self.assertEqual(self.character.crysalis, crysalis)
        self.assertEqual(self.character.date_of_crysalis, date_of_crysalis)
        self.assertTrue(self.character.has_changeling_history())

    def test_random_freebie_functions(self):
        random_freebie_functions = self.character.random_freebie_functions()
        self.assertIn("attribute", random_freebie_functions)
        self.assertIn("ability", random_freebie_functions)
        self.assertIn("background", random_freebie_functions)
        self.assertIn("willpower", random_freebie_functions)
        self.assertIn("meritflaw", random_freebie_functions)
        self.assertIn("art", random_freebie_functions)
        self.assertIn("realm", random_freebie_functions)
        self.assertIn("glamour", random_freebie_functions)

    def test_random_xp_functions(self):
        random_xp_functions = self.character.random_xp_functions()
        self.assertIn("attribute", random_xp_functions)
        self.assertIn("ability", random_xp_functions)
        self.assertIn("background", random_xp_functions)
        self.assertIn("willpower", random_xp_functions)
        self.assertIn("art", random_xp_functions)
        self.assertIn("realm", random_xp_functions)
        self.assertIn("glamour", random_xp_functions)


class TestRandomChangeling(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")
        changeling_setup(self.player)

    def test_random_house(self):
        self.character.title = 1
        self.character.court = "seelie"
        self.assertFalse(self.character.has_house())
        self.character.set_house(House.objects.get(name="House 0"))
        self.assertTrue(self.character.has_house())

    def test_random_seeming(self):
        self.assertFalse(self.character.has_seeming())
        self.assertTrue(self.character.random_seeming())
        self.assertTrue(self.character.has_seeming())

    def test_random_court(self):
        self.assertFalse(self.character.has_court())
        self.assertTrue(self.character.random_court())
        self.assertTrue(self.character.has_court())

    def test_random_seelie_legacy(self):
        self.assertFalse(self.character.has_seelie_legacy())
        self.character.random_seelie_legacy()
        self.assertTrue(self.character.has_seelie_legacy())

    def test_random_unseelie_legacy(self):
        self.assertFalse(self.character.has_unseelie_legacy())
        self.character.random_unseelie_legacy()
        self.assertTrue(self.character.has_unseelie_legacy())

    def test_random_background(self):
        self.fail()

    def test_random_changeling_history(self):
        self.fail()

    def test_random_changeling_appearance(self):
        self.fail()

    def test_random_kith(self):
        self.assertFalse(self.character.has_kith())
        self.character.random_kith()
        self.assertTrue(self.character.has_kith())

    def test_random_art(self):
        total = self.character.total_arts()
        self.character.random_art()
        self.assertEqual(self.character.total_arts(), total + 1)

    def test_random_arts(self):
        self.assertFalse(self.character.has_arts())
        self.character.random_arts()
        self.assertTrue(self.character.has_arts())

    def test_random_realm(self):
        total = self.character.total_realms()
        self.character.random_realm()
        self.assertEqual(self.character.total_realms(), total + 1)

    def test_random_realms(self):
        self.assertFalse(self.character.has_realms())
        self.character.random_realms()
        self.assertTrue(self.character.has_realms())

    def test_random_musing_threshold(self):
        self.assertFalse(self.character.has_musing_threshold())
        self.character.random_musing_threshold()
        self.assertTrue(self.character.has_musing_threshold())

    def test_random_ravaging_threshold(self):
        self.assertFalse(self.character.has_ravaging_threshold())
        self.character.random_ravaging_threshold()
        self.assertTrue(self.character.has_ravaging_threshold())

    def test_random_antithesis(self):
        self.assertFalse(self.character.has_antithesis())
        self.character.random_antithesis()
        self.assertTrue(self.character.has_antithesis())

    def test_random_freebies(self):
        self.assertEqual(self.character.freebies, 15)
        self.character.random_freebies()
        self.assertEqual(self.character.freebies, 0)

    def test_random_spend_xp(self):
        self.character.xp = 15
        self.character.random_xp()
        self.assertLess(self.character.xp, 15)

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        self.assertFalse(self.character.has_kith())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_backgrounds())
        self.assertFalse(self.character.has_finishing_touches())
        self.assertFalse(self.character.has_history())
        self.assertFalse(self.character.has_seeming())
        self.assertFalse(self.character.has_court())
        self.assertFalse(self.character.has_seelie_legacy())
        self.assertFalse(self.character.has_unseelie_legacy())
        self.assertFalse(self.character.has_arts())
        self.assertFalse(self.character.has_realms())
        self.assertFalse(self.character.has_musing_threshold())
        self.assertFalse(self.character.has_ravaging_threshold())
        self.assertFalse(self.character.has_antithesis())
        self.assertFalse(self.character.has_changeling_history())
        self.assertFalse(self.character.has_changeling_appearance())
        self.character.random(freebies=0, xp=0)
        self.assertTrue(self.character.has_name())
        self.assertTrue(self.character.has_concept())
        self.assertTrue(self.character.has_kith())
        self.assertTrue(self.character.has_attributes())
        self.assertTrue(self.character.has_abilities())
        self.assertTrue(self.character.has_specialties())
        self.assertTrue(self.character.has_backgrounds())
        self.assertTrue(self.character.has_finishing_touches())
        self.assertTrue(self.character.has_history())
        self.assertTrue(self.character.has_seeming())
        self.assertTrue(self.character.has_court())
        self.assertTrue(self.character.has_seelie_legacy())
        self.assertTrue(self.character.has_unseelie_legacy())
        self.assertTrue(self.character.has_arts())
        self.assertTrue(self.character.has_realms())
        self.assertTrue(self.character.has_musing_threshold())
        self.assertTrue(self.character.has_ravaging_threshold())
        self.assertTrue(self.character.has_antithesis())
        self.assertTrue(self.character.has_house())
        self.assertTrue(self.character.has_changeling_history())
        self.assertTrue(self.character.has_changeling_appearance())

    def test_random_freebies_art(self):
        self.fail()

    def test_random_freebies_realm(self):
        self.fail()

    def test_random_freebies_glamour(self):
        self.fail()

    def test_random_xp_art(self):
        self.fail()

    def test_random_xp_realm(self):
        self.fail()

    def test_random_xp_glamour(self):
        self.fail()


class TestMotley(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        changeling_setup(self.player)

    def test_motley_creation(self):
        motley = Motley.objects.create(name="Motley 1")
        motley.members.set(Changeling.objects.all())
        motley.leader = Changeling.objects.first()
        motley.save()
        self.assertEqual(motley.members.count(), 5)
        self.assertIsNotNone(motley.leader)

    def test_random(self):
        motley = Motley.objects.create(name="Motley 1")
        motley.random(num_chars=5, new_characters=False)
        self.assertEqual(motley.members.count(), 5)
        for changeling in Changeling.objects.all():
            self.assertIn(changeling, motley.members.all())
        motley = Motley.objects.create(name="Motley 2")
        motley.random(num_chars=5, new_characters=True)
        self.assertEqual(motley.members.count(), 5)

    def test_exception(self):
        motley = Motley.objects.create(name="Motley 10")
        with self.assertRaises(ValueError):
            motley.random(num_chars=10, new_characters=False)

    def test_str(self):
        motley = Motley.objects.create(name="Motley 1")
        self.assertEqual(str(motley), "Motley 1")


class TestChangelingDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.changeling = Changeling.objects.create(
            name="Test Changeling", owner=self.player
        )

    def test_changeling_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.changeling.id}/")
        self.assertEqual(response.status_code, 200)

    def test_changeling_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.changeling.id}/")
        self.assertTemplateUsed(
            response, "wod/characters/changeling/changeling/detail.html"
        )


class TestMotleyDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.motley = Motley.objects.create(name="Test Motley")

    def test_motley_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/groups/{self.motley.id}/")
        self.assertEqual(response.status_code, 200)

    def test_motley_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/groups/{self.motley.id}/")
        self.assertTemplateUsed(
            response, "wod/characters/changeling/motley/detail.html"
        )
