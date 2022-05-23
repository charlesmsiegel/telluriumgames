from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.mage import Mage


# Create your tests here.
class TestMage(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="Test")
        self.character = Mage.objects.create(name="", player=self.user.wod_profile)

    def test_get_abilities(self):
        self.fail()

    def test_get_talents(self):
        self.fail()

    def test_get_skills(self):
        self.fail()

    def test_get_knowledges(self):
        self.fail()

    def test_get_spheres(self):
        self.fail()

    def test_add_sphere(self):
        self.fail()

    def test_filter_spheres(self):
        self.fail()

    def test_has_spheres(self):
        self.fail()

    def test_set_affinity_sphere(self):
        self.fail()

    def test_has_affinity_sphere(self):
        self.fail()

    def test_add_arete(self):
        self.fail()

    def test_add_quintessence(self):
        self.fail()

    def test_set_faction(self):
        self.fail()

    def test_has_faction(self):
        self.fail()

    def test_set_focus(self):
        self.fail()

    def test_has_focus(self):
        self.fail()

    def test_freebie_cost(self):
        self.fail()

    def test_spend_freebies(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()

    def test_random_freebies(self):
        self.fail()

    def test_random_spend_xp(self):
        self.fail()

    def test_random(self):
        self.fail()


class TestRandomMage(TestCase):
    def test_random_affinity_sphere(self):
        self.fail()

    def test_random_faction(self):
        self.fail()

    def test_random_focus(self):
        self.fail()

    def test_random_sphere(self):
        self.fail()

    def test_random_spheres(self):
        self.fail()

    def test_random_arete(self):
        self.fail()


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
