from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.aberrant import Aberrant, MegaEdge, Transformation


# Create your tests here.
class TestAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)
        for i in range(1, 5):
            for j in range(5):
                MegaEdge.objects.create(name=f"MegaEdge {5*i+j}", ratings=[i, i + 1])
        MegaEdge.objects.create(
            name="MegaEdge with Prereq", ratings=[2, 4], prereqs=("MegaEdge 5", 2)
        )

    def test_add_megaedge(self):
        self.assertEqual(self.character.total_megaedges(), 0)
        self.assertEqual(self.character.megaedges.count(), 0)
        self.assertTrue(
            self.character.add_megaedge(MegaEdge.objects.get(name="MegaEdge 5"))
        )
        self.assertEqual(self.character.total_megaedges(), 1)
        self.assertEqual(self.character.megaedges.count(), 1)
        self.assertFalse(
            MegaEdge.objects.get(name="MegaEdge with Prereq").check_prereqs(
                self.character
            )
        )
        self.assertTrue(
            self.character.add_megaedge(MegaEdge.objects.get(name="MegaEdge 5"))
        )
        self.assertEqual(self.character.total_megaedges(), 1)
        self.assertEqual(self.character.megaedges.count(), 2)
        self.assertTrue(
            MegaEdge.objects.get(name="MegaEdge with Prereq").check_prereqs(
                self.character
            )
        )

    def test_filter_megaedges(self):
        MegaEdge.objects.create(name="MegaEdge 0", ratings=[1, 2], prereqs=[("mega_might", 2)])
        e2 = MegaEdge.objects.create(
            name="MegaEdge 1", ratings=[1, 2], prereqs=[("science", 2)]
        )
        e3 = MegaEdge.objects.create(name="MegaEdge 2", ratings=[1, 2])
        MegaEdge.objects.create(name="MegaEdge 3", ratings=[1, 2], prereqs=[("MegaEdge 2", 2)])
        
        self.assertEqual(len(self.character.filter_mega_edges()), 1)
        self.character.add_edge(e3)
        self.assertEqual(len(self.character.filter_mega_edges()), 1)
        self.assertEqual(len(self.character.filter_mega_edges(dots=1)), 1)
        self.character.might = 2
        self.assertEqual(len(self.character.filter_mega_edges()), 2)
        self.character.science = 2
        self.assertEqual(len(self.character.filter_mega_edges()), 3)
        self.character.add_edge(e2)
        self.assertEqual(len(self.character.filter_mega_edges()), 3)
        self.character.add_edge(e3)
        self.assertEqual(len(self.character.filter_mega_edges()), 3)
        self.assertNotIn(e3, self.character.filter_mega_edges())
        m4 = MegaEdge.objects.create(name="MegaEdge 4", ratings=[1, 2, 3, 4, 5], prereqs=[("quantum", "dots")])
        self.character.quantum = 1
        self.assertIn(m4, self.character.filter_mega_edges())
        self.test_add_megaedge(m4)
        self.assertNotIn(m4, self.character.filter_mega_edges())
        self.character.quantum = 2
        self.assertIn(m4, self.character.filter_mega_edges())

    def test_add_megaattribute(self):
        self.assertEqual(self.character.mega_might, 0)
        self.assertTrue(self.character.add_mega_attribute("might"))
        self.assertEqual(self.character.mega_might, 1)

    def set_attributes(self):
        self.character.might = 5
        self.character.dexterity = 4
        self.character.stamina = 3
        self.character.intellect = 2
        self.character.cunning = 1
        self.character.resolve = 2
        self.character.presence = 3
        self.character.manipulation = 4
        self.character.composure = 5

    def set_mega_attributes(self):
        self.character.mega_might = 0
        self.character.mega_dexterity = 2
        self.character.mega_stamina = 2
        self.character.mega_intellect = 2
        self.character.mega_cunning = 0
        self.character.mega_resolve = 0
        self.character.mega_presence = 0
        self.character.mega_manipulation = 1
        self.character.mega_composure = 2

    def test_get_megaattributes(self):
        self.assertEqual(
            self.character.get_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 0,
                "mega_stamina": 0,
                "mega_intellect": 0,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 0,
                "mega_composure": 0,
            },
        )
        self.set_mega_attributes()
        self.assertEqual(
            self.character.get_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 2,
                "mega_stamina": 2,
                "mega_intellect": 1,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 1,
                "mega_composure": 2,
            },
        )

    def test_filter_megaattribute(self):
        self.set_attributes()
        self.character.quantum = 2
        self.assertEqual(
            self.character.filter_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 0,
                "mega_stamina": 0,
                "mega_intellect": 0,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 0,
                "mega_composure": 0,
            },
        )
        self.set_mega_attributes()
        self.assertEqual(
            self.character.filter_mega_attributes(),
            {
                "mega_might": 0,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 1,
            },
        )
        self.character.quantum = 3
        self.assertEqual(
            self.character.filter_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 2,
                "mega_stamina": 2,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 1,
                "mega_composure": 2,
            },
        )

    def test_mega_attribute_bonuses(self):
        self.fail("Mega Intellect Edges")
        self.fail("Mega Cunning Edges")
        self.fail("Mega Manipulation Edges")
        self.fail("Mega Composure Edges")

    def test_add_power_suite(self):
        self.fail()

    def test_add_power(self):
        self.fail()

    def test_filter_tags(self):
        self.fail()

    def test_add_tag(self):
        self.fail("Check Adding a Tag")
        self.fail("Check can be added to an appropriate power")
        self.fail("Check can't be added to incorrect power")
        self.fail("Check only permitted ratings happen")
        self.fail("Reduced Cost can be bought more than once?")

    def test_remove_tag(self):
        self.fail()

    def test_add_transcendance(self):
        for i in range(3):
            for level in ['low', 'med', 'high']:
                Transformation.objects.create(name=f"{level.title()} Transformation {i}", level=level)
        low_level = Transformation.objects.create(name="Low Transformation 5", level=level)
        self.assertEqual(self.character.transcendence, 0)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 1)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 2)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 3)
        self.assertTrue(self.character.add_transcendence(transformation=low_level))
        self.assertEqual(self.character.transcendence, 4)
        self.assertEqual(self.character.transformations.count(), 1)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 5)
        self.assertEqual(self.character.transformations.filter(level='low').count(), 2)
        self.assertEqual(self.character.transformations.count(), 2)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 6)
        self.assertEqual(self.character.transformations.filter(level='med').count(), 1)
        self.assertEqual(self.character.transformations.count(), 3)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 7)
        self.assertEqual(self.character.transformations.filter(level='med').count(), 2)
        self.assertEqual(self.character.transformations.count(), 4)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 8)
        self.assertEqual(self.character.transformations.filter(level='high').count(), 1)
        self.assertEqual(self.character.transformations.count(), 5)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 9)
        self.assertEqual(self.character.transformations.filter(level='high').count(), 2)
        self.assertEqual(self.character.transformations.count(), 6)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 10)
        self.assertFalse(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 10)

    def test_add_quantum(self):
        t = Transformation.objects.create(name="Test Transformation", level="med")
        self.character.quantum = 3
        self.character.update_quantum_points()
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.transcendence, 1)
        self.assertEqual(self.character.quantum, 4)
        self.assertEqual(self.character.quantum_points, 30)
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.transcendence, 2)
        self.assertEqual(self.character.quantum, 5)
        self.assertEqual(self.character.quantum_points, 35)
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.quantum, 5)
        self.assertEqual(self.character.quantum_points, 35)
        self.assertTrue(self.character.add_quantum(start=False))
        self.assertEqual(self.character.transcendence, 3)
        self.assertEqual(self.character.quantum, 6)
        self.assertEqual(self.character.quantum_points, 40)
        self.assertTrue(self.character.add_quantum(start=False, transformation=t))
        self.assertEqual(self.character.transcendence, 4)
        self.assertEqual(self.character.quantum, 7)
        self.assertIn(t, self.character.transformations.all())


    def test_add_transformation(self):
        # Can't have more than 2 * quantum transformations
        # Come in Low, Med, High
        self.fail()

    def test_has_transformation(self):
        self.fail()

    def test_filter_transformation(self):
        self.fail()

    def test_assign_advantages(self):
        self.fail()

    def test_has_template(self):
        self.assertFalse(self.character.has_template())
        self.character.quantum = 1
        self.fail("One dot in favored approach")
        self.fail("Either 1 dot of Fame or 1 dot of Alternate Identity Edge")
        self.character.xp = 150
        self.assertTrue(self.character.has_template())

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("mega attribute"), 12)
        self.assertEqual(self.character.xp_cost("mega edge"), 12)
        self.assertEqual(self.character.xp_cost("power tag"), 12)
        self.assertEqual(self.character.xp_cost("quantum<=5"), 16)
        self.assertEqual(self.character.xp_cost("quantum>5"), 32)
        self.assertEqual(self.character.xp_cost("quantum power"), 12)
        self.assertEqual(self.character.xp_cost("remove tag"), 12)
        self.assertEqual(
            self.character.xp_cost("mega attribute", transcendence=True), 6
        )
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
