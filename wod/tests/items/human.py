from django.test import TestCase

from wod.models.items.human import WoDItem


# Create your tests here.
class TestRandomWoDItem(TestCase):
    def test_random_name(self):
        self.fail()


class TestItemIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/wod/items/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/items/")
        self.assertTemplateUsed(response, "wod/items/index.html")

    def test_index_content(self):
        for i in range(10):
            WoDItem.objects.create(name=f"Item {i}",)
        response = self.client.post("/wod/items/")
        for i in range(10):
            self.assertContains(response, f"Item {i}")


class TestItemDetailView(TestCase):
    def setUp(self) -> None:
        self.item = WoDItem.objects.create(name="Test Item")

    def test_object_detail_view_status_code(self):
        response = self.client.get(f"/wod/items/{self.item.id}/")
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(f"/wod/items/{self.item.id}/")
        self.assertTemplateUsed(response, "wod/items/human/item/detail.html")
