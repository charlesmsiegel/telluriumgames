from django.contrib.auth.models import User
from django.test import TestCase

from cod.models.character.mortal import Merit, Mortal, Specialty


# Create your tests here.
class TestMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="", player=self.player.cod_profile)

    def test_add_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.add_name("Test Name"))
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
            self.character.filter_virtues(virtue_list=test_virtues), ["Virtue 2", "Virtue 3"]
        )
        self.character.virtue = "Virtue 1, Virtue 2"
        self.assertEqual(self.character.filter_virtues(virtue_list=test_virtues), ["Virtue 3"])

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

    def test_add_attribute(self):
        self.character.strength = 1
        self.assertTrue(self.character.add_attribute("strength"))
        self.assertEqual(self.character.strength, 2)
        self.character.strength = 5
        self.assertFalse(self.character.add_attribute("strength", max=5))
        self.assertEqual(self.character.strength, 5)
        self.assertTrue(self.character.add_attribute("strength", max=6))
        self.assertEqual(self.character.strength, 6)

    def test_filter_attributes(self):
        self.character.strength = 5
        self.assertEqual(
            self.character.filter_attributes(max=4),
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
            self.character.filter_attributes(max=5),
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
        self.assertEqual(self.character.filter_attributes(min=3), {"strength": 4})
        self.assertEqual(
            self.character.filter_attributes(min=3, max=5), {"strength": 4}
        )
        self.assertEqual(self.character.filter_attributes(min=5, max=6), {})

    def test_has_attributes(self):
        triple = [
            self.character.get_physical_attributes(),
            self.character.get_mental_attributes(),
            self.character.get_social_attributes(),
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
            self.character.get_physical_attributes(),
            self.character.get_mental_attributes(),
            self.character.get_social_attributes(),
        ]
        triple.sort()
        self.assertEqual(triple, [6, 7, 8])
        self.character.composure = 3
        triple = [
            self.character.get_physical_attributes(),
            self.character.get_mental_attributes(),
            self.character.get_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 7, 8])

    def test_add_skill(self):
        self.character.occult = 0
        self.assertTrue(self.character.add_attribute("occult"))
        self.assertEqual(self.character.occult, 1)
        self.character.occult = 5
        self.assertFalse(self.character.add_attribute("occult", max=5))
        self.assertEqual(self.character.occult, 5)
        self.assertTrue(self.character.add_attribute("occult", max=6))
        self.assertEqual(self.character.occult, 6)

    def test_filter_skills(self):
        self.character.occult = 5
        self.assertEqual(
            self.character.filter_skills(max=4),
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
            self.character.filter_skills(max=6),
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
        self.assertEqual(self.character.filter_skills(min=3), {"occult": 4})
        self.assertEqual(self.character.filter_skills(min=3, max=5), {"occult": 4})
        self.assertEqual(self.character.filter_skills(min=5, max=6), {})

    def test_has_skills(self):
        triple = [
            self.character.get_physical_skills(),
            self.character.get_mental_skills(),
            self.character.get_social_skills(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [4, 7, 11])
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
        triple = [
            self.character.get_physical_skills(),
            self.character.get_mental_skills(),
            self.character.get_social_skills(),
        ]
        triple.sort()
        self.assertEqual(triple, [4, 7, 11])
        self.character.subterfuge = 1
        triple = [
            self.character.get_physical_skills(),
            self.character.get_mental_skills(),
            self.character.get_social_skills(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [4, 7, 11])

    def test_add_specialty(self):
        specialty = Specialty.objects.create(name="Biology", skill="science")
        specialty2 = Specialty.objects.create(name="Physics", skill="science")
        self.assertTrue(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertFalse(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertTrue(self.character.add_specialty(specialty2))
        self.assertEqual(self.character.specialties.count(), 2)

    def test_filter_specialties(self):
        specialty = Specialty.objects.create(name="Biology", skill="science")
        Specialty.objects.create(name="Physics", skill="science")
        Specialty.objects.create(name="Dogs", skill="animal_ken")
        Specialty.objects.create(name="Guns", skill="firearms")
        self.character.add_specialty(specialty)
        self.assertEqual(len(self.character.filter_specialties()), 3)
        self.assertEqual(len(self.character.filter_specialties(skill="firearms")), 1)

    def test_has_specialties(self):
        Specialty.objects.create(name="Literature", skill="academics")
        Specialty.objects.create(name="Dogs", skill="animal_ken")
        Specialty.objects.create(name="Poetry", skill="expression")
        Specialty.objects.create(name="Reading People", skill="empathy")
        Specialty.objects.create(name="Directions", skill="streetwise")
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
        self.assertFalse(self.character.has_specialties())
        for skill in self.character.filter_skills(min=3).keys():
            s = Specialty.objects.filter(skill=skill).order_by("?").first()
            self.character.add_specialty(s)
            self.assertFalse(self.character.has_specialties())
        self.assertTrue(self.character.has_specialties())

    def test_add_merit(self):
        m = Merit.objects.create(name="Merit 1", ratings=[1, 2, 4])
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

    def test_filter_merits(self):
        m1 = Merit.objects.create(name="Merit 1", ratings=[1, 2])
        m2 = Merit.objects.create(name="Merit 2", ratings=[2, 3])
        m3 = Merit.objects.create(name="Merit 3", ratings=[3, 4])
        m4 = Merit.objects.create(name="Merit 4", ratings=[1, 4])
        m5 = Merit.objects.create(name="Merit 5", ratings=[2, 4])
        m6 = Merit.objects.create(name="Merit 6", ratings=[3, 4])
        merit_list = self.character.filter_merits(
            dots=3
        )  # Gives all merits with cost <= dots that character could add
        merit_set = set(merit_list)
        correct_set = {m1, m2, m3, m4, m5, m6}
        self.assertEqual(merit_set, correct_set)
        self.character.add_mert(m3)
        self.assertEqual(
            set(self.character.filter_merits(dots=3)), {m1, m2, m4, m5, m6}
        )
        self.character.add_mert(m2)
        self.assertEqual(
            set(self.character.filter_merits(dots=3)), {m1, m2, m4, m5, m6}
        )

    def test_has_merits(self):
        m1 = Merit.objects.create(name="Merit 1", ratings=[1, 2])
        m2 = Merit.objects.create(name="Merit 2", ratings=[2, 3])
        m3 = Merit.objects.create(name="Merit 3", ratings=[3, 4])
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m1)
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m1)
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m2)
        self.assertFalse(self.character.has_merits())
        self.character.add_merit(m3)
        self.assertTrue(self.character.has_merits())


class TestRandomMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="", player=self.player.cod_profile)

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
        num = self.character.specialties.count()
        self.character.random_specialty()
        self.assertEqual(self.character.specialties.count(), num + 1)

    def test_random_skill_specialties(self):
        self.assertFalse(self.character.has_specialties())
        self.character.random_specialties()
        self.assertTrue(self.character.has_specialties())

    def test_random_merit(self):
        num = self.character.total_merits()
        self.character.random_merit()
        self.assertGreater(self.character.total_merits(), num)

    def test_random_merits(self):
        self.assertFalse(self.character.has_merits())
        self.character.random_merits()
        self.assertTrue(self.character.has_merits())
