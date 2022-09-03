from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.changeling import Changeling


# Create your tests here.
class TestKith(TestCase):
    pass


class TestHouse(TestCase):
    pass


class TestCtDHuman(TestCase):
    pass


class TestChangeling(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")

    def test_set_seeming(self):
        self.assertFalse(self.character.has_seeming())
        glamour = self.character.glamour
        willpower = self.character.willpower
        self.assertTrue(self.character.set_seeming("childer"))
        self.assertEqual(self.character.glamour, glamour + 1)
        self.assertTrue(self.character.has_seeming())
        self.assertTrue(self.character.set_seeming("wilder"))
        self.assertEqual(self.character.glamour + self.character.willpower, glamour + willpower + 1)
        self.assertTrue(self.character.set_seeming("grump")) 
        self.assertEqual(self.character.willpower, willpower + 1)

    def test_has_seeming(self):
        self.assertFalse(self.character.has_seeming())
        self.character.set_seeming("childer")
        self.assertTrue(self.character.has_seeming())


class TestRandomChangeling(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")

    def test_random_seeming(self):
        self.assertFalse(self.character.has_seeming())
        self.assertTrue(self.character.random_seeming())
        self.assertTrue(self.character.has_seeming())


class TestMotley(TestCase):
    pass


class TestChangelingDetailView(TestCase):
    pass
