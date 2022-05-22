from django.test import TestCase

from wod.models.object.mage import Wonder


# Create your tests here.
class TestIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/wod/objects/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/objects/")
        self.assertTemplateUsed(response, "wod/objects/index.html")

    def test_index_content(self):
        for i in range(10):
            Wonder.objects.create(name=f"Wonder {i}",)
        response = self.client.post("/wod/objects/")
        for i in range(15):
            self.assertContains(response, f"Wonder {i}")


class TestObjectDetailView(TestCase):
    def setUp(self) -> None:
        self.wonder = Wonder.objects.create(name="Test Wonder",)

    def test_object_detail_view_status_code(self):
        response = self.client.get(f"/wod/objects/{self.wonder.id}/")
        self.assertEqual(response.status_code, 200)

    def test_object_detail_view_templates(self):
        wonder = Wonder.objects.create(
            name="Test Wonder",
            rank=3,
            background_cost=6,
            quintessence_max=15,
            description="Test Description",
        )
        response = self.client.get(f"/wod/wonder/{wonder.id}/")
        self.assertTemplateUsed(response, "wod/objects/mage/wonder.html")
        # TODO: Test all templates here
