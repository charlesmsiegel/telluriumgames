from collections import Counter

from cod.templatetags.dots import dots
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
        self.fail()

    def test_get_max_rating(self):
        self.fail()

    def test_choose_detail(self):
        self.fail()


class TestMortalMechanics(TestCase):
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
