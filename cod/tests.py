from collections import Counter
from locale import MON_1

from cod.models import Merit, MeritRating, Mortal, Specialty
from cod.templatetags.dots import dots
from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class TestDots(TestCase):
    def test_length(self):
        output_5 = dots(4)
        output_10 = dots(4, maximum=10)
        output_10_2 = dots(6)
        self.assertEqual(len(output_5), 5)
        self.assertEqual(len(output_10), 10)
        self.assertEqual(len(output_10_2), 10)

    def test_correct_ratio(self):
        self.assertEqual(Counter(dots(3))["●"], 3)
        self.assertEqual(Counter(dots(3))["○"], 2)
        self.assertEqual(Counter(dots(3, maximum=10))["●"], 3)
        self.assertEqual(Counter(dots(3, maximum=10))["○"], 7)
        self.assertEqual(Counter(dots(6))["●"], 6)
        self.assertEqual(Counter(dots(6))["○"], 4)


class TestMerit(TestCase):
    def test_prereq_skill_specialty(self):
        player = User.objects.create(username="Test User")
        character = Mortal.objects.create(name="Test", player=player.cod_profile)
        occult_specialty = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("occult", "specialty")],
            allowed_ratings=[1],
        )
        specialty_in_occult = Specialty.objects.create(skill="occ", specialty="Spec")
        self.assertFalse(occult_specialty.check_prereqs(character))
        character.specialties.add(specialty_in_occult)
        self.assertTrue(occult_specialty.check_prereqs(character))

    def test_prereq_specialty_minimum_value(self):
        player = User.objects.create(username="Test User")
        character = Mortal.objects.create(name="Test", player=player.cod_profile)
        any_specialty_2 = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("specialty", 2)],
            allowed_ratings=[1],
        )
        specialty_in_occult = Specialty.objects.create(skill="occ", specialty="Spec")
        character.specialties.add(specialty_in_occult)
        self.assertFalse(any_specialty_2.check_prereqs(character))
        character.occult = 2
        self.assertTrue(any_specialty_2.check_prereqs(character))

    def test_prereq_skill_minimum_value(self):
        player = User.objects.create(username="Test User")
        character = Mortal.objects.create(name="Test", player=player.cod_profile)
        occult_3 = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("occult", 3)],
            allowed_ratings=[1],
        )
        self.assertFalse(occult_3.check_prereqs(character))
        character.occult = 3
        self.assertTrue(occult_3.check_prereqs(character))

    def test_any_skill_minimum_value(self):
        player = User.objects.create(username="Test User")
        character = Mortal.objects.create(name="Test", player=player.cod_profile)
        occult_3 = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("skill", 3)],
            allowed_ratings=[1],
        )
        self.assertFalse(occult_3.check_prereqs(character))
        character.occult = 3
        self.assertTrue(occult_3.check_prereqs(character))

    def test_merit_prereq(self):
        player = User.objects.create(username="Test User")
        character = Mortal.objects.create(name="Test", player=player.cod_profile)
        prereq_merit = Merit.objects.create(
            name="Prereq for other", allowed_ratings=[1]
        )
        prereq_merit_tester = Merit.objects.create(
            name="Occult Specialty Requirement",
            merit_prereqs=[("Prereq for other", 1)],
            allowed_ratings=[1],
        )
        self.assertFalse(prereq_merit_tester.check_prereqs(character))
        MeritRating.objects.create(character=character, merit=prereq_merit, rating=1)
        self.assertTrue(prereq_merit_tester.check_prereqs(character))

    def test_get_max_rating(self):
        occult_specialty = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("occult", "specialty")],
            allowed_ratings=[1, 3, 4],
        )
        self.assertEqual(occult_specialty.get_max_rating(), 4)

    def test_choose_detail(self):
        player = User.objects.create(username="Test User")
        character = Mortal.objects.create(name="Test", player=player.cod_profile)
        spec = Specialty.objects.create(skill="occ", specialty="Spec")
        character.specialties.add(spec)
        area_of_expertise = Merit.objects.create(
            name="Area of Expertise", allowed_ratings=[1]
        )
        self.assertEqual(area_of_expertise.choose_detail(character), "Spec")
        interdisciplinary_specialty = Merit.objects.create(
            name="Interdisciplinary Specialty", allowed_ratings=[1]
        )
        self.assertNotEqual(
            interdisciplinary_specialty.choose_detail(character), "Spec"
        )
        character.occult = 3
        self.assertEqual(interdisciplinary_specialty.choose_detail(character), "Spec")
        investigative_aide = Merit.objects.create(
            name="Investigative Aide", allowed_ratings=[1]
        )
        self.assertEqual(investigative_aide.choose_detail(character), "occult")
        hobbyist_clique = Merit.objects.create(
            name="Hobbyist Clique", allowed_ratings=[1]
        )
        self.assertEqual(hobbyist_clique.choose_detail(character), "occult")
        professional_training = Merit.objects.create(
            name="Professional Training",
            allowed_ratings=[1],
            list_of_details=["Test (Occult, Science)"],
        )
        self.assertNotEqual(professional_training.choose_detail(character), "Spec")
        character.science = 1
        self.assertEqual(
            professional_training.choose_detail(character), "Test (Occult, Science)"
        )
        other_merit = Merit.objects.create(
            name="Other", allowed_ratings=[1], list_of_details=["Test Detail 1"]
        )
        self.assertEqual(other_merit.choose_detail(character), "Test Detail 1")


class TestMortalMechanics(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="", player=self.player.cod_profile)
        self.merit1 = Merit.objects.create(name="Merit 1", allowed_ratings=[1])
        self.merit2 = Merit.objects.create(name="Merit 2", allowed_ratings=[2])
        self.merit3 = Merit.objects.create(name="Merit 3", allowed_ratings=[3])

    def test_has_name(self):
        self.assertFalse(self.character.has_name())
        self.character.name = "Test Character"
        self.character.save()
        self.assertTrue(self.character.has_name())

    def test_has_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.concept = "Character Concept"
        self.character.save()
        self.assertTrue(self.character.has_concept())

    def test_get_mental_attributes(self):
        self.character.intelligence = 1
        self.character.resolve = 2
        self.character.wits = 3
        self.character.save()
        self.assertEqual(
            {"intelligence": 1, "resolve": 2, "wits": 3},
            self.character.get_mental_attributes(),
        )

    def test_get_physical_attributes(self):
        self.character.strength = 3
        self.character.dexterity = 2
        self.character.stamina = 1
        self.character.save()
        self.assertEqual(
            {"stamina": 1, "dexterity": 2, "strength": 3},
            self.character.get_physical_attributes(),
        )

    def test_get_social_attributes(self):
        self.character.composure = 3
        self.character.presence = 2
        self.character.manipulation = 1
        self.character.save()
        self.assertEqual(
            {"manipulation": 1, "presence": 2, "composure": 3},
            self.character.get_social_attributes(),
        )

    def test_physical_attribute_sum(self):
        self.character.strength = 3
        self.character.dexterity = 2
        self.character.stamina = 1
        self.character.save()
        self.assertEqual(self.character.physical_attribute_sum(), 6)
        self.character.stamina = 2
        self.assertEqual(self.character.physical_attribute_sum(), 7)
        self.character.strength = 1
        self.assertEqual(self.character.physical_attribute_sum(), 5)

    def test_mental_attribute_sum(self):
        self.character.intelligence = 1
        self.character.resolve = 2
        self.character.wits = 3
        self.character.save()
        self.assertEqual(self.character.mental_attribute_sum(), 6)
        self.character.intelligence = 2
        self.assertEqual(self.character.mental_attribute_sum(), 7)
        self.character.wits = 1
        self.assertEqual(self.character.mental_attribute_sum(), 5)

    def test_social_attribute_sum(self):
        self.character.composure = 3
        self.character.presence = 2
        self.character.manipulation = 1
        self.character.save()
        self.assertEqual(self.character.social_attribute_sum(), 6)
        self.character.manipulation = 2
        self.assertEqual(self.character.social_attribute_sum(), 7)
        self.character.composure = 1
        self.assertEqual(self.character.social_attribute_sum(), 5)

    def test_get_mental_skills(self):
        self.character.academics = 0
        self.character.computer = 1
        self.character.crafts = 2
        self.character.investigation = 3
        self.character.medicine = 4
        self.character.occult = 5
        self.character.politics = 0
        self.character.science = 3
        self.character.save()
        self.assertEqual(
            {
                "academics": 0,
                "computer": 1,
                "crafts": 2,
                "investigation": 3,
                "medicine": 4,
                "occult": 5,
                "politics": 0,
                "science": 3,
            },
            self.character.get_mental_skills(),
        )

    def test_get_physical_skills(self):
        self.character.athletics = 0
        self.character.brawl = 1
        self.character.drive = 2
        self.character.firearms = 3
        self.character.larceny = 4
        self.character.stealth = 5
        self.character.survival = 0
        self.character.weaponry = 3
        self.character.save()
        self.assertEqual(
            {
                "athletics": 0,
                "brawl": 1,
                "drive": 2,
                "firearms": 3,
                "larceny": 4,
                "stealth": 5,
                "survival": 0,
                "weaponry": 3,
            },
            self.character.get_physical_skills(),
        )

    def test_get_social_skills(self):
        self.character.animal_ken = 0
        self.character.empathy = 1
        self.character.expression = 2
        self.character.intimidation = 3
        self.character.persuasion = 4
        self.character.socialize = 5
        self.character.streetwise = 0
        self.character.subterfuge = 3
        self.character.save()
        self.assertEqual(
            {
                "animal_ken": 0,
                "empathy": 1,
                "expression": 2,
                "intimidation": 3,
                "persuasion": 4,
                "socialize": 5,
                "streetwise": 0,
                "subterfuge": 3,
            },
            self.character.get_social_skills(),
        )

    def test_get_skills(self):
        self.character.academics = 0
        self.character.computer = 1
        self.character.crafts = 2
        self.character.investigation = 3
        self.character.medicine = 4
        self.character.occult = 5
        self.character.politics = 0
        self.character.science = 3
        self.character.athletics = 0
        self.character.brawl = 1
        self.character.drive = 2
        self.character.firearms = 3
        self.character.larceny = 4
        self.character.stealth = 5
        self.character.survival = 0
        self.character.weaponry = 3
        self.character.animal_ken = 0
        self.character.empathy = 1
        self.character.expression = 2
        self.character.intimidation = 3
        self.character.persuasion = 4
        self.character.socialize = 5
        self.character.streetwise = 0
        self.character.subterfuge = 3
        self.assertEqual(
            {
                "academics": 0,
                "computer": 1,
                "crafts": 2,
                "investigation": 3,
                "medicine": 4,
                "occult": 5,
                "politics": 0,
                "science": 3,
                "athletics": 0,
                "brawl": 1,
                "drive": 2,
                "firearms": 3,
                "larceny": 4,
                "stealth": 5,
                "survival": 0,
                "weaponry": 3,
                "animal_ken": 0,
                "empathy": 1,
                "expression": 2,
                "intimidation": 3,
                "persuasion": 4,
                "socialize": 5,
                "streetwise": 0,
                "subterfuge": 3,
            },
            self.character.get_skills(),
        )

    def test_mental_skill_sum(self):
        self.character.academics = 0
        self.character.computer = 1
        self.character.crafts = 2
        self.character.investigation = 3
        self.character.medicine = 4
        self.character.occult = 5
        self.character.politics = 0
        self.character.science = 3
        self.assertEqual(self.character.mental_skill_sum(), 18)
        self.character.politics = 3
        self.assertEqual(self.character.mental_skill_sum(), 21)

    def test_physical_skill_sum(self):
        self.character.athletics = 0
        self.character.brawl = 1
        self.character.drive = 2
        self.character.firearms = 3
        self.character.larceny = 4
        self.character.stealth = 5
        self.character.survival = 0
        self.character.weaponry = 3
        self.assertEqual(self.character.physical_skill_sum(), 18)
        self.character.survival = 3
        self.assertEqual(self.character.physical_skill_sum(), 21)

    def test_social_skill_sum(self):
        self.character.animal_ken = 0
        self.character.empathy = 1
        self.character.expression = 2
        self.character.intimidation = 3
        self.character.persuasion = 4
        self.character.socialize = 5
        self.character.streetwise = 0
        self.character.subterfuge = 3
        self.assertEqual(self.character.social_skill_sum(), 18)
        self.character.streetwise = 3
        self.assertEqual(self.character.social_skill_sum(), 21)

    def test_total_merits(self):
        MeritRating.objects.create(
            character=self.character, merit=self.merit1, rating=1
        )
        self.assertEqual(self.character.total_merits(), 1)
        MeritRating.objects.create(
            character=self.character, merit=self.merit1, rating=2
        )
        self.assertEqual(self.character.total_merits(), 3)
        MeritRating.objects.create(
            character=self.character, merit=self.merit1, rating=3
        )
        self.assertEqual(self.character.total_merits(), 6)

    def test_filter_merits(self):
        Merit.objects.all().delete()
        for i in range(1, 6):
            for j in range(3):
                Merit.objects.create(
                    name=f"Merit {5*j+i-1}", allowed_ratings=[i, i + 1]
                )

        self.assertEqual(len(self.character.filter_merits(3)), 9)

        MeritRating.objects.create(
            character=self.character, merit=Merit.objects.get(name="Merit 0"), rating=1
        )
        self.assertEqual(len(self.character.filter_merits(5)), 14)

        m = Merit.objects.create(
            name="Variable Merit", allowed_ratings=[1], needs_detail=True
        )
        MeritRating.objects.create(
            character=self.character, merit=m, rating=1, detail="D1"
        )
        self.assertIn(m, self.character.filter_merits(5))

        anonymity = Merit.objects.create(
            name="Anonymity", allowed_ratings=[1, 2, 3, 4, 5], merit_type="Social",
        )
        fame = Merit.objects.create(
            name="Fame", allowed_ratings=[1, 2, 3], merit_type="Social",
        )

        rating = MeritRating.objects.create(character=self.character, merit=anonymity, rating=1)
        self.assertNotIn(fame, self.character.filter_merits(5))
        rating.delete()
        rating = MeritRating.objects.create(character=self.character, merit=fame, rating=1)
        self.assertNotIn(anonymity, self.character.filter_merits(5))

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

    def test_apply_merits(self):
        self.fail("Giant")
        self.fail("Fast Reflexes")
        self.fail("Small-Framed")
        self.fail("Fleet of Foot")
        self.fail("Vice-Ridden")
        self.fail("Virtuous")
        self.fail("Defensive Combat (Brawl)")
        self.fail("Defensive Combat (Weaponry)")


class TestMortalRandom(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(
            name="Test Name", player=self.player.cod_profile
        )

    def test_random_vice(self):
        self.assertIn(
            self.character.random_vice(),
            ["Ambitious", "Arrogant", "Competitive", "Greedy"],
        )

    def test_random_virtue(self):
        self.assertIn(
            self.character.random_virtue(), ["Competitive", "Generous", "Just", "Loyal"]
        )

    def test_random_basis(self):
        self.character.random_basis()
        self.assertIn(
            self.character.vice, ["Ambitious", "Arrogant", "Competitive", "Greedy"]
        )
        self.assertIn(
            self.character.virtue, ["Competitive", "Generous", "Just", "Loyal"]
        )
        self.assertEqual(self.character.concept, "Concept")

    def test_random_attributes(self):
        self.character.random_attributes()
        self.character.save()
        triple = [
            self.character.physical_attribute_sum(),
            self.character.social_attribute_sum(),
            self.character.mental_attribute_sum(),
        ]
        triple.sort()
        self.assertEqual(triple, [6, 7, 8])
        for _, value in self.character.get_physical_attributes().items():
            self.assertLessEqual(value, 5)
        for _, value in self.character.get_social_attributes().items():
            self.assertLessEqual(value, 5)
        for _, value in self.character.get_mental_attributes().items():
            self.assertLessEqual(value, 5)

    def test_random_skills(self):
        self.character.random_skills()
        self.character.save()
        triple = [
            self.character.physical_skill_sum(),
            self.character.social_skill_sum(),
            self.character.mental_skill_sum(),
        ]
        triple.sort()
        self.assertEqual(triple, [4, 7, 11])
        for _, value in self.character.get_physical_skills().items():
            self.assertLessEqual(value, 5)
        for _, value in self.character.get_social_skills().items():
            self.assertLessEqual(value, 5)
        for _, value in self.character.get_mental_skills().items():
            self.assertLessEqual(value, 5)

    def test_random_specialties(self):
        self.character.random_skills()
        for key in Specialty.skill_keys:
            for i in range(3):
                Specialty.objects.create(skill=key, specialty=f"{key} Spec {i+1}")
        self.character.random_specialties(num_specs=3)
        self.assertEqual(self.character.specialties.count(), 3)

    def test_random_merits(self):
        for i in range(5):
            for j in range(3):
                Merit.objects.create(name=f"Merit {5*j+i}", allowed_ratings=[i])

        self.character.random_merits()
        self.assertEqual(self.character.total_merits(), 7)
        self.character.merits.set([])
        self.assertEqual(self.character.total_merits(), 0)
        MeritRating.objects.create(
            character=self.character, merit=Merit.objects.get(name="Merit 3"), rating=3
        )
        self.assertEqual(self.character.total_merits(), 3)
        self.character.random_merits()
        self.assertEqual(self.character.total_merits(), 7)
        self.character.merits.set([])
        self.assertEqual(self.character.total_merits(), 0)
        MeritRating.objects.create(
            character=self.character, merit=Merit.objects.get(name="Merit 3"), rating=3
        )
        self.assertEqual(self.character.total_merits(), 3)
        MeritRating.objects.create(
            character=self.character, merit=Merit.objects.get(name="Merit 8"), rating=3
        )
        self.assertEqual(self.character.total_merits(), 6)
        self.character.random_merits()
        self.assertEqual(self.character.total_merits(), 7)
