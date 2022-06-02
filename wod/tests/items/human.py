from django.test import TestCase

from wod.models.items.human import Item


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
            Item.objects.create(name=f"Item {i}",)
        response = self.client.post("/wod/items/")
        for i in range(10):
            self.assertContains(response, f"Item {i}")


class TestItemDetailView(TestCase):
    def setUp(self) -> None:
        self.item = Item.objects.create(name="Test Item")

    def test_object_detail_view_status_code(self):
        response = self.client.get(f"/wod/items/{self.item.id}/")
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        response = self.client.get(f"/wod/items/{self.item.id}/")
        self.assertTemplateUsed(response, "wod/items/item/detail.html")

class TestItemView(TestCase):
    def test_random_status_code(self):
        self.fail()
        
    def test_random_template(self):
        self.fail()
        
    def test_input_sanitization(self):
        self.fail()
