from django.contrib.auth.models import User
from django.test import TestCase

from exalted.models.characters.mortals import (
    ExMerit,
    ExMortal,
    ExSpecialty,
    Intimacy,
    MeritRating,
)
from exalted.models.characters.utils import ABILITIES


# Create your tests here.
def ex_setup():
    for ability in ABILITIES:
        for i in range(10):
            ExSpecialty.objects.create(
                name=f"{ability.replace('_', ' ').title()} Specialty {i}",
                ability=ability,
            )
    for intimacy_type in ["tie", "principle"]:
        for strength in ["minor", "major", "defining"]:
            for is_negative in [True, False]:
                name = f"{strength.title()} {intimacy_type.title()}"
                if is_negative:
                    name = "Negative " + name
                Intimacy.objects.create(
                    name=name,
                    intimacy_type=intimacy_type,
                    strength=strength,
                    is_negative=is_negative,
                )
    for merit_type in ["innate", "purchased", "story"]:
        for i in range(1, 5):
            ExMerit.objects.create(
                name=f"{merit_type.title()} Merit {i}",
                merit_type=merit_type,
                ratings=[i, i + 1],
            )


class TestMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = ExMortal.objects.create(name="", owner=self.player)
        ex_setup()

    def test_absolute_url(self):
        self.assertEqual(
            self.character.get_absolute_url(),
            f"/exalted/characters/{self.character.id}/",
        )

    def test_has_name(self):
        self.character.name = ""
        self.assertFalse(self.character.has_name())
        self.character.name = "Test"
        self.assertTrue(self.character.has_name())

    def test_set_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.set_name("Test"))
        self.assertNotEqual(self.character.name, "")

    def test_has_concept(self):
        self.character.concept = ""
        self.assertFalse(self.character.has_concept())
        self.character.concept = "Test"
        self.assertTrue(self.character.has_concept())

    def test_set_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.set_concept("Test Concept"))
        self.assertEqual(self.character.concept, "Test Concept")

    def test_add_attribute(self):
        self.character.strength = 1
        self.assertTrue(self.character.add_attribute("strength"))
        self.assertEqual(self.character.strength, 2)
        self.character.strength = 5
        self.assertFalse(self.character.add_attribute("strength", maximum=5))
        self.assertEqual(self.character.strength, 5)
        self.assertTrue(self.character.add_attribute("strength", maximum=6))
        self.assertEqual(self.character.strength, 6)

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

    def test_has_attributes(self):
        self.assertFalse(self.character.has_attributes())
        self.character.strength = 3
        self.character.dexterity = 3
        self.character.stamina = 3
        self.character.intelligence = 3
        self.character.wits = 2
        self.character.perception = 2
        self.character.charisma = 2
        self.character.manipulation = 2
        self.character.appearance = 2
        self.assertTrue(self.character.has_attributes())
        self.character.perception = 3
        self.assertFalse(self.character.has_attributes())

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

    def test_total_attributes(self):
        total = self.character.total_attributes()
        self.assertEqual(total, 9)

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

    def test_add_ability(self):
        self.character.occult = 0
        self.assertTrue(self.character.add_ability("occult"))
        self.assertEqual(self.character.occult, 1)
        self.character.occult = 5
        self.assertFalse(self.character.add_ability("occult", maximum=5))
        self.assertEqual(self.character.occult, 5)
        self.assertTrue(self.character.add_ability("occult", maximum=6))
        self.assertEqual(self.character.occult, 6)

    def set_abilities(self):
        self.character.archery = 3
        self.character.melee = 2
        self.character.awareness = 1
        self.character.dodge = 1
        self.character.craft = 1
        self.character.presence = 2
        self.character.martial_arts = 3
        self.character.linguistics = 3
        self.character.lore = 2
        self.character.bureaucracy = 2
        self.character.socialize = 3
        self.character.sail = 1
        self.character.ride = 1
        self.character.war = 3

    def test_martial_arts_requirement(self):
        self.assertFalse(self.character.add_ability("martial_arts"))
        self.assertTrue(self.character.add_ability("brawl"))
        self.assertTrue(
            self.character.add_merit(
                ExMerit.objects.create(name="Martial Artist", ratings=[4])
            )
        )
        self.assertTrue(self.character.add_ability("martial_arts"))

    def test_get_abilities(self):
        self.assertEqual(
            self.character.get_abilities(),
            {
                "archery": 0,
                "athletics": 0,
                "awareness": 0,
                "brawl": 0,
                "bureaucracy": 0,
                "craft": 0,
                "dodge": 0,
                "integrity": 0,
                "investigation": 0,
                "larceny": 0,
                "linguistics": 0,
                "lore": 0,
                "martial_arts": 0,
                "medicine": 0,
                "melee": 0,
                "occult": 0,
                "performance": 0,
                "presence": 0,
                "resistance": 0,
                "ride": 0,
                "sail": 0,
                "socialize": 0,
                "stealth": 0,
                "survival": 0,
                "thrown": 0,
                "war": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_abilities(),
            {
                "archery": 3,
                "athletics": 0,
                "awareness": 1,
                "brawl": 0,
                "bureaucracy": 2,
                "craft": 1,
                "dodge": 1,
                "integrity": 0,
                "investigation": 0,
                "larceny": 0,
                "linguistics": 3,
                "lore": 2,
                "martial_arts": 3,
                "medicine": 0,
                "melee": 2,
                "occult": 0,
                "performance": 0,
                "presence": 2,
                "resistance": 0,
                "ride": 1,
                "sail": 1,
                "socialize": 3,
                "stealth": 0,
                "survival": 0,
                "thrown": 0,
                "war": 3,
            },
        )

    def test_has_abilities(self):
        self.assertFalse(self.character.has_abilities())
        self.set_abilities()
        self.assertTrue(self.character.has_abilities())

    def test_filter_abilities(self):
        self.assertEqual(len(self.character.filter_abilities()), 26)
        self.assertEqual(len(self.character.filter_abilities(maximum=1)), 26)
        self.assertEqual(len(self.character.filter_abilities(minimum=1)), 0)
        self.set_abilities()
        self.assertEqual(len(self.character.filter_abilities(minimum=0, maximum=5)), 26)
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=5)), 14)
        self.assertEqual(len(self.character.filter_abilities(minimum=2, maximum=5)), 9)
        self.assertEqual(len(self.character.filter_abilities(minimum=3, maximum=5)), 5)
        self.assertEqual(len(self.character.filter_abilities(minimum=4, maximum=5)), 0)
        self.assertEqual(len(self.character.filter_abilities(minimum=5, maximum=5)), 0)
        self.assertEqual(len(self.character.filter_abilities(minimum=0, maximum=4)), 26)
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=4)), 14)
        self.assertEqual(len(self.character.filter_abilities(minimum=2, maximum=4)), 9)
        self.assertEqual(len(self.character.filter_abilities(minimum=3, maximum=4)), 5)
        self.assertEqual(len(self.character.filter_abilities(minimum=4, maximum=4)), 0)
        self.assertEqual(len(self.character.filter_abilities(minimum=0, maximum=3)), 26)
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=3)), 14)
        self.assertEqual(len(self.character.filter_abilities(minimum=2, maximum=3)), 9)
        self.assertEqual(len(self.character.filter_abilities(minimum=3, maximum=3)), 5)
        self.assertEqual(len(self.character.filter_abilities(minimum=0, maximum=2)), 21)
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=2)), 9)
        self.assertEqual(len(self.character.filter_abilities(minimum=2, maximum=2)), 4)
        self.assertEqual(len(self.character.filter_abilities(minimum=0, maximum=1)), 17)
        self.assertEqual(len(self.character.filter_abilities(minimum=1, maximum=1)), 5)
        self.assertEqual(len(self.character.filter_abilities(minimum=0, maximum=0)), 12)

    def test_total_abilities(self):
        total = self.character.total_abilities()
        self.assertEqual(total, 0)
        self.character.random_ability()
        self.assertEqual(self.character.total_abilities(), 1)

    def test_ability_types(self):
        types = self.character.ability_types()
        self.assertEqual(len(types), 4)

    def test_get_combat_abilities(self):
        abilities = self.character.get_combat_abilities()
        self.assertEqual(len(abilities), 12)

    def test_total_combat_abilities(self):
        total = self.character.total_combat_abilities()
        self.assertEqual(total, 0)

    def test_get_crafting_abilities(self):
        abilities = self.character.get_crafting_abilities()
        self.assertEqual(len(abilities), 3)

    def test_total_crafting_abilities(self):
        total = self.character.total_crafting_abilities()
        self.assertEqual(total, 0)

    def test_get_social_abilities(self):
        abilities = self.character.get_social_abilities()
        self.assertEqual(len(abilities), 5)

    def test_total_social_abilities(self):
        total = self.character.total_social_abilities()
        self.assertEqual(total, 0)

    def test_get_sorcery_abilities(self):
        abilities = self.character.get_sorcery_abilities()
        self.assertEqual(len(abilities), 1)

    def test_total_sorcery_abilities(self):
        total = self.character.total_sorcery_abilities()
        self.assertEqual(total, 0)

    def test_add_specialty(self):
        num = self.character.specialties.count()
        spec = ExSpecialty.objects.filter(ability="occult").first()
        self.assertFalse(self.character.add_specialty(spec))
        self.assertEqual(self.character.specialties.count(), num)
        self.character.occult = 1
        self.assertTrue(self.character.add_specialty(spec))
        self.assertEqual(self.character.specialties.count(), num + 1)

    def test_has_specialties(self):
        self.assertFalse(self.character.has_specialties())
        for ability in ["occult", "war", "melee", "archery"]:
            setattr(self.character, ability, 1)
            self.assertTrue(
                self.character.add_specialty(
                    ExSpecialty.objects.filter(ability=ability).first()
                )
            )
        self.assertTrue(self.character.has_specialties())

    def test_filter_specialties(self):
        self.assertEqual(len(self.character.filter_specialties()), 0)
        self.set_abilities()
        self.assertEqual(len(self.character.filter_specialties()), 140)
        self.character.add_specialty(ExSpecialty.objects.filter(ability="war").first())
        self.assertEqual(len(self.character.filter_specialties()), 139)

    def test_add_merit(self):
        m = ExMerit.objects.create(
            name="Merit 1", ratings=[1, 2, 4], merit_type="innate"
        )
        self.assertNotIn(m, self.character.merits.all())
        self.assertTrue(self.character.add_merit(m))
        self.assertIn(m, self.character.merits.all())
        self.assertEqual(self.character.merit_rating("Merit 1"), 1)
        self.assertTrue(self.character.add_merit(m))
        self.assertEqual(self.character.merit_rating("Merit 1"), 2)
        self.assertTrue(self.character.add_merit(m))
        self.assertEqual(self.character.merit_rating("Merit 1"), 4)
        self.assertFalse(self.character.add_merit(m))
        self.assertEqual(self.character.merit_rating("Merit 1"), 4)

    def test_total_merits(self):
        total = self.character.total_merits()
        self.assertEqual(total, 0)
        self.character.add_merit(ExMerit.objects.create(name="", ratings=[1, 2]))

    def test_merit_rating(self):
        merit = ExMerit.objects.create(name="Test Merit", ratings=[1, 2, 3])
        MeritRating.objects.create(character=self.character, merit=merit, rating=3)
        rating = self.character.merit_rating("Test Merit")
        self.assertEqual(rating, 3)

    def test_has_merits(self):
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(ExMerit.objects.get(name="Story Merit 3"))
        self.character.add_merit(ExMerit.objects.get(name="Innate Merit 4"))
        self.assertTrue(self.character.has_merits())

    def test_filter_merits(self):
        merit_list = self.character.filter_merits(dots=3)
        self.assertEqual(len(merit_list), 9)
        self.character.add_merit(merit_list[0])
        self.assertEqual(len(self.character.filter_merits(dots=3)), 9)
        self.character.add_merit(merit_list[0])
        self.assertEqual(len(self.character.filter_merits(dots=3)), 8)

    def test_has_intimacies(self):
        self.assertFalse(self.character.has_intimacies())
        self.character.add_intimacy(Intimacy.objects.get(name="Defining Tie"))
        self.assertFalse(self.character.has_intimacies())
        self.character.add_intimacy(Intimacy.objects.get(name="Major Tie"))
        self.assertFalse(self.character.has_intimacies())
        self.character.add_intimacy(Intimacy.objects.get(name="Defining Principle"))
        self.assertFalse(self.character.has_intimacies())
        self.character.add_intimacy(
            Intimacy.objects.get(name="Negative Minor Principle")
        )
        self.assertTrue(self.character.has_intimacies())

    def test_add_intimacy(self):
        i = Intimacy.objects.first()
        num = self.character.intimacies.count()
        self.assertTrue(self.character.add_intimacy(i))
        self.assertEqual(self.character.intimacies.count(), num + 1)

    def test_bonus_cost(self):
        self.assertEqual(self.character.bonus_cost("primary attribute"), 4)
        self.assertEqual(self.character.bonus_cost("secondary attribute"), 4)
        self.assertEqual(self.character.bonus_cost("tertiary attribute"), 3)
        self.assertEqual(self.character.bonus_cost("ability"), 2)
        self.assertEqual(self.character.bonus_cost("specialty"), 1)
        self.assertEqual(self.character.bonus_cost("merit"), 1)
        self.assertEqual(self.character.bonus_cost("willpower"), 2)

    def test_spend_bonus_points(self):
        self.character.tertiary = self.character.get_physical_attributes
        self.assertEqual(self.character.bonus_points, 21)
        self.assertTrue(self.character.spend_bonus_points("wits"))
        self.assertEqual(self.character.bonus_points, 17)
        self.assertTrue(self.character.spend_bonus_points("dexterity"))
        self.assertEqual(self.character.bonus_points, 14)
        self.assertTrue(self.character.spend_bonus_points("occult"))
        self.assertEqual(self.character.bonus_points, 12)
        self.assertTrue(self.character.spend_bonus_points("Occult Specialty 0"))
        self.assertEqual(self.character.bonus_points, 11)
        self.assertTrue(self.character.spend_bonus_points("Innate Merit 1"))
        self.assertEqual(self.character.bonus_points, 10)
        self.assertTrue(self.character.spend_bonus_points("willpower"))
        self.assertEqual(self.character.bonus_points, 8)

    def test_random_bonus_functions(self):
        functions = self.character.random_bonus_functions()
        self.assertEqual(
            set(functions.keys()),
            {"attribute", "ability", "specialty", "merit", "willpower"},
        )

    def test_has_finishing_touches(self):
        self.assertFalse(self.character.has_finishing_touches())
        self.character.willpower = 3
        self.character.health_levels = 7
        self.character.essence = 0
        self.assertTrue(self.character.has_finishing_touches())

    def test_add_willpower(self):
        initial_willpower = self.character.willpower
        self.character.add_willpower()
        new_willpower = self.character.willpower
        self.assertEqual(new_willpower, initial_willpower + 1)

    def test_apply_finishing_touches(self):
        self.assertFalse(self.character.has_finishing_touches())
        self.assertTrue(self.character.apply_finishing_touches())
        self.assertTrue(self.character.has_finishing_touches())

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("new ability"), 3)
        self.assertEqual(self.character.xp_cost("ability"), 2)
        self.assertEqual(self.character.xp_cost("specialty"), 3)
        self.assertEqual(self.character.xp_cost("merit"), 3)
        self.assertEqual(self.character.xp_cost("willpower"), 8)

    def test_spend_xp(self):
        self.character.xp = 100
        self.assertTrue(self.character.spend_xp("strength"))
        self.assertEqual(self.character.xp, 96)
        self.assertTrue(self.character.spend_xp("occult"))
        self.assertEqual(self.character.xp, 93)
        self.assertTrue(self.character.spend_xp("occult"))
        self.assertEqual(self.character.xp, 91)
        self.assertTrue(self.character.spend_xp("Occult Specialty 0"))
        self.assertEqual(self.character.xp, 88)
        self.assertTrue(self.character.spend_xp("Purchased Merit 1"))
        self.assertEqual(self.character.xp, 85)
        self.assertTrue(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 77)

    def test_random_xp_functions(self):
        functions = self.character.random_xp_functions()
        self.assertEqual(
            set(functions.keys()),
            {"attribute", "ability", "specialty", "merit", "willpower"},
        )

    def test_add_to_spend(self):
        self.character.add_to_spend("test_trait", 1, 5)
        self.assertIn("Test Trait 1 (5 XP)", self.character.spent_xp)


class TestRandomMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = ExMortal.objects.create(
            name="", owner=self.player, xp=50, willpower=1
        )
        ex_setup()

    def test_random_name(self):
        self.assertFalse(self.character.has_name())
        self.character.random_name()
        self.assertTrue(self.character.has_name())

    def test_random_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.random_concept()
        self.assertTrue(self.character.has_concept())

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
        self.assertEqual(triple, [9, 7, 6])

    def test_random_ability(self):
        num = self.character.total_abilities()
        self.character.random_ability()
        self.assertEqual(self.character.total_abilities(), num + 1)

    def test_random_abilities(self):
        self.assertFalse(self.character.has_abilities())
        self.character.random_abilities()
        self.assertTrue(self.character.has_abilities())

    def test_random_specialty(self):
        self.character.war = 1
        self.character.random_specialty()
        self.assertEqual(self.character.specialties.count(), 1)

    def test_random_specialties(self):
        self.character.archery = 3
        self.character.melee = 2
        self.character.awareness = 1
        self.character.dodge = 1
        self.character.craft = 1
        self.character.presence = 2
        self.character.martial_arts = 3
        self.character.linguistics = 3
        self.character.lore = 2
        self.character.bureaucracy = 2
        self.character.socialize = 3
        self.character.sail = 1
        self.character.ride = 1
        self.character.war = 3
        self.assertFalse(self.character.has_specialties())
        self.character.random_specialties()
        self.assertTrue(self.character.has_specialties())

    def test_random_merit(self):
        num = self.character.merits.count()
        self.character.random_merit()
        self.assertEqual(self.character.merits.count(), num + 1)

    def test_random_merits(self):
        self.assertFalse(self.character.has_merits())
        self.character.random_merits()
        self.assertTrue(self.character.has_merits())

    def test_random_intimacy(self):
        num = self.character.intimacies.count()
        self.character.random_intimacy()
        self.assertEqual(self.character.intimacies.count(), num + 1)

    def test_random_intimacies(self):
        self.assertFalse(self.character.has_intimacies())
        self.character.random_intimacies()
        self.assertTrue(self.character.has_intimacies())

    def test_random_spend_bonus_points(self):
        self.character.tertiary = self.character.get_physical_attributes
        self.character.random_abilities()
        self.assertEqual(self.character.bonus_points, 21)
        self.character.random_spend_bonus_points()
        self.assertEqual(self.character.bonus_points, 0)

    def test_random_spend_xp(self):
        self.character.xp = 15
        self.character.occult = 1
        self.character.war = 1
        self.character.awareness = 1
        self.character.random_spend_xp()
        self.assertLessEqual(self.character.xp, 1)

    def test_random_bonus_attribute(self):
        initial_bonus_points = self.character.bonus_points
        self.character.random_bonus_attribute()
        self.assertTrue(self.character.bonus_points < initial_bonus_points)

    def test_random_bonus_ability(self):
        initial_bonus_points = self.character.bonus_points
        self.character.random_bonus_ability()
        self.assertTrue(self.character.bonus_points < initial_bonus_points)

    def test_random_bonus_specialty(self):
        self.character.occult = 1
        specialty = ExSpecialty.objects.create(name="Test Specialty", ability="occult")
        initial_bonus_points = self.character.bonus_points
        self.character.random_bonus_specialty()
        self.assertTrue(self.character.bonus_points < initial_bonus_points)

    def test_random_bonus_merit(self):
        merit = ExMerit.objects.create(name="Test Merit", ratings=[1, 2, 3])
        initial_bonus_points = self.character.bonus_points
        self.character.random_bonus_merit()
        self.assertTrue(self.character.bonus_points < initial_bonus_points)

    def test_random_bonus_willpower(self):
        initial_bonus_points = self.character.bonus_points
        initial_willpower = self.character.willpower
        self.character.random_bonus_willpower()
        self.assertTrue(self.character.bonus_points < initial_bonus_points)
        self.assertTrue(self.character.willpower > initial_willpower)

    def test_random_xp_attribute(self):
        initial_xp = self.character.xp
        self.character.random_xp_attribute()
        self.assertTrue(self.character.xp < initial_xp)

    def test_random_xp_ability(self):
        initial_xp = self.character.xp
        self.character.random_xp_ability()
        self.assertTrue(self.character.xp < initial_xp)

    def test_random_xp_specialty(self):
        self.character.occult = 1
        specialty = ExSpecialty.objects.create(name="Test Specialty", ability="occult")
        initial_xp = self.character.xp
        self.character.random_xp_specialty()
        self.assertTrue(self.character.xp < initial_xp)

    def test_random_xp_merit(self):
        merit = ExMerit.objects.create(name="Test Merit", ratings=[1, 2, 3])
        initial_xp = self.character.xp
        self.character.random_xp_merit()
        self.assertTrue(self.character.xp < initial_xp)

    def test_random_xp_willpower(self):
        initial_xp = self.character.xp
        initial_willpower = self.character.willpower
        self.assertTrue(self.character.random_xp_willpower())
        self.assertTrue(self.character.xp < initial_xp)
        self.assertTrue(self.character.willpower > initial_willpower)

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_specialties())
        self.assertFalse(self.character.has_merits())
        self.assertFalse(self.character.has_intimacies())
        self.assertEqual(self.character.bonus_points, 21)
        self.assertFalse(self.character.has_finishing_touches())
        self.character.random(xp=0, bonus_points=0)
        self.assertTrue(self.character.has_name())
        self.assertTrue(self.character.has_concept())
        self.assertTrue(self.character.has_attributes())
        self.assertTrue(self.character.has_abilities())
        self.assertTrue(self.character.has_specialties())
        self.assertTrue(self.character.has_merits())
        self.assertTrue(self.character.has_intimacies())
        self.assertEqual(self.character.bonus_points, 0)
        self.assertTrue(self.character.has_finishing_touches())


class TestExMerit(TestCase):
    def setUp(self):
        self.merit = ExMerit.objects.create(
            name="Test Merit",
            description="Test Merit Description",
            merit_type="innate",
            ratings=[1, 2, 3],
            merit_class="standard",
        )

    def test_save(self):
        self.assertEqual(self.merit.max_rating, 3)

    def test_prereq_satisfied(self):
        character = ExMortal.objects.create(name="Test Character",)
        character.strength = 3
        character.athletics = 2

        prereq1 = ("strength", 4)
        prereq2 = ("athletics", 3)
        prereq3 = ("Test Merit", 2)

        self.assertFalse(self.merit.prereq_satisfied(prereq1, character))
        self.assertFalse(self.merit.prereq_satisfied(prereq2, character))
        self.assertFalse(self.merit.prereq_satisfied(prereq3, character))

        character.strength = 5
        character.athletics = 3
        character.add_merit(self.merit)
        character.add_merit(self.merit)
        character.add_merit(self.merit)

        self.assertTrue(self.merit.prereq_satisfied(prereq1, character))
        self.assertTrue(self.merit.prereq_satisfied(prereq2, character))
        self.assertTrue(self.merit.prereq_satisfied(prereq3, character))


class TestCharacterIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/exalted/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/exalted/characters/")
        self.assertTemplateUsed(response, "exalted/characters/index.html")

    def test_index_content(self):
        player = User.objects.create_user(username="User1", password="12345")
        for i in range(10):
            ExMortal.objects.create(name=f"Mortal {i}", owner=player)
        response = self.client.post("/exalted/characters/")
        for i in range(10):
            self.assertContains(response, f"Mortal {i}")


class TestMortalDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.human = ExMortal.objects.create(name="Test Mortal", owner=self.player)

    def test_mortal_detail_view_status_code(self):
        response = self.client.get(f"/exalted/characters/{self.human.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mortal_detail_view_template(self):
        response = self.client.get(f"/exalted/characters/{self.human.id}/")
        self.assertTemplateUsed(
            response, "exalted/characters/mortal/mortal/detail.html"
        )


class TestGenericCharacterDetailViews(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.mortal = ExMortal.objects.create(name="Test Mortal", owner=self.player)

    def test_character_detail_view_templates(self):
        response = self.client.get(f"/exalted/characters/{self.mortal.id}/")
        self.assertTemplateUsed(
            response, "exalted/characters/mortal/mortal/detail.html"
        )
