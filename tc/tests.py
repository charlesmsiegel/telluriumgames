from html.entities import codepoint2name

from django.contrib.auth.models import User
from django.test import TestCase

from tc.models import (
    Aberrant,
    Edge,
    Human,
    Path,
    PathConnection,
    PathConnectionRating,
    Specialty,
    Trick,
)
from tc.models.talent import EdgeRating, EnhancedEdge


# Create your tests here.
class TestTalent(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Human.objects.create(name="", player=self.player.tc_profile)
        Edge.objects.create(name="Edge 1")
        path_edge = Edge.objects.create(name="Path Edge")
        EnhancedEdge.objects.create(name="Enhanced Edge")
        path1 = Path.objects.create(
            name="Test Origin",
            type="ORI",
            skills=["aim", "athletics", "close_combat", "command"],
        )
        path1.edges.add(path_edge)
        conn1 = PathConnection.objects.create(name="Connection 1", path=path1)
        PathConnectionRating.objects.create(
            character=self.character, path=path1, path_connection=conn1, rating=1
        )
        Trick.objects.create(name="Trick")
        Specialty.objects.create(specialty="Specialty")

    def test_has_attributes(self):
        for att in [
            "intellect",
            "cunning",
            "resolve",
            "might",
            "dexterity",
            "stamina",
            "presence",
            "manipulation",
            "composure",
        ]:
            self.assertTrue(
                hasattr(self.character, att),
                msg=f"obj lacking an attribute. {self.character=}, {att=}",
            )

    def test_has_skills(self):
        for skill in [
            "aim",
            "athletics",
            "close_combat",
            "command",
            "culture",
            "empathy",
            "enigmas",
            "humanities",
            "integrity",
            "larceny",
            "medicine",
            "persuasion",
            "pilot",
            "science",
            "survival",
            "technology",
        ]:
            self.assertTrue(
                hasattr(self.character, skill),
                msg=f"obj lacking an attribute. {self.character=}, {skill=}",
            )

    def test_attribute_getters_and_sums(self):
        self.character.intellect = 1
        self.character.cunning = 2
        self.character.resolve = 3
        self.character.might = 4
        self.character.dexterity = 5
        self.character.stamina = 3
        self.character.presence = 2
        self.character.manipulation = 4
        self.character.composure = 1

        self.assertEqual(
            self.character.get_physical_attributes(),
            {"might": 4, "dexterity": 5, "stamina": 3},
        )
        self.assertEqual(self.character.physical_attribute_sum(), 12)

        self.assertEqual(
            self.character.get_mental_attributes(),
            {"intellect": 1, "cunning": 2, "resolve": 3},
        )
        self.assertEqual(self.character.mental_attribute_sum(), 6)

        self.assertEqual(
            self.character.get_social_attributes(),
            {"presence": 2, "manipulation": 4, "composure": 1},
        )
        self.assertEqual(self.character.social_attribute_sum(), 7)

        self.assertEqual(
            self.character.get_force_attributes(),
            {"intellect": 1, "might": 4, "presence": 2},
        )
        self.assertEqual(self.character.force_attribute_sum(), 7)

        self.assertEqual(
            self.character.get_finesse_attributes(),
            {"cunning": 2, "dexterity": 5, "manipulation": 4},
        )
        self.assertEqual(self.character.finesse_attribute_sum(), 11)

        self.assertEqual(
            self.character.get_resilience_attributes(),
            {"resolve": 3, "stamina": 3, "composure": 1},
        )
        self.assertEqual(self.character.resilience_attribute_sum(), 7)

    def test_get_skills(self):
        self.character.aim = 1
        self.character.athletics = 2
        self.character.close_combat = 3
        self.character.command = 4
        self.character.culture = 5
        self.character.empathy = 4
        self.character.enigmas = 3
        self.character.humanities = 2
        self.character.integrity = 1
        self.character.larceny = 2
        self.character.medicine = 3
        self.character.persuasion = 4
        self.character.pilot = 5
        self.character.science = 4
        self.character.survival = 3
        self.character.technology = 2
        self.assertEqual(
            self.character.get_skills(),
            {
                "aim": 1,
                "athletics": 2,
                "close_combat": 3,
                "command": 4,
                "culture": 5,
                "empathy": 4,
                "enigmas": 3,
                "humanities": 2,
                "integrity": 1,
                "larceny": 2,
                "medicine": 3,
                "persuasion": 4,
                "pilot": 5,
                "science": 4,
                "survival": 3,
                "technology": 2,
            },
        )
        self.assertEqual(self.character.total_skills(), 48)

    def test_specialties(self):
        spec1 = Specialty.objects.create(skill="sci", specialty="Physica")
        spec2 = Specialty.objects.create(skill="sci", specialty="Biology")
        self.assertEqual(self.character.specialties.count(), 0)
        self.character.add_specialty(spec1)
        self.assertEqual(self.character.specialties.count(), 1)
        self.character.add_specialty(spec2)
        self.assertEqual(self.character.specialties.count(), 1)

    def test_tricks(self):
        trick1 = Trick.objects.create(skill="sci", name="Trick 1")
        trick2 = Trick.objects.create(skill="sci", name="Trick 2")
        self.assertEqual(self.character.tricks.count(), 0)
        self.character.tricks.add(trick1)
        self.assertEqual(self.character.tricks.count(), 1)
        self.character.tricks.add(trick2)
        self.assertEqual(self.character.tricks.count(), 2)

    def test_final_touches(self):
        att_total = self.character.total_attributes()
        edge_total = self.character.total_edges()
        for i in range(1, 5):
            for j in range(3):
                Edge.objects.create(name=f"Edge {5*j + i - 1}", ratings=[i])
        self.character.final_touches()
        self.assertEqual(att_total + 1, self.character.total_attributes())
        self.assertEqual(edge_total + 4, self.character.total_edges())
        self.assertEqual(self.character.defense, 1)

    # def test_spend_xp(self):
    #     self.fail()

    def test_xp_costs(self):
        self.assertEqual(self.character.xp_cost("might", 1), 10)
        self.assertEqual(self.character.xp_cost("Edge 1", 1), 3)
        self.assertEqual(self.character.xp_cost("Edge 1", 2), 6)
        self.assertEqual(self.character.xp_cost("Path Edge", 1), 2)
        self.assertEqual(self.character.xp_cost("Path Edge", 3), 6)
        self.assertEqual(self.character.xp_cost("Enhanced Edge", 1), 6)
        self.assertEqual(self.character.xp_cost("Change Approach", 1), 15)
        self.assertEqual(self.character.xp_cost("science", 1), 5)
        self.assertEqual(self.character.xp_cost("science", 2), 10)
        self.assertEqual(self.character.xp_cost("Trick", 1), 3)
        self.assertEqual(self.character.xp_cost("Specialty", 1), 3)
        self.assertEqual(self.character.xp_cost("Test Origin", 1), 18)

    def test_apply_edge(self):
        edge = Edge.objects.create(name="Test Edge", ratings=[1, 2, 4])
        self.assertNotIn(edge, self.character.edges.all())
        self.character.add_edge(edge, 2)
        self.assertIn(edge, self.character.edges.all())
        self.assertEqual(
            EdgeRating.objects.get(character=self.character, edge=edge).rating, 2
        )

        prereq_edge = Edge.objects.create(
            name="Prereq Edge", ratings=[1], prereqs=[("might", 2)]
        )
        self.assertFalse(prereq_edge.check_prereqs(self.character))
        self.character.might = 3
        self.assertTrue(prereq_edge.check_prereqs(self.character))

        self.character.add_edge(edge, 4)
        self.assertEqual(
            EdgeRating.objects.filter(character=self.character, edge=edge).count(), 1
        )
        self.assertEqual(
            EdgeRating.objects.get(character=self.character, edge=edge).rating, 4
        )


class TestAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)

    def test_has_megaattributes(self):
        for att in [
            "mega_intellect",
            "mega_cunning",
            "mega_resolve",
            "mega_might",
            "mega_dexterity",
            "mega_stamina",
            "mega_presence",
            "mega_manipulation",
            "mega_composure",
        ]:
            self.assertTrue(
                hasattr(self.character, att),
                msg=f"obj lacking an attribute. {self.character=}, {att=}",
            )

    # def test_apply_template(self):
    #     self.fail("Quantum of 1")
    #     self.fail("One dot in favored approach")
    #     self.fail("Either 1 dot of Fame or 1 dot of Alternate Identity Edge")
    #     self.fail("150 XP")
    #     self.fail("Check spend_xp?")

    # def test_final_touches(self):
    #     self.fail("Check that character doesn't take final_touches trait bonuses like in Human/Talent")

    # def test_spend_xp(self):
    #     self.fail()

    # def test_mega_attribute_cleanup(self):
    #     self.fail("Mega Intellect Edges")
    #     self.fail("Mega Cunning Edges")
    #     self.fail("Mega Manipulation Edges")
    #     self.fail("Mega Composure Edges")

    # def test_pay_cost(self):
    #     self.fail("Mega Attribute Cost")
    #     self.fail("Mega Attribute Cost With Transcendence")
    #     self.fail("Mega Edge Cost")
    #     self.fail("Mega Edge Cost With Transcendence")
    #     self.fail("Power Tag Cost")
    #     self.fail("Quantum <= 5 Cost")
    #     self.fail("Quantum > 5 Cost")
    #     self.fail("Quantum Power Cost")
    #     self.fail("Quantum Power Cost With Transcendence")
    #     self.fail("Remove Tag Cost")

    # def test_add_transcendance(self):
    #     self.fail("Check Transcendence Increase")
    #     self.fail("Check Addition of Transformations")

    # def test_apply_mega_edge(self):
    #     self.fail("Add Edge at Rating")
    #     self.fail("Check Mega Edge Prereqs")
    #     self.fail("Increase rating of edge")
    #     self.fail("Do not add duplicate Edge")

    # def test_apply_power_tag(self):
    #     self.fail("Check Adding a Tag")
    #     self.fail("Check can be added to an appropriate power")
    #     self.fail("Check can't be added to incorrect power")
    #     self.fail("Check only permitted ratings happen")

    # def test_add_quantum(self):
    #     self.fail("Add quantum dot")
    #     self.fail("Fail to Add quantum dot above 5 at chargen")

    # def test_power_suite(self):
    #     self.fail()

    # def test_reduced_cost_tag_can_be_bought_multiple_times(self):
    #     self.fail()

    # def test_mega_edge_negative_one_is_dots(self):
    #     self.fail()


class TestRandomAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)
        for skill in self.character.get_skills().keys():
            for i in range(5):
                Specialty.objects.create(skill=skill[:3], specialty=f"Specialty {i}")
                Trick.objects.create(skill=skill[:3], name=f"Trick {i}")

        path1 = Path.objects.create(
            name="Test Origin",
            type="ORI",
            skills=["aim", "athletics", "close_combat", "command"],
        )
        path2 = Path.objects.create(
            name="Test Role",
            type="ROL",
            skills=["culture", "empathy", "enigmas", "humanities"],
        )
        path3 = Path.objects.create(
            name="Test Society",
            type="SOC",
            skills=["integrity", "larceny", "medicine", "persuasion"],
        )

        conn1 = PathConnection.objects.create(name="Connection 1", path=path1)
        conn2 = PathConnection.objects.create(name="Connection 2", path=path2)
        conn3 = PathConnection.objects.create(name="Connection 3", path=path3)

        PathConnectionRating.objects.create(
            character=self.character, path=path1, path_connection=conn1, rating=1
        )
        PathConnectionRating.objects.create(
            character=self.character, path=path2, path_connection=conn2, rating=1
        )
        PathConnectionRating.objects.create(
            character=self.character, path=path3, path_connection=conn3, rating=1
        )

    def test_random_concept(self):
        self.assertEqual(self.character.concept, "")
        self.character.random_concept()
        self.assertNotEqual(self.character.concept, "")

    def test_random_aspirations(self):
        self.assertEqual(self.character.short_term_aspiration_1, "")
        self.assertEqual(self.character.short_term_aspiration_2, "")
        self.assertEqual(self.character.long_term_aspiration, "")
        self.character.random_aspirations()
        self.assertNotEqual(self.character.short_term_aspiration_1, "")
        self.assertNotEqual(self.character.short_term_aspiration_2, "")
        self.assertNotEqual(self.character.long_term_aspiration, "")

    def test_add_random_attribute(self):
        for v in self.character.get_attributes().values():
            self.assertEqual(v, 1)
        self.assertEqual(len(self.character.get_attributes().keys()), 9)
        self.character.random_attributes()
        triple = [
            self.character.physical_attribute_sum(),
            self.character.social_attribute_sum(),
            self.character.mental_attribute_sum(),
        ]
        triple.sort()
        self.assertEqual(triple, [6, 8, 10])

    # def test_add_random_edge(self):
    #     self.fail()

    # def test_add_random_enhanced_edge(self):
    #     self.fail()

    # def test_random_change_approach(self):
    #     self.fail()

    def test_add_random_skills(self):
        for v in self.character.get_skills().values():
            self.assertEqual(v, 0)
        self.assertEqual(len(self.character.get_skills().keys()), 16)
        self.character.random_skills()
        self.assertEqual(self.character.total_skills(), 15)
        should_have_specs = [
            k for k, v in self.character.get_skills().items() if v >= 3
        ]
        for key in should_have_specs:
            self.assertEqual(
                self.character.specialties.filter(skill=key[:3]).count(), 1
            )

        should_have_tricks = {
            k: v for k, v in self.character.get_skills().items() if v >= 3
        }
        total = 0
        for key, value in should_have_tricks.items():
            self.assertGreaterEqual(
                self.character.tricks.filter(skill=key[:3]).count(), value - 2
            )
            total += value - 2
        self.assertEqual(self.character.tricks.count(), total + 1)

    # def test_add_random_skill_trick(self):
    #     self.fail()

    # def test_add_random_skill_specialty(self):
    #     self.fail()

    # def test_add_random_path_dot(self):
    #     self.fail()

    # def test_add_random_mega_attribute(self):
    #     self.fail()

    # def test_add_random_mega_edge(self):
    #     self.fail()

    # def test_add_random_power_tag(self):
    #     self.fail()

    # def test_add_random_power(self):
    #     self.fail()

    # def test_random_edges_and_tags_favor_lower_values(self):
    #     self.fail()

    # def test_random_power_prefers_higher_rank_to_more_powers(self):
    #     self.fail()
