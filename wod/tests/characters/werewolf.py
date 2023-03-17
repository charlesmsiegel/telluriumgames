from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from wod.models.characters.human import Archetype, Derangement, MeritFlaw, WoDSpecialty
from wod.models.characters.werewolf import (
    Camp,
    Gift,
    Pack,
    RenownIncident,
    Rite,
    Totem,
    Tribe,
    Werewolf,
)
from wod.models.characters.werewolf.fomori import Fomor, FomoriPower
from wod.models.characters.werewolf.garou import BattleScar
from wod.models.characters.werewolf.kinfolk import Kinfolk
from wod.models.characters.werewolf.wtahuman import WtAHuman
from wod.models.items.werewolf import Fetish


# Create your tests here.
def werewolf_setup(player):
    for i in range(5):
        w = Werewolf.objects.create(name=f"Character {i}", owner=player)
    for i in range(5):
        Totem.objects.create(name=f"Totem {i}", cost=10 + i)
    for i in range(1, 6):
        Gift.objects.create(name=f"Gift {i}", rank=i, allowed={"garou": []})
        Gift.objects.create(name=f"Gift {5+i}", rank=i, allowed={"garou": []})
    t = Tribe.objects.create(name="Test Tribe", willpower=5)
    Tribe.objects.create(name="Test Tribe 2", willpower=3)
    Camp.objects.create(name="Test Camp", tribe=t)
    for t in Tribe.objects.all():
        Gift.objects.create(name=f"{t.name} Gift", rank=1, allowed={"garou": [t.name]})
    for auspice in ["ragabash", "theurge", "philodox", "galliard", "ahroun"]:
        Gift.objects.create(
            name=f"{auspice.title()} Gift", rank=1, allowed={"garou": [auspice]}
        )
    for breed in ["homid", "metis", "lupus"]:
        Gift.objects.create(
            name=f"{breed.title()} Gift", rank=1, allowed={"garou": [breed]}
        )
    for i in range(6):
        Rite.objects.create(name=f"Rite {i}", level=i)
        Rite.objects.create(name=f"Rite {6+i}", level=i)
    for i in range(5):
        MeritFlaw.objects.create(name=f"Merit {i}", ratings=[i], garou=True)
        MeritFlaw.objects.create(name=f"Flaw {i}", ratings=[-i], garou=True)
    for i in range(10):
        for trait in w.get_attributes():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )

        for trait in w.get_abilities():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )
    for i in range(20):
        Archetype.objects.create(name=f"Archetype {i}")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                RenownIncident.objects.create(
                    name=f"Incident {i}, {j}, {k}",
                    glory=i - 1,
                    honor=j - 1,
                    wisdom=k - 1,
                )
    for i in range(6):
        Fetish.objects.create(name=f"Fetish {i}", rank=i, gnosis=i)
        Fetish.objects.create(name=f"Fetish {i+6}", rank=i, gnosis=i)
        Fetish.objects.create(name=f"Fetish {i+12}", rank=i, gnosis=i)
        Fetish.objects.create(name=f"Fetish {i+18}", rank=i, gnosis=i)
        Fetish.objects.create(name=f"Fetish {i+24}", rank=i, gnosis=i)


class TestWtAHuman(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = WtAHuman.objects.create(
            name="Test WtAHuman", owner=self.player
        )
        werewolf_setup(self.player)

    def set_abilities(self):
        self.character.brawl = 1
        self.character.expression = 3
        self.character.intimidation = 2
        self.character.subterfuge = 1
        self.character.leadership = 4
        self.character.crafts = 2
        self.character.etiquette = 1
        self.character.animal_ken = 5
        self.character.larceny = 2
        self.character.survival = 1
        self.character.computer = 4
        self.character.science = 5
        self.character.law = 3
        self.character.rituals = 2
        self.character.technology = 1

    def test_get_abilities(self):
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "expression": 0,
                "intimidation": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "leadership": 0,
                "primal_urge": 0,
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 0,
                "larceny": 0,
                "performance": 0,
                "survival": 0,
                "academics": 0,
                "computer": 0,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
                "enigmas": 0,
                "law": 0,
                "occult": 0,
                "rituals": 0,
                "technology": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 1,
                "empathy": 0,
                "expression": 3,
                "intimidation": 2,
                "streetwise": 0,
                "subterfuge": 1,
                "leadership": 4,
                "primal_urge": 0,
                "crafts": 2,
                "drive": 0,
                "etiquette": 1,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 5,
                "larceny": 2,
                "performance": 0,
                "survival": 1,
                "academics": 0,
                "computer": 4,
                "investigation": 0,
                "medicine": 0,
                "science": 5,
                "enigmas": 0,
                "law": 3,
                "occult": 0,
                "rituals": 2,
                "technology": 1,
            },
        )

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
                "streetwise": 0,
                "subterfuge": 0,
                "leadership": 0,
                "primal_urge": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 1,
                "empathy": 0,
                "expression": 3,
                "intimidation": 2,
                "streetwise": 0,
                "subterfuge": 1,
                "leadership": 4,
                "primal_urge": 0,
            },
        )

    def test_get_skills(self):
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 0,
                "larceny": 0,
                "performance": 0,
                "survival": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 2,
                "drive": 0,
                "etiquette": 1,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 5,
                "larceny": 2,
                "performance": 0,
                "survival": 1,
            },
        )

    def test_get_knowledges(self):
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
                "enigmas": 0,
                "law": 0,
                "occult": 0,
                "rituals": 0,
                "technology": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 4,
                "investigation": 0,
                "medicine": 0,
                "science": 5,
                "enigmas": 0,
                "law": 3,
                "occult": 0,
                "rituals": 2,
                "technology": 1,
            },
        )

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 0,
                "ancestors": 0,
                "fate": 0,
                "fetish": 0,
                "kinfolk_rating": 0,
                "pure_breed": 0,
                "contacts": 0,
                "rites": 0,
                "spirit_heritage": 0,
                "mentor": 0,
                "resources": 0,
                "totem": 0,
            },
        )
        self.character.allies = 1
        self.character.ancestors = 3
        self.character.kinfolk_rating = 3
        self.character.pure_breed = 2
        self.character.mentor = 2
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 1,
                "ancestors": 3,
                "fate": 0,
                "fetish": 0,
                "kinfolk_rating": 3,
                "pure_breed": 2,
                "contacts": 0,
                "rites": 0,
                "spirit_heritage": 0,
                "mentor": 2,
                "resources": 0,
                "totem": 0,
            },
        )

    def test_total_backgrounds(self):
        self.character.allies = 3
        self.character.ancestors = 4
        self.character.resources = 1
        self.character.fetish = 2
        self.assertEqual(self.character.total_backgrounds(), 10)
        self.character.spirit_heritage = 2
        self.assertEqual(self.character.total_backgrounds(), 12)


class TestKinfolk(TestCase):
    def setUp(self):
        self.tribe = Tribe.objects.create(name="Test Tribe")
        self.gift = Gift.objects.create(name="Test Gift", rank=1)
        self.fetish = Fetish.objects.create(name="Test Fetish", rank=1)
        self.kinfolk = Kinfolk.objects.create(name="Test Kinfolk")

    def test_has_breed(self):
        self.assertFalse(self.kinfolk.has_breed())
        self.kinfolk.set_breed("homid")
        self.assertTrue(self.kinfolk.has_breed())

    def test_set_breed(self):
        self.assertEqual(self.kinfolk.breed, "")
        self.assertTrue(self.kinfolk.set_breed("lupus"))
        self.assertEqual(self.kinfolk.breed, "lupus")

    def test_set_tribe(self):
        self.assertIsNone(self.kinfolk.tribe)
        self.assertTrue(self.kinfolk.set_tribe(self.tribe))
        self.assertEqual(self.kinfolk.tribe, self.tribe)
        self.kinfolk.set_breed("homid")
        rt = Tribe.objects.create(name="Red Talons")
        sf = Tribe.objects.create(name="Silver Fangs")
        bsd = Tribe.objects.create(name="Black Spiral Dancers")
        self.assertFalse(self.kinfolk.set_tribe(rt))
        self.kinfolk.set_breed("lupus")
        self.assertTrue(self.kinfolk.set_tribe(rt))
        self.assertTrue(self.kinfolk.set_tribe(sf))
        self.assertGreater(self.kinfolk.pure_breed, 0)
        Derangement.objects.create(name="Test Derangement")
        self.assertTrue(self.kinfolk.set_tribe(bsd))
        self.assertGreater(self.kinfolk.derangements.count(), 0)

    def test_has_tribe(self):
        self.assertFalse(self.kinfolk.has_tribe())
        self.kinfolk.set_tribe(self.tribe)
        self.assertTrue(self.kinfolk.has_tribe())

    def test_get_backgrounds(self):
        backgrounds = self.kinfolk.get_backgrounds()
        self.assertEqual(backgrounds["allies"], 0)
        self.assertEqual(backgrounds["contacts"], 0)
        self.assertEqual(backgrounds["mentor"], 0)
        self.assertEqual(backgrounds["pure_breed"], 0)
        self.assertEqual(backgrounds["resources"], 0)

    def test_add_background(self):
        bg = Tribe.objects.create(name="Bone Gnawers")
        self.kinfolk.set_tribe(bg)
        self.assertFalse(self.kinfolk.add_background("pure_breed"))
        self.assertTrue(self.kinfolk.add_background("resources"))
        self.assertTrue(self.kinfolk.add_background("resources"))
        self.assertTrue(self.kinfolk.add_background("resources"))
        self.assertFalse(self.kinfolk.add_background("resources"))
        gw = Tribe.objects.create(name="Glass Walkers")
        self.kinfolk.set_tribe(gw)
        self.kinfolk.resources = 0
        self.assertFalse(self.kinfolk.add_background("pure_breed"))
        self.assertFalse(self.kinfolk.add_background("mentor"))
        rt = Tribe.objects.create(name="Red Talons")
        self.kinfolk.set_tribe(rt)
        self.assertFalse(self.kinfolk.add_background("resources"))
        sl = Tribe.objects.create(name="Shadow Lords")
        self.kinfolk.set_tribe(sl)
        self.assertFalse(self.kinfolk.add_background("mentor"))
        self.kinfolk.resources = 3
        ss = Tribe.objects.create(name="Silent Striders")
        self.kinfolk.set_tribe(ss)
        self.assertFalse(self.kinfolk.add_background("resources"))
        sg = Tribe.objects.create(name="Stargazers")
        self.kinfolk.set_tribe(sg)
        self.assertFalse(self.kinfolk.add_background("resources"))
        w = Tribe.objects.create(name="Wendigo")
        self.kinfolk.set_tribe(w)
        self.assertFalse(self.kinfolk.add_background("resources"))

    def test_xp_cost(self):
        self.assertEqual(self.kinfolk.xp_cost("attribute"), 4)
        self.assertEqual(self.kinfolk.xp_cost("ability"), 2)
        self.assertEqual(self.kinfolk.xp_cost("gift"), 15)
        self.assertEqual(self.kinfolk.xp_cost("outside gift"), 20)

    def test_spend_xp(self):
        self.kinfolk.xp = 100
        self.kinfolk.set_tribe(Tribe.objects.create(name="Test Tribe"))
        g1 = Gift.objects.create(name="G1", rank=1, allowed={"garou": ["Test Tribe"]})
        g2 = Gift.objects.create(name="G2", rank=1, allowed={"garou": []})
        self.kinfolk.spend_xp(g1.name)
        self.assertEqual(self.kinfolk.xp, 85)
        self.kinfolk.spend_xp(g2.name)
        self.assertEqual(self.kinfolk.xp, 65)

    def test_random_xp_functions(self):
        functions = self.kinfolk.random_xp_functions()
        self.assertTrue(callable(functions["attribute"]))
        self.assertTrue(callable(functions["ability"]))
        self.assertTrue(callable(functions["background"]))
        self.assertTrue(callable(functions["willpower"]))
        self.assertTrue(callable(functions["gift"]))

    def test_add_gift(self):
        self.assertTrue(self.kinfolk.add_gift(self.gift))
        self.assertFalse(self.kinfolk.add_gift(self.gift))

    def test_set_relation(self):
        self.assertTrue(self.kinfolk.set_relation("Test Relation"))

    def test_has_relation(self):
        self.assertFalse(self.kinfolk.has_relation())
        self.kinfolk.relation = "Test Relation"
        self.assertTrue(self.kinfolk.has_relation())

    def test_mf_based_corrections(self):
        gnosis = MeritFlaw.objects.create(name="Gnosis", ratings=[5, 6, 7])
        fetish = MeritFlaw.objects.create(name="Fetish", ratings=[5, 6, 7])
        Fetish.objects.create(name="Test Fetish", rank=1)
        self.kinfolk.add_mf(gnosis, 5)
        self.kinfolk.add_mf(fetish, 5)
        self.kinfolk.mf_based_corrections()
        self.assertNotEqual(self.kinfolk.gnosis, 0)
        self.assertTrue(self.kinfolk.fetishes_owned.exists())

    def test_add_fetish(self):
        # Test that a Kinfolk can add a fetish successfully
        self.assertTrue(self.kinfolk.add_fetish(self.fetish))

        # Test that a Kinfolk cannot add a fetish they already own
        self.assertFalse(self.kinfolk.add_fetish(self.fetish))

    def test_filter_fetishes(self):
        # Test that the method returns the correct set of fetishes
        filtered_fetishes = self.kinfolk.filter_fetishes(min_rating=3, max_rating=5)
        self.assertNotIn(self.fetish, filtered_fetishes)


class TestRandomKinfolk(TestCase):
    def setUp(self):
        self.kinfolk = Kinfolk.objects.create(name="Test Kinfolk")

    def test_random_breed(self):
        with patch("random.choice", return_value="homid"):
            self.kinfolk.random_breed()
            self.assertEqual(self.kinfolk.breed, "homid")
        with patch("random.choice", return_value="lupus"):
            self.kinfolk.random_breed()
            self.assertEqual(self.kinfolk.breed, "lupus")

    def test_random_tribe(self):
        Tribe.objects.create(name="Test Tribe 1")
        Tribe.objects.create(name="Test Tribe 2")
        self.kinfolk.random_tribe()
        self.assertIsInstance(self.kinfolk.tribe, Tribe)

    def test_choose_random_gift(self):
        Gift.objects.create(
            name="Test Gift 1", rank=1, allowed={"garou": ["homid", "Test Tribe"]}
        )
        Gift.objects.create(
            name="Test Gift 2", rank=1, allowed={"garou": ["lupus", "Test Tribe"]}
        )
        Gift.objects.create(name="Test Gift 3", rank=2)
        Gift.objects.create(name="Test Gift 4", rank=2)
        self.kinfolk.set_breed("homid")
        self.kinfolk.set_tribe(Tribe.objects.create(name="Test Tribe"))
        choice = self.kinfolk.choose_random_gift()
        self.assertIsInstance(choice, Gift)
        choice = self.kinfolk.choose_random_gift(breed=True)
        self.assertIsInstance(choice, Gift)
        choice = self.kinfolk.choose_random_gift(tribe=True)
        self.assertIsInstance(choice, Gift)
        choice = self.kinfolk.choose_random_gift(breed=True, tribe=True)
        self.assertIsInstance(choice, Gift)

    def test_random_xp_gift(self):
        self.kinfolk.xp = 20
        self.kinfolk.set_breed("homid")
        self.kinfolk.set_tribe(Tribe.objects.create(name="Test Tribe"))
        Gift.objects.create(name="Test Gift 1", rank=1)
        self.assertTrue(self.kinfolk.random_xp_gift())
        self.assertEqual(self.kinfolk.xp, 0)

    def test_random_relation(self):
        with patch("random.choice", return_value="Test Relation"):
            self.kinfolk.random_relation()
            self.assertEqual(self.kinfolk.relation, "Test Relation")

    def test_random_fetish(self):
        Fetish.objects.create(name="Test", rank=2)
        fetish_count_before = self.kinfolk.fetishes_owned.count()
        self.kinfolk.random_fetish()
        fetish_count_after = self.kinfolk.fetishes_owned.count()
        self.assertNotEqual(fetish_count_before, fetish_count_after)

    def test_random(self):
        player = User.objects.create_user(username="Player")
        werewolf_setup(player)
        self.kinfolk.random(freebies=0)
        self.assertEqual(self.kinfolk.status, "Ran")
        self.assertTrue(self.kinfolk.has_name())
        self.assertTrue(self.kinfolk.has_breed())
        self.assertTrue(self.kinfolk.has_tribe())
        self.assertTrue(self.kinfolk.has_relation())
        self.assertTrue(self.kinfolk.has_attributes(primary=6, secondary=4, tertiary=3))
        self.assertTrue(self.kinfolk.has_abilities(primary=11, secondary=7, tertiary=4))
        self.assertTrue(self.kinfolk.has_backgrounds())
        self.assertTrue(self.kinfolk.has_history())
        self.assertTrue(self.kinfolk.has_finishing_touches())


class TestGift(TestCase):
    def setUp(self):
        self.gift = Gift.objects.create()

    def test_save(self):
        self.assertIn("garou", self.gift.allowed)


class TestFomor(TestCase):
    def setUp(self):
        self.power1 = FomoriPower.objects.create(name="Power 1")
        self.power2 = FomoriPower.objects.create(name="Power 2")
        self.power3 = FomoriPower.objects.create(name="Power 3")
        self.fomor = Fomor.objects.create(name="Test Fomor", allies=2, contacts=1)

    def test_get_backgrounds(self):
        expected = {
            "allies": 2,
            "contacts": 1,
            "resources": 0,
        }
        self.assertEqual(self.fomor.get_backgrounds(), expected)

    def test_add_power(self):
        self.fomor.add_power(self.power1)
        self.assertEqual(self.fomor.powers.count(), 1)
        self.assertEqual(list(self.fomor.powers.all()), [self.power1])

    def test_filter_powers(self):
        self.fomor.add_power(self.power1)
        self.fomor.add_power(self.power2)
        self.fomor.add_power(self.power3)
        filtered_powers = self.fomor.filter_powers()
        self.assertEqual(filtered_powers.count(), 0)
        self.fomor.powers.remove(self.power3)
        filtered_powers = self.fomor.filter_powers()
        self.assertEqual(filtered_powers.count(), 1)
        self.assertEqual(list(filtered_powers.all()), [self.power3])


class TestRandomFomor(TestCase):
    def setUp(self):
        self.power1 = FomoriPower.objects.create(name="Power 1")
        self.power2 = FomoriPower.objects.create(name="Power 2")
        self.power3 = FomoriPower.objects.create(name="Power 3")
        FomoriPower.objects.create(name="Immunity to the Delirium")
        self.fomor = Fomor.objects.create(name="Test Fomor")
        for attribute in self.fomor.get_attributes():
            WoDSpecialty.objects.create(name=f"{attribute} Spec", stat=attribute)
        for ability in self.fomor.get_abilities():
            WoDSpecialty.objects.create(name=f"{ability} Spec", stat=ability)
        for i in range(10):
            Archetype.objects.create(name=f"Archetype {i}")

    def test_random_power(self):
        self.assertEqual(self.fomor.powers.count(), 0)
        self.fomor.random_power()
        self.assertEqual(self.fomor.powers.count(), 1)

    def test_random_powers(self):
        self.fomor.random_powers(num_powers=2)
        self.assertGreaterEqual(self.fomor.powers.count(), 2)

    def test_random(self):
        self.fomor.random(freebies=0, xp=0)
        self.assertTrue(self.fomor.has_name())
        self.assertTrue(self.fomor.has_concept())
        self.assertTrue(self.fomor.has_archetypes())
        self.assertTrue(self.fomor.has_attributes(primary=6, secondary=4, tertiary=3))
        self.assertTrue(self.fomor.has_abilities(primary=11, secondary=7, tertiary=3))
        self.assertTrue(self.fomor.has_backgrounds())
        self.assertGreater(self.fomor.powers.count(), 0)


class TestTribe(TestCase):
    def setUp(self):
        self.tribe = Tribe.objects.create(name="Test Tribe", willpower=4)
        self.tribe_no = Tribe.objects.create(name="Other Tribe", willpower=4)
        self.camp = Camp.objects.create(name="Test Camp", tribe=self.tribe)
        self.camp_no = Camp.objects.create(name="Other Camp", tribe=self.tribe_no)
        self.gift1 = Gift.objects.create(
            name="Test Gift 1", rank=1, allowed={"garou": [self.tribe.name]}
        )
        self.gift2 = Gift.objects.create(
            name="Test Gift 2", rank=2, allowed={"garou": [self.tribe.name]}
        )
        self.gift3 = Gift.objects.create(
            name="Test Gift 3", rank=3, allowed={"garou": [self.tribe.name]}
        )
        self.gift4 = Gift.objects.create(
            name="Test Gift 4", rank=4, allowed={"garou": [self.tribe.name]}
        )
        self.gift5 = Gift.objects.create(
            name="Test Gift 5", rank=5, allowed={"garou": [self.tribe.name]}
        )
        self.gift6 = Gift.objects.create(
            name="Test Gift 6", rank=6, allowed={"garou": [self.tribe.name]}
        )
        self.gift1_no = Gift.objects.create(
            name="Test No Gift 1", rank=1, allowed={"garou": ["Tribe 2"]}
        )
        self.gift2_no = Gift.objects.create(
            name="Test No Gift 2", rank=2, allowed={"garou": ["Tribe 2"]}
        )
        self.gift3_no = Gift.objects.create(
            name="Test No Gift 3", rank=3, allowed={"garou": ["Tribe 2"]}
        )
        self.gift4_no = Gift.objects.create(
            name="Test No Gift 4", rank=4, allowed={"garou": ["Tribe 2"]}
        )
        self.gift5_no = Gift.objects.create(
            name="Test No Gift 5", rank=5, allowed={"garou": ["Tribe 2"]}
        )
        self.gift6_no = Gift.objects.create(
            name="Test No Gift 6", rank=6, allowed={"garou": ["Tribe 2"]}
        )

    def test_camp_list(self):
        output = self.tribe.camp_list()
        self.assertFalse(self.camp_no.name in output)
        self.assertTrue(self.camp.name in output)

    def test_gifts_level_1(self):
        output = ", ".join(self.tribe.gifts_level_1())
        self.assertFalse(self.gift1_no.name in output)
        self.assertTrue(self.gift1.name in output)

    def test_gifts_level_2(self):
        output = ", ".join(self.tribe.gifts_level_2())
        self.assertFalse(self.gift2_no.name in output)
        self.assertTrue(self.gift2.name in output)

    def test_gifts_level_3(self):
        output = ", ".join(self.tribe.gifts_level_3())
        self.assertFalse(self.gift3_no.name in output)
        self.assertTrue(self.gift3.name in output)

    def test_gifts_level_4(self):
        output = ", ".join(self.tribe.gifts_level_4())
        self.assertFalse(self.gift4_no.name in output)
        self.assertTrue(self.gift4.name in output)

    def test_gifts_level_5(self):
        output = ", ".join(self.tribe.gifts_level_5())
        self.assertFalse(self.gift5_no.name in output)
        self.assertTrue(self.gift5.name in output)

    def test_gifts_level_6(self):
        output = ", ".join(self.tribe.gifts_level_6())
        self.assertFalse(self.gift6_no.name in output)
        self.assertTrue(self.gift6.name in output)


class TestWerewolf(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = Werewolf.objects.create(
            name="Test Werewolf", owner=self.player
        )
        werewolf_setup(self.player)

    def test_add_gift(self):
        g = Gift.objects.get(name="Gift 1")
        self.assertEqual(self.character.gifts.count(), 0)
        self.assertTrue(self.character.add_gift(g))
        self.assertEqual(self.character.gifts.count(), 1)
        self.assertIn(g, self.character.gifts.all())

    def test_filter_gifts(self):
        self.character.rank = 2
        self.assertEqual(len(self.character.filter_gifts()), 14)
        self.character.add_gift(Gift.objects.get(name="Gift 1"))
        self.character.add_gift(Gift.objects.get(name="Gift 2"))
        self.assertEqual(len(self.character.filter_gifts()), 12)

    def test_has_gifts(self):
        t = Tribe.objects.get(name="Test Tribe", willpower=5)
        self.character.set_tribe(t)
        self.character.set_breed("homid")
        self.character.set_auspice("ragabash")
        g1 = Gift.objects.get(name="Test Tribe Gift")
        g2 = Gift.objects.get(name="Ragabash Gift")
        g3 = Gift.objects.get(name="Homid Gift")
        self.assertFalse(self.character.has_gifts())
        self.character.add_gift(g1)
        self.assertFalse(self.character.has_gifts())
        self.character.add_gift(g2)
        self.assertFalse(self.character.has_gifts())
        self.character.add_gift(g3)
        self.assertTrue(self.character.has_gifts())

    def test_total_rites(self):
        rite = Rite.objects.create(name="Test", level=1)
        self.character.add_rite(rite)
        self.character.add_rite(rite)
        self.assertEqual(self.character.total_rites(), 1)

    def test_add_rite(self):
        r = Rite.objects.get(name="Rite 1", level=1)
        self.assertEqual(self.character.rites_known.count(), 0)
        self.assertTrue(self.character.add_rite(r))
        self.assertEqual(self.character.rites_known.count(), 1)
        self.assertIn(r, self.character.rites_known.all())

    def test_filter_rites(self):
        self.assertEqual(len(self.character.filter_rites()), 12)
        self.character.add_rite(Rite.objects.get(name="Rite 1"))
        self.character.add_rite(Rite.objects.get(name="Rite 2"))
        self.assertEqual(len(self.character.filter_rites()), 10)

    def test_has_rites(self):
        self.character.rites = 3
        self.assertFalse(self.character.has_rites())
        self.character.add_rite(Rite.objects.get(name="Rite 3"))
        self.assertTrue(self.character.has_rites())

    def test_set_tribe(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.assertFalse(self.character.has_tribe())
        self.assertTrue(self.character.set_tribe(t))
        self.assertTrue(self.character.has_tribe())

    def test_has_tribe(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.assertFalse(self.character.has_tribe())
        self.character.set_tribe(t)
        self.assertTrue(self.character.has_tribe())

    def test_set_breed(self):
        self.assertFalse(self.character.has_breed())
        self.assertTrue(self.character.set_breed("homid"))
        self.assertTrue(self.character.has_breed())

    def test_has_breed(self):
        self.assertFalse(self.character.has_breed())
        self.character.set_breed("homid")
        self.assertTrue(self.character.has_breed())

    def test_breed_sets_gnosis(self):
        self.character.set_breed("homid")
        self.assertEqual(self.character.gnosis, 1)
        self.character.set_breed("metis")
        self.assertEqual(self.character.gnosis, 3)
        self.character.set_breed("lupus")
        self.assertEqual(self.character.gnosis, 5)

    def test_add_camp(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        c = Camp.objects.get(name="Test Camp")
        self.assertFalse(self.character.has_camp())
        self.assertTrue(self.character.add_camp(c))
        self.assertTrue(self.character.has_camp())

    def test_has_camp(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        c = Camp.objects.get(name="Test Camp", tribe=t)
        self.assertFalse(self.character.has_camp())
        self.character.add_camp(c)
        self.assertTrue(self.character.has_camp())

    def test_set_gnosis(self):
        self.character.set_gnosis(4)
        self.assertEqual(self.character.gnosis, 4)

    def test_add_gnosis(self):
        self.assertEqual(self.character.gnosis, 0)
        self.assertTrue(self.character.add_gnosis())
        self.assertEqual(self.character.gnosis, 1)
        self.character.gnosis = 10
        self.assertFalse(self.character.add_gnosis())

    def test_set_rage(self):
        self.character.set_rage(5)
        self.assertEqual(self.character.rage, 5)

    def test_add_rage(self):
        self.assertEqual(self.character.rage, 0)
        self.assertTrue(self.character.add_rage())
        self.assertEqual(self.character.rage, 1)
        self.character.rage = 10
        self.assertFalse(self.character.add_rage())

    def test_tribe_sets_willpower(self):
        t = Tribe.objects.get(name="Test Tribe 2")
        self.character.set_tribe(t)
        self.assertEqual(self.character.willpower, 3)
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        self.assertEqual(self.character.willpower, 5)

    def test_set_glory(self):
        self.assertEqual(self.character.glory, 0)
        self.assertTrue(self.character.set_glory(3))
        self.assertEqual(self.character.glory, 3)

    def test_set_honor(self):
        self.assertEqual(self.character.honor, 0)
        self.assertTrue(self.character.set_honor(3))
        self.assertEqual(self.character.honor, 3)

    def test_set_wisdom(self):
        self.assertEqual(self.character.wisdom, 0)
        self.assertTrue(self.character.set_wisdom(3))
        self.assertEqual(self.character.wisdom, 3)

    def test_has_renown(self):
        self.assertFalse(self.character.has_renown())
        self.character.set_auspice("ragabash")
        self.assertEqual(
            self.character.glory + self.character.honor + self.character.wisdom, 3
        )
        self.assertTrue(self.character.has_renown())

    def test_set_auspice(self):
        self.assertFalse(self.character.has_auspice())
        self.assertTrue(self.character.set_auspice("ragabash"))
        self.assertTrue(self.character.has_auspice())

    def test_has_auspice(self):
        self.assertFalse(self.character.has_breed())
        self.character.set_breed("homid")
        self.assertTrue(self.character.has_breed())

    def test_auspice_sets_rage(self):
        self.assertEqual(self.character.rage, 0)
        self.character.set_auspice("ragabash")
        self.assertEqual(self.character.rage, 1)
        self.character.set_auspice("theurge")
        self.assertEqual(self.character.rage, 2)
        self.character.set_auspice("philodox")
        self.assertEqual(self.character.rage, 3)
        self.character.set_auspice("galliard")
        self.assertEqual(self.character.rage, 4)
        self.character.set_auspice("ahroun")
        self.assertEqual(self.character.rage, 5)

    def test_auspice_sets_renown(self):
        self.assertEqual(
            self.character.glory + self.character.honor + self.character.wisdom, 0
        )
        self.character.set_auspice("ragabash")
        self.assertEqual(
            self.character.glory + self.character.honor + self.character.wisdom, 3
        )
        self.character.set_auspice("theurge")
        self.assertEqual(self.character.glory, 0)
        self.assertEqual(self.character.honor, 0)
        self.assertEqual(self.character.wisdom, 3)
        self.character.set_auspice("philodox")
        self.assertEqual(self.character.glory, 0)
        self.assertEqual(self.character.honor, 3)
        self.assertEqual(self.character.wisdom, 0)
        self.character.set_auspice("galliard")
        self.assertEqual(self.character.glory, 2)
        self.assertEqual(self.character.honor, 0)
        self.assertEqual(self.character.wisdom, 1)
        self.character.set_auspice("ahroun")
        self.assertEqual(self.character.glory, 2)
        self.assertEqual(self.character.honor, 1)
        self.assertEqual(self.character.wisdom, 0)

    def test_set_rank(self):
        self.assertEqual(self.character.rank, 1)
        self.character.set_rank(3)
        self.assertEqual(self.character.rank, 3)

    def test_increase_rank(self):
        self.assertEqual(self.character.rank, 1)
        self.character.set_auspice("ragabash")
        self.assertFalse(self.character.increase_rank())
        self.character.set_glory(3)
        self.character.set_honor(3)
        self.character.set_wisdom(1)
        self.assertTrue(self.character.increase_rank())

    def test_freebie_cost(self):
        self.assertEqual(self.character.freebie_cost("attribute"), 5)
        self.assertEqual(self.character.freebie_cost("ability"), 2)
        self.assertEqual(self.character.freebie_cost("background"), 1)
        self.assertEqual(self.character.freebie_cost("willpower"), 1)
        self.assertEqual(self.character.freebie_cost("meritflaw"), 1)
        self.assertEqual(self.character.freebie_cost("gift"), 7)
        self.assertEqual(self.character.freebie_cost("rage"), 1)
        self.assertEqual(self.character.freebie_cost("gnosis"), 2)

    def test_spend_freebies(self):
        self.character.set_tribe(Tribe.objects.get(name="Test Tribe"))
        self.assertEqual(self.character.freebies, 15)
        self.assertTrue(self.character.spend_freebies("strength"))
        self.assertEqual(self.character.freebies, 10)
        self.assertTrue(self.character.spend_freebies("occult"))
        self.assertEqual(self.character.freebies, 8)
        self.assertTrue(self.character.spend_freebies("mentor"))
        self.assertEqual(self.character.freebies, 7)
        self.assertTrue(self.character.spend_freebies("willpower"))
        self.assertEqual(self.character.freebies, 6)
        self.assertTrue(self.character.spend_freebies("Merit 1"))
        self.assertEqual(self.character.freebies, 5)
        self.character.freebies = 15
        self.assertEqual(self.character.freebies, 15)
        self.assertTrue(self.character.spend_freebies("Test Tribe Gift"))
        self.assertEqual(self.character.freebies, 8)
        self.assertTrue(self.character.spend_freebies("rage"))
        self.assertEqual(self.character.freebies, 7)
        self.assertTrue(self.character.spend_freebies("gnosis"))
        self.assertEqual(self.character.freebies, 5)

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("ability"), 2)
        self.assertEqual(self.character.xp_cost("background"), 3)
        self.assertEqual(self.character.xp_cost("new background"), 5)
        self.assertEqual(self.character.xp_cost("willpower"), 1)
        self.assertEqual(self.character.xp_cost("new ability"), 3)

        self.assertEqual(self.character.xp_cost("gift"), 3)
        self.assertEqual(self.character.xp_cost("outside gift"), 5)
        self.assertEqual(self.character.xp_cost("rage"), 1)
        self.assertEqual(self.character.xp_cost("gnosis"), 2)

    def test_spend_xp(self):
        self.character.xp = 100
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        self.character.set_auspice("ragabash")
        self.character.set_breed("homid")
        self.assertTrue(self.character.spend_xp("strength"))
        self.assertEqual(self.character.xp, 96)
        self.assertTrue(self.character.spend_xp("occult"))
        self.assertEqual(self.character.xp, 93)
        self.assertTrue(self.character.spend_xp("occult"))
        self.assertEqual(self.character.xp, 91)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 86)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 83)
        self.assertTrue(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 78)
        self.assertTrue(self.character.spend_xp("Test Tribe Gift"))
        self.assertEqual(self.character.xp, 75)
        self.assertTrue(self.character.spend_xp("rage"))
        self.assertEqual(self.character.xp, 74)
        self.assertTrue(self.character.spend_xp("gnosis"))
        self.assertEqual(self.character.xp, 72)
        self.assertTrue(self.character.spend_xp("Gift 1"))
        self.assertEqual(self.character.xp, 67)

    def test_has_werewolf_history(self):
        self.assertFalse(self.character.has_werewolf_history())
        self.character.first_change = "Young"
        self.assertFalse(self.character.has_werewolf_history())
        self.character.age_of_first_change = 13
        self.assertTrue(self.character.has_werewolf_history())

    def test_no_homid_red_talons(self):
        self.character.breed = "homid"
        self.assertFalse(
            self.character.set_tribe(Tribe.objects.create(name="Red Talons"))
        )

    def test_no_male_black_furies(self):
        self.character.sex = "Male"
        self.assertFalse(
            self.character.set_tribe(Tribe.objects.create(name="Black Furies"))
        )

    def test_silver_fangs_have_pure_breed_three(self):
        self.character.set_tribe(Tribe.objects.create(name="Silver Fangs"))
        self.assertEqual(self.character.pure_breed, 3)

    def test_num_renown_incidents(self):
        self.character.add_renown_incident(RenownIncident.objects.create(name="Test 1"))
        self.assertEqual(self.character.num_renown_incidents(), 1)
        self.character.add_renown_incident(RenownIncident.objects.create(name="Test 2"))
        self.assertEqual(self.character.num_renown_incidents(), 2)

    def test_add_renown_incident(self):
        r = RenownIncident.objects.create(
            name="Test Renown Incident", glory=1, honor=1, wisdom=1
        )
        self.assertTrue(self.character.add_renown_incident(r))
        self.assertEqual(self.character.num_renown_incidents(), 1)
        self.assertIn("Test Renown Incident", self.character.renown_incidents)
        self.assertEqual(self.character.temporary_glory, 1)
        self.assertEqual(self.character.temporary_honor, 1)
        self.assertEqual(self.character.temporary_wisdom, 1)

    def test_update_renown(self):
        self.character.glory = 2
        self.character.temporary_glory = 10
        self.character.update_renown()
        self.assertEqual(self.character.glory, 3)
        self.assertEqual(self.character.temporary_glory, 0)

    def test_achieved_age_only_once(self):
        r = RenownIncident.objects.create(
            name="One Off", glory=1, wisdom=2, only_once=True
        )
        self.assertTrue(self.character.add_renown_incident(r))
        self.assertFalse(self.character.add_renown_incident(r))

    def test_breed_renown_correct(self):
        r = RenownIncident.objects.create(name="Lupus Award", breed="lupus")
        self.character.set_breed("homid")
        self.assertFalse(self.character.add_renown_incident(r))

    def test_renown_check_if_has_rite(self):
        rite = Rite.objects.create(name="Test Rite for Renown")
        renown = RenownIncident.objects.create(
            name="Used Test Rite for Renown", rite=rite
        )
        self.assertFalse(self.character.add_renown_incident(renown))
        self.character.add_rite(rite)
        self.assertTrue(self.character.add_renown_incident(renown))

    def test_wont_add_if_last_is_posthumous(self):
        r1 = RenownIncident.objects.create(
            name="Award (posthumous)", glory=3, honor=3, wisdom=0, posthumous=True
        )
        r2 = RenownIncident.objects.create(name="Award", glory=3, honor=3, wisdom=0)
        self.assertTrue(self.character.add_renown_incident(r1))
        self.assertFalse(self.character.add_renown_incident(r2))

    def test_learn_a_new_rite(self):
        r = RenownIncident.objects.create(name="Learning a new rite")
        num = self.character.rites_known.count()
        self.character.add_renown_incident(r)
        self.assertEqual(self.character.rites_known.count(), num + 1)

    def test_add_battle_scar(self):
        scar = BattleScar.objects.create(name="Test Scar")
        self.assertTrue(self.character.add_battle_scar(scar))
        self.assertFalse(self.character.add_battle_scar(scar))

    def test_random_freebie_functions(self):
        functions = self.character.random_freebie_functions()
        self.assertIn("attribute", functions)
        self.assertIn("ability", functions)
        self.assertIn("background", functions)
        self.assertIn("willpower", functions)
        self.assertIn("meritflaw", functions)
        self.assertIn("gift", functions)
        self.assertIn("rage", functions)
        self.assertIn("gnosis", functions)

    def test_random_xp_functions(self):
        functions = self.character.random_xp_functions()
        self.assertIn("attribute", functions)
        self.assertIn("ability", functions)
        self.assertIn("background", functions)
        self.assertIn("willpower", functions)
        self.assertIn("gift", functions)
        self.assertIn("rage", functions)
        self.assertIn("gnosis", functions)

    def test_add_fetish(self):
        fetish = Fetish.objects.create(name="Test")
        self.assertTrue(self.character.add_fetish(fetish))
        self.assertFalse(self.character.add_fetish(fetish))

    def test_filter_fetishes(self):
        filtered = self.character.filter_fetishes(min_rating=1, max_rating=3)
        self.assertEqual(filtered.count(), 15)

    def test_total_fetish_rating(self):
        fetish = Fetish.objects.create(name="Test", rank=2)
        self.character.add_fetish(fetish)
        self.assertEqual(self.character.total_fetish_rating(), 2)


class TestTotem(TestCase):
    pass


class TestRandomTotem(TestCase):
    # Cost 1 - 3 points for WP, Rage, and Gnosis
    # Cost 1 - Totem can speak to pack without Spirit Speech
    # Cost 1 - Totam can always find pack members
    # Cost 2 - Totem is nearly always with pack members
    # Cost 2 - Totem is respected by other spirits
    # Cost 2 - Per charm
    # Cost 3 - Per extra pack member who can use the totem's powers in same turn
    # Cost 4 - Totem connected mystically to all pack maembers allowing communication
    # Cost 5 - Totem is feared by the Wyrm
    pass


class TestRandomWerewolf(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = Werewolf.objects.create(name="", owner=self.player)
        werewolf_setup(self.player)

    def test_random_tribe(self):
        self.assertFalse(self.character.has_tribe())
        self.character.random_tribe()
        self.assertTrue(self.character.has_tribe())

    def test_random_auspice(self):
        self.assertFalse(self.character.has_auspice())
        self.character.random_auspice()
        self.assertTrue(self.character.has_auspice())

    def test_choose_random_gift(self):
        self.fail()

    def test_random_gift(self):
        self.fail()

    def test_random_gifts(self):
        self.character.random_tribe()
        self.character.random_auspice()
        self.character.random_breed()
        self.assertFalse(self.character.has_gifts())
        self.character.random_gifts()
        self.assertTrue(self.character.has_gifts())

    def test_random_breed(self):
        self.fail()

    def test_random_camp(self):
        self.fail()

    def test_random_rite(self):
        self.fail()

    def test_random_rites(self):
        self.character.rites = 3
        self.assertFalse(self.character.has_rites())
        self.character.random_rites()
        self.assertTrue(self.character.has_rites())

    def test_random_spend_xp(self):
        self.character.random_tribe()
        self.character.random_auspice()
        self.character.science = 1
        self.character.xp = 15
        self.character.random_xp()
        self.assertLess(self.character.xp, 15)

    def test_random_freebies(self):
        self.character.random_tribe()
        self.assertEqual(self.character.freebies, 15)
        self.character.random_freebies()
        self.assertEqual(self.character.freebies, 0)

    def test_random_freebies_gift(self):
        self.fail()

    def test_random_freebies_Rage(self):
        self.fail()

    def test_random_freebies_gnosis(self):
        self.fail()

    def test_random_renown_incident(self):
        self.character.auspice = "ahroun"
        num = self.character.num_renown_incidents()
        self.character.random_renown_incident()
        self.assertEqual(self.character.num_renown_incidents(), num + 1)

    def test_random_battle_scar(self):
        self.fail()

    def test_random_werewolf_history(self):
        self.fail()

    def test_random_xp_gift(self):
        self.fail()

    def test_random_xp_rage(self):
        self.fail()

    def test_random_xp_gnosis(self):
        self.fail()

    def test_random_xp(self):
        self.fail()

    def test_random_fetish(self):
        self.fail()

    def test_random_fetishes(self):
        self.fail()

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        self.assertFalse(self.character.has_archetypes())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_backgrounds())
        self.assertFalse(self.character.has_finishing_touches())
        self.assertFalse(self.character.has_history())
        self.assertFalse(self.character.has_gifts())
        self.assertFalse(self.character.has_tribe())
        self.assertFalse(self.character.has_auspice())
        self.assertFalse(self.character.has_camp())
        self.assertFalse(self.character.has_renown())
        self.assertFalse(self.character.has_werewolf_history())
        self.character.random(freebies=0, xp=0)
        self.assertTrue(self.character.has_name())
        self.assertTrue(self.character.has_concept())
        self.assertTrue(self.character.has_archetypes())
        self.assertTrue(self.character.has_attributes())
        self.assertTrue(self.character.has_abilities())
        self.assertTrue(self.character.has_specialties())
        self.assertTrue(self.character.has_backgrounds())
        self.assertTrue(self.character.has_finishing_touches())
        self.assertTrue(self.character.has_history())
        self.assertTrue(self.character.has_gifts())
        self.assertTrue(self.character.has_rites())
        self.assertTrue(self.character.has_tribe())
        self.assertTrue(self.character.has_auspice())
        self.assertTrue(self.character.has_renown())
        self.assertTrue(self.character.has_werewolf_history())


class TestPack(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        werewolf_setup(self.player)

    def test_pack_creation(self):
        pack = Pack.objects.create(name="Pack 1")
        pack.members.set(Werewolf.objects.all())
        pack.leader = Werewolf.objects.first()
        pack.save()
        self.assertEqual(pack.members.count(), 5)
        self.assertIsNotNone(pack.leader)

    def test_random_pack(self):
        pack = Pack.objects.create(name="Pack 1")
        pack.random(num_chars=5, new_characters=False)
        self.assertEqual(pack.members.count(), 5)
        for werewolf in Werewolf.objects.all():
            self.assertIn(werewolf, pack.members.all())
        pack = Pack.objects.create(name="Pack 2")
        pack.random(num_chars=5, new_characters=True)
        self.assertEqual(pack.members.count(), 5)

    def test_exception(self):
        pack = Pack.objects.create(name="Pack 10")
        with self.assertRaises(ValueError):
            pack.random(num_chars=10, new_characters=False)

    def test_totem_total(self):
        p = Pack.objects.create(name="Pack")
        self.assertEqual(p.total_totem(), 0)
        for i in range(4):
            w = Werewolf.objects.create(name=f"Werewolf {i}", owner=self.player)
            w.totem = i + 1
            w.save()
            p.members.add(w)
            p.save()
        self.assertEqual(p.total_totem(), 10)

    def test_set_totem(self):
        pack = Pack.objects.create(name="Pack 1")
        t = Totem.objects.first()
        self.assertFalse(pack.has_totem())
        self.assertTrue(pack.set_totem(t))
        self.assertTrue(pack.has_totem())

    def test_has_totem(self):
        pack = Pack.objects.create(name="Pack 1")
        t = Totem.objects.first()
        self.assertFalse(pack.has_totem())
        pack.set_totem(t)
        self.assertTrue(pack.has_totem())

    def test_random_totem(self):
        p = Pack.objects.create(name="Pack")
        for i in range(4):
            w = Werewolf.objects.create(name=f"Werewolf {i}", owner=self.player)
            w.totem = i + 1
            w.save()
            p.members.add(w)
            p.save()
        self.assertFalse(p.has_totem())
        self.assertTrue(p.random_totem())
        self.assertTrue(p.has_totem())

    def test_str(self):
        pack = Pack.objects.create(name="Pack 1")
        self.assertEqual(str(pack), "Pack 1")


class TestWerewolfDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.werewolf = Werewolf.objects.create(name="Test Werewolf", owner=self.player)

    def test_werewolf_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.werewolf.id}/")
        self.assertEqual(response.status_code, 200)

    def test_werewolf_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.werewolf.id}/")
        self.assertTemplateUsed(
            response, "wod/characters/werewolf/werewolf/detail.html"
        )


class TestPackDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.pack = Pack.objects.create(name="Test Pack")

    def test_pack_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/groups/{self.pack.id}/")
        self.assertEqual(response.status_code, 200)

    def test_pack_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/groups/{self.pack.id}/")
        self.assertTemplateUsed(response, "wod/characters/werewolf/pack/detail.html")
