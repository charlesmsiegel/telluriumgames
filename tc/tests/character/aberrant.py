from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.aberrant import Aberrant

# Create your tests here.
class TestAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)

    def test_add_megaedge(self):
        self.fail("Add Edge at Rating")
        self.fail("Check Mega Edge Prereqs")
        self.fail("Increase rating of edge")
        self.fail("Do not add duplicate Edge")

    def test_filter_megaedges(self):
        self.fail()

    def test_mega_edge_negative_one_is_dots(self):
        self.fail()

    def test_add_megaattribute(self):
        self.assertEqual(self.character.mega_might, 0)
        self.assertTrue(self.character.add_mega_attribute("might"))
        self.assertEqual(self.character.mega_might, 1)

    def test_filter_megaattribute(self):
        self.fail()

    def test_mega_attribute_bonuses(self):
        self.fail("Mega Intellect Edges")
        self.fail("Mega Cunning Edges")
        self.fail("Mega Manipulation Edges")
        self.fail("Mega Composure Edges")

    def test_add_power_suite(self):
        self.fail()

    def test_add_power(self):
        self.fail()

    def test_filter_tag(self):
        self.fail()

    def test_add_tag(self):
        self.fail("Check Adding a Tag")
        self.fail("Check can be added to an appropriate power")
        self.fail("Check can't be added to incorrect power")
        self.fail("Check only permitted ratings happen")

    def test_filter_tag(self):
        self.fail()

    def test_remove_tag(self):
        self.fail()

    def test_reduced_cost_tag_can_be_bought_multiple_times(self):
        self.fail()

    def test_add_transcendance(self):
        self.fail("Check Transcendence Increase")
        self.fail("Check Addition of Transformations")

    def test_add_quantum(self):
        self.character.quantum = 3
        self.character.update_quantum_points()
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.quantum, 4)
        self.assertEqual(self.character.quantum_points, 30)
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.quantum, 5)
        self.assertEqual(self.character.quantum_points, 35)
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.quantum, 5)
        self.assertEqual(self.character.quantum_points, 35)
        self.assertTrue(self.character.add_quantum(start=False))
        self.assertEqual(self.character.quantum, 6)
        self.assertEqual(self.character.quantum_points, 40)
        
    def test_add_transformation(self):
        self.fail()

    def test_has_transformation(self):
        self.fail()

    def test_filter_transformation(self):
        self.fail()

    def test_assign_advantages(self):
        self.fail()

    def test_has_template(self):
        self.fail("Quantum of 1")
        self.fail("One dot in favored approach")
        self.fail("Either 1 dot of Fame or 1 dot of Alternate Identity Edge")
        self.fail("150 XP")
        self.fail("Check spend_xp?")

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 10)
        self.assertEqual(self.character.xp_cost("edge"), 3)
        self.assertEqual(self.character.xp_cost("path edge"), 2)
        self.assertEqual(self.character.xp_cost("enhanced edge"), 6)
        self.assertEqual(self.character.xp_cost("skill"), 5)
        self.assertEqual(self.character.xp_cost("skill trick"), 3)
        self.assertEqual(self.character.xp_cost("skill specialty"), 3)
        self.assertEqual(self.character.xp_cost("path"), 18)
        self.assertEqual(self.character.xp_cost("favored approach"), 15)

        self.assertEqual(self.character.xp_cost("mega attribute"), 12)
        self.assertEqual(self.character.xp_cost("mega edge"), 12)
        self.assertEqual(self.character.xp_cost("power tag"), 12)
        self.assertEqual(self.character.xp_cost("quantum<=5"), 16)
        self.assertEqual(self.character.xp_cost("quantum>5"), 32)
        self.assertEqual(self.character.xp_cost("quantum power"), 12)
        self.assertEqual(self.character.xp_cost("remove tag"), 12)
        self.assertEqual(self.character.xp_cost("mega attribute", transcendence=True), 6)
        self.assertEqual(self.character.xp_cost("mega edge", transcendence=True), 6)
        self.assertEqual(self.character.xp_cost("quantum power", transcendence=True), 6)

    def test_spend_xp(self):
        self.fail()


class TestRandomAberrant(TestCase):
    def test_random_mega_attribute(self):
        self.fail()

    def test_random_mega_edge(self):
        self.fail()

    def test_random_power_tag(self):
        self.fail()

    def test_random_power(self):
        self.fail()

    def test_random_template_choices(self):
        self.fail()

    def test_random_xp_spend(self):
        self.fail()

    def test_random_edges_and_tags_favor_lower_values(self):
        self.fail()

    def test_random_power_prefers_higher_rank_to_more_powers(self):
        self.fail()

    def test_random(self):
        self.fail()


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
