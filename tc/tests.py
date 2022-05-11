from django.test import TestCase
from django.contrib.auth.models import User
from tc.models import Aberrant


# Create your tests here.
class TestTalent(TestCase):
    # TODO: Create Talent class and replace the Aberrant here with it
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)

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
        self.assertEqual(self.character.get_skills(), {
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
        })
        self.assertEqual(self.character.total_skills(), 48)

    def test_specialties(self):
        self.fail()

    def test_tricks(self):
        self.fail()

    def test_final_touches(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()

    def test_pay_cost(self):
        self.fail()

    def test_weight_rating_list(self):
        self.fail()

    def test_apply_edge(self):
        self.fail()

    def test_rating_prob_fix(self):
        self.fail()


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

    def test_apply_template(self):
        self.fail()

    def test_final_touches(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()

    def test_mega_attribute_cleanup(self):
        self.fail()

    def test_compute_quantum_points(self):
        self.fail()

    def test_pay_cost(self):
        self.fail()

    def test_add_transcendance(self):
        self.fail()

    def test_apply_mega_edge(self):
        self.fail()

    def test_apply_power_tag(self):
        self.fail()

    def test_add_quantum(self):
        self.fail()

    def test_power_suite(self):
        self.fail()

    def test_reduced_cost_tag_can_be_bought_multiple_times(self):
        self.fail()

    def test_mega_edge_negative_one_is_dots(self):
        self.fail()


class TestRandomAberrant(TestCase):
    def test_random_concept(self):
        self.fail()

    def test_random_aspirations(self):
        self.fail()

    def test_random(self):
        self.fail()

    def test_add_random_attribute(self):
        self.fail()

    def test_add_random_edge(self):
        self.fail()

    def test_add_random_enhanced_edge(self):
        self.fail()

    def test_random_change_approach(self):
        self.fail()

    def test_add_random_skill(self):
        self.fail()

    def test_add_random_skill_trick(self):
        self.fail()

    def test_add_random_skill_specialty(self):
        self.fail()

    def test_add_random_path_dot(self):
        self.fail()

    def test_add_random_mega_attribute(self):
        self.fail()

    def test_add_random_mega_edge(self):
        self.fail()

    def test_add_random_power_tag(self):
        self.fail()

    def test_add_random_power(self):
        self.fail()

    def test_random_edges_and_tags_favor_lower_values(self):
        self.fail()

    def test_random_power_prefers_higher_rank_to_more_powers(self):
        self.fail()
