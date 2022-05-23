from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.human import Character, Human


# Create your tests here.
class TestCharacter(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Character.objects.create(
            player=self.player.wod_profile, name=""
        )

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


class TestHuman(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="Test")
        self.character = Human.objects.create(name="", player=self.user.wod_profile)

    def test_has_archetypes(self):
        self.fail()

    def test_archetypes(self):
        self.fail()

    # Nature and Demeanor
    # Attributes
    # Abilities
    # Specialties
    # Well-Skills Craftsman Plan!
    # Backgrounds
    # Willpower
    # Merits and Flaws
    # Freebies
    # Freebie Costs
    # Freebie Spend
    # XP Costs
    # XP Spend
    pass


class TestRandomHuman(TestCase):
    pass


class TestCharacterIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/wod/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/characters/")
        self.assertTemplateUsed(response, "wod/characters/index.html")

    def test_index_content(self):
        for i in range(10):
            Human.objects.create(name=f"Human {i}",)
        response = self.client.post("/wod/characters/")
        for i in range(10):
            self.assertContains(response, f"Human {i}")


class TestHumanDetailView(TestCase):
    def setUp(self) -> None:
        self.human = Human.objects.create(name="Test Human")

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/human/detail.html")
        # TODO: Test all templates here
