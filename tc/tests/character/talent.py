from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.talent import Talent


# Create your tests here.
class TestTalent(TestCase):
    def test_add_moment_of_inspiration(self):
        self.fail()

    def has_moment_of_inspiration(self):
        self.fail()

    def test_add_inspiration(self):
        self.fail()

    def test_has_inspiration(self):
        self.fail()

    def test_add_facet(self):
        self.fail()

    def test_has_facets(self):
        self.fail()

    def test_filter_facets(self):
        self.fail()

    def test_add_gift(self):
        self.fail()

    def test_has_gifts(self):
        self.fail()

    def test_filter_gifts(self):
        self.fail()

    def test_assign_advantages(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()


class TestRandomTalent(TestCase):
    def test_random_facets(self):
        self.fail()

    def test_random_gifts(self):
        self.fail()

    def test_random_template_choices(self):
        self.fail()

    def test_random_xp_spend(self):
        self.fail()

    def test_random(self):
        self.fail()


# class TestTalentDetailView(TestCase):
#     def setUp(self) -> None:
#         User.objects.create_user("Test User", "test@user.com", "testpass")
#         self.character = Talent.objects.create(
#             name="Test Character",
#             player=User.objects.get(username="Test User").tc_profile,
#         )
#         print(self.character.type)
#         print(self.character.id)

#     def test_talent_detail_view_status_code(self):
#         response = self.client.get(f"/tc/characters/{self.character.id}/")
#         self.assertEqual(response.status_code, 200)

#     def test_talent_detail_view_template(self):
#         response = self.client.get(f"/tc/characters/{self.character.id}/")
#         self.assertTemplateUsed(response, "tc/characters/talent/detail.html")
