from django.test import TestCase

from wod.models.items.human import Item
from wod.models.items.mage import Wonder


# Create your tests here.
class TestItemIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/wod/items/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/items/")
        self.assertTemplateUsed(response, "wod/items/index.html")

    def test_index_content(self):
        for i in range(10):
            Wonder.objects.create(name=f"Wonder {i}",)
        response = self.client.post("/wod/items/")
        for i in range(10):
            self.assertContains(response, f"Wonder {i}")


class TestItemDetailView(TestCase):
    def setUp(self) -> None:
        self.item = Item.objects.create(
            name="Test Item", rank=3, background_cost=6, quintessence_max=15
        )

    def test_object_detail_view_status_code(self):
        response = self.client.get(f"/wod/items/{self.item.id}/")
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(f"/wod/wonder/{self.item.id}/")
        self.assertTemplateUsed(response, "wod/items/human/item/detail.html")
        # TODO: Test all templates here


# TODO: Come up with base object
