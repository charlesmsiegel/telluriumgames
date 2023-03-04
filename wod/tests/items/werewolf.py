from django.test import TestCase

from wod.models.items.werewolf import Fetish


# Create your tests here.
class TestFetish(TestCase):
    def test_save(self):
        fetish = Fetish.objects.create(rank=2)
        self.assertEqual(fetish.background_cost, 2)
