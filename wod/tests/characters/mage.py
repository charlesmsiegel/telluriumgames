from unittest import mock
from unittest.mock import Mock

from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.human import MeritFlaw
from wod.models.characters.mage import (
    Cabal,
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
)


# Create your tests here.
def mage_setup(player):
    for i in range(5):
        Mage.objects.create(name=f"Character {i}", player=player.wod_profile)

    for i in range(15):
        Instrument.objects.create(name=f"Instrument {i}")

    for i in range(5):
        practice = Practice.objects.create(name=f"Practice {i}")
        practice.instruments.set(Instrument.objects.all())
        practice.save()

    for i in range(3):
        paradigm = Paradigm.objects.create(name=f"Paradigm {i}")
        paradigm.practices.set(Practice.objects.all())
        paradigm.save()

    trad = MageFaction.objects.create(name="Traditions")
    MageFaction.objects.create(name="Akashayana", parent=trad)

    for faction in MageFaction.objects.exclude(parent=None):
        faction.paradigms.set(Paradigm.objects.all())
        faction.practices.set(Practice.objects.all())
        faction.save()
        MageFaction.objects.create(name=f"sub-{faction.name}", parent=faction)

    for i in range(5):
        MeritFlaw.objects.create(name=f"Merit {i}", ratings=[i])
        MeritFlaw.objects.create(name=f"Flaw {i}", ratings=[-i])


class TestMage(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.character = Mage.objects.create(name="", player=self.player.wod_profile)
        mage_setup(self.player)

    def set_abilities(self):
        self.character.alertness = 1
        self.character.art = 2
        self.character.empathy = 3
        self.character.streetwise = 2
        self.character.firearms = 3
        self.character.melee = 4
        self.character.stealth = 2
        self.character.technology = 1
        self.character.cosmology = 3
        self.character.law = 2
        self.character.area_knowledge = 1
        self.character.belief_systems = 1
        self.character.cryptography = 1

    def test_get_abilities(self):
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 0,
                "awareness": 0,
                "art": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "martial_arts": 0,
                "meditation": 0,
                "melee": 0,
                "research": 0,
                "stealth": 0,
                "survival": 0,
                "technology": 0,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
                "academics": 0,
                "computer": 0,
                "cosmology": 0,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 0,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 0,
                "belief_systems": 0,
                "cryptography": 0,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 1,
                "awareness": 0,
                "art": 2,
                "athletics": 0,
                "brawl": 0,
                "empathy": 3,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 2,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 3,
                "martial_arts": 0,
                "meditation": 0,
                "melee": 4,
                "research": 0,
                "stealth": 2,
                "survival": 0,
                "technology": 1,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
                "academics": 0,
                "computer": 0,
                "cosmology": 3,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 2,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 1,
                "belief_systems": 1,
                "cryptography": 1,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
            },
        )

    def test_get_talents(self):
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 0,
                "awareness": 0,
                "art": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 1,
                "awareness": 0,
                "art": 2,
                "athletics": 0,
                "brawl": 0,
                "empathy": 3,
                "intimidation": 0,
                "leadership": 0,
                "expression": 0,
                "streetwise": 2,
                "subterfuge": 0,
                "animal_kinship": 0,
                "blatancy": 0,
                "carousing": 0,
                "do": 0,
                "flying": 0,
                "high_ritual": 0,
                "lucid_dreaming": 0,
                "search": 0,
                "seduction": 0,
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
                "martial_arts": 0,
                "meditation": 0,
                "melee": 0,
                "research": 0,
                "stealth": 0,
                "survival": 0,
                "technology": 0,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 3,
                "martial_arts": 0,
                "meditation": 0,
                "melee": 4,
                "research": 0,
                "stealth": 2,
                "survival": 0,
                "technology": 1,
                "acrobatics": 0,
                "archery": 0,
                "biotech": 0,
                "energy_weapons": 0,
                "hypertech": 0,
                "jetpack": 0,
                "riding": 0,
                "torture": 0,
            },
        )

    def test_get_knowledges(self):
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "cosmology": 0,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 0,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 0,
                "belief_systems": 0,
                "cryptography": 0,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "cosmology": 3,
                "enigmas": 0,
                "esoterica": 0,
                "investigation": 0,
                "law": 2,
                "medicine": 0,
                "occult": 0,
                "politics": 0,
                "science": 0,
                "area_knowledge": 1,
                "belief_systems": 1,
                "cryptography": 1,
                "demolitions": 0,
                "finance": 0,
                "lore": 0,
                "media": 0,
                "pharmacopeia": 0,
            },
        )

    def set_spheres(self):
        self.character.correspondence = 1
        self.character.time = 2
        self.character.spirit = 3
        self.character.matter = 4
        self.character.forces = 5
        self.character.life = 4
        self.character.entropy = 3
        self.character.mind = 2
        self.character.prime = 1

    def test_get_spheres(self):
        self.assertEqual(
            self.character.get_spheres(),
            {
                "correspondence": 0,
                "time": 0,
                "spirit": 0,
                "matter": 0,
                "forces": 0,
                "life": 0,
                "entropy": 0,
                "mind": 0,
                "prime": 0,
            },
        )
        self.set_spheres()
        self.assertEqual(
            self.character.get_spheres(),
            {
                "correspondence": 1,
                "time": 2,
                "spirit": 3,
                "matter": 4,
                "forces": 5,
                "life": 4,
                "entropy": 3,
                "mind": 2,
                "prime": 1,
            },
        )

    def test_add_sphere(self):
        self.character.arete = 2
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertEqual(self.character.forces, 2)
        self.assertFalse(self.character.add_sphere("forces"))
        self.character.arete = 3
        self.assertTrue(self.character.add_sphere("forces"))

    def test_filter_spheres(self):
        self.character.arete = 3
        self.assertEqual(len(self.character.filter_spheres().keys()), 9)
        self.set_spheres()
        self.assertEqual(len(self.character.filter_spheres().keys()), 4)
        self.assertEqual(len(self.character.filter_spheres(minimum=2).keys()), 2)
        self.assertEqual(len(self.character.filter_spheres(maximum=1).keys()), 2)

    def test_has_spheres(self):
        self.assertFalse(self.character.has_spheres())
        self.character.arete = 3
        self.character.set_affinity_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("matter")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("matter")
        self.assertFalse(self.character.has_spheres())
        self.character.add_sphere("matter")
        self.assertTrue(self.character.has_spheres())

    def test_set_affinity_sphere(self):
        self.character.arete = 1
        self.assertFalse(self.character.has_affinity_sphere())
        self.assertTrue(self.character.set_affinity_sphere("forces"))
        self.assertTrue(self.character.has_affinity_sphere())
        self.assertEqual(self.character.forces, 1)

    def test_has_affinity_sphere(self):
        self.character.arete = 1
        self.assertFalse(self.character.has_affinity_sphere())
        self.character.affinity_sphere = "forces"
        self.character.forces = 1
        self.assertTrue(self.character.has_affinity_sphere())

    def test_sphere_names(self):
        spheres = [
            "correspondence",
            "forces",
            "time",
            "life",
            "spirit",
            "matter",
            "prime",
            "mind",
            "entropy",
        ]
        for sphere in spheres:
            self.assertTrue(hasattr(self.character, f"{sphere}"))
        self.assertEqual(self.character.get_corr_name_display(), "Correspondence")
        self.assertEqual(self.character.get_spirit_name_display(), "Spirit")
        self.assertEqual(self.character.get_prime_name_display(), "Prime")
        self.character.corr_name = "data"
        self.character.prime_name = "primal_utility"
        self.character.spirit_name = "dimensional_science"
        self.assertEqual(self.character.get_corr_name_display(), "Data")
        self.assertEqual(
            self.character.get_spirit_name_display(), "Dimensional Science"
        )
        self.assertEqual(self.character.get_prime_name_display(), "Primal Utility")

    def test_add_arete(self):
        self.assertEqual(self.character.arete, 0)
        self.assertTrue(self.character.add_arete())
        self.assertEqual(self.character.arete, 1)
        self.character.arete = 10
        self.assertFalse(self.character.add_arete())

    def test_total_spheres(self):
        self.character.forces = 2
        self.assertEqual(self.character.total_spheres(), 2)
        self.character.matter = 3
        self.assertEqual(self.character.total_spheres(), 5)
        self.character.matter = 2
        self.character.life = 1
        self.assertEqual(self.character.total_spheres(), 5)

    def test_mage_numbers(self):
        self.assertEqual(self.character.willpower, 5)
        self.assertEqual(self.character.background_points, 7)

    def test_set_faction(self):
        self.fail()

    def test_has_faction(self):
        self.fail()

    def test_set_focus(self):
        self.fail()

    def test_has_focus(self):
        self.fail()

    def test_set_essence(self):
        self.fail()

    def test_has_essence(self):
        self.fail()

    def test_freebie_cost(self):
        self.fail()

    def test_spend_freebies(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()

    def test_add_resonance_dot(self):
        self.fail()

    def test_total_resonance(self):
        self.fail()

    def test_learn_rote(self):
        self.fail()

    def test_has_mage_history(self):
        self.assertFalse(self.character.has_mage_history())
        self.character.awakening = "Young"
        self.character.seekings = "Several"
        self.character.quiets = "None"
        self.character.age_of_awakening = 13
        self.character.avatar_description = "The Random Graph"
        self.assertTrue(self.character.has_mage_history())


class TestRandomMage(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.character = Mage.objects.create(name="", player=self.player.wod_profile)
        mage_setup(self.player)

    def test_random_affinity_sphere(self):
        self.assertFalse(self.character.has_affinity_sphere())
        self.character.random_affinity_sphere()
        self.assertTrue(self.character.has_affinity_sphere())

    def test_random_faction(self):
        self.assertFalse(self.character.has_faction())
        self.character.random_faction()
        self.assertTrue(self.character.has_faction())
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mocker = Mock()
        mocker.side_effect = [0.01]
        with mock.patch("random.random", mocker):
            mage.random_faction()
        self.assertIsNotNone(mage.subfaction)

    def test_random_focus(self):
        self.assertFalse(self.character.has_focus())
        self.character.random_focus()
        self.assertTrue(self.character.has_focus())

    def test_random_sphere(self):
        self.character.arete = 3
        self.character.affinity_sphere = "forces"
        num = self.character.total_spheres()
        self.character.random_sphere()
        self.assertEqual(self.character.total_spheres(), num + 1)

    def test_random_spheres(self):
        self.character.arete = 3
        self.assertFalse(self.character.has_spheres())
        self.character.random_spheres()
        self.assertTrue(self.character.has_spheres())

    def test_random_arete(self):
        self.assertEqual(self.character.arete, 0)
        self.character.random_arete()
        self.assertNotEqual(self.character.arete, 0)

    def test_random_xp_spend(self):
        self.character.science = 1
        self.character.xp = 15
        self.character.random_xp_spend()
        self.assertLess(self.character.xp, 15)

    def test_random_freebies(self):
        self.assertEqual(self.character.freebies, 15)
        self.character.random_freebies
        self.assertEqual(self.character.freebies, 0)

    def test_random_essence(self):
        self.assertFalse(self.character.has_essence())
        self.character.random_essence()
        self.assertTrue(self.character.has_essence())

    def test_random_resonance_dot(self):
        self.assertEqual(self.character.total_resonance(), 0)
        self.character.random_resonance()
        self.assertEqual(self.character.total_resonance(), 1)

    def test_random_rote(self):
        self.fail()

    def test_random_rotes(self):
        self.fail()

    def test_random(self):
        self.fail()


class TestCabal(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        mage_setup(self.player)

    def test_cabal_creation(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.members.set(Mage.objects.all())
        cabal.leader = Mage.objects.first()
        cabal.save()
        self.assertEqual(cabal.members.count(), 5)
        self.assertIsNotNone(cabal.leader)

    def test_random_cabal(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.random(5, new_characters=False)
        self.assertEqual(cabal.members.count(), 5)
        for mage in Mage.objects.all():
            self.assertIn(mage, cabal.members.all())
        cabal = Cabal.objects.create(name="Cabal 2")
        cabal.random(5, new_characters=True)
        self.assertEqual(cabal.members.count(), 5)

    def test_exception(self):
        cabal = Cabal.objects.create(name="Cabal 10")
        with self.assertRaises(ValueError):
            cabal.random(10, new_characters=False)

    def test_str(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        self.assertEqual(str(cabal), "Cabal 1")


class TestMageFaction(TestCase):
    def test_affinities(self):
        faction = MageFaction.objects.create(name="Faction 1", parent=None)
        faction.affinities = ["forces", "correspondence"]
        self.assertEqual(len(faction.affinities), 2)
        faction.affinities = faction.affinities + ["life"]
        self.assertEqual(len(faction.affinities), 3)
        faction.affinities.append("prime")
        self.assertEqual(len(faction.affinities), 4)
        faction.affinities.pop()
        self.assertEqual(len(faction.affinities), 3)

    def test_str(self):
        faction = MageFaction.objects.create(name="Faction 1", parent=None)
        self.assertEqual(str(faction), "Faction 1")


class TestPractice(TestCase):
    def test_abilities(self):
        practice = Practice.objects.create(name="Practice 1")
        practice.abilities = ["martial_arts", "awareness"]
        self.assertEqual(len(practice.abilities), 2)

    def test_str(self):
        practice = Practice.objects.create(name="Practice 1")
        self.assertEqual(str(practice), "Practice 1")


class TestInstrument(TestCase):
    def test_str(self):
        instrument = Instrument.objects.create(name="Instrument 1")
        self.assertEqual(str(instrument), "Instrument 1")


class TestParadigm(TestCase):
    def test_str(self):
        paradigm = Paradigm.objects.create(name="Paradigm 1")
        self.assertEqual(str(paradigm), "Paradigm 1")


class TestMageDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.mage = Mage.objects.create(
            name="Test Mage", player=self.player.wod_profile
        )

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/detail.html")
