from django.test import TestCase

from wod.models.location.mage import Node


# Create your tests here.
class TestNode(TestCase):
    pass


class TestNodeDetailView(TestCase):
    def setUp(self) -> None:
        self.location = Node.objects.create(name="Test Node")

    def test_location_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "wod/locations/mage/node/detail.html")
