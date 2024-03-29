from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.timezone import now

from core.models import Language
from wod.models.characters.human import (
    Archetype,
    Character,
    Derangement,
    Group,
    Human,
    MeritFlaw,
    MeritFlawRating,
    WoDSpecialty,
)
from wod.models.characters.mage import Cabal, Mage
from wod.models.characters.werewolf import Pack, Werewolf


# Create your tests here.
class TestCharacter(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Character.objects.create(owner=self.player, name="")

    def test_has_name(self):
        self.assertFalse(self.character.has_name())
        self.character.set_name("Test")
        self.assertTrue(self.character.has_name())

    def test_set_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.set_name("Test"))
        self.assertNotEqual(self.character.name, "")

    def test_has_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.set_concept("Test")
        self.assertTrue(self.character.has_concept())

    def test_set_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.set_concept("Test"))
        self.assertNotEqual(self.character.concept, "")

    def test_absolute_url(self):
        self.assertEqual(
            self.character.get_absolute_url(), f"/wod/characters/{self.character.id}/"
        )


class TestRandomCharacter(TestCase):
    def setUp(self):
        self.character = Character.objects.create()

    def test_random_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.random_concept()
        self.assertTrue(self.character.has_concept())

    def test_random_name(self):
        name_count = Character.objects.count()
        self.assertNotEqual(self.character.name, f"Random Character {name_count}")
        self.character.random_name()
        self.assertEqual(self.character.name, f"Random Character {name_count}")


class TestHuman(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="Test")
        self.character = Human.objects.create(name="", owner=self.user)
        for i in range(10):
            Archetype.objects.create(name=f"Archetype {i}")
        for i in range(1, 6):
            for j in [-1, 1]:
                if j == 1:
                    MeritFlaw.objects.create(name=f"Merit {i}", ratings=[i], human=True)
                else:
                    MeritFlaw.objects.create(name=f"Flaw {i}", ratings=[-i], human=True)
        for i in range(10):
            for stat in self.character.get_abilities():
                WoDSpecialty.objects.create(
                    name=f"{stat.replace('_', ' ').title()} Specialty {i}", stat=stat,
                )
        for i in range(10):
            for stat in self.character.get_attributes():
                WoDSpecialty.objects.create(
                    name=f"{stat.replace('_', ' ').title()} Specialty {i}", stat=stat,
                )
        for i in range(20):
            Language.objects.create(name=f"TL {i}")

    def test_has_archetypes(self):
        self.assertFalse(self.character.has_archetypes())
        self.character.nature = Archetype.objects.first()
        self.character.demeanor = Archetype.objects.first()
        self.assertTrue(self.character.has_archetypes())

    def test_set_archetypes(self):
        self.assertFalse(self.character.has_archetypes())
        self.assertTrue(
            self.character.set_archetypes(
                Archetype.objects.first(), Archetype.objects.first()
            )
        )
        self.assertTrue(self.character.has_archetypes())

    def test_languages(self):
        english = Language.objects.create(name="English")
        self.assertEqual(self.character.languages.count(), 0)
        self.character.languages.add(english)
        self.assertEqual(self.character.languages.count(), 1)

    def set_attributes(self):
        self.character.strength = 5
        self.character.dexterity = 4
        self.character.stamina = 3
        self.character.perception = 2
        self.character.intelligence = 1
        self.character.wits = 2
        self.character.charisma = 3
        self.character.manipulation = 4
        self.character.appearance = 5

    def test_get_attributes(self):
        self.assertEqual(
            self.character.get_attributes(),
            {
                "strength": 1,
                "dexterity": 1,
                "stamina": 1,
                "perception": 1,
                "intelligence": 1,
                "wits": 1,
                "charisma": 1,
                "manipulation": 1,
                "appearance": 1,
            },
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_attributes(),
            {
                "strength": 5,
                "dexterity": 4,
                "stamina": 3,
                "perception": 2,
                "intelligence": 1,
                "wits": 2,
                "charisma": 3,
                "manipulation": 4,
                "appearance": 5,
            },
        )

    def test_get_physical_attributes(self):
        self.assertEqual(
            self.character.get_physical_attributes(),
            {"strength": 1, "dexterity": 1, "stamina": 1,},
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_physical_attributes(),
            {"strength": 5, "dexterity": 4, "stamina": 3,},
        )

    def test_get_mental_attributes(self):
        self.assertEqual(
            self.character.get_mental_attributes(),
            {"perception": 1, "intelligence": 1, "wits": 1,},
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_mental_attributes(),
            {"perception": 2, "intelligence": 1, "wits": 2,},
        )

    def test_get_social_attributes(self):
        self.assertEqual(
            self.character.get_social_attributes(),
            {"charisma": 1, "manipulation": 1, "appearance": 1,},
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_social_attributes(),
            {"charisma": 3, "manipulation": 4, "appearance": 5,},
        )

    def test_add_attribute(self):
        self.character.strength = 1
        self.assertTrue(self.character.add_attribute("strength"))
        self.assertEqual(self.character.strength, 2)
        self.character.strength = 5
        self.assertFalse(self.character.add_attribute("strength", maximum=5))
        self.assertEqual(self.character.strength, 5)
        self.assertTrue(self.character.add_attribute("strength", maximum=6))
        self.assertEqual(self.character.strength, 6)

    def test_filter_attributes(self):
        self.character.strength = 5
        self.assertEqual(
            self.character.filter_attributes(maximum=4),
            {
                "dexterity": 1,
                "stamina": 1,
                "intelligence": 1,
                "wits": 1,
                "perception": 1,
                "appearance": 1,
                "manipulation": 1,
                "charisma": 1,
            },
        )
        self.assertEqual(
            self.character.filter_attributes(maximum=5),
            {
                "strength": 5,
                "dexterity": 1,
                "stamina": 1,
                "intelligence": 1,
                "wits": 1,
                "perception": 1,
                "appearance": 1,
                "manipulation": 1,
                "charisma": 1,
            },
        )
        self.character.strength = 4
        self.assertEqual(self.character.filter_attributes(minimum=3), {"strength": 4})
        self.assertEqual(
            self.character.filter_attributes(minimum=3, maximum=5), {"strength": 4}
        )
        self.assertEqual(self.character.filter_attributes(minimum=5, maximum=6), {})

    def test_has_attributes(self):
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 8, 10])
        self.character.strength = 3
        self.character.dexterity = 4
        self.character.stamina = 3
        self.character.intelligence = 3
        self.character.wits = 3
        self.character.perception = 2
        self.character.charisma = 2
        self.character.manipulation = 2
        self.character.appearance = 2
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertEqual(triple, [6, 8, 10])
        self.character.perception = 3
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 8, 10])

    def test_total_physical_attribute(self):
        self.character.strength = 1
        self.character.dexterity = 2
        self.character.stamina = 3
        self.assertEqual(self.character.total_physical_attributes(), 6)
        self.character.stamina = 2
        self.assertEqual(self.character.total_physical_attributes(), 5)

    def test_total_mental_attribute(self):
        self.character.perception = 1
        self.character.intelligence = 2
        self.character.wits = 3
        self.assertEqual(self.character.total_mental_attributes(), 6)
        self.character.wits = 2
        self.assertEqual(self.character.total_mental_attributes(), 5)

    def test_total_social_attribute(self):
        self.character.charisma = 1
        self.character.manipulation = 2
        self.character.appearance = 3
        self.assertEqual(self.character.total_social_attributes(), 6)
        self.character.appearance = 2
        self.assertEqual(self.character.total_social_attributes(), 5)

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
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "academics": 0,
                "computer": 0,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 3,
                "athletics": 3,
                "brawl": 3,
                "empathy": 3,
                "expression": 1,
                "intimidation": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "crafts": 3,
                "drive": 3,
                "etiquette": 3,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "academics": 3,
                "computer": 2,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
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
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 3,
                "athletics": 3,
                "brawl": 3,
                "empathy": 3,
                "expression": 1,
                "intimidation": 0,
                "streetwise": 0,
                "subterfuge": 0,
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
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 3,
                "drive": 3,
                "etiquette": 3,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
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
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 3,
                "computer": 2,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
            },
        )

    def test_add_ability(self):
        self.character.occult = 0
        self.assertTrue(self.character.add_ability("occult"))
        self.assertEqual(self.character.occult, 1)
        self.character.occult = 5
        self.assertFalse(self.character.add_ability("occult", maximum=5))
        self.assertEqual(self.character.occult, 5)
        self.assertTrue(self.character.add_ability("occult", maximum=6))
        self.assertEqual(self.character.occult, 6)

    def test_filter_abilities(self):
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=3)), 0)
        self.assertEqual(len(self.character.filter_abilities(minimum=0, maximum=3)), 19)
        self.set_abilities()
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=3)), 10)
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=2)), 2)

    def set_abilities(self):
        self.character.alertness = 3
        self.character.athletics = 3
        self.character.brawl = 3
        self.character.empathy = 3
        self.character.expression = 1
        self.character.crafts = 3
        self.character.drive = 3
        self.character.etiquette = 3
        self.character.academics = 3
        self.character.computer = 2

    def test_has_abilities(self):
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [5, 9, 13])
        self.set_abilities()
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertEqual(triple, [5, 9, 13])
        self.character.subterfuge = 1
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [5, 9, 13])

    def test_add_specialty(self):
        num = self.character.specialties.count()
        self.assertTrue(
            self.character.add_specialty(
                WoDSpecialty.objects.get(name="Athletics Specialty 3", stat="athletics")
            )
        )
        self.assertEqual(self.character.specialties.count(), num + 1)

    def test_filter_specialties(self):
        self.assertEqual(len(self.character.filter_specialties()), 280)
        self.assertEqual(len(self.character.filter_specialties(stat="strength")), 10)
        self.assertEqual(len(self.character.filter_specialties(stat="athletics")), 10)
        self.character.add_specialty(
            WoDSpecialty.objects.get(name="Athletics Specialty 3", stat="athletics")
        )
        self.assertEqual(len(self.character.filter_specialties(stat="athletics")), 9)

    def test_has_specialties(self):
        self.character.dexterity = 2
        self.character.stamina = 3
        self.character.perception = 4
        self.character.intelligence = 5
        self.character.wits = 4
        self.character.charisma = 3
        self.character.manipulation = 2
        self.character.appearance = 4
        self.character.alertness = 1
        self.character.athletics = 2
        self.character.brawl = 4
        self.character.crafts = 1
        self.character.drive = 2
        self.character.etiquette = 5
        self.character.firearms = 3
        self.character.stealth = 4
        self.character.medicine = 2
        self.character.science = 1
        for attribute, value in self.character.get_attributes().items():
            if value >= 4:
                self.assertGreaterEqual(
                    self.character.specialties.filter(stat=attribute).count(), 0
                )
        for ability, value in self.character.get_abilities().items():
            if value >= 4 or (
                ability
                in [
                    "arts",
                    "athletics",
                    "crafts",
                    "firearms",
                    "martial_arts",
                    "melee",
                    "academics",
                    "esoterica",
                    "lore",
                    "politics",
                    "science",
                ]
                and value > 0
            ):
                self.assertGreaterEqual(
                    self.character.specialties.filter(stat=ability).count(), 0
                )

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(), {"contacts": 0, "mentor": 0,},
        )
        self.character.contacts = 3
        self.character.mentor = 2
        self.assertEqual(
            self.character.get_backgrounds(), {"contacts": 3, "mentor": 2,},
        )

    def test_add_background(self):
        total = self.character.total_backgrounds()
        self.assertTrue(self.character.add_background("contacts"))
        self.assertEqual(self.character.total_backgrounds(), total + 1)

    def test_filter_backgrounds(self):
        self.assertEqual(len(self.character.filter_backgrounds()), 2)
        self.character.contacts = 4
        self.character.mentor = 2
        self.assertEqual(len(self.character.filter_backgrounds(minimum=3)), 1)
        self.assertEqual(len(self.character.filter_backgrounds(maximum=3)), 1)

    def test_has_backgrounds(self):
        self.assertFalse(self.character.has_backgrounds())
        self.character.contacts = 2
        self.character.mentor = 3
        self.assertTrue(self.character.has_backgrounds())

    def test_add_willpower(self):
        self.assertEqual(self.character.willpower, 3)
        self.assertTrue(self.character.add_willpower())
        self.assertEqual(self.character.willpower, 4)

    def test_add_mf(self):
        m3 = MeritFlaw.objects.get(name="Merit 3")
        self.assertEqual(self.character.merits_and_flaws.count(), 0)
        self.assertTrue(self.character.add_mf(m3, 3))
        self.assertEqual(self.character.merits_and_flaws.count(), 1)
        self.assertIn(m3, self.character.merits_and_flaws.all())

    def test_has_max_flaws(self):
        self.assertFalse(self.character.has_max_flaws())
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 3"), -3)
        self.assertFalse(self.character.has_max_flaws())
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 4"), -4)
        self.assertTrue(self.character.has_max_flaws())

    def test_filter_mfs(self):
        self.assertEqual(len(self.character.filter_mfs()), 10)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 1"), 1)
        self.assertEqual(len(self.character.filter_mfs()), 9)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 2"), 2)
        self.assertEqual(len(self.character.filter_mfs()), 8)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 2"), -2)
        self.assertEqual(len(self.character.filter_mfs()), 7)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 5"), -5)
        self.assertEqual(len(self.character.filter_mfs()), 3)
        m = MeritFlaw.objects.create(name="Test Merit", ratings=[1, 2, 3])
        self.assertNotIn(m, self.character.filter_mfs())
        m.human = True
        m.save()
        self.assertIn(m, self.character.filter_mfs())

    def test_total_merits(self):
        self.assertEqual(self.character.total_merits(), 0)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 3"), 3)
        self.assertEqual(self.character.total_merits(), 3)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 3"), -3)
        self.assertEqual(self.character.total_merits(), 3)

    def test_total_flaws(self):
        self.assertEqual(self.character.total_flaws(), 0)
        self.character.add_mf(MeritFlaw.objects.get(name="Flaw 3"), -3)
        self.assertEqual(self.character.total_flaws(), -3)
        self.character.add_mf(MeritFlaw.objects.get(name="Merit 3"), 3)
        self.assertEqual(self.character.total_flaws(), -3)

    def test_freebie_cost(self):
        self.assertEqual(self.character.freebie_cost("attribute"), 5)
        self.assertEqual(self.character.freebie_cost("ability"), 2)
        self.assertEqual(self.character.freebie_cost("background"), 1)
        self.assertEqual(self.character.freebie_cost("willpower"), 1)
        self.assertEqual(self.character.freebie_cost("meritflaw"), 1)

    def test_spend_freebies(self):
        self.assertEqual(self.character.freebies, 15)
        self.assertTrue(self.character.spend_freebies("strength"))
        self.assertEqual(self.character.freebies, 10)
        self.assertTrue(self.character.spend_freebies("science"))
        self.assertEqual(self.character.freebies, 8)
        self.assertTrue(self.character.spend_freebies("mentor"))
        self.assertEqual(self.character.freebies, 7)
        self.assertTrue(self.character.spend_freebies("willpower"))
        self.assertEqual(self.character.freebies, 6)
        self.assertTrue(self.character.spend_freebies("Merit 1"))
        self.assertEqual(self.character.freebies, 5)

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("ability"), 2)
        self.assertEqual(self.character.xp_cost("background"), 3)
        self.assertEqual(self.character.xp_cost("new background"), 5)
        self.assertEqual(self.character.xp_cost("willpower"), 1)
        self.assertEqual(self.character.xp_cost("new ability"), 3)

    def test_spend_xp(self):
        self.character.xp = 100
        self.assertTrue(self.character.spend_xp("strength"))
        self.assertEqual(self.character.xp, 96)
        self.assertTrue(self.character.spend_xp("science"))
        self.assertEqual(self.character.xp, 93)
        self.assertTrue(self.character.spend_xp("science"))
        self.assertEqual(self.character.xp, 91)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 86)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 83)
        self.assertTrue(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 80)

    def test_add_to_spend(self):
        self.character.xp = 100
        self.assertEqual(self.character.spent_xp, "")
        self.assertEqual(self.character.strength, 1)
        self.character.spend_xp("strength")
        self.assertEqual(self.character.strength, 2)
        self.assertEqual(self.character.spent_xp, "Strength 2 (4 XP)")
        self.character.spend_xp("strength")
        self.assertEqual(self.character.strength, 3)
        self.assertEqual(
            self.character.spent_xp, "Strength 2 (4 XP), Strength 3 (8 XP)"
        )
        self.character.spend_xp("science")
        self.assertEqual(self.character.science, 1)
        self.assertEqual(
            self.character.spent_xp,
            "Strength 2 (4 XP), Strength 3 (8 XP), Science 1 (3 XP)",
        )

    def test_has_finishing_touches(self):
        self.assertFalse(self.character.has_finishing_touches())
        self.character.age = 18
        self.assertFalse(self.character.has_finishing_touches())
        self.character.date_of_birth = now()
        self.assertFalse(self.character.has_finishing_touches())
        self.character.hair = "Black"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.eyes = "Brown"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.ethnicity = "White"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.nationality = "American"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.height = "5'11\""
        self.assertFalse(self.character.has_finishing_touches())
        self.character.weight = "150 lbs"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.sex = "Male"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.description = "Hardcore Asshole"
        self.assertFalse(self.character.has_finishing_touches())
        self.character.apparent_age = 18
        self.assertTrue(self.character.has_finishing_touches())

    def test_has_history(self):
        self.assertFalse(self.character.has_history())
        self.character.childhood = "Was a kid, it sucked."
        self.assertFalse(self.character.has_history())
        self.character.history = "Got older."
        self.assertFalse(self.character.has_history())
        self.character.goals = "Get older still."
        self.assertTrue(self.character.has_history())

    def test_notes_field(self):
        self.assertEqual(self.character.notes, "")
        self.character.notes = "This is a note."
        self.assertNotEqual(self.character.notes, "")

    def test_static_numbers(self):
        self.assertEqual(self.character.willpower, 3)
        self.assertEqual(self.character.background_points, 5)
        self.assertEqual(self.character.freebies, 15)

    def test_add_damage(self):
        self.assertEqual(self.character.get_wound_penalty(), 0)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), 0)
        self.character.add_aggravated()
        self.assertEqual(self.character.current_health_levels, "AB")
        self.assertEqual(self.character.get_wound_penalty(), -1)
        self.character.add_lethal()
        self.assertEqual(self.character.current_health_levels, "ALB")
        self.assertEqual(self.character.get_wound_penalty(), -1)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -2)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -2)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -5)
        self.character.add_bashing()
        self.assertEqual(self.character.current_health_levels, "ALBBBBB")
        self.character.add_bashing()
        self.assertEqual(self.character.current_health_levels, "ALLBBBB")
        self.character.add_aggravated()
        self.assertEqual(self.character.get_wound_penalty(), -1000)

    def test_language_merit(self):
        m = MeritFlaw.objects.create(name="Language", ratings=[1, 2, 3, 4, 5])
        self.assertEqual(self.character.languages.count(), 0)
        for i in range(5):
            self.character.add_mf(m, i + 1)
            self.assertEqual(self.character.languages.count(), 1 + i)

    def test_natural_linguist_merit(self):
        self.assertEqual(self.character.languages.count(), 0)
        nl = MeritFlaw.objects.create(name="Natural Linguist", ratings=[1])
        m = MeritFlaw.objects.create(name="Language", ratings=[1, 2, 3, 4, 5])
        self.character.add_mf(nl, 1)
        for i in range(5):
            self.character.add_mf(m, i + 1)
            self.assertEqual(self.character.languages.count(), 2 * (i + 1))
        lt = Human.objects.create(name="language tester", owner=self.user)
        self.assertEqual(lt.languages.count(), 0)
        lt.add_mf(m, 1)
        self.assertEqual(lt.languages.count(), 1)
        lt.add_mf(nl, 1)
        self.assertEqual(lt.languages.count(), 2)

    def test_ability_deficit_flaw(self):
        mf = MeritFlaw.objects.create(name="Ability Deficit", ratings=[-2])
        self.character.add_mf(mf, -2)
        self.character.alertness = 3
        self.character.athletics = 2
        self.character.drive = 3
        self.character.etiquette = 2
        self.character.academics = 3
        self.character.computer = 2
        self.character.mf_based_corrections()
        self.assertEqual(self.character.total_abilities(), 10)
        l = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        l.sort()
        self.assertEqual([0, 5, 5], l)

    def test_attribute_specialties(self):
        self.character.specialties.create(name="strength focus", stat="strength")
        self.character.specialties.create(name="charisma focus", stat="charisma")
        self.assertEqual(self.character.strength_specialty().name, "strength focus")
        self.assertEqual(self.character.charisma_specialty().name, "charisma focus")

    def test_total_attributes(self):
        self.character.strength = 3
        self.character.dexterity = 2
        self.character.stamina = 4
        self.assertEqual(self.character.total_attributes(), 15)

    def test_total_talents(self):
        self.character.alertness = 2
        self.character.athletics = 1
        self.character.brawl = 1
        self.assertEqual(self.character.total_talents(), 4)

    def test_total_skills(self):
        self.character.etiquette = 2
        self.character.firearms = 1
        self.character.stealth = 3
        self.assertEqual(self.character.total_skills(), 6)

    def test_total_knowledges(self):
        self.character.academics = 1
        self.character.investigation = 2
        self.assertEqual(self.character.total_knowledges(), 3)

    def test_total_abilities(self):
        self.character.add_ability("brawl")
        self.character.add_ability("firearms")
        self.assertEqual(self.character.total_abilities(), 2)

    def test_total_backgrounds(self):
        self.character.add_background("contacts")
        self.character.add_background("mentor")
        self.assertEqual(self.character.total_backgrounds(), 2)

    def test_add_derangement(self):
        d = Derangement.objects.create(name="Test Derangement")
        self.assertTrue(self.character.add_derangement(d))
        self.assertFalse(self.character.add_derangement(d))

    def test_mf_rating(self):
        mf = MeritFlaw.objects.create(name="Test Merit Flaw", ratings=[-2, -1])
        MeritFlawRating.objects.create(character=self.character, mf=mf, rating=-2)
        self.assertEqual(self.character.mf_rating(mf), -2)

    def test_spend_freebies_attribute(self):
        self.character.freebies = 10
        self.assertTrue(self.character.spend_freebies_attribute("strength"))
        self.assertEqual(self.character.freebies, 5)
        self.assertEqual(self.character.strength, 2)

    def test_spend_freebies_ability(self):
        self.character.freebies = 10
        self.assertTrue(self.character.spend_freebies_ability("brawl"))
        self.assertEqual(self.character.freebies, 8)
        self.assertEqual(self.character.brawl, 1)

    def test_spend_freebies_background(self):
        self.character.freebies = 10
        self.assertTrue(self.character.spend_freebies_background("mentor"))
        self.assertEqual(self.character.freebies, 9)
        self.assertEqual(self.character.mentor, 1)

    def test_spend_freebies_willpower(self):
        self.character.freebies = 10
        self.assertTrue(self.character.spend_freebies_willpower())
        self.assertEqual(self.character.freebies, 9)
        self.assertEqual(self.character.willpower, 4)

    def test_spend_freebies_mf(self):
        self.character.freebies = 10
        mf = MeritFlaw.objects.create(name="Phobia (heights)", ratings=[-2])
        self.assertTrue(self.character.spend_freebies_mf(mf.name))
        self.assertEqual(self.character.freebies, 12)
        self.assertEqual(self.character.mf_rating(mf), -2)

    def test_random_freebie_functions(self):
        functions = self.character.random_freebie_functions()
        self.assertEqual(
            set(functions.keys()),
            {"attribute", "ability", "background", "willpower", "meritflaw"},
        )

    def test_random_xp_attribute(self):
        self.character.xp = 10
        self.assertTrue(self.character.random_xp_attributes())
        self.assertEqual(self.character.xp, 6)
        self.assertEqual(self.character.total_attributes(), 10)

    def test_random_xp_ability(self):
        self.character.xp = 10
        self.assertTrue(self.character.random_xp_abilities())
        self.assertEqual(self.character.xp, 7)
        self.assertEqual(self.character.total_abilities(), 1)

    def test_random_xp_background(self):
        self.character.xp = 10
        self.assertTrue(self.character.random_xp_background())
        self.assertEqual(self.character.xp, 5)
        self.assertEqual(self.character.total_backgrounds(), 1)

    def test_random_xp_willpower(self):
        self.character.xp = 10
        self.character.willpower = 4
        self.assertTrue(self.character.random_xp_willpower())
        self.assertEqual(self.character.xp, 6)
        self.assertEqual(self.character.willpower, 5)

    def test_random_xp_functions(self):
        functions = self.character.random_xp_functions()
        self.assertEqual(
            set(functions.keys()), {"attribute", "ability", "background", "willpower"}
        )


class TestRandomHuman(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="Test")
        self.character = Human.objects.create(name="", owner=self.user)
        for i in range(10):
            Archetype.objects.create(name=f"Archetype {i}")
        for i in range(10):
            for ability in self.character.get_abilities():
                WoDSpecialty.objects.create(
                    name=f"{ability.replace('_', ' ').title()} Specialty {i}",
                    stat=ability,
                )
        for i in range(10):
            for attribute in self.character.get_attributes():
                WoDSpecialty.objects.create(
                    name=f"{attribute.replace('_', ' ').title()} Specialty {i}",
                    stat=attribute,
                )
        for i in range(1, 6):
            for j in [-1, 1]:
                if j == 1:
                    MeritFlaw.objects.create(name=f"Merit {i}", ratings=[i], human=True)
                else:
                    MeritFlaw.objects.create(name=f"Flaw {i}", ratings=[-i], human=True)

    def test_random_name(self):
        self.assertFalse(self.character.has_name())
        self.character.random_name()
        self.assertTrue(self.character.has_name())

    def test_random_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.random_concept()
        self.assertTrue(self.character.has_concept())

    def test_random_archetypes(self):
        self.assertFalse(self.character.has_archetypes())
        self.character.random_archetypes()
        self.assertTrue(self.character.has_archetypes())

    def test_random_attribute(self):
        num = self.character.total_attributes()
        self.character.random_attribute()
        self.assertEqual(self.character.total_attributes(), num + 1)

    def test_random_attributes(self):
        self.character.random_attributes()
        triple = [
            self.character.total_mental_attributes(),
            self.character.total_physical_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort(key=lambda x: -x)
        self.assertEqual(triple, [10, 8, 6])

    def test_random_ability(self):
        num = self.character.total_abilities()
        self.character.random_ability()
        self.assertEqual(self.character.total_abilities(), num + 1)

    def test_random_abilities(self):
        self.character.random_abilities()
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort(key=lambda x: -x)
        self.assertEqual(triple, [13, 9, 5])
        for _, value in self.character.get_abilities().items():
            self.assertLessEqual(value, 3)

    def test_random_specialty(self):
        self.character.stealth = 3
        self.assertFalse(self.character.random_specialty("stealth"))
        self.assertEqual(self.character.specialties.count(), 0)
        self.character.stealth = 4
        self.assertTrue(self.character.random_specialty("stealth"))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertTrue(self.character.random_specialty("stealth"))
        self.assertEqual(self.character.specialties.count(), 2)

    def test_random_specialties(self):
        self.character.science = 4
        self.character.athletics = 4
        self.character.alertness = 4
        self.assertFalse(self.character.has_specialties())
        self.character.random_specialties()
        self.assertTrue(self.character.has_specialties())

    def test_add_random_language(self):
        Language.objects.create(name="Test Language", frequency=1)
        self.character.add_random_language()
        self.assertGreater(self.character.languages.count(), 0)

    def test_random_derangement(self):
        Derangement.objects.create(name="Test Derangement")
        self.character.random_derangement()
        self.assertGreater(self.character.derangements.count(), 0)

    def test_random_background(self):
        self.character.random_background()
        self.assertGreater(self.character.total_backgrounds(), 0)

    def test_random_backgrounds(self):
        self.assertFalse(self.character.has_backgrounds())
        self.character.random_backgrounds()
        self.assertTrue(self.character.has_backgrounds())

    def test_random_birthdate(self):
        age = 25
        birthdate = self.character.random_birthdate(age)
        self.assertIsInstance(birthdate, date)

    def test_random_finishing_touches(self):
        self.character.random_finishing_touches()
        self.assertIsInstance(self.character.age, int)
        self.assertIsInstance(self.character.date_of_birth, date)
        self.assertIsInstance(self.character.height, str)
        self.assertIsInstance(self.character.weight, str)
        self.assertIsInstance(self.character.apparent_age, int)

    def test_random_history(self):
        self.character.random_history()
        self.assertIsInstance(self.character.childhood, str)
        self.assertIsInstance(self.character.history, str)
        self.assertIsInstance(self.character.goals, str)

    def test_random_freebies(self):
        self.assertEqual(self.character.freebies, 15)
        self.character.random_freebies()
        self.assertEqual(self.character.freebies, 0)

    def test_random_xp(self):
        self.character.xp = 100
        self.character.random_xp()
        self.assertLess(self.character.xp, 100)

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        self.assertFalse(self.character.has_archetypes())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_backgrounds())
        self.assertFalse(self.character.has_finishing_touches())
        self.assertFalse(self.character.has_history())
        self.character.random(freebies=0, xp=0)
        self.assertTrue(self.character.has_name())
        self.assertTrue(self.character.has_concept())
        self.assertTrue(self.character.has_archetypes())
        self.assertTrue(self.character.has_attributes())
        self.assertTrue(self.character.has_abilities())
        self.assertTrue(self.character.has_backgrounds())
        self.assertTrue(self.character.has_specialties())
        self.assertTrue(self.character.has_finishing_touches())
        self.assertTrue(self.character.has_history())
        self.assertEqual(self.character.freebies, 0)

    def test_random_freebies_attributes(self):
        self.character.freebies = 10
        self.character.random_freebies_attributes()
        self.assertEqual(self.character.freebies, 5)
        self.assertEqual(self.character.total_attributes(), 10)

    def test_random_freebies_abilities(self):
        self.character.freebies = 10
        self.character.random_freebies_abilities()
        self.assertEqual(self.character.freebies, 8)
        self.assertEqual(self.character.total_abilities(), 1)

    def test_random_freebies_backgrounds(self):
        self.character.freebies = 10
        self.character.random_freebies_background()
        self.assertEqual(self.character.freebies, 9)
        self.assertEqual(self.character.total_backgrounds(), 1)

    def test_random_freebies_willpower(self):
        self.character.freebies = 10
        num = self.character.willpower
        self.character.random_freebies_willpower()
        self.assertEqual(self.character.freebies, 9)
        self.assertEqual(self.character.willpower, num + 1)

    def test_random_freebies_meritflaw(self):
        self.character.freebies = 10
        MeritFlaw.objects.create(name="Test Merit/Flaw", ratings=[1, 2, 3])
        self.character.random_freebies_meritflaw()
        mf = MeritFlawRating.objects.filter(character=self.character).first().rating
        self.assertEqual(self.character.freebies, 10 - mf)
        self.assertGreater(self.character.merits_and_flaws.count(), 0)

    def test_random_xp_attributes(self):
        self.character.xp = 10
        self.character.random_xp_attributes()
        self.assertEqual(self.character.xp, 6)
        self.assertEqual(self.character.total_attributes(), 10)

    def test_random_xp_abilities(self):
        self.character.xp = 10
        self.character.random_xp_abilities()
        self.assertEqual(self.character.xp, 7)
        self.assertEqual(self.character.total_abilities(), 1)

    def test_random_xp_backgruond(self):
        self.character.xp = 10
        self.character.random_xp_background()
        self.assertEqual(self.character.xp, 5)
        self.assertEqual(self.character.total_backgrounds(), 1)

    def test_random_xp_willpower(self):
        self.character.xp = 10
        num = self.character.willpower
        self.character.random_xp_willpower()
        self.assertEqual(self.character.xp, 10 - num)
        self.assertEqual(self.character.willpower, num + 1)


class TestRandomGroup(TestCase):
    def setUp(self):
        self.group = Group.objects.create()
        for key in list(Human().get_abilities().keys()) + list(
            Human().get_attributes().keys()
        ):
            for i in range(5):
                WoDSpecialty.objects.create(
                    name=f"{key.title()} Specialty {i}", stat=key
                )

    def test_random_name(self):
        self.group.random_name()
        self.assertTrue(self.group.name.startswith("Random Group"))

    def test_random(self):
        self.group.random(
            num_chars=5, new_characters=True, random_names=True, freebies=15, xp=0
        )
        self.assertEqual(self.group.members.count(), 5)
        self.assertIsNotNone(self.group.leader)
        self.assertIn(self.group.leader, self.group.members.all())


class TestMeritFlaw(TestCase):
    def setUp(self):
        self.merit_flaw = MeritFlaw.objects.create(
            ratings=[1, 2, 3],
            human=True,
            kinfolk=False,
            garou=True,
            mage=False,
            changeling=True,
        )

    def test_save(self):
        self.merit_flaw.ratings = [1, 2, 3, 4]
        self.merit_flaw.save()
        self.assertEqual(self.merit_flaw.max_rating, 4)

    def test_booleans(self):
        self.assertEqual(self.merit_flaw.booleans(), "Human, Garou")


class TestCharacterIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/wod/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/characters/")
        self.assertTemplateUsed(response, "wod/characters/index.html")

    def test_index_content(self):
        player = User.objects.create_user(username="User1", password="12345")
        for i in range(10):
            Human.objects.create(name=f"Human {i}", owner=player)
        response = self.client.post("/wod/characters/")
        for i in range(10):
            self.assertContains(response, f"Human {i}")


class TestHumanDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.human = Human.objects.create(name="Test Human", owner=self.player)

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/human/detail.html")


class TestGenericCharacterDetailViews(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.character = Character.objects.create(
            name="Test Character", owner=self.player
        )
        self.human = Human.objects.create(name="Test Human", owner=self.player)
        self.werewolf = Werewolf.objects.create(name="Test Werewolf", owner=self.player)
        self.mage = Mage.objects.create(name="Test Mage", owner=self.player)

    def test_character_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/character/detail.html")
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/human/detail.html")
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/mage/detail.html")
        response = self.client.get(f"/wod/characters/{self.werewolf.id}/")
        self.assertTemplateUsed(
            response, "wod/characters/werewolf/werewolf/detail.html"
        )


class TestGroupDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.group = Group.objects.create(name="Test Group")

    def test_group_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/groups/{self.group.id}/")
        self.assertEqual(response.status_code, 200)

    def test_group_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/groups/{self.group.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/group/detail.html")


class TestGenericGroupDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.group = Group.objects.create(name="Group Test")
        self.cabal = Cabal.objects.create(name="Cabal Test")
        self.pack = Pack.objects.create(name="Pack Test")

    def test_generic_group_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/groups/{self.group.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/group/detail.html")
        response = self.client.get(f"/wod/characters/groups/{self.cabal.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/cabal/detail.html")
        response = self.client.get(f"/wod/characters/groups/{self.pack.id}/")
        self.assertTemplateUsed(response, "wod/characters/werewolf/pack/detail.html")
