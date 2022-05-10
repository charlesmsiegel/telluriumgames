from collections import Counter
from django.contrib.auth.models import User

from cod.templatetags.dots import dots
from cod.models import MeritRating, Mortal, Merit, Specialty
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
    def test_prereq_checking(self):
        occult_specialty = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("occult", "specialty")],
            allowed_ratings=[1],
        )
        any_specialty_2 = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("specialty", 2)],
            allowed_ratings=[1],
        )
        occult_3 = Merit.objects.create(
            name="Occult Specialty Requirement",
            attribute_and_skill_prereqs=[("occult", 3)],
            allowed_ratings=[1],
        )
        prereq_merit = Merit.objects.create(
            name="Prereq for other", allowed_ratings=[1]
        )
        prereq_merit_tester = Merit.objects.create(
            name="Occult Specialty Requirement",
            merit_prereqs=[("Prereq for other", 1)],
            allowed_ratings=[1],
        )
        player = User.objects.create(username="Test User")
        character = Mortal.objects.create(name="Test", player=player.cod_profile)
        specialty_in_occult = Specialty.objects.create(skill="occ", specialty="Spec")
        self.assertFalse(occult_specialty.check_prereqs(character))
        character.specialties.add(specialty_in_occult)
        self.assertTrue(occult_specialty.check_prereqs(character))

        self.assertFalse(any_specialty_2.check_prereqs(character))
        character.occult = 2
        self.assertTrue(any_specialty_2.check_prereqs(character))

        self.assertFalse(occult_3.check_prereqs(character))
        character.occult = 3
        self.assertTrue(occult_3.check_prereqs(character))

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
        pass

    def test_has_name(self):
        self.fail()

    def test_has_concept(self):
        self.fail()

    def test_get_mental_attributes(self):
        self.fail()

    def test_get_physical_attributes(self):
        self.fail()

    def test_get_social_attributes(self):
        self.fail()

    def test_physical_attribute_sum(self):
        self.fail()

    def test_mental_attribute_sum(self):
        self.fail()

    def test_social_attribute_sum(self):
        self.fail()

    def test_get_mental_skills(self):
        self.fail()

    def test_get_physical_skills(self):
        self.fail()

    def test_get_social_skills(self):
        self.fail()

    def test_get_skills(self):
        self.fail()

    def test_mental_skill_sum(self):
        self.fail()

    def test_physical_skill_sum(self):
        self.fail()

    def test_social_skill_sum(self):
        self.fail()

    def test_total_merits(self):
        self.fail()

    def test_filter_merits(self):
        self.fail()

    def test_assign_advantages(self):
        self.fail()

    def test_apply_merits(self):
        self.fail()


class TestMortalRandom(TestCase):
    def setUp(self):
        pass

    def test_random_name(self):
        self.fail()

    def test_random_vice(self):
        self.fail()

    def test_random_virtue(self):
        self.fail()

    def test_random_basis(self):
        self.fail()

    def test_random(self):
        self.fail()

    def test_random_attributes(self):
        self.fail()

    def test_random_skills(self):
        self.fail()

    def test_random_specialties(self):
        self.fail()

    def test_random_merits(self):
        self.fail()
