from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.aberrant import (
    Aberrant,
    MegaEdge,
    MegaEdgeRating,
    Power,
    PowerRating,
    Tag,
    Transformation,
)
from tc.models.character.human import Edge, Path, Specialty, Trick


# Create your tests here.
class TestAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)
        for i in range(1, 5):
            for j in range(5):
                MegaEdge.objects.create(name=f"MegaEdge {5*i+j}", ratings=[i, i + 1])
        MegaEdge.objects.create(
            name="MegaEdge with Prereq", ratings=[2, 4], prereqs=[("MegaEdge 5", 2)]
        )

    def test_add_mega_edge(self):
        self.assertEqual(self.character.total_mega_edges(), 0)
        self.assertEqual(self.character.mega_edges.count(), 0)
        self.assertTrue(
            self.character.add_mega_edge(MegaEdge.objects.get(name="MegaEdge 5"))
        )
        self.assertEqual(self.character.total_mega_edges(), 1)
        self.assertEqual(self.character.mega_edges.count(), 1)
        self.assertFalse(
            MegaEdge.objects.get(name="MegaEdge with Prereq").check_prereqs(
                self.character
            )
        )
        self.assertTrue(
            self.character.add_mega_edge(MegaEdge.objects.get(name="MegaEdge 5"))
        )
        self.assertEqual(self.character.total_mega_edges(), 2)
        self.assertEqual(self.character.mega_edges.count(), 1)
        self.assertTrue(
            MegaEdge.objects.get(name="MegaEdge with Prereq").check_prereqs(
                self.character
            )
        )

    def test_filter_mega_edges(self):
        MegaEdge.objects.create(
            name="MegaEdge 100", ratings=[1, 2], prereqs=[("mega_might", 2)]
        )
        e2 = MegaEdge.objects.create(
            name="MegaEdge 101", ratings=[1, 2], prereqs=[("science", 2)]
        )
        e3 = MegaEdge.objects.create(name="MegaEdge 102", ratings=[1, 2])
        MegaEdge.objects.create(
            name="MegaEdge 103", ratings=[1, 2], prereqs=[("MegaEdge 102", 2)]
        )

        self.assertEqual(len(self.character.filter_mega_edges()), 21)
        self.character.add_mega_edge(e3)
        self.assertEqual(len(self.character.filter_mega_edges()), 21)
        self.assertEqual(len(self.character.filter_mega_edges(dots=1)), 6)
        self.character.mega_might = 2
        self.assertEqual(len(self.character.filter_mega_edges()), 22)
        self.character.science = 2
        self.assertEqual(len(self.character.filter_mega_edges()), 23)
        self.character.add_mega_edge(e2)
        self.assertEqual(len(self.character.filter_mega_edges()), 23)
        self.character.add_mega_edge(e3)
        self.assertEqual(len(self.character.filter_mega_edges()), 23)
        self.assertNotIn(e3, self.character.filter_mega_edges())
        m4 = MegaEdge.objects.create(
            name="MegaEdge 104", ratings=[1, 2, 3, 4, 5], prereqs=[("quantum", "dots")]
        )
        self.character.quantum = 1
        self.assertIn(m4, self.character.filter_mega_edges())
        self.character.add_mega_edge(m4)
        self.assertNotIn(m4, self.character.filter_mega_edges())
        self.character.quantum = 2
        self.assertIn(m4, self.character.filter_mega_edges())

    def test_add_mega_attribute(self):
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
                "mega_intellect": 2,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 1,
                "mega_composure": 2,
            },
        )

    def test_filter_mega_attribute(self):
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

    def test_add_power(self):
        p = Power.objects.create(name="Test Power 1", quantum_minimum=0)
        self.assertEqual(self.character.total_powers(), 0)
        self.assertTrue(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 1)
        p = Power.objects.create(name="Test Power 2", quantum_minimum=3)
        self.assertFalse(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 1)
        self.character.quantum = 3
        self.assertTrue(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 2)
        self.assertTrue(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 3)

    def test_filter_tags(self):
        p = Power.objects.create(name="Test Power")
        self.character.add_power(p)
        t1 = Tag.objects.create(name="Tag 1", ratings=[1, 2])
        t1.permitted_powers.add(p)
        t1.save()
        t2 = Tag.objects.create(name="Tag 2", ratings=[1, 2])
        t2.permitted_powers.add(p)
        t2.save()
        t3 = Tag.objects.create(name="Tag 3", ratings=[1, 2])
        t3.permitted_powers.add(p)
        t3.save()
        t4 = Tag.objects.create(name="Tag 4", ratings=[1, 2])
        self.assertEqual(len(self.character.filter_tags(p)), 3)
        self.character.add_tag(p, t1)
        self.character.add_tag(p, t1)
        self.assertEqual(len(self.character.filter_tags(p)), 2)

    def test_add_tag(self):
        p = Power.objects.create(name="Test Power")
        self.assertTrue(self.character.add_power(p))
        t1 = Tag.objects.create(name="Tag 1", ratings=[1, 2])
        t1.permitted_powers.add(p)
        t1.save()
        t2 = Tag.objects.create(name="Tag 2", ratings=[1, 2])
        t2.permitted_powers.add(p)
        t2.save()
        t3 = Tag.objects.create(name="Tag 3", ratings=[1, 2])
        t3.permitted_powers.add(p)
        t3.save()
        t4 = Tag.objects.create(name="Tag 4", ratings=[1, 2])
        self.assertFalse(self.character.add_tag(p, t4))
        self.assertTrue(self.character.add_tag(p, t1))
        self.assertEqual(self.character.tag_rating(p, t1), 1)
        self.assertTrue(self.character.add_tag(p, t1))
        self.assertEqual(self.character.tag_rating(p, t1), 2)
        self.assertFalse(self.character.add_tag(p, t1))

    def test_add_transcendance(self):
        for i in range(3):
            for level in ["low", "med", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )
        low_level = Transformation.objects.create(
            name="Low Transformation 5", level="low"
        )
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
        self.assertEqual(self.character.transformations.filter(level="low").count(), 2)
        self.assertEqual(self.character.transformations.count(), 2)
        self.character.quantum = 3
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 6)
        self.assertEqual(self.character.transformations.filter(level="med").count(), 1)
        self.assertEqual(self.character.transformations.count(), 3)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 7)
        self.assertEqual(self.character.transformations.filter(level="med").count(), 2)
        self.assertEqual(self.character.transformations.count(), 4)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 8)
        self.assertEqual(self.character.transformations.filter(level="high").count(), 1)
        self.assertEqual(self.character.transformations.count(), 5)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 9)
        self.assertEqual(self.character.transformations.filter(level="high").count(), 2)
        self.assertEqual(self.character.transformations.count(), 6)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 10)
        self.assertFalse(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 10)

    def test_add_quantum(self):
        t = Transformation.objects.create(name="Test Transformation", level="med")
        for i in range(10):
            for level in ["low", "med", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )

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
        self.assertFalse(self.character.add_quantum())
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
        for i in range(10):
            for level in ["low", "med", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )

        self.character.quantum = 3
        all_transformations = list(Transformation.objects.order_by("?"))
        for i in range(6):
            self.assertTrue(self.character.add_transformation(all_transformations[i]))
        self.assertEqual(self.character.transformations.count(), 6)
        for i in range(6, 10):
            self.assertFalse(self.character.add_transformation(all_transformations[i]))
        self.assertEqual(self.character.transformations.count(), 6)
        self.character.quantum = 5
        for i in range(6, 10):
            self.assertTrue(self.character.add_transformation(all_transformations[i]))
        self.assertEqual(self.character.transformations.count(), 10)

    def test_filter_transformation(self):
        transformation_dict = {"low": [], "med": [], "high": []}
        for i in range(10):
            for level in ["low", "med", "high"]:
                transformation_dict[level].append(
                    Transformation.objects.create(
                        name=f"{level.title()} Transformation {i}", level=level
                    )
                )
        self.character.quantum = 3
        self.character.add_transformation(transformation_dict["low"][0])
        self.character.add_transformation(transformation_dict["low"][1])
        self.character.add_transformation(transformation_dict["med"][0])
        self.assertEqual(len(self.character.filter_transformations()), 27)
        self.assertEqual(len(self.character.filter_transformations(level="low")), 8)
        self.assertEqual(len(self.character.filter_transformations(level="med")), 9)
        self.assertEqual(len(self.character.filter_transformations(level="high")), 10)

    def test_has_template(self):
        self.character.approach = "RES"
        self.character.might = 3
        self.character.dexterity = 3
        self.character.stamina = 4
        self.character.intellect = 3
        self.character.cunning = 2
        self.character.resolve = 3
        self.character.presence = 2
        self.character.manipulation = 2
        self.character.composure = 2
        e = Edge.objects.create(name="Fame", ratings=[1])
        self.assertFalse(self.character.has_template())
        self.character.quantum = 1
        self.assertFalse(self.character.has_template())
        self.character.resolve = 4
        self.assertFalse(self.character.has_template())
        self.character.add_edge(e)
        self.character.xp = 150
        self.assertTrue(self.character.has_template())

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("mega attribute"), 12)
        self.assertEqual(self.character.xp_cost("mega edge"), 12)
        self.assertEqual(self.character.xp_cost("power tag"), 12)
        self.assertEqual(self.character.xp_cost("quantum<=5"), 16)
        self.assertEqual(self.character.xp_cost("quantum>5"), 32)
        self.assertEqual(self.character.xp_cost("quantum power"), 12)
        self.assertEqual(
            self.character.xp_cost("mega attribute", transcendence=True), 6
        )
        self.assertEqual(self.character.xp_cost("mega edge", transcendence=True), 6)
        self.assertEqual(self.character.xp_cost("quantum power", transcendence=True), 6)
        # TODO: Add Transformation price decrease

    def test_spend_xp(self):
        MegaEdge.objects.create(name="MegaEdge 1", ratings=[1, 2, 3])
        p = Power.objects.create(name="Power 1")
        t = Tag.objects.create(name="Power Tag 1", ratings=[1, 2])
        t.permitted_powers.add(p)
        t.save()

        self.character.might = 4
        self.character.quantum = 4
        self.character.xp = 1000
        self.assertTrue(self.character.spend_xp("mega_might"))
        self.assertEqual(self.character.xp, 988)
        self.assertEqual(self.character.total_mega_attributes(), 1)
        self.assertTrue(self.character.spend_xp("MegaEdge 1"))
        self.assertEqual(self.character.xp, 976)
        self.assertEqual(self.character.total_mega_edges(), 1)
        self.assertTrue(self.character.spend_xp("Power 1"))
        self.assertEqual(self.character.xp, 964)
        self.assertEqual(self.character.total_powers(), 1)
        self.assertIn(Power.objects.get(name="Power 1"), self.character.powers.all())
        self.assertTrue(self.character.spend_xp("Power Tag 1", power="Power 1"))
        self.assertEqual(self.character.xp, 952)
        self.assertEqual(
            len(self.character.get_tags(Power.objects.get(name="Power 1"))), 1
        )
        self.assertTrue(self.character.spend_xp("quantum"))
        self.assertEqual(self.character.xp, 936)
        self.assertEqual(self.character.quantum, 5)
        self.assertTrue(self.character.spend_xp("quantum"))
        self.assertEqual(self.character.xp, 904)
        self.assertEqual(self.character.quantum, 6)
        self.assertTrue(self.character.spend_xp("mega_might", transcendence=True))
        self.assertEqual(self.character.xp, 898)
        self.assertEqual(self.character.total_mega_attributes(), 2)
        self.assertTrue(self.character.spend_xp("MegaEdge 1", transcendence=True))
        self.assertEqual(self.character.xp, 892)
        self.assertEqual(self.character.total_mega_edges(), 2)
        self.assertTrue(self.character.spend_xp("Power 1", transcendence=True))
        self.assertEqual(self.character.xp, 886)
        self.assertEqual(self.character.total_powers(), 2)
        # TODO: Test transformations to decrease cost


class TestRandomAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", player=self.player.tc_profile)
        for skill in self.character.get_skills().keys():
            for i in range(5):
                Specialty.objects.create(name=f"{skill} Specialty {i}", skill=skill)
                Trick.objects.create(name=f"{skill} Trick {i}", skill=skill)
        for t in ["origin", "role", "society"]:
            for k in range(3):
                p = Path.objects.create(name=f"{t} Path {k}", type=t)
                for i in range(4):
                    for j in range(4):
                        p.skills.append(
                            list(self.character.get_skills().keys())[4 * i + j]
                        )
                        p.gift_keywords.append(
                            list(self.character.get_skills().keys())[4 * i + j]
                        )
                        p.edges.add(
                            Edge.objects.create(
                                name=f"{t} Edge {4*j+i}, {k}", ratings=[i + 1, i + 2]
                            )
                        )
                    p.save()
        for i in range(10):
            for level in ["low", "med", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )

        p1 = Power.objects.create(name="Power Test 1", quantum_minimum=0)
        p2 = Power.objects.create(name="Power Test 2", quantum_minimum=2)
        p3 = Power.objects.create(name="Power Test 3", quantum_minimum=3)
        p4 = Power.objects.create(name="Power Test 4", quantum_minimum=1)

        p = [p1, p2, p3, p4]

        for i, ratings in enumerate([[1, 2], [2, 4], [2], [1]]):
            t = Tag.objects.create(name=f"Tag {i}", ratings=ratings)
            for j in ratings:
                t.permitted_powers.add(p[j - 1])

        for i in range(4):
            for j in range(4):
                if i != j:
                    MegaEdge.objects.create(name=f"MegaEdge{4*i+j}", ratings=[i, j])
                else:
                    MegaEdge.objects.create(name=f"MegaEdge{4*i+j}", ratings=[i])


def test_random_mega_attribute(self):
    num = self.character.total_mega_attributes()
    self.character.random_mega_attribute()
    self.assertEqual(self.character.total_mega_attributes(), num + 1)


def test_random_mega_edge(self):
    num = self.character.total_mega_edges()
    self.character.random_mega_edge(dots=1)
    self.assertEqual(self.character.total_mega_edges(), num + 1)


def test_random_power_tag(self):
    self.character.random_power()
    p = self.character.powers.first()
    self.assertEqual(len(self.character.get_tags(p)), 0)
    self.character.random_tag(p)
    self.assertEqual(len(self.character.get_tags(p)), 1)


def test_random_power(self):
    num = self.character.total_powers()
    self.character.random_power()
    self.assertEqual(self.character.total_powers(), num + 1)


def test_random_template_choices(self):
    self.character.random_attributes()
    self.character.random_paths()
    self.assertFalse(self.character.has_template())
    self.character.apply_random_template()
    self.assertTrue(self.character.has_template())


def test_random_xp_spend(self):
    self.character.xp = 15
    self.character.random_xp_spend()
    self.assertLess(self.character.xp, 15)


def test_random(self):
    character = Aberrant.objects.create(player=self.player.tc_profile)
    self.assertFalse(character.has_name())
    self.assertFalse(character.has_concept())
    self.assertFalse(character.has_paths())
    self.assertFalse(character.has_aspirations())
    self.assertFalse(character.has_attributes())
    self.assertFalse(character.has_skills())
    self.assertFalse(character.has_basics())
    self.assertFalse(character.has_template())
    character.xp = 0
    character.random()
    self.assertTrue(character.has_name())
    self.assertTrue(character.has_concept())
    self.assertTrue(character.has_paths())
    self.assertTrue(character.has_aspirations())
    self.assertTrue(character.has_attributes(template=True))
    self.assertTrue(character.has_skills())
    self.assertTrue(character.has_specialties())
    self.assertTrue(character.has_tricks())
    self.assertTrue(character.has_basics())
    self.assertTrue(character.has_template())


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
