from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.mage import Mage


# Create your tests here.
class TestMage(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Test")
        self.character = Mage.objects.create(name="", player=self.user.wod_profile)

    # Spheres
    # Arete
    # Quintessence
    # Focus
    # Spheres
    # Affinity Sphere
    # Arete
    # Paradox
    pass


class TestRandomMage(TestCase):
    pass


class TestMageDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.mage = Mage.objects.create(
            name="Test Mage", player=self.player.wod_profile
        )

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/mage/detail.html")
        # TODO: Test all templates here
