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

    def set_spheres(self):
        self.character.correspondence = 1
        self.character.time = 2
        self.character.spirit = 3
        self.character.matter = 4
        self.character.forces = 5
        self.character.life = 4
        self.character.entropy = 3
        self.character.mind = 2
        self.character.prime = 1

    def test_get_spheres(self):
        self.assertEqual(
            self.character.get_spheres(),
            {
                "correspondence": 0,
                "time": 0,
                "spirit": 0,
                "matter": 0,
                "forces": 0,
                "life": 0,
                "entropy": 0,
                "mind": 0,
                "prime": 0,
            },
        )
        self.set_spheres()
        self.assertEqual(
            self.character.get_spheres(),
            {
                "correspondence": 1,
                "time": 2,
                "spirit": 3,
                "matter": 4,
                "forces": 5,
                "life": 4,
                "entropy": 3,
                "mind": 2,
                "prime": 1,
            },
        )

    def test_add_sphere(self):
        self.character.arete = 2
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertTrue(self.character.add_sphere("forces"))
        self.assertEqual(self.character.forces, 2)
        self.assertFalse(self.character.add_sphere("forces"))
        self.character.arete = 3
        self.assertTrue(self.character.add_sphere("forces"))

    def test_filter_spheres(self):
        self.fail()

    def test_has_spheres(self):
        self.assertFalse(self.character.has_spheres())
        self.character.arete = 3
        self.character.set_affinity_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.acharacter.add_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.acharacter.add_sphere("forces")
        self.assertFalse(self.character.has_spheres())
        self.acharacter.add_sphere("matter")
        self.assertFalse(self.character.has_spheres())
        self.acharacter.add_sphere("matter")
        self.assertFalse(self.character.has_spheres())
        self.acharacter.add_sphere("matter")
        self.assertTrue(self.character.has_spheres())

    def test_set_affinity_sphere(self):
        self.assertFalse(self.character.has_affinity_sphere())
        self.assertTrue(self.character.set_affinity_sphere("forces"))
        self.assertTrue(self.character.has_affinity_sphere())

    def test_has_affinity_sphere(self):
        self.assertFalse(self.character.has_affinity_sphere())
        self.character.affinity_sphere = "forces"
        self.assertTrue(self.character.has_affinity_sphere())

    def test_add_arete(self):
        self.assertEqual(self.character.arete, 1)
        self.assertTrue(self.character.add_arete())
        self.assertEqual(self.character.arete, 2)
        self.character.arete = 10
        self.assertFalse(self.character.add_arete())

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
    def setUp(self):
        self.user = User.objects.create_user(username="Test")
        self.character = Mage.objects.create(name="", player=self.user.wod_profile)

    def test_random_affinity_sphere(self):
        self.assertFalse(self.character.has_affinity_sphere())
        self.character.random_affinity_sphere()
        self.assertTrue(self.character.has_affinity_sphere())

    def test_random_faction(self):
        self.assertFalse(self.character.has_faction())
        self.character.random_faction()
        self.assertTrue(self.character.has_faction())

    def test_random_focus(self):
        self.assertFalse(self.character.has_focus())
        self.character.random_focus()
        self.assertTrue(self.character.has_focus())

    def test_random_sphere(self):
        num = self.character.total_spheres()
        self.random_sphere()
        self.assertEqual(self.character.total_spheres(), num + 1)

    def test_random_spheres(self):
        self.assertFalse(self.character.has_spheres())
        self.random_spheres()
        self.assertTrue(self.character.has_spheres())

    def test_random_arete(self):
        self.assertEqual(self.character.arete, 0)
        self.random_arete()
        self.assertNotEqual(self.character.arete, 0)

    def test_random_xp_spend(self):
        self.character.science = 1
        self.character.xp = 15
        self.character.random_xp_spend()
        self.assertLess(self.character.xp, 15)


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
        self.assertTemplateUsed(response, "wod/characters/mage/detail.html")
