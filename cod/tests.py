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
