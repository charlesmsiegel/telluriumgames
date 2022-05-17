from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.aberrant import Aberrant

# Create your tests here.
# class TestAberrant(TestCase):
#     def setUp(self):
#         self.player = User.objects.create(username="Test User")
#         self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)

#     def test_add_megaedge(self):
#         self.fail()

#     def test_has_megaedges(self):
#         self.fail()

#     def test_filter_megaedges(self):
#         self.fail()

#     def test_add_megaattribute(self):
#         self.fail()

#     def test_has_megaattribute(self):
#         self.fail()

#     def test_filter_megaattribute(self):
#         self.fail()

#     def test_add_power_suite(self):
#         self.fail()

#     def test_add_power(self):
#         self.fail()

#     def test_has_powers(self):
#         self.fail()

#     def test_filter_tag(self):
#         self.fail()

#     def test_add_tag(self):
#         self.fail()

#     def test_has_tag(self):
#         self.fail()

#     def test_filter_tag(self):
#         self.fail()

#     def test_remove_tag(self):
#         self.fail()

#     def test_add_transcendance(self):
#         self.fail()

#     def test_add_quantum(self):
#         self.fail()

#     def test_add_transformation(self):
#         self.fail()

#     def test_has_transformation(self):
#         self.fail()

#     def test_filter_transformation(self):
#         self.fail()

#     def test_assign_advantages(self):
#         self.fail()

#     def test_has_template(self):
#         self.fail("Quantum of 1")
#         self.fail("One dot in favored approach")
#         self.fail("Either 1 dot of Fame or 1 dot of Alternate Identity Edge")
#         self.fail("150 XP")
#         self.fail("Check spend_xp?")

#     def test_xp_cost(self):
#         self.fail("Human costs too")
#         self.fail("Mega Attribute Cost")
#         self.fail("Mega Attribute Cost With Transcendence")
#         self.fail("Mega Edge Cost")
#         self.fail("Mega Edge Cost With Transcendence")
#         self.fail("Power Tag Cost")
#         self.fail("Quantum <= 5 Cost")
#         self.fail("Quantum > 5 Cost")
#         self.fail("Quantum Power Cost")
#         self.fail("Quantum Power Cost With Transcendence")
#         self.fail("Remove Tag Cost")

#     def test_spend_xp(self):
#         self.fail()


# class TestRandomAberrant(TestCase):
#     def test_random_power(self):
#         self.fail()

#     def test_random_template_choices(self):
#         self.fail()

#     def test_random_xp_spend(self):
#         self.fail()

#     def test_random(self):
#         self.fail()


class TestAberrantDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.character = Aberrant.objects.create(
            name="Test Character",
            player=User.objects.get(username="Test User").tc_profile,
        )

    def test_mortal_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mortal_detail_view_template(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "tc/characters/aberrant/detail.html")
