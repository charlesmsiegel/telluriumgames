import random
from unittest import mock
from unittest.mock import Mock

from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Language, Noun
from wod.models.characters.human import Archetype, MeritFlaw, WoDSpecialty
from wod.models.characters.mage import (
    Cabal,
    Effect,
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
)
from wod.models.characters.mage.mage import Rote
from wod.models.characters.mage.mtahuman import MtAHuman
from wod.models.characters.mage.resonance import ResRating
from wod.models.characters.mage.utils import ABILITY_LIST
from wod.models.locations.mage import NodeMeritFlaw
from wod.models.locations.mage.library import Library
from wod.models.locations.mage.nodes import Node


# Create your tests here.
def mage_setup(player):
    for i in range(10):
        Noun.objects.create(name=f"Mage Noun {i}")

    for i in range(5):
        m = Mage.objects.create(name=f"Character {i}", owner=player)

    for i in range(15):
        Instrument.objects.create(name=f"Instrument {i}")

    for i in range(5):
        practice = Practice.objects.create(
            name=f"Practice {i}", abilities=list(random.sample(ABILITY_LIST, k=4))
        )
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
        MeritFlaw.objects.create(name=f"Merit {i}", ratings=[i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Flaw {i}", ratings=[-i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Merit2 {i}", ratings=[i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Flaw2 {i}", ratings=[-i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Merit3 {i}", ratings=[i], human=True, mage=True)
        MeritFlaw.objects.create(name=f"Flaw3 {i}", ratings=[-i], human=True, mage=True)
        NodeMeritFlaw.objects.create(name=f"Node Merit {i}", ratings=[i])
        NodeMeritFlaw.objects.create(name=f"Node Flaw {i}", ratings=[-i])

    for i in range(1, 11):
        Resonance.objects.create(name=f"Resonance {i}")

    for i in range(1, 6):
        Effect.objects.create(name=f"Correspondence {i}", correspondence=i)
        Effect.objects.create(name=f"Time {i}", time=i)
        Effect.objects.create(name=f"Spirit {i}", spirit=i)
        Effect.objects.create(name=f"Forces {i}", forces=i)
        Effect.objects.create(name=f"Matter {i}", matter=i)
        Effect.objects.create(name=f"Life {i}", life=i)
        Effect.objects.create(name=f"Entropy {i}", entropy=i)
        Effect.objects.create(name=f"Prime {i}", prime=i)
        Effect.objects.create(name=f"Mind {i}", mind=i)

    for i in range(10):
        for trait in m.get_attributes():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )

        for trait in m.get_abilities():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )

        for trait in m.get_spheres():
            WoDSpecialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )
            for i in range(5):
                Resonance.objects.get_or_create(
                    name=f"{trait.title()} Resonance {i}", **{trait: True}
                )

    for i in range(20):
        Archetype.objects.create(name=f"Archetype {i}")

    for i in range(1, 11):
        Language.objects.create(name=f"Language {i}", frequency=i)


class TestMtAHuman(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.character = MtAHuman.objects.create(name="", owner=self.player)
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
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
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
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
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
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
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
                "cooking": 0,
                "diplomacy": 0,
                "instruction": 0,
                "intrigue": 0,
                "intuition": 0,
                "mimicry": 0,
                "negotiation": 0,
                "newspeak": 0,
                "scan": 0,
                "scrounging": 0,
                "style": 0,
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
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
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
                "blind_fighting": 0,
                "climbing": 0,
                "disguise": 0,
                "elusion": 0,
                "escapology": 0,
                "fast_draw": 0,
                "fast_talk": 0,
                "fencing": 0,
                "fortune_telling": 0,
                "gambling": 0,
                "gunsmith": 0,
                "heavy_weapons": 0,
                "hunting": 0,
                "hypnotism": 0,
                "jury_rigging": 0,
                "microgravity_operations": 0,
                "misdirection": 0,
                "networking": 0,
                "pilot": 0,
                "psychology": 0,
                "security": 0,
                "speed_reading": 0,
                "swimming": 0,
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
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
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
                "conspiracy_theory": 0,
                "chantry_politics": 0,
                "covert_culture": 0,
                "cultural_savvy": 0,
                "helmsman": 0,
                "history_knowledge": 0,
                "power_brokering": 0,
                "propaganda": 0,
                "theology": 0,
                "unconventional_warface": 0,
                "vice": 0,
            },
        )

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "contacts": 0,
                "mentor": 0,
                "allies": 0,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 0,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 0,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 0,
                "enhancement": 0,
                "fame": 0,
                "familiar": 0,
                "influence": 0,
                "legend": 0,
                "library": 0,
                "node": 0,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )
        self.character.mentor = 3
        self.character.chantry = 2
        self.character.fame = 1
        self.character.dream = 3
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "contacts": 0,
                "mentor": 3,
                "allies": 0,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 0,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 2,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 3,
                "enhancement": 0,
                "fame": 1,
                "familiar": 0,
                "influence": 0,
                "legend": 0,
                "library": 0,
                "node": 0,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )


class TestMage(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.character = Mage.objects.create(name="", owner=self.player)
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

    def test_do_is_akashic_only(self):
        self.character.awareness = 2
        self.assertFalse(self.character.add_ability("do"))
        self.character.faction = MageFaction.objects.get(name="Akashayana")
        self.assertTrue(self.character.add_ability("do"))

    def test_do_requires_limbs(self):
        self.character.faction = MageFaction.objects.get(name="Akashayana")
        self.assertFalse(self.character.add_ability("do"))
        self.character.awareness = 2
        self.assertTrue(self.character.add_ability("do"))
        self.character.cosmology = 3
        self.assertTrue(self.character.add_ability("do"))
        self.assertTrue(self.character.add_ability("do"))
        self.assertFalse(self.character.add_ability("do"))

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
        self.character.arete = 7
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertFalse(self.character.add_sphere("forces"))

    def test_batini_no_entropy(self):
        self.character.faction = MageFaction.objects.create(name="Ahl-i-Batin")
        self.character.add_arete()
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertFalse(self.character.add_sphere("entropy"))

    def test_filter_spheres(self):
        self.character.arete = 3
        self.assertEqual(len(self.character.filter_spheres().keys()), 9)
        self.set_spheres()
        self.assertEqual(len(self.character.filter_spheres(maximum=2).keys()), 4)
        self.assertEqual(
            len(self.character.filter_spheres(minimum=2, maximum=2).keys()), 2
        )
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
        self.character.set_corr_name("data")
        self.character.set_prime_name("primal_utility")
        self.character.set_spirit_name("dimensional_science")
        self.assertEqual(self.character.get_corr_name_display(), "Data")
        self.assertEqual(
            self.character.get_spirit_name_display(), "Dimensional Science"
        )
        self.assertEqual(self.character.get_prime_name_display(), "Primal Utility")
        with self.assertRaises(ValueError):
            self.character.set_corr_name("blah")

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
        # self.assertEqual(self.character.willpower, 5)
        self.assertEqual(self.character.background_points, 7)

    def test_add_background(self):
        num = self.character.total_backgrounds()
        self.assertFalse(self.character.add_background("test"))
        self.assertEqual(num, self.character.total_backgrounds())
        self.assertTrue(self.character.add_background("avatar"))
        self.assertEqual(num + 1, self.character.total_backgrounds())

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 0,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 0,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 0,
                "contacts": 0,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 0,
                "enhancement": 0,
                "fame": 0,
                "familiar": 0,
                "influence": 0,
                "legend": 0,
                "library": 0,
                "mentor": 0,
                "node": 0,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )
        self.character.allies = 1
        self.character.avatar = 3
        self.character.chantry = 3
        self.character.legend = 2
        self.character.node = 2
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 1,
                "alternate_identity": 0,
                "arcane": 0,
                "avatar": 3,
                "backup": 0,
                "blessing": 0,
                "certification": 0,
                "chantry": 3,
                "contacts": 0,
                "cult": 0,
                "demesne": 0,
                "destiny": 0,
                "dream": 0,
                "enhancement": 0,
                "fame": 0,
                "familiar": 0,
                "influence": 0,
                "legend": 2,
                "library": 0,
                "mentor": 0,
                "node": 2,
                "past_lives": 0,
                "patron": 0,
                "rank": 0,
                "requisitions": 0,
                "resources": 0,
                "retainers": 0,
                "sanctum": 0,
                "secret_weapons": 0,
                "spies": 0,
                "status_background": 0,
                "totem": 0,
                "wonder": 0,
            },
        )

    def test_total_backgrounds(self):
        self.character.allies = 3
        self.character.avatar = 4
        self.character.resources = 1
        self.character.sanctum = 2
        self.assertEqual(self.character.total_backgrounds(), 12)
        self.character.wonder = 2
        self.assertEqual(self.character.total_backgrounds(), 14)

    def test_technocracy_only_backgrounds(self):
        tech_char = Mage.objects.create(name="Tech", owner=self.player)
        tech_char.affiliation = MageFaction.objects.create(name="Technocratic Union")
        trad_char = Mage.objects.create(name="Trad", owner=self.player)
        trad_char.affiliation = MageFaction.objects.get(name="Traditions")
        self.assertTrue(tech_char.add_background("secret_weapons"))
        self.assertFalse(trad_char.add_background("secret_weapons"))
        self.assertEqual(tech_char.total_backgrounds(), 1)
        self.assertEqual(trad_char.total_backgrounds(), 0)
        self.assertTrue(tech_char.add_background("requisitions"))
        self.assertFalse(trad_char.add_background("requisitions"))
        self.assertEqual(tech_char.total_backgrounds(), 2)
        self.assertEqual(trad_char.total_backgrounds(), 0)

    def test_set_faction(self):
        self.assertFalse(self.character.has_focus())
        affiliation = MageFaction.objects.create(name="Affiliation")
        faction = MageFaction.objects.create(name="Faction", parent=affiliation)
        subfaction = MageFaction.objects.create(name="Subfaction", parent=faction)

        affiliation2 = MageFaction.objects.create(name="Affiliation2")
        faction2 = MageFaction.objects.create(name="Faction2", parent=affiliation2)
        subfaction2 = MageFaction.objects.create(name="Subfaction2", parent=faction2)

        self.assertFalse(
            self.character.set_faction(affiliation, faction, subfaction=subfaction2)
        )
        self.assertTrue(
            self.character.set_faction(affiliation, faction, subfaction=subfaction)
        )
        self.assertTrue(self.character.has_faction())
        self.assertTrue(
            self.character.set_faction(
                subfaction2.parent.parent, subfaction2.parent, subfaction=subfaction2
            )
        )
        self.assertTrue(self.character.has_faction())

    def test_has_faction(self):
        self.assertFalse(self.character.has_focus())
        affiliation = MageFaction.objects.create(name="Affiliation")
        faction = MageFaction.objects.create(name="Faction", parent=affiliation)
        subfaction = MageFaction.objects.create(name="Subfaction", parent=faction)
        self.character.set_faction(
            affiliation=affiliation, faction=faction, subfaction=subfaction
        )
        self.assertTrue(self.character.has_faction())

    def test_set_focus(self):
        paradigms = Paradigm.objects.order_by("?")[:2]
        practices = Practice.objects.order_by("?")[:2]
        instruments = Instrument.objects.order_by("?")[:7]
        self.assertFalse(self.character.has_focus())
        self.assertFalse(
            self.character.set_focus(
                paradigms=paradigms, practices=practices, instruments=instruments[:3]
            )
        )
        self.assertTrue(
            self.character.set_focus(
                paradigms=paradigms, practices=practices, instruments=instruments
            )
        )
        self.assertTrue(self.character.has_focus())

    def test_has_focus(self):
        paradigms = Paradigm.objects.order_by("?")[:2]
        practices = Practice.objects.order_by("?")[:2]
        instruments = Instrument.objects.order_by("?")[:7]
        self.assertFalse(self.character.has_focus())
        self.character.set_focus(
            paradigms=paradigms, practices=practices, instruments=instruments
        )
        self.assertTrue(self.character.has_focus())

    def test_set_essence(self):
        self.assertFalse(self.character.has_essence())
        self.assertTrue(self.character.set_essence("questing"))
        self.assertTrue(self.character.has_essence())

    def test_has_essence(self):
        self.assertFalse(self.character.has_essence())
        self.character.set_essence("questing")
        self.assertTrue(self.character.has_essence())

    def test_freebie_cost(self):
        self.assertEqual(self.character.freebie_cost("attribute"), 5)
        self.assertEqual(self.character.freebie_cost("ability"), 2)
        self.assertEqual(self.character.freebie_cost("background"), 1)
        self.assertEqual(self.character.freebie_cost("willpower"), 1)
        self.assertEqual(self.character.freebie_cost("meritflaw"), 1)
        self.assertEqual(self.character.freebie_cost("sphere"), 7)
        self.assertEqual(self.character.freebie_cost("arete"), 4)
        self.assertEqual(self.character.freebie_cost("quintessence"), 1)
        self.assertEqual(self.character.freebie_cost("rote points"), 1)
        self.assertEqual(self.character.freebie_cost("resonance"), 3)

    def test_spend_freebies(self):
        self.character.arete = 1
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
        self.assertTrue(self.character.spend_freebies("arete"))
        self.assertEqual(self.character.freebies, 11)
        self.assertTrue(self.character.spend_freebies("forces"))
        self.assertEqual(self.character.freebies, 4)
        self.assertTrue(self.character.spend_freebies("quintessence"))
        self.assertEqual(self.character.freebies, 3)
        self.assertTrue(self.character.spend_freebies("rote points"))
        self.assertEqual(self.character.freebies, 2)
        ResRating.objects.create(
            mage=self.character,
            resonance=Resonance.objects.create(name="TestRes"),
            rating=1,
        )
        self.character.freebies = 30
        self.assertTrue(self.character.spend_freebies("resonance"))
        self.character.freebies = 27
        self.assertTrue(self.character.spend_freebies("resonance"))
        self.character.freebies = 21
        self.assertTrue(self.character.spend_freebies("resonance"))
        self.character.freebies = 12

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("ability"), 2)
        self.assertEqual(self.character.xp_cost("background"), 3)
        self.assertEqual(self.character.xp_cost("new background"), 5)
        self.assertEqual(self.character.xp_cost("willpower"), 1)
        self.assertEqual(self.character.xp_cost("new ability"), 3)

        self.assertEqual(self.character.xp_cost("sphere"), 8)
        self.assertEqual(self.character.xp_cost("new sphere"), 10)
        self.assertEqual(self.character.xp_cost("arete"), 8)
        self.assertEqual(self.character.xp_cost("affinity sphere"), 7)
        self.assertEqual(self.character.xp_cost("rote points"), 1)

    def test_spend_xp(self):
        self.character.arete = 1
        self.character.willpower = 5
        self.character.set_affinity_sphere("matter")
        self.character.xp = 100
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
        self.assertTrue(self.character.spend_xp("arete"))
        self.assertEqual(self.character.xp, 70)
        self.assertTrue(self.character.spend_xp("forces"))
        self.assertEqual(self.character.xp, 60)
        self.assertTrue(self.character.spend_xp("forces"))
        self.assertEqual(self.character.xp, 52)
        self.assertTrue(self.character.spend_xp("matter"))
        self.assertEqual(self.character.xp, 45)
        self.assertTrue(self.character.spend_xp("rote points"))
        self.assertEqual(self.character.xp, 44)

    def test_add_resonance(self):
        res = Resonance.objects.order_by("?").first()
        self.assertEqual(self.character.resonance_rating(res), 0)
        self.assertTrue(self.character.add_resonance(res))
        self.assertEqual(self.character.resonance_rating(res), 1)

    def test_filter_resonance(self):
        self.assertEqual(len(self.character.filter_resonance()), 55)
        for res in Resonance.objects.order_by("?")[:3]:
            self.assertTrue(self.character.add_resonance(res))
        self.assertEqual(len(self.character.filter_resonance(maximum=0)), 52)

    def test_total_resonance(self):
        resonance = Resonance.objects.order_by("?")[:2]
        for res in resonance:
            self.character.add_resonance(res)
            self.character.add_resonance(res)
        self.assertEqual(self.character.total_resonance(), 4)
        self.assertNotEqual(self.character.total_resonance(), 5)
        self.character.add_resonance(resonance[0])
        self.assertEqual(self.character.total_resonance(), 5)

    def test_add_effect(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.random_focus()
        r1 = Effect.objects.create(name="Fireball", forces=3, prime=2)
        r2 = Effect.objects.create(name="Teleport", correspondence=3)
        num = self.character.effects.count()
        self.assertTrue(self.character.add_effect(r1))
        self.assertEqual(self.character.effects.count(), num + 1)
        self.assertIn(r1, self.character.effects.all())
        self.assertFalse(self.character.add_effect(r2))
        self.character.correspondence = 3
        self.assertNotIn(r2, self.character.effects.all())
        self.assertTrue(self.character.add_effect(r2))
        self.assertIn(r2, self.character.effects.all())

    def test_has_effects(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.matter = 1
        self.character.random_focus()
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Forces 3"))
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Matter 1"))
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Prime 1"))
        self.assertFalse(self.character.has_effects())
        self.character.add_effect(Effect.objects.get(name="Forces 1"))
        self.assertTrue(self.character.has_effects())

    def test_total_effects(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.correspondence = 3
        self.character.random_focus()
        r1 = Effect.objects.create(name="Fireball", forces=3, prime=2)
        r2 = Effect.objects.create(name="Teleport", correspondence=3)
        self.character.add_effect(r1)
        self.assertEqual(self.character.total_effects(), 5)
        self.character.add_effect(r2)
        self.assertEqual(self.character.total_effects(), 8)

    def test_filter_effects(self):
        self.character.arete = 5
        self.character.correspondence = 5
        self.character.time = 5
        self.character.spirit = 5
        self.character.forces = 5
        self.character.matter = 5
        self.character.life = 5
        self.character.entropy = 5
        self.character.prime = 5
        self.character.mind = 5
        self.assertEqual(len(self.character.filter_effects()), 45)
        self.character.mind = 4
        self.assertEqual(len(self.character.filter_effects()), 44)
        self.character.prime = 1
        self.assertEqual(len(self.character.filter_effects()), 40)
        self.character.correspondence = 1
        self.character.time = 1
        self.character.spirit = 1
        self.character.forces = 2
        self.character.matter = 0
        self.character.life = 0
        self.character.entropy = 0
        self.character.prime = 0
        self.character.mind = 0
        self.assertEqual(len(self.character.filter_effects()), 5)

    def test_has_mage_history(self):
        self.assertFalse(self.character.has_mage_history())
        self.character.awakening = "Young"
        self.assertFalse(self.character.has_mage_history())
        self.character.seekings = "Several"
        self.assertFalse(self.character.has_mage_history())
        self.character.quiets = "None"
        self.assertFalse(self.character.has_mage_history())
        self.character.age_of_awakening = 13
        self.assertFalse(self.character.has_mage_history())
        self.character.avatar_description = "The Random Graph"
        self.assertTrue(self.character.has_mage_history())

    def test_set_quiet_rating(self):
        self.assertEqual(self.character.quiet, 0)
        self.character.set_quiet_rating(3)
        self.assertEqual(self.character.quiet, 3)

    def test_set_quiet_type(self):
        self.assertEqual(self.character.quiet_type, "none")
        self.character.set_quiet_type("denial")
        self.assertEqual(self.character.quiet_type, "denial")

    def test_marauders_have_quiet(self):
        top_level = MageFaction.objects.create(name="TopLevel Faction", parent=None)
        marauder = MageFaction.objects.create(name="Marauders", parent=None)
        self.assertEqual(self.character.quiet, 0)
        self.assertEqual(self.character.quiet_type, "none")
        self.character.set_faction(top_level, None, None)
        self.assertEqual(self.character.quiet, 0)
        self.assertEqual(self.character.quiet_type, "none")
        self.character.set_faction(marauder, None, None)
        self.assertNotEqual(self.character.quiet, 0)
        self.assertNotEqual(self.character.quiet_type, "none")

    def test_count_limbs(self):
        self.character.alertness = 1
        self.character.athletics = 2
        self.character.do = 3
        self.assertEqual(self.character.count_limbs(), 2)
        self.character.awareness = 1
        self.character.enigmas = 2
        self.character.meditation = 3
        self.assertEqual(self.character.count_limbs(), 3)
        self.character.esoterica = 1
        self.character.medicine = 2
        self.character.survival = 3
        self.assertEqual(self.character.count_limbs(), 5)
        self.character.art = 1
        self.character.crafts = 2
        self.character.etiquette = 3
        self.assertEqual(self.character.count_limbs(), 7)
        self.character.academics = 1
        self.character.belief_systems = 2
        self.character.cosmology = 3
        self.assertEqual(self.character.count_limbs(), 8)
        self.character.melee = 1
        self.character.stealth = 2
        self.character.subterfuge = 3
        self.assertEqual(self.character.count_limbs(), 8)

    def test_resonance_rating(self):
        resonance = Resonance.objects.create(name="test_resonance")
        res_rating = ResRating.objects.create(
            mage=self.character, resonance=resonance, rating=3
        )
        self.assertEqual(self.character.resonance_rating(resonance), res_rating.rating)

    def test_has_specialties(self):
        self.assertTrue(self.character.has_specialties())
        self.character.forces = 4
        self.assertFalse(self.character.has_specialties())
        self.character.add_specialty(WoDSpecialty.objects.create(stat="forces"))
        self.assertTrue(self.character.has_specialties())

    def test_has_library(self):
        self.assertFalse(self.character.has_library())
        library = Library.objects.create(name="test_library", rank=3)
        self.character.library_owned = library
        self.character.library = 3
        self.assertTrue(self.character.has_library())

    def test_has_node(self):
        self.assertFalse(self.character.has_node())
        node = Node.objects.create(name="test_node", rank=2)
        self.character.node_owned = node
        self.character.node = 2
        self.assertTrue(self.character.has_node())

    def test_random_freebie_functions(self):
        random_freebie_functions = self.character.random_freebie_functions()
        self.assertIn("attribute", random_freebie_functions)
        self.assertIn("ability", random_freebie_functions)
        self.assertIn("background", random_freebie_functions)
        self.assertIn("willpower", random_freebie_functions)
        self.assertIn("meritflaw", random_freebie_functions)
        self.assertIn("sphere", random_freebie_functions)
        self.assertIn("arete", random_freebie_functions)
        self.assertIn("quintessence", random_freebie_functions)
        self.assertIn("rote points", random_freebie_functions)
        self.assertIn("resonance", random_freebie_functions)

    def test_random_xp_functions(self):
        random_xp_functions = self.character.random_xp_functions()
        self.assertIn("attribute", random_xp_functions)
        self.assertIn("ability", random_xp_functions)
        self.assertIn("background", random_xp_functions)
        self.assertIn("willpower", random_xp_functions)
        self.assertIn("sphere", random_xp_functions)
        self.assertIn("arete", random_xp_functions)
        self.assertIn("rote points", random_xp_functions)


class TestRandomMage(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Test")
        self.character = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.player)

    def test_random_affinity_sphere(self):
        self.assertFalse(self.character.has_affinity_sphere())
        self.character.random_affinity_sphere()
        self.assertTrue(self.character.has_affinity_sphere())

    def test_random_faction(self):
        self.assertFalse(self.character.has_faction())
        self.character.random_faction()
        self.assertTrue(self.character.has_faction())
        mage = Mage.objects.create(name="Random Character", owner=self.player)
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

    def test_random_spend_xp(self):
        self.character.science = 1
        self.character.xp = 15
        self.character.random_xp()
        self.assertLess(self.character.xp, 15)

    def test_random_freebies(self):
        self.assertEqual(self.character.freebies, 15)
        self.character.random_freebies()
        self.assertEqual(self.character.freebies, 0)

    def test_random_essence(self):
        self.assertFalse(self.character.has_essence())
        self.character.random_essence()
        self.assertTrue(self.character.has_essence())

    def test_random_resonance(self):
        self.assertEqual(self.character.total_resonance(), 0)
        self.character.random_resonance()
        self.assertEqual(self.character.total_resonance(), 1)

    def test_random_effect(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.matter = 1
        self.character.random_focus()
        num = self.character.effects.count()
        self.character.random_effect()
        self.assertEqual(self.character.effects.count(), num + 1)

    def test_random_effects(self):
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.matter = 1
        self.character.random_focus()
        self.assertFalse(self.character.has_effects())
        self.character.random_effects()
        self.assertTrue(self.character.has_effects())

    def test_created_node_when_has_node(self):
        self.character.node = 3
        self.assertFalse(self.character.has_node())
        self.character.random_node()
        self.assertTrue(self.character.has_node())

    def test_created_library_when_has_library(self):
        self.character.library = 3
        self.assertFalse(self.character.has_library())
        self.character.random_library()
        self.assertTrue(self.character.has_library())

    def test_random_specialties(self):
        self.character.forces = 4
        self.character.random_specialties()
        self.assertTrue(self.character.has_specialties())
        self.assertGreater(self.character.specialties.filter(stat="forces").count(), 0)

    def test_random_quiet(self):
        self.character.random_quiet()
        self.assertGreater(self.character.quiet, 0)
        self.assertNotEqual(self.character.quiet_type, "none")

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        self.assertFalse(self.character.has_archetypes())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_backgrounds())
        self.assertFalse(self.character.has_finishing_touches())
        self.assertFalse(self.character.has_history())
        self.assertFalse(self.character.has_spheres())
        self.assertFalse(self.character.has_affinity_sphere())
        self.assertFalse(self.character.has_faction())
        self.assertFalse(self.character.has_focus())
        self.assertFalse(self.character.has_essence())
        self.assertFalse(self.character.has_effects())
        self.assertFalse(self.character.has_mage_history())
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
        self.assertTrue(self.character.has_spheres())
        self.assertTrue(self.character.has_affinity_sphere())
        self.assertTrue(self.character.has_faction())
        self.assertTrue(self.character.has_focus())
        self.assertTrue(self.character.has_essence())
        self.assertTrue(self.character.has_effects())
        self.assertTrue(self.character.has_mage_history())
        if self.character.node != 0:
            self.assertTrue(self.character.has_node())
        else:
            self.assertFalse(self.character.has_node())
        if self.character.library != 0:
            self.assertTrue(self.character.has_library())
        else:
            self.assertFalse(self.character.has_library())

    def test_choose_random_resonance(self):
        res = self.character.choose_random_resonance()
        self.assertIsNotNone(res)
        self.assertIsInstance(res, Resonance)

    def test_random_mage_history(self):
        self.character.random_mage_history()
        self.assertIsNotNone(self.character.awakening)
        self.assertIsNotNone(self.character.seekings)
        self.assertIsNotNone(self.character.quiets)
        self.assertIsNotNone(self.character.age_of_awakening)
        self.assertIsNotNone(self.character.avatar_description)

    def test_random_xp_sphere(self):
        self.character.xp = 20
        self.character.arete = 1
        self.assertTrue(self.character.random_xp_sphere())
        self.assertEqual(self.character.xp, 10)
        self.assertEqual(self.character.total_spheres(), 1)

    def test_random_xp_arete(self):
        self.character.xp = 20
        self.character.arete = 2
        self.assertTrue(self.character.random_xp_arete())
        self.assertEqual(self.character.xp, 4)
        self.assertEqual(self.character.arete, 3)

    def test_random_xp_rote_points(self):
        self.character.xp = 20
        self.character.rote_points = 0
        self.assertTrue(self.character.random_xp_rote_points())
        self.assertEqual(self.character.xp, 19)
        self.assertEqual(self.character.rote_points, 3)

    def test_random_freebies_sphere(self):
        self.character.freebies = 20
        self.character.arete = 2
        self.assertTrue(self.character.random_freebies_sphere())
        self.assertEqual(self.character.freebies, 13)
        self.assertEqual(self.character.total_spheres(), 1)

    def test_random_freebies_quintessence(self):
        self.character.freebies = 20
        self.character.quintessence = 0
        self.assertTrue(self.character.random_freebies_quintessence())
        self.assertEqual(self.character.freebies, 19)
        self.assertEqual(self.character.quintessence, 4)

    def test_random_freebies_rote_points(self):
        self.character.freebies = 20
        self.character.rote_points = 0
        self.assertTrue(self.character.random_freebies_rote_points())
        self.assertEqual(self.character.freebies, 19)
        self.assertEqual(self.character.rote_points, 4)

    def test_random_freebies_resonance(self):
        self.character.freebies = 20
        self.character.random_resonance()
        self.assertTrue(self.character.random_freebies_resonance())
        self.assertEqual(self.character.freebies, 17)
        self.assertEqual(self.character.total_resonance(), 2)

    def test_random_freebies_arete(self):
        self.character.freebies = 20
        self.character.arete = 2
        self.assertTrue(self.character.random_freebies_arete())
        self.assertEqual(self.character.freebies, 16)
        self.assertEqual(self.character.arete, 3)

    def test_random_abilities(self):
        self.character.random_abilities()
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertEqual(triple, [5, 9, 13])

    def test_random_ability(self):
        self.character.random_ability()
        self.assertGreater(self.character.total_abilities(), 0)


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

    def test_random(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.random(num_chars=5, new_characters=False)
        self.assertEqual(cabal.members.count(), 5)
        for mage in Mage.objects.all():
            self.assertIn(mage, cabal.members.all())
        cabal = Cabal.objects.create(name="Cabal 2")
        cabal.random(num_chars=5, new_characters=True)
        self.assertEqual(cabal.members.count(), 5)

    def test_exception(self):
        cabal = Cabal.objects.create(name="Cabal 10")
        with self.assertRaises(ValueError):
            cabal.random(num_chars=10, new_characters=False)

    def test_str(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        self.assertEqual(str(cabal), "Cabal 1")


class TestMageFaction(TestCase):
    def setUp(self):
        self.faction1 = MageFaction.objects.create()
        self.faction2 = MageFaction.objects.create(parent=self.faction1)
        self.faction3 = MageFaction.objects.create(parent=self.faction2)

        self.paradigm1 = Paradigm.objects.create(name="Paradigm 1")
        self.paradigm2 = Paradigm.objects.create(name="Paradigm 2")
        self.paradigm3 = Paradigm.objects.create(name="Paradigm 3")

        self.practice1 = Practice.objects.create(name="Practice 1")
        self.practice2 = Practice.objects.create(name="Practice 2")
        self.practice3 = Practice.objects.create(name="Practice 3")

        self.faction1.paradigms.add(self.paradigm1, self.paradigm2)
        self.faction2.paradigms.add(self.paradigm2, self.paradigm3)
        self.faction3.paradigms.add(self.paradigm1, self.paradigm3)

        self.faction1.practices.add(self.practice1, self.practice2)
        self.faction2.practices.add(self.practice2, self.practice3)
        self.faction3.practices.add(self.practice1, self.practice3)

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

    def test_get_all_paradigms(self):
        expected_paradigms = Paradigm.objects.filter(id__in=[1, 2, 3])
        self.assertQuerySetEqual(
            self.faction3.get_all_paradigms(), expected_paradigms, ordered=False
        )

    def test_get_all_practices(self):
        expected_practices = Practice.objects.filter(id__in=[1, 2, 3])
        self.assertQuerySetEqual(
            self.faction3.get_all_practices(), expected_practices, ordered=False
        )

    def test_str(self):
        faction = MageFaction.objects.create(name="Faction 1", parent=None)
        self.assertEqual(str(faction), "Faction 1")


class TestPractice(TestCase):
    def test_abilities(self):
        practice = Practice.objects.create(name="Practice 1")
        practice.abilities = ["martial_arts", "awareness"]
        self.assertEqual(len(practice.abilities), 2)

    def test_str(self):
        practice = Practice.objects.create(
            name="Practice 1", abilities=list(random.sample(ABILITY_LIST, k=4))
        )
        self.assertEqual(str(practice), "Practice 1")


class TestInstrument(TestCase):
    def test_str(self):
        instrument = Instrument.objects.create(name="Instrument 1")
        self.assertEqual(str(instrument), "Instrument 1")


class TestParadigm(TestCase):
    def test_str(self):
        paradigm = Paradigm.objects.create(name="Paradigm 1")
        self.assertEqual(str(paradigm), "Paradigm 1")


class TestEffect(TestCase):
    def setUp(self):
        self.mage = Mage.objects.create(
            name="Test Mage",
            correspondence=2,
            time=2,
            spirit=2,
            matter=2,
            forces=2,
            life=2,
            entropy=2,
            mind=2,
            prime=2,
        )
        self.effect = Effect.objects.create(
            name="Test Effect",
            correspondence=1,
            time=1,
            spirit=1,
            matter=1,
            forces=1,
            life=1,
            entropy=1,
            mind=1,
            prime=1,
        )

    def test_save(self):
        self.effect.save()
        self.assertEqual(self.effect.rote_cost, 9)
        self.assertEqual(self.effect.max_sphere, 1)

    def test_is_learnable(self):
        self.assertTrue(self.effect.is_learnable(self.mage))
        self.mage.correspondence = 0
        self.assertFalse(self.effect.is_learnable(self.mage))


class TestRandomRote(TestCase):
    def setUp(self):
        self.mage = Mage.objects.create(name="Test Mage", occult=3)
        self.effect = Effect.objects.create(name="Test Effect")
        self.practice = Practice.objects.create(
            name="Test Practice", abilities=["occult"]
        )
        self.mage.practices.add(self.practice)
        self.rote = Rote.objects.create(mage=self.mage, effect=self.effect)

    def test_save(self):
        self.rote.save()
        self.assertIsNotNone(self.rote.practice)

    def test_random(self):
        self.rote.random()
        self.assertIsNotNone(self.rote.practice)
        self.assertIsNotNone(self.rote.attribute)
        self.assertIsNotNone(self.rote.ability)


class TestMageDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.mage = Mage.objects.create(name="Test Mage", owner=self.player)

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/mage/detail.html")


class TestCabalDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.cabal = Cabal.objects.create(name="Test Cabal")

    def test_cabal_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/groups/{self.cabal.id}/")
        self.assertEqual(response.status_code, 200)

    def test_cabal_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/groups/{self.cabal.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/cabal/detail.html")
