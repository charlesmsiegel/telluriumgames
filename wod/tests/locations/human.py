from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.human import Character
from wod.models.locations.human import City, Location


# Create your tests here.
class TestLocation(TestCase):
    def setUp(self) -> None:
        self.location = Location.objects.create(name="Location 1")
        self.child = Location.objects.create(name="Location 2", parent=self.location)

    def test_location_parent(self):
        self.assertEqual(self.child.parent, self.location)
        self.assertIn(self.child, self.location.children.all())


class TestCity(TestCase):
    """Manage Tests for City"""

    def test_add_character(self):
        city = City.objects.create(name="New York City", population=28000000)
        player = User.objects.create_user(username="User")
        char = Character.objects.create(name="NPC 1", player=player.wod_profile)
        city.add_character(char)
        self.assertIn(char, city.characters.all())


class TestLocationIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/wod/locations/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/locations/")
        self.assertTemplateUsed(response, "wod/locations/index.html")

    def test_index_content(self):
        for i in range(10):
            Location.objects.create(name=f"Location {i}",)
        response = self.client.post("/wod/locations/")
        for i in range(10):
            self.assertContains(response, f"Location {i}")


class TestLocationDetailView(TestCase):
    def setUp(self) -> None:
        self.location = Location.objects.create(name="Location 1")

    def test_location_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "wod/locations/location/detail.html")


class TestCityDetailView(TestCase):
    def setUp(self) -> None:
        self.location = City.objects.create(name="Test Location")

    def test_location_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "wod/locations/city/detail.html")
