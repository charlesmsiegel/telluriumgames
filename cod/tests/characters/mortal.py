from django.contrib.auth.models import User
from django.test import TestCase

from cod.models.characters.mage import Mage
from cod.models.characters.mortal import (
    CoDMerit,
    CoDSpecialty,
    Condition,
    MeritRating,
    Mortal,
)

NUM_STATUSES = 7

# Create your tests here.
class TestMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="", owner=self.player)

    def test_set_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.set_name("Test Name"))
        self.assertEqual(self.character.name, "Test Name")

    def test_has_name(self):
        self.character.name = ""
        self.assertFalse(self.character.has_name())
        self.character.name = "Test"
        self.assertTrue(self.character.has_name())

    def test_add_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.add_concept("Test Concept"))
        self.assertEqual(self.character.concept, "Test Concept")

    def test_has_concept(self):
        self.character.concept = ""
        self.assertFalse(self.character.has_concept())
        self.character.concept = "Test"
        self.assertTrue(self.character.has_concept())

    def test_add_virtue(self):
        self.assertEqual(self.character.virtue, "")
        self.assertTrue(self.character.add_virtue("Virtue 1"))
        self.assertEqual(self.character.virtue, "Virtue 1")
        self.assertTrue(self.character.add_virtue("Virtue 2"))
        self.assertEqual(self.character.virtue, "Virtue 1, Virtue 2")
        self.assertFalse(self.character.add_virtue("Virtue 1"))

    def test_filter_virtue(self):
        test_virtues = ["Virtue 1", "Virtue 2", "Virtue 3"]
        self.character.virtue = "Virtue 1"
        self.assertEqual(
            self.character.filter_virtues(virtue_list=test_virtues),
            ["Virtue 2", "Virtue 3"],
        )
        self.character.virtue = "Virtue 1, Virtue 2"
        self.assertEqual(
            self.character.filter_virtues(virtue_list=test_virtues), ["Virtue 3"]
        )

    def test_has_virtue(self):
        self.character.virtue = ""
        self.assertFalse(self.character.has_virtue())
        self.character.virtue = "Test"
        self.assertTrue(self.character.has_virtue())

    def test_add_vice(self):
        self.assertEqual(self.character.vice, "")
        self.assertTrue(self.character.add_vice("Vice 1"))
        self.assertEqual(self.character.vice, "Vice 1")
        self.assertTrue(self.character.add_vice("Vice 2"))
        self.assertEqual(self.character.vice, "Vice 1, Vice 2")
        self.assertFalse(self.character.add_vice("Vice 1"))

    def test_filter_vice(self):
        test_vices = ["Vice 1", "Vice 2", "Vice 3"]
        self.character.vice = "Vice 1"
        self.assertEqual(
            self.character.filter_vices(vice_list=test_vices), ["Vice 2", "Vice 3"]
        )
        self.character.vice = "Vice 1, Vice 2"
        self.assertEqual(self.character.filter_vices(vice_list=test_vices), ["Vice 3"])

    def test_has_vice(self):
        self.character.vice = ""
        self.assertFalse(self.character.has_vice())
        self.character.vice = "Test"
        self.assertTrue(self.character.has_vice())

    def test_has_aspirations(self):
        self.fail()

    def test_add_short_term_aspirations(self):
        self.fail()

    def test_add_long_term_aspiration(self):
        self.fail()

    def test_add_attribute(self):
        self.character.strength = 1
        self.assertTrue(self.character.add_attribute("strength"))
        self.assertEqual(self.character.strength, 2)
        self.character.strength = 5
        self.assertFalse(self.character.add_attribute("strength", maximum=5))
        self.assertEqual(self.character.strength, 5)
        self.assertTrue(self.character.add_attribute("strength", maximum=6))
        self.assertEqual(self.character.strength, 6)

    def test_get_mental_attributes(self):
        self.fail()

    def test_get_physical_attributes(self):
        self.fail()

    def test_get_social_attributes(self):
        self.fail()

    def test_get_attributes(self):
        self.fail()

    def test_total_physical_attributes(self):
        self.fail()

    def test_total_mental_attributes(self):
        self.fail()

    def test_total_social_attributes(self):
        self.fail()

    def test_total_attributes(self):
        self.fail()

    def test_filter_attributes(self):
        self.character.strength = 5
        self.assertEqual(
            self.character.filter_attributes(maximum=4),
            {
                "dexterity": 1,
                "stamina": 1,
                "intelligence": 1,
                "wits": 1,
                "composure": 1,
                "resolve": 1,
                "manipulation": 1,
                "presence": 1,
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
                "composure": 1,
                "resolve": 1,
                "manipulation": 1,
                "presence": 1,
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
        self.assertNotEqual(triple, [6, 7, 8])
        self.character.strength = 3
        self.character.dexterity = 3
        self.character.stamina = 2
        self.character.intelligence = 3
        self.character.wits = 2
        self.character.resolve = 2
        self.character.presence = 2
        self.character.manipulation = 2
        self.character.composure = 2
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertEqual(triple, [6, 7, 8])
        self.character.composure = 3
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 7, 8])

    def test_add_skill(self):
        self.character.occult = 0
        self.assertTrue(self.character.add_attribute("occult"))
        self.assertEqual(self.character.occult, 1)
        self.character.occult = 5
        self.assertFalse(self.character.add_attribute("occult", maximum=5))
        self.assertEqual(self.character.occult, 5)
        self.assertTrue(self.character.add_attribute("occult", maximum=6))
        self.assertEqual(self.character.occult, 6)

    def test_filter_skills(self):
        self.character.occult = 5
        self.assertEqual(
            self.character.filter_skills(maximum=4),
            {
                "academics": 0,
                "computer": 0,
                "crafts": 0,
                "investigation": 0,
                "medicine": 0,
                "politics": 0,
                "science": 0,
                "athletics": 0,
                "brawl": 0,
                "drive": 0,
                "firearms": 0,
                "larceny": 0,
                "stealth": 0,
                "survival": 0,
                "weaponry": 0,
                "animal_ken": 0,
                "empathy": 0,
                "expression": 0,
                "intimidation": 0,
                "persuasion": 0,
                "socialize": 0,
                "streetwise": 0,
                "subterfuge": 0,
            },
        )
        self.assertEqual(
            self.character.filter_skills(maximum=6),
            {
                "academics": 0,
                "computer": 0,
                "crafts": 0,
                "investigation": 0,
                "medicine": 0,
                "politics": 0,
                "occult": 5,
                "science": 0,
                "athletics": 0,
                "brawl": 0,
                "drive": 0,
                "firearms": 0,
                "larceny": 0,
                "stealth": 0,
                "survival": 0,
                "weaponry": 0,
                "animal_ken": 0,
                "empathy": 0,
                "expression": 0,
                "intimidation": 0,
                "persuasion": 0,
                "socialize": 0,
                "streetwise": 0,
                "subterfuge": 0,
            },
        )
        self.character.occult = 4
        self.assertEqual(self.character.filter_skills(minimum=3), {"occult": 4})
        self.assertEqual(
            self.character.filter_skills(minimum=3, maximum=5), {"occult": 4}
        )
        self.assertEqual(self.character.filter_skills(minimum=5, maximum=6), {})

    def test_has_skills(self):
        triple = [
            self.character.total_physical_skills(),
            self.character.total_mental_skills(),
            self.character.total_social_skills(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [4, 7, 11])
        self.set_skills()
        triple = [
            self.character.total_physical_skills(),
            self.character.total_mental_skills(),
            self.character.total_social_skills(),
        ]
        triple.sort()
        self.assertEqual(triple, [4, 7, 11])
        self.character.subterfuge = 1
        triple = [
            self.character.total_physical_skills(),
            self.character.total_mental_skills(),
            self.character.total_social_skills(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [4, 7, 11])

    def test_get_mental_skills(self):
        self.fail()

    def test_get_physical_skills(self):
        self.fail()

    def test_get_social_skills(self):
        self.fail()

    def test_get_skills(self):
        self.fail()

    def test_total_physical_skills(self):
        self.fail()

    def test_total_mental_skills(self):
        self.fail()

    def test_total_social_skills(self):
        self.fail()

    def test_total_skills(self):
        self.fail()

    def test_add_specialty(self):
        specialty = CoDSpecialty.objects.create(name="Biology", skill="science")
        specialty2 = CoDSpecialty.objects.create(name="Physics", skill="science")
        self.assertTrue(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertFalse(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertTrue(self.character.add_specialty(specialty2))
        self.assertEqual(self.character.specialties.count(), 2)

    def test_filter_specialties(self):
        specialty = CoDSpecialty.objects.create(name="Biology", skill="science")
        CoDSpecialty.objects.create(name="Physics", skill="science")
        CoDSpecialty.objects.create(name="Dogs", skill="animal_ken")
        CoDSpecialty.objects.create(name="Guns", skill="firearms")
        self.character.add_specialty(specialty)
        self.assertEqual(len(self.character.filter_specialties()), 3)
        self.assertEqual(len(self.character.filter_specialties(skill="firearms")), 1)

    def set_skills(self):
        self.character.academics = 1
        self.character.computer = 1
        self.character.crafts = 1
        self.character.investigation = 1
        self.character.medicine = 0
        self.character.politics = 0
        self.character.occult = 0
        self.character.science = 0
        self.character.athletics = 2
        self.character.brawl = 2
        self.character.drive = 2
        self.character.firearms = 1
        self.character.larceny = 0
        self.character.stealth = 0
        self.character.survival = 0
        self.character.weaponry = 0
        self.character.animal_ken = 3
        self.character.empathy = 3
        self.character.expression = 3
        self.character.intimidation = 2
        self.character.persuasion = 0
        self.character.socialize = 0
        self.character.streetwise = 0
        self.character.subterfuge = 0

    def test_has_specialties(self):
        s1 = CoDSpecialty.objects.create(name="Literature", skill="academics")
        s2 = CoDSpecialty.objects.create(name="Dogs", skill="animal_ken")
        s3 = CoDSpecialty.objects.create(name="Poetry", skill="expression")
        CoDSpecialty.objects.create(name="Reading People", skill="empathy")
        CoDSpecialty.objects.create(name="Directions", skill="streetwise")
        self.set_skills()
        self.assertFalse(self.character.has_specialties())
        self.character.add_specialty(s1)
        self.assertFalse(self.character.has_specialties())
        self.character.add_specialty(s2)
        self.assertFalse(self.character.has_specialties())
        self.character.add_specialty(s3)
        self.assertTrue(self.character.has_specialties())

    def test_add_merit(self):
        m = CoDMerit.objects.create(
            name="Merit 1", ratings=[1, 2, 4], merit_type="Physical"
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
        m2 = CoDMerit.objects.create(
            name="Merit with Details",
            requires_detail=True,
            possible_details=["Detail 1", "Detail 2"],
            ratings=[1, 2],
            merit_type="Physical",
        )
        with self.assertRaises(Exception):
            self.character.add_merit(m2)
        self.assertTrue(self.character.add_merit(m2, detail="Detail 1"))
        self.assertEqual(
            self.character.merit_rating("Merit with Details", detail="Detail 1"), 1
        )
        self.assertTrue(self.character.add_merit(m2, detail="Detail 2"))
        self.assertEqual(
            self.character.merit_rating("Merit with Details", detail="Detail 2"), 1
        )
        self.assertTrue(self.character.add_merit(m2, detail="Detail 1"))
        self.assertEqual(
            self.character.merit_rating("Merit with Details", detail="Detail 1"), 2
        )

    def test_remove_merit(self):
        self.fail()

    def test_merit_rating(self):
        self.fail()

    def test_filter_merits(self):
        m1 = CoDMerit.objects.create(
            name="Merit 1", ratings=[1, 2], merit_type="Physical"
        )
        m2 = CoDMerit.objects.create(
            name="Merit 2", ratings=[2, 3], merit_type="Mental"
        )
        m3 = CoDMerit.objects.create(
            name="Merit 3", ratings=[3, 4], merit_type="Social", is_style=True
        )
        m4 = CoDMerit.objects.create(
            name="Merit 4", ratings=[1, 4], merit_type="Fighting"
        )
        m5 = CoDMerit.objects.create(
            name="Merit 5", ratings=[2, 4], merit_type="Supernatural"
        )
        m6 = CoDMerit.objects.create(
            name="Merit 6", ratings=[3, 4], merit_type="Physical"
        )
        CoDMerit.objects.create(name="Merit 7", ratings=[3, 4], merit_type="Mage")
        merit_list = self.character.filter_merits(
            dots=3
        )  # Gives all merits with cost <= dots that character could add
        merit_set = set(merit_list)
        correct_set = {m1, m2, m3, m4, m5, m6}
        self.assertEqual(merit_set, correct_set)
        self.character.add_merit(m3)
        self.assertEqual(
            set(self.character.filter_merits(dots=3)), {m1, m2, m4, m5, m6}
        )
        self.character.add_merit(m2)
        self.assertEqual(
            set(self.character.filter_merits(dots=3)), {m1, m2, m4, m5, m6}
        )

    def test_has_merits(self):
        m1 = CoDMerit.objects.create(
            name="Merit 1", ratings=[1, 2], merit_type="Physical"
        )
        m2 = CoDMerit.objects.create(
            name="Merit 2", ratings=[2, 3], merit_type="Physical"
        )
        m3 = CoDMerit.objects.create(
            name="Merit 3", ratings=[3, 4], merit_type="Physical"
        )
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m1)
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m1)
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m2)
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m3)
        self.assertTrue(self.character.has_merits())

    def test_total_merits(self):
        self.fail()

    def test_assign_advantages(self):
        self.character.resolve = 2
        self.character.composure = 1
        self.character.assign_advantages()
        self.assertEqual(self.character.willpower, 3)
        self.character.composure = 3
        self.character.assign_advantages()
        self.assertEqual(self.character.willpower, 5)
        self.character.size = 5
        self.character.stamina = 1
        self.character.assign_advantages()
        self.assertEqual(self.character.health, 6)
        self.character.stamina = 2
        self.character.assign_advantages()
        self.assertEqual(self.character.health, 7)
        self.character.strength = 1
        self.character.dexterity = 1
        self.character.assign_advantages()
        self.assertEqual(self.character.speed, 7)
        self.character.strength = 2
        self.character.dexterity = 2
        self.character.assign_advantages()
        self.assertEqual(self.character.speed, 9)
        self.character.dexterity = 2
        self.character.composure = 2
        self.character.assign_advantages()
        self.assertEqual(self.character.initiative_modifier, 4)
        self.character.dexterity = 5
        self.character.composure = 2
        self.character.assign_advantages()
        self.assertEqual(self.character.initiative_modifier, 7)
        self.character.wits = 1
        self.character.dexterity = 3
        self.character.assign_advantages()
        self.assertEqual(self.character.defense, 1)
        self.character.athletics = 5
        self.character.assign_advantages()
        self.assertEqual(self.character.defense, 6)

    def test_giant_merit(self):
        giant = CoDMerit.objects.create(
            name="Giant", ratings=[1], merit_type="Physical"
        )
        self.character.stamina = 2
        self.character.assign_advantages()
        self.assertEqual(self.character.size, 5)
        self.assertEqual(self.character.health, 7)
        self.character.add_merit(giant)
        self.character.assign_advantages()
        self.assertEqual(self.character.size, 6)
        self.assertEqual(self.character.health, 8)
        small_framed = CoDMerit.objects.create(
            name="Small-Framed", ratings=[1], merit_type="Physical"
        )
        self.assertFalse(self.character.add_merit(small_framed))
        self.assertEqual(self.character.merits.count(), 1)

    def test_fast_reflexes_merit(self):
        fast_reflexes = CoDMerit.objects.create(
            name="Fast Reflexes", ratings=[1, 2, 3], merit_type="Physical"
        )
        self.character.dexterity = 2
        self.character.composure = 3
        self.character.assign_advantages()
        self.assertEqual(self.character.initiative_modifier, 5)
        self.character.add_merit(fast_reflexes)
        self.character.assign_advantages()
        self.assertEqual(self.character.initiative_modifier, 6)
        self.character.add_merit(fast_reflexes)
        self.character.assign_advantages()
        self.assertEqual(self.character.initiative_modifier, 7)
        self.character.add_merit(fast_reflexes)
        self.character.assign_advantages()
        self.assertEqual(self.character.initiative_modifier, 8)

    def test_small_framed_merit(self):
        small_framed = CoDMerit.objects.create(
            name="Small-Framed", ratings=[1], merit_type="Physical"
        )
        self.character.stamina = 2
        self.assertEqual(self.character.size, 5)
        self.character.add_merit(small_framed)
        self.character.assign_advantages()
        self.assertEqual(self.character.size, 4)
        self.assertEqual(self.character.health, 6)
        giant = CoDMerit.objects.create(name="Giant", ratings=[1])
        self.assertFalse(self.character.add_merit(giant))
        self.assertEqual(self.character.merits.count(), 1)

    def test_fleet_of_foot_merit(self):
        fleet_of_foot = CoDMerit.objects.create(
            name="Fleet of Foot", ratings=[1, 2, 3], merit_type="Physical"
        )
        self.character.strength = 1
        self.character.dexterity = 2
        self.character.assign_advantages()
        self.assertEqual(self.character.speed, 8)
        self.character.add_merit(fleet_of_foot)
        self.character.assign_advantages()
        self.assertEqual(self.character.speed, 9)
        self.character.add_merit(fleet_of_foot)
        self.character.assign_advantages()
        self.assertEqual(self.character.speed, 10)
        self.character.add_merit(fleet_of_foot)
        self.character.assign_advantages()
        self.assertEqual(self.character.speed, 11)

    def test_vice_ridden_merit(self):
        vice_ridden = CoDMerit.objects.create(
            name="Vice-Ridden", ratings=[1], merit_type="Physical"
        )
        self.character.add_vice("Vice 1")
        self.assertNotIn(", ", self.character.vice)
        self.character.add_merit(vice_ridden)
        self.character.assign_advantages()
        self.assertEqual(len(self.character.vice.split(", ")), 2)

    def test_virtuous_merit(self):
        virtuous = CoDMerit.objects.create(
            name="Virtuous", ratings=[1], merit_type="Physical"
        )
        self.character.add_virtue("Virtue 1")
        self.assertNotIn(", ", self.character.virtue)
        self.character.add_merit(virtuous)
        self.character.assign_advantages()
        self.assertEqual(len(self.character.virtue.split(", ")), 2)

    def test_defensive_combat_merit(self):
        defensive_combat_brawl = CoDMerit.objects.create(
            name="Defensive Combat (Brawl)", ratings=[1], merit_type="Physical"
        )
        defensive_combat_weaponry = CoDMerit.objects.create(
            name="Defensive Combat (Weaponry)", ratings=[1], merit_type="Physical"
        )
        self.character.wits = 2
        self.character.dexterity = 2
        self.character.athletics = 3
        self.character.brawl = 4
        self.character.weaponry = 5
        self.character.assign_advantages()
        self.assertEqual(self.character.defense, 5)
        self.character.add_merit(defensive_combat_brawl)
        self.character.assign_advantages()
        self.assertEqual(self.character.defense, 6)
        self.character.remove_merit(defensive_combat_brawl)
        self.character.add_merit(defensive_combat_weaponry)
        self.character.assign_advantages()
        self.assertEqual(self.character.defense, 7)

    def test_anonymity_and_fame(self):
        fame = CoDMerit.objects.create(name="Fame", ratings=[1], merit_type="Physical")
        anonymity = CoDMerit.objects.create(
            name="Anonymity", ratings=[1], merit_type="Physical"
        )
        self.assertEqual(self.character.merits.count(), 0)
        self.assertTrue(self.character.add_merit(fame))
        self.assertEqual(self.character.merits.count(), 1)
        self.assertFalse(self.character.add_merit(anonymity))
        self.assertEqual(self.character.merits.count(), 1)
        self.assertTrue(self.character.remove_merit(fame))
        self.assertEqual(self.character.merits.count(), 0)
        self.assertTrue(self.character.add_merit(anonymity))
        self.assertEqual(self.character.merits.count(), 1)
        self.assertFalse(self.character.add_merit(fame))
        self.assertEqual(self.character.merits.count(), 1)

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("merit"), 1)
        self.assertEqual(self.character.xp_cost("specialty"), 1)
        self.assertEqual(self.character.xp_cost("skill"), 2)
        self.assertEqual(self.character.xp_cost("morality"), 2)
        self.assertEqual(self.character.xp_cost("willpower"), 1)

    def test_get_absolute_url(self):
        self.assertEqual(
            self.character.get_absolute_url(), f"/cod/characters/{self.character.id}/"
        )

    def test_random_xp_functions(self):
        self.fail()

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
            self.character.spent_xp, "Strength 2 (4 XP), Strength 3 (4 XP)"
        )
        self.character.spend_xp("occult")
        self.assertEqual(self.character.occult, 1)
        self.assertEqual(
            self.character.spent_xp,
            "Strength 2 (4 XP), Strength 3 (4 XP), Occult 1 (2 XP)",
        )

    def test_spend_xp_attribute(self):
        self.fail()

    def test_spend_xp_skill(self):
        self.fail()

    def test_spend_xp_merit(self):
        self.fail()

    def test_spend_xp_specialty(self):
        self.fail()

    def test_add_morality(self):
        self.fail()

    def test_add_willpower(self):
        self.fail()

    def test_spend_xp_morality(self):
        self.fail()

    def test_spend_xp_willpower(self):
        self.character.resolve = 2
        self.character.composure = 3
        self.character.assign_advantages()
        self.character.xp = 3
        self.assertFalse(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 3)
        self.character.willpower = 3
        self.assertTrue(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 2)
        self.assertTrue(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 1)
        self.assertFalse(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 1)

    def test_spend_xp(self):
        self.fail()

    def test_contacts_merit(self):
        contacts = CoDMerit.objects.create(
            name="Contacts", ratings=[1, 2, 3, 4, 5], merit_type="Physical"
        )
        self.character.occult = 3
        while contacts not in self.character.merits.all():
            self.character.random_merit()
        rating = MeritRating.objects.get(character=self.character, merit=contacts)
        rating.detail = "Occult Contact 1"

    def test_integrity_prereq(self):
        integrity = CoDMerit.objects.create(
            name="Integrity Merit",
            ratings=[1],
            prereqs=[[("Morality Name", "Integritude")]],
        )
        self.assertFalse(integrity.check_prereqs(self.character))
        integrity.prereqs = [[("Morality Name", "Integrity")]]
        self.assertTrue(integrity.check_prereqs(self.character))

    def test_low_integrity_prereq(self):
        integrity = CoDMerit.objects.create(
            name="Integrity Merit", ratings=[1], prereqs=[[("morality", -5)]]
        )
        self.assertFalse(integrity.check_prereqs(self.character))
        self.character.morality = 5
        self.assertTrue(integrity.check_prereqs(self.character))
        integrity2 = CoDMerit.objects.create(
            name="Integrity Merit", ratings=[1], prereqs=[[("morality", 6)]]
        )
        self.assertFalse(integrity2.check_prereqs(self.character))
        self.character.morality = 6
        self.assertTrue(integrity2.check_prereqs(self.character))

    def test_add_condition(self):
        Condition.objects.create(name="Test Condition")
        self.assertEqual(self.character.conditions.count(), 0)
        self.character.add_condition(Condition.objects.first())
        self.assertEqual(self.character.conditions.count(), 1)

    def test_remove_condition(self):
        Condition.objects.create(name="Test Condition")
        self.character.add_condition(Condition.objects.first())
        self.assertEqual(self.character.conditions.count(), 1)
        self.character.remove_condition(self.character.conditions.first())
        self.assertEqual(self.character.conditions.count(), 0)


class TestRandomMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="", owner=self.player)
        for skill in self.character.get_skills().keys():
            for i in range(3):
                CoDSpecialty.objects.create(name=f"{skill} spec {i}", skill=skill)
        for i in range(10):
            for j in range(1, 6):
                CoDMerit.objects.create(
                    name=f"Merit {10*j + i}", ratings=[j], merit_type="Physical"
                )
        for i in range(10):
            Condition.objects.create(name=f"Condition {i}")

    def test_random_name(self):
        self.fail()

    def test_random_basis(self):
        self.character.random_basis()
        self.assertNotEqual(self.character.name, "")
        self.assertIn(
            self.character.vice,
            [
                "Ambitious",
                "Arrogant",
                "Competitive",
                "Greedy",
                "Pessimistic",
                "Hateful",
                "Deceitful",
                "Cruel",
                "Addictive",
                "Hasty",
                "Corrupt",
                "Dogmatic",
            ],
        )
        self.assertIn(
            self.character.virtue,
            [
                "Competitive",
                "Generous",
                "Just",
                "Loyal",
                "Hopeful",
                "Loving",
                "Honest",
                "Trustworthy",
                "Ambitious",
                "Patient",
                "Courageous",
            ],
        )
        self.assertEqual(self.character.concept, "Concept")
        self.assertEqual(
            self.character.short_term_aspiration_1, "Short Term Aspiration 1"
        )
        self.assertEqual(
            self.character.short_term_aspiration_2, "Short Term Aspiration 2"
        )
        self.assertEqual(self.character.long_term_aspiration, "Long Term Aspiration")

    def test_random_virtue(self):
        self.assertFalse(self.character.has_virtue())
        self.character.random_virtue()
        self.assertTrue(self.character.has_virtue())

    def test_random_vice(self):
        self.assertFalse(self.character.has_vice())
        self.character.random_vice()
        self.assertTrue(self.character.has_vice())

    def test_random_attribute(self):
        num = self.character.total_attributes()
        self.character.random_attribute()
        self.assertEqual(self.character.total_attributes(), num + 1)

    def test_random_attributes(self):
        self.assertFalse(self.character.has_attributes())
        self.character.random_attributes()
        self.assertTrue(self.character.has_attributes())

    def test_random_skill(self):
        num = self.character.total_skills()
        self.character.random_skill()
        self.assertEqual(self.character.total_skills(), num + 1)

    def test_random_skills(self):
        self.assertFalse(self.character.has_skills())
        self.character.random_skills()
        self.assertTrue(self.character.has_skills())

    def test_random_specialty(self):
        self.character.occult = 1
        num = self.character.specialties.count()
        self.character.random_specialty()
        self.assertEqual(self.character.specialties.count(), num + 1)

    def test_random_specialties(self):
        self.character.occult = 1
        self.character.science = 1
        self.character.athletics = 1
        self.assertFalse(self.character.has_specialties())
        self.character.random_specialties()
        self.assertTrue(self.character.has_specialties())

    def test_random_merit(self):
        num = self.character.total_merits()
        self.character.random_merit(dots=7)
        self.assertGreater(self.character.total_merits(), num)

    def test_random_merits(self):
        self.assertFalse(self.character.has_merits())
        self.character.random_merits()
        self.assertTrue(self.character.has_merits())

    def test_random_aspirations(self):
        self.assertFalse(self.character.has_aspirations())
        self.character.random_aspirations()
        self.assertTrue(self.character.has_aspirations())

    def test_random_spend_xp(self):
        self.character.science = 1
        self.character.xp = 15
        self.character.random_spend_xp()
        self.assertLess(self.character.xp, 15)

    def test_random_xp_willpower(self):
        self.fail()

    def test_random_xp_attribute(self):
        self.fail()

    def test_random_xp_skill(self):
        self.fail()

    def test_random_xp_merit(self):
        self.fail()

    def test_random_xp_specialty(self):
        self.fail()

    def test_random_xp_morality(self):
        self.fail()

    def test_random(self):
        character = Mortal.objects.create(owner=self.player)
        self.assertFalse(character.has_name())
        self.assertFalse(character.has_concept())
        self.assertFalse(character.has_virtue())
        self.assertFalse(character.has_vice())
        self.assertFalse(character.has_aspirations())
        self.assertFalse(character.has_attributes())
        self.assertFalse(character.has_skills())
        self.assertFalse(character.has_specialties())
        self.assertFalse(character.has_merits())
        character.random()
        self.assertTrue(character.has_name())
        self.assertTrue(character.has_concept())
        self.assertTrue(character.has_virtue())
        self.assertTrue(character.has_vice())
        self.assertTrue(character.has_aspirations())
        self.assertTrue(character.has_attributes())
        self.assertTrue(character.has_skills())
        self.assertTrue(character.has_specialties())
        self.assertTrue(character.has_merits())

    def test_random_condition(self):
        self.assertEqual(self.character.conditions.count(), 0)
        self.character.random_condition()
        self.assertEqual(self.character.conditions.count(), 1)


class TestMerit(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="Test", owner=self.player)

    def test_save(self):
        self.fail()

    def test_prereq_satisfied(self):
        self.fail()

    def test_check_prereqs(self):
        self.fail()

    def test_count_prereqs(self):
        self.fail()

    def test_prereq_skill_specialty(self):
        occult_specialty = CoDMerit.objects.create(
            name="Occult Specialty Requirement",
            prereqs=[[("occult", "specialty")]],
            ratings=[1],
            merit_type="Physical",
        )
        specialty_in_occult = CoDSpecialty.objects.create(skill="occult", name="Spec")
        self.assertFalse(occult_specialty.check_prereqs(self.character))
        self.character.add_specialty(specialty_in_occult)
        self.assertTrue(occult_specialty.check_prereqs(self.character))

    def test_prereq_minimum_skill_specialty(self):
        any_specialty_2 = CoDMerit.objects.create(
            name="Occult Specialty Requirement",
            prereqs=[[("specialty", 2)]],
            ratings=[1],
            merit_type="Physical",
        )
        specialty_in_occult = CoDSpecialty.objects.create(skill="occult", name="Spec")
        self.character.add_specialty(specialty_in_occult)
        self.assertFalse(any_specialty_2.check_prereqs(self.character))
        self.character.occult = 2
        self.assertTrue(any_specialty_2.check_prereqs(self.character))

    def test_prereq_skill_minimum_value(self):
        occult_3 = CoDMerit.objects.create(
            name="Occult Specialty Requirement",
            prereqs=[[("occult", 3)]],
            ratings=[1],
            merit_type="Physical",
        )
        self.assertFalse(occult_3.check_prereqs(self.character))
        self.character.occult = 3
        self.assertTrue(occult_3.check_prereqs(self.character))

    def test_prereq_any_skill_minimum_value(self):
        occult_3 = CoDMerit.objects.create(
            name="Occult Specialty Requirement",
            prereqs=[[("skill", 3)]],
            ratings=[1],
            merit_type="Physical",
        )
        self.assertFalse(occult_3.check_prereqs(self.character))
        self.character.occult = 3
        self.assertTrue(occult_3.check_prereqs(self.character))

    def test_merit_prereq(self):
        prereq_merit = CoDMerit.objects.create(
            name="Prereq for other", ratings=[1], merit_type="Physical"
        )
        prereq_merit_tester = CoDMerit.objects.create(
            name="Occult Specialty Requirement",
            prereqs=[[("Prereq for other", 1)]],
            ratings=[1],
            merit_type="Physical",
        )
        self.assertFalse(prereq_merit_tester.check_prereqs(self.character))
        self.character.add_merit(prereq_merit)
        self.assertTrue(prereq_merit_tester.check_prereqs(self.character))

    def test_filter_details(self):
        area_of_expertise = CoDMerit.objects.create(
            name="Area of Expertise",
            ratings=[1],
            requires_detail=True,
            merit_type="Physical",
        )
        self.assertEqual(len(area_of_expertise.filter_details(self.character)), 0)
        spec = CoDSpecialty.objects.create(name="Occult Specailty", skill="occult")
        self.character.add_specialty(spec)
        self.assertEqual(len(area_of_expertise.filter_details(self.character)), 1)

        interdisciplinary_specialty = CoDMerit.objects.create(
            name="Interdisciplinary Specialty",
            ratings=[1],
            requires_detail=True,
            merit_type="Physical",
        )
        self.assertEqual(
            len(interdisciplinary_specialty.filter_details(self.character)), 0
        )
        self.character.occult = 3
        self.assertEqual(
            len(interdisciplinary_specialty.filter_details(self.character)), 1
        )

        investigative_aide = CoDMerit.objects.create(
            name="Investigative Aide",
            ratings=[1],
            requires_detail=True,
            merit_type="Physical",
        )
        self.assertEqual(len(investigative_aide.filter_details(self.character)), 1)
        self.character.science = 3
        self.assertEqual(len(investigative_aide.filter_details(self.character)), 2)

        hobbyist_clique = CoDMerit.objects.create(
            name="Hobbyist Clique",
            ratings=[1],
            requires_detail=True,
            merit_type="Physical",
        )
        self.assertEqual(len(hobbyist_clique.filter_details(self.character)), 2)
        self.character.athletics = 2
        self.assertEqual(len(hobbyist_clique.filter_details(self.character)), 3)

        protessional_training = CoDMerit.objects.create(
            name="Professional Training",
            ratings=[1],
            requires_detail=True,
            possible_details=[
                "Prof 1 (Occult, Science)",
                "Prof 2 (Athletics, Empathy)",
                "Prof 3 (Animal Ken, Firearms)",
            ],
            merit_type="Physical",
        )
        self.assertEqual(len(protessional_training.filter_details(self.character)), 1)
        self.character.empathy = 1
        self.assertEqual(len(protessional_training.filter_details(self.character)), 2)

        merit = CoDMerit.objects.create(
            name="Merit with no weird detail",
            ratings=[1],
            requires_detail=True,
            possible_details=["Detail 1", "Detail 2"],
            merit_type="Physical",
        )
        self.assertEqual(len(merit.filter_details(self.character)), 2)

    def test_prereq_or(self):
        merit = CoDMerit.objects.create(
            name="Prereq Testing",
            ratings=[1, 2, 3],
            prereqs=[[("occult", 2)], [("science", 2)]],
            merit_type="Physical",
        )
        self.assertFalse(merit.check_prereqs(self.character))
        self.character.occult = 2
        self.assertTrue(merit.check_prereqs(self.character))
        self.character.occult = 1
        self.assertFalse(merit.check_prereqs(self.character))
        self.character.science = 2
        self.assertTrue(merit.check_prereqs(self.character))


class TestIndexView(TestCase):
    def setUp(self) -> None:
        for i in range(NUM_STATUSES):
            User.objects.create_user(username=f"Player {i}")

    def test_index_status_code(self):
        response = self.client.get("/cod/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/cod/characters/")
        self.assertTemplateUsed(response, "cod/characters/index.html")

    def test_index_post(self):
        for i in range(NUM_STATUSES):
            player = User.objects.get(username=f"Player {i}")
            for j in range(3):
                Mortal.objects.create(
                    name=f"Character {NUM_STATUSES*j+i}",
                    owner=player,
                    status=Mortal.status_keys[i],
                )
        response = self.client.post("/cod/characters/")
        for i in range(15):
            self.assertContains(response, f"Character {i}")
        for i in range(5):
            self.assertContains(response, f"Player {i}")
        for status in Mortal.statuses:
            self.assertContains(response, status)


class TestMortalDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testself.fail()")
        self.character = Mortal.objects.create(
            name="Test Character", owner=User.objects.get(username="Test User"),
        )

    def test_mortal_detail_view_status_code(self):
        response = self.client.get(f"/cod/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mortal_detail_view_template(self):
        response = self.client.get(f"/cod/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "cod/characters/mortal/mortal/detail.html")


class CharacterDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testself.fail()")
        self.character = Mortal.objects.create(
            name="Test Character", owner=User.objects.get(username="Test User"),
        )
        self.mage = Mage.objects.create(
            name="Test Mage", owner=User.objects.get(username="Test User"),
        )

    def test_character_detail_view_status_code(self):
        response = self.client.get(f"/cod/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_character_detail_view_templates(self):
        response = self.client.get(f"/cod/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "cod/characters/mortal/mortal/detail.html")
        response = self.client.get(f"/cod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "cod/characters/mage/mage/detail.html")
