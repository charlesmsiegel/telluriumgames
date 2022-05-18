from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.aberrant import Aberrant
from tc.models.character.human import Edge, EnhancedEdge, Human, Path, Specialty, Trick
from tc.models.character.talent import Talent


# Create your tests here.
class TestHuman(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Human.objects.create(name="", player=self.player.tc_profile)

    def test_add_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.add_name("Test Name"))
        self.assertEqual(self.character.name, "Test Name")

    def test_has_name(self):
        self.character.name = ""
        self.assertFalse(self.character.has_name())
        self.character.name = "Test"
        self.assertTrue(self.character.has_name())

    def test_add_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.add_concept("Test Concept"))
        self.assertEqual(self.character.concept, "Test Concept")

    def test_has_concept(self):
        self.character.concept = ""
        self.assertFalse(self.character.has_concept())
        self.character.concept = "Test"
        self.assertTrue(self.character.has_concept())

    def test_has_aspirations(self):
        self.assertFalse(self.character.has_aspirations())
        self.character.short_term_aspiration_1 = "Test 1"
        self.character.short_term_aspiration_2 = "Test 2"
        self.character.long_term_aspiration = "Test 3"
        self.assertTrue(self.character.has_aspirations())

    def has_basics(self):
        self.assertFalse(self.character.has_basics())
        self.character.add_name("Test Name")
        self.character.add_concept("Test Concept")
        self.character.add_aspiration("Test Asp 1", type="short", number=1)
        self.character.add_aspiration("Test Asp 2", type="short", number=2)
        self.character.add_aspiration("Test Asp 3", type="long")
        self.assertTrue(self.character.has_basics())

    def test_add_path(self):
        self.assertEqual(self.character.paths.count(), 0)
        path = Path.objects.create(name="Path")
        self.assertTrue(self.character.add_path(path))
        self.assertEqual(self.character.paths.count(), 1)

    def test_has_paths(self):
        path_origin = Path.objects.create(name="Origin Path", type="origin")
        path_role = Path.objects.create(name="Role Path", type="role")
        path_society = Path.objects.create(name="Society Path", type="society")
        self.character.add_path(path_origin)
        self.assertFalse(self.character.has_paths())
        self.character.add_path(path_role)
        self.assertFalse(self.character.has_paths())
        self.character.add_path(path_society)
        self.assertTrue(self.character.has_paths())

    def test_add_edge(self):
        e = Edge.objects.create(name="Edge", ratings=[2])
        self.assertEqual(self.character.total_edges(), 0)
        self.assertTrue(self.character.add_edge(e))
        self.assertEqual(self.character.total_edges(), 2)
        self.assertFalse(self.character.add_edge(e))

    def test_total_edges(self):
        e1 = Edge.objects.create(name="Edge", ratings=[1, 2])
        e2 = Edge.objects.create(name="Edge", ratings=[2, 3])
        e3 = Edge.objects.create(name="Edge", ratings=[4])
        e4 = Edge.objects.create(name="Edge", ratings=[2])
        self.assertEqual(self.character.total_edges(), 0)
        self.character.add_edge(e1)
        self.assertEqual(self.character.total_edges(), 1)
        self.character.add_edge(e4)
        self.assertEqual(self.character.total_edges(), 3)
        self.character.add_edge(e2)
        self.assertEqual(self.character.total_edges(), 5)
        self.character.add_edge(e1)
        self.assertEqual(self.character.total_edges(), 6)
        self.character.add_edge(e2)
        self.assertEqual(self.character.total_edges(), 7)
        self.character.add_edge(e3)
        self.assertEqual(self.character.total_edges(), 11)

    def test_filter_edges(self):
        e1 = Edge.objects.create(name="Edge 0", ratings=[1, 2], prereqs=[("might", 2)])
        e2 = Edge.objects.create(
            name="Edge 1", ratings=[1, 2], prereqs=[("science", 2)]
        )
        e3 = Edge.objects.create(name="Edge 2", ratings=[1, 2])
        e4 = Edge.objects.create(name="Edge 3", ratings=[1, 2], prereqs=[("Edge 2", 2)])
        self.assertEqual(len(self.character.filter_edges()), 1)
        self.character.add_edge(e3)
        self.assertEqual(len(self.character.filter_edges()), 1)
        self.assertEqual(len(self.character.filter_edges(dots=1)), 1)
        self.character.might = 2
        self.assertEqual(len(self.character.filter_edges()), 2)
        self.character.science = 2
        self.assertEqual(len(self.character.filter_edges()), 3)
        self.character.add_edge(e2)
        self.assertEqual(len(self.character.filter_edges()), 3)
        self.character.add_edge(e3)
        self.assertEqual(len(self.character.filter_edges()), 3)
        self.assertNotIn(e3, self.character.filter_edges())

    def test_has_edges(self):
        types = ["origin", "role", "society"]
        for i in range(3):
            p = Path.objects.create(name=f"{types[i].title} Path", type=types[i])
            for j in range(4):
                e = Edge.objects.create(name=f"Path {i} Edge {j}", ratings=[1, 2])
                p.edges.add(e)
                p.save()
            self.character.add_path(p)

        self.assertFalse(self.character.has_edges())
        p1 = self.character.paths.filter(type="origin").first()
        self.character.add_edge(p1.edges.first())
        self.character.add_edge(p1.edges.first())
        p2 = self.character.paths.filter(type="role").first()
        self.character.add_edge(p2.edges.first())
        self.character.add_edge(p2.edges.first())
        p3 = self.character.paths.filter(type="society").first()
        self.character.add_edge(p3.edges.first())
        self.character.add_edge(p3.edges.first())
        self.assertEqual(self.character.total_path_edges(), 6)
        self.assertGreaterEqual(self.character.total_path_edges(path=p1), 2)
        self.assertGreaterEqual(self.character.total_path_edges(path=p2), 2)
        self.assertGreaterEqual(self.character.total_path_edges(path=p3), 2)
        self.assertTrue(self.character.has_edges(start=True))

    def test_add_skill(self):
        self.character.science = 0
        self.assertTrue(self.character.add_attribute("science"))
        self.assertEqual(self.character.science, 1)
        self.character.science = 5
        self.assertFalse(self.character.add_attribute("science", maximum=5))
        self.assertEqual(self.character.science, 5)
        self.assertTrue(self.character.add_attribute("science", maximum=6))
        self.assertEqual(self.character.science, 6)

    def test_filter_skills(self):
        self.character.science = 5
        self.assertEqual(
            self.character.filter_skills(maximum=4),
            {
                "aim": 0,
                "athletics": 0,
                "close_combat": 0,
                "command": 0,
                "culture": 0,
                "empathy": 0,
                "enigmas": 0,
                "humanities": 0,
                "integrity": 0,
                "larceny": 0,
                "medicine": 0,
                "persuasion": 0,
                "pilot": 0,
                "survival": 0,
                "technology": 0,
            },
        )
        self.assertEqual(
            self.character.filter_skills(maximum=6),
            {
                "aim": 0,
                "athletics": 0,
                "close_combat": 0,
                "command": 0,
                "culture": 0,
                "empathy": 0,
                "enigmas": 0,
                "humanities": 0,
                "integrity": 0,
                "larceny": 0,
                "medicine": 0,
                "persuasion": 0,
                "pilot": 0,
                "science": 5,
                "survival": 0,
                "technology": 0,
            },
        )
        self.character.science = 4
        self.assertEqual(self.character.filter_skills(minimum=3), {"science": 4})
        self.assertEqual(
            self.character.filter_skills(minimum=3, maximum=5), {"science": 4}
        )
        self.assertEqual(self.character.filter_skills(minimum=5, maximum=6), {})

    def set_skills(self):
        self.character.aim = 0
        self.character.athletics = 1
        self.character.close_combat = 2
        self.character.command = 3
        self.character.culture = 4
        self.character.empathy = 5
        self.character.enigmas = 4
        self.character.humanities = 3
        self.character.integrity = 2
        self.character.larceny = 1
        self.character.medicine = 0
        self.character.persuasion = 1
        self.character.pilot = 2
        self.character.science = 3
        self.character.survival = 4
        self.character.technology = 5

    def set_starting_skills(self):
        self.character.aim = 0
        self.character.athletics = 0
        self.character.close_combat = 0
        self.character.command = 0
        self.character.culture = 0
        self.character.empathy = 0
        self.character.enigmas = 0
        self.character.humanities = 1
        self.character.integrity = 1
        self.character.larceny = 1
        self.character.medicine = 1
        self.character.persuasion = 1
        self.character.pilot = 1
        self.character.science = 3
        self.character.survival = 3
        self.character.technology = 3

    def test_get_skills(self):
        self.assertEqual(
            self.character.get_skills(),
            {
                "aim": 0,
                "athletics": 0,
                "close_combat": 0,
                "command": 0,
                "culture": 0,
                "empathy": 0,
                "enigmas": 0,
                "humanities": 0,
                "integrity": 0,
                "larceny": 0,
                "medicine": 0,
                "persuasion": 0,
                "pilot": 0,
                "science": 0,
                "survival": 0,
                "technology": 0,
            },
        )
        self.set_skills()
        self.assertEqual(
            self.character.get_skills(),
            {
                "aim": 0,
                "athletics": 1,
                "close_combat": 2,
                "command": 3,
                "culture": 4,
                "empathy": 5,
                "enigmas": 4,
                "humanities": 3,
                "integrity": 2,
                "larceny": 1,
                "medicine": 0,
                "persuasion": 1,
                "pilot": 2,
                "science": 3,
                "survival": 4,
                "technology": 5,
            },
        )

    def test_total_skills(self):
        self.assertEqual(self.character.total_skills(), 0)
        self.set_skills()
        self.assertEqual(self.character.total_skills(), 40)

    def test_has_skills(self):
        self.character.add_path(
            Path.objects.create(name="TestPath 1", type="origin", skills=["technology"])
        )
        self.character.add_path(
            Path.objects.create(name="TestPath 2", type="role", skills=["survival"])
        )
        self.character.add_path(
            Path.objects.create(name="TestPath 3", type="society", skills=["science"])
        )
        self.assertFalse(self.character.has_skills())
        self.set_starting_skills()
        self.assertTrue(self.character.has_skills())

    def test_add_trick(self):
        self.assertEqual(self.character.tricks.count(), 0)
        trick = Trick.objects.create(name="Trick")
        self.assertTrue(self.character.add_trick(trick))
        self.assertEqual(self.character.tricks.count(), 1)

    def test_has_tricks(self):
        science_spec1 = Trick.objects.create(name="SciSpec", skill="science")
        larceny_spec1 = Trick.objects.create(name="LarSpec", skill="larceny")
        larceny_spec2 = Trick.objects.create(name="LarSpec2", skill="larceny")
        command_spec1 = Trick.objects.create(name="ComSpec", skill="command")
        command_spec2 = Trick.objects.create(name="ComSpec2", skill="command")
        command_spec3 = Trick.objects.create(name="ComSpec3", skill="command")
        self.character.science = 3
        self.character.larceny = 4
        self.character.command = 5
        self.assertFalse(self.character.has_tricks())
        self.assertTrue(self.character.add_trick(science_spec1))
        self.assertTrue(self.character.add_trick(larceny_spec1))
        self.assertTrue(self.character.add_trick(command_spec1))
        self.assertFalse(self.character.has_tricks())
        self.assertTrue(self.character.add_trick(larceny_spec2))
        self.assertTrue(self.character.add_trick(command_spec2))
        self.assertFalse(self.character.has_tricks())
        self.assertTrue(self.character.add_trick(command_spec3))
        self.assertTrue(self.character.has_tricks())

    def test_filter_tricks(self):
        trick = Trick.objects.create(name="Science Trick 1", skill="science")
        Trick.objects.create(name="Science Trick 1", skill="science")
        Trick.objects.create(name="Command Trick", skill="command")
        Trick.objects.create(name="Technology Trick", skill="technology")
        self.character.add_trick(trick)
        self.assertEqual(len(self.character.filter_tricks()), 3)
        self.assertEqual(len(self.character.filter_tricks(skill="technology")), 1)

    def test_add_specialty(self):
        specialty = Specialty.objects.create(name="Biology", skill="science")
        specialty2 = Specialty.objects.create(name="Physics", skill="science")
        self.assertTrue(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertFalse(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertTrue(self.character.add_specialty(specialty2))
        self.assertEqual(self.character.specialties.count(), 2)

    def test_filter_specialties(self):
        specialty = Specialty.objects.create(name="Biology", skill="science")
        Specialty.objects.create(name="Physics", skill="science")
        Specialty.objects.create(name="Dogs", skill="command")
        Specialty.objects.create(name="Guns", skill="technology")
        self.character.add_specialty(specialty)
        self.assertEqual(len(self.character.filter_specialties()), 3)
        self.assertEqual(len(self.character.filter_specialties(skill="technology")), 1)

    def test_has_specialties(self):
        science_spec = Specialty.objects.create(name="SciSpec", skill="science")
        larceny_spec = Specialty.objects.create(name="LarSpec", skill="larceny")
        command_spec = Specialty.objects.create(name="ComSpec", skill="command")
        self.character.science = 3
        self.character.larceny = 4
        self.character.command = 5
        self.assertFalse(self.character.has_specialties())
        self.assertTrue(self.character.add_specialty(science_spec))
        self.assertTrue(self.character.add_specialty(larceny_spec))
        self.assertTrue(self.character.add_specialty(command_spec))
        self.assertTrue(self.character.has_specialties())

    def test_add_attribute(self):
        self.character.might = 1
        self.assertTrue(self.character.add_attribute("might"))
        self.assertEqual(self.character.might, 2)
        self.character.might = 5
        self.assertFalse(self.character.add_attribute("might", maximum=5))
        self.assertEqual(self.character.might, 5)
        self.assertTrue(self.character.add_attribute("might", maximum=6))
        self.assertEqual(self.character.might, 6)

    def test_filter_attributes(self):
        self.character.might = 5
        self.assertEqual(
            self.character.filter_attributes(maximum=4),
            {
                "dexterity": 1,
                "stamina": 1,
                "intellect": 1,
                "cunning": 1,
                "resolve": 1,
                "presence": 1,
                "manipulation": 1,
                "composure": 1,
            },
        )
        self.assertEqual(
            self.character.filter_attributes(maximum=5),
            {
                "might": 5,
                "dexterity": 1,
                "stamina": 1,
                "intellect": 1,
                "cunning": 1,
                "resolve": 1,
                "presence": 1,
                "manipulation": 1,
                "composure": 1,
            },
        )
        self.character.might = 4
        self.assertEqual(self.character.filter_attributes(minimum=3), {"might": 4})
        self.assertEqual(
            self.character.filter_attributes(minimum=3, maximum=5), {"might": 4}
        )
        self.assertEqual(self.character.filter_attributes(minimum=5, maximum=6), {})

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

    def set_starting_attributes(self):
        self.character.might = 3
        self.character.dexterity = 3
        self.character.stamina = 4
        self.character.intellect = 2
        self.character.cunning = 2
        self.character.resolve = 4
        self.character.presence = 2
        self.character.manipulation = 2
        self.character.composure = 2

    def test_has_attributes(self):
        self.assertFalse(self.character.has_attributes())
        self.set_starting_attributes()
        self.assertTrue(self.character.has_attributes())

    def test_get_attributes(self):
        self.assertEqual(
            self.character.get_attributes(),
            {
                "might": 1,
                "dexterity": 1,
                "stamina": 1,
                "intellect": 1,
                "cunning": 1,
                "resolve": 1,
                "presence": 1,
                "manipulation": 1,
                "composure": 1,
            },
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_attributes(),
            {
                "might": 5,
                "dexterity": 4,
                "stamina": 3,
                "intellect": 2,
                "cunning": 1,
                "resolve": 2,
                "presence": 3,
                "manipulation": 4,
                "composure": 5,
            },
        )

    def test_total_attributes(self):
        self.assertEqual(self.character.total_attributes(), 9)
        self.set_attributes()
        self.assertEqual(self.character.total_attributes(), 29)

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

    def test_has_template(self):
        self.character.stamina = 5
        att_total = self.character.total_attributes()
        edge_total = self.character.total_edges()
        for i in range(1, 5):
            for j in range(3):
                Edge.objects.create(name=f"Edge {5*j + i - 1}", ratings=[i])
        self.character.apply_random_template()
        self.assertEqual(att_total + 1, self.character.total_attributes())
        self.assertEqual(edge_total + 4, self.character.total_edges())
        self.assertEqual(self.character.defense, 1)
        self.assertEqual(self.character.bruised_levels, 2)
        self.assertEqual(self.character.injured_levels, 2)
        self.assertEqual(self.character.maimed_levels, 1)

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

    def test_spend_xp(self):
        Edge.objects.create(name="Edge 1", ratings=[1, 2])
        Edge.objects.create(name="Edge 2", ratings=[3])
        pe = Edge.objects.create(name="Path Edge", ratings=[2])

        Trick.objects.create(name="Trick", skill="science")
        Specialty.objects.create(name="Specialty", skill="science")

        ee = EnhancedEdge.objects.create(name="Enhanced Edge", prereqs=[("Edge 1", 2)])

        p = Path.objects.create(
            name="Path", skills=["science", "technology", "command", "close_combat"]
        )
        p.edges.add(pe)
        p.save()

        self.character.approach = "RES"

        self.character.add_path(p)

        self.character.xp = 1000
        self.assertTrue(self.character.spend_xp("might"))
        self.assertEqual(self.character.xp, 990)
        self.assertEqual(self.character.might, 2)
        self.assertTrue(self.character.spend_xp("Edge 1"))
        self.assertEqual(self.character.xp, 987)
        self.assertEqual(self.character.edge_rating("Edge 1"), 1)
        self.assertTrue(self.character.spend_xp("Edge 2"))
        self.assertEqual(self.character.xp, 978)
        self.assertEqual(self.character.edge_rating("Edge 2"), 3)
        self.assertTrue(self.character.spend_xp("Edge 1"))
        self.assertEqual(self.character.xp, 975)
        self.assertEqual(self.character.edge_rating("Edge 1"), 2)
        self.assertTrue(self.character.spend_xp("Path Edge"))
        self.assertEqual(self.character.xp, 971)
        self.assertEqual(self.character.edge_rating("Path Edge"), 2)
        self.assertTrue(self.character.spend_xp("Enhanced Edge"))
        self.assertEqual(self.character.xp, 965)
        self.assertEqual(self.character.enhanced_edges.first(), ee)
        self.assertTrue(self.character.spend_xp("science"))
        self.assertEqual(self.character.xp, 960)
        self.assertEqual(self.character.science, 2)
        self.assertTrue(self.character.spend_xp("Trick"))
        self.assertEqual(self.character.xp, 957)
        self.assertEqual(self.character.tricks.count(), 1)
        self.assertTrue(self.character.spend_xp("Specialty"))
        self.assertEqual(self.character.xp, 954)
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertTrue(self.character.spend_xp("Path"))
        self.assertEqual(self.character.xp, 936)
        self.assertEqual(self.character.path_rating("Path"), 2)
        self.assertTrue(self.character.spend_xp("Favor FIN"))
        self.assertEqual(self.character.xp, 921)
        self.assertEqual(self.character.approach, "FIN")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.character.get_absolute_url(), f"/tc/characters/{self.character.id}/"
        )


class TestRandomHuman(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Human.objects.create(name="", player=self.player.tc_profile)
        for skill in self.character.get_skills().keys():
            for i in range(5):
                Specialty.objects.create(name=f"Specialty {i}", skill=skill)
                Trick.objects.create(name=f"Specialty {i}", skill=skill)
        for i in range(4):
            for t in ["origin", "role", "society"]:
                p = Path.objects.create(name="Path", type=t)
                for j in range(4):
                    p.skills.append(list(self.character.get_skills().keys())[4 * i + j])
                    p.edges.add(
                        Edge.objects.create(
                            name=f"Edge {4*j+i}", ratings=[i + 1, i + 2]
                        )
                    )
                p.save()

    def test_random_aspirations(self):
        self.assertFalse(self.character.has_aspirations())
        self.character.random_aspirations()
        self.assertTrue(self.character.has_aspirations())

    def test_random_basics(self):
        self.assertFalse(self.character.has_basics())
        self.character.random_basics()
        self.assertTrue(self.character.has_basics())

    def test_random_path(self):
        num = self.character.paths.count()
        self.character.random_skill()
        self.assertEqual(self.character.paths.count(), num + 1)
        self.character.random_skill(type="origin")
        self.assertEqual(self.character.paths.count(), num + 2)

    def test_random_paths(self):
        self.assertFalse(self.character.has_paths())
        self.character.random_path()
        self.assertTrue(self.character.has_paths())

    def test_random_skill(self):
        num = self.character.total_skills()
        self.character.random_skill()
        self.assertEqual(self.character.total_skills(), num + 1)

    def test_random_skills(self):
        self.assertFalse(self.character.has_skills())
        self.character.random_skills()
        self.assertTrue(self.character.has_skills())

    def test_random_trick(self):
        self.character.science = 3
        num = self.character.tricks.count()
        self.character.random_trick(skill="science")
        self.assertEqual(self.character.tricks.count(), num + 1)
        self.character.random_trick(skill="science")
        self.assertEqual(self.character.tricks.count(), num + 1)
        self.character.science = 4
        self.character.random_trick(skill="science")
        self.assertEqual(self.character.tricks.count(), num + 2)

    def test_random_tricks(self):
        self.character.science = 3
        self.character.command = 4
        self.character.close_combat = 3
        self.assertFalse(self.character.has_tricks())
        self.character.random_tricks()
        self.assertTrue(self.character.has_tricks())

    def test_random_specialty(self):
        self.character.science = 3
        num = self.character.specialties.count()
        self.character.random_specialty(skill="science")
        self.assertEqual(self.character.specialties.count(), num + 1)

    def test_random_specialties(self):
        self.character.science = 3
        self.character.command = 3
        self.character.close_combat = 3
        self.assertFalse(self.character.has_specialties())
        self.character.random_specialties()
        self.assertTrue(self.character.has_specialties())

    def test_random_attribute(self):
        num = self.character.total_attributes()
        self.character.random_attribute()
        self.assertEqual(self.character.total_attributes(), num + 1)

    def test_random_attributes(self):
        self.assertFalse(self.character.has_attributes())
        self.character.random_attributes()
        self.assertTrue(self.character.has_attributes())

    def test_random_edge(self):
        num = self.character.total_edges()
        self.character.random_edge(dots=1)
        self.assertEqual(self.character.total_edges(), num + 1)

    def test_random_template_choices(self):
        attributes = self.character.total_attributes()
        edges = self.character.total_edges()
        self.character.apply_random_template()
        self.assertEqual(self.character.total_attributes(), attributes + 1)
        self.assertEqual(self.character.total_edges(), edges + 4)

    def test_random_xp_spend(self):
        self.character.xp = 15
        self.character.random_xp_spend()
        self.assertLess(self.character.xp, 15)

    def test_random(self):
        character = Human.objects.create(player=self.player.tc_profile)
        self.assertFalse(character.has_name())
        self.assertFalse(character.has_concept())
        self.assertFalse(character.has_paths())
        self.assertFalse(character.has_aspirations())
        self.assertFalse(character.has_attributes())
        self.assertFalse(character.has_skills())
        self.assertFalse(character.has_specialties())
        self.assertFalse(character.has_tricks())
        self.assertFalse(character.has_basics())
        self.assertFalse(character.has_template())
        character.random()
        self.assertTrue(character.has_name())
        self.assertTrue(character.has_concept())
        self.assertTrue(character.has_paths())
        self.assertTrue(character.has_aspirations())
        self.assertTrue(character.has_attributes())
        self.assertTrue(character.has_skills())
        self.assertTrue(character.has_specialties())
        self.assertTrue(character.has_tricks())
        self.assertTrue(character.has_basics())
        self.assertTrue(character.has_template())


class TestHumanDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.character = Human.objects.create(
            name="Test Character",
            player=User.objects.get(username="Test User").tc_profile,
        )

    def test_mortal_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mortal_detail_view_template(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "tc/characters/human/detail.html")


class CharacterDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.human = Human.objects.create(
            name="Test Human", player=User.objects.get(username="Test User").tc_profile,
        )
        self.talent = Talent.objects.create(
            name="Test Talent",
            player=User.objects.get(username="Test User").tc_profile,
        )
        self.aberrant = Aberrant.objects.create(
            name="Test Aberrant",
            player=User.objects.get(username="Test User").tc_profile,
        )

    def test_character_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.human.id}/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/tc/characters/{self.talent.id}/")
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/tc/characters/{self.aberrant.id}/")
        self.assertEqual(response.status_code, 200)

    def test_character_detail_view_templates(self):
        response = self.client.get(f"/tc/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "tc/characters/human/detail.html")
        response = self.client.get(f"/tc/characters/{self.talent.id}/")
        self.assertTemplateUsed(response, "tc/characters/talent/detail.html")
        response = self.client.get(f"/tc/characters/{self.aberrant.id}/")
        self.assertTemplateUsed(response, "tc/characters/aberrant/detail.html")


class TestIndexView(TestCase):
    def setUp(self) -> None:
        for i in range(5):
            User.objects.create_user(username=f"Player {i}")

    def test_index_status_code(self):
        response = self.client.get("/tc/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/tc/characters/")
        self.assertTemplateUsed(response, "tc/characters/index.html")

    def test_index_content(self):
        for i in range(5):
            player = User.objects.get(username=f"Player {i}")
            for j in range(3):
                Human.objects.create(
                    name=f"Human {5*j+i}",
                    player=player.tc_profile,
                    status=Human.status_keys[i],
                )
                Talent.objects.create(
                    name=f"Talent {5*j+i}",
                    player=player.tc_profile,
                    status=Talent.status_keys[i],
                )
                Aberrant.objects.create(
                    name=f"Aberrant {5*j+i}",
                    player=player.tc_profile,
                    status=Aberrant.status_keys[i],
                )
        response = self.client.get("/tc/characters/")
        for i in range(15):
            self.assertContains(response, f"Human {i}")
            self.assertContains(response, f"Talent {i}")
            self.assertContains(response, f"Aberrant {i}")
        for i in range(5):
            self.assertContains(response, f"Player {i}")
        for status in Human.statuses:
            self.assertContains(response, status)
