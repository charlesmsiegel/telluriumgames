from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.characters.human import (
    Edge,
    EnhancedEdge,
    PathConnection,
    Specialty,
    TCPath,
    Trick,
)
from tc.models.characters.talent import MomentOfInspiration, Talent, TCGift


# Create your tests here.
class TestTalent(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Talent.objects.create(name="", owner=self.player)
        self.moment = MomentOfInspiration.objects.create(name="", attributes=["might"])

    def test_add_moment_of_inspiration(self):
        m = MomentOfInspiration.objects.create(
            name="Got Inspired", attributes=["might"]
        )
        self.assertFalse(self.character.has_moment_of_inspiration())
        self.assertTrue(self.character.add_moment_of_inspiration(m))
        self.assertTrue(self.character.has_moment_of_inspiration())

    def test_has_moment_of_inspiration(self):
        m = MomentOfInspiration.objects.create(
            name="Got Inspired", attributes=["might"]
        )
        self.assertFalse(self.character.has_moment_of_inspiration())
        self.character.moment_of_inspiration = m
        self.assertTrue(self.character.has_moment_of_inspiration())

    def test_has_template(self):
        self.assertFalse(self.character.has_template())

        # Create the necessary paths, gifts, and moment of inspiration
        path_origin = TCPath.objects.create(
            name="Origin Path", type="origin", gift_keywords=["o"]
        )
        path_role = TCPath.objects.create(
            name="Role Path", type="role", gift_keywords=["r"]
        )
        path_society = TCPath.objects.create(
            name="Society Path", type="society", gift_keywords=["s"]
        )

        self.character.might = 5
        self.character.intellect = 5
        self.character.cunning = 5
        self.character.presence = 5

        gift1 = TCGift.objects.create(name="Gift1", keywords=["o"])
        gift2 = TCGift.objects.create(name="Gift2", keywords=["r"])
        gift3 = TCGift.objects.create(name="Gift3", keywords=["s"])
        gift4 = TCGift.objects.create(name="Gift4")

        moment_of_inspiration = MomentOfInspiration.objects.create(name="Inspiration 1")

        # Assign created objects to the character
        self.character.paths.add(path_origin, path_role, path_society)
        self.character.add_gift(gift1)
        self.character.add_gift(gift2)
        self.character.add_gift(gift3)
        self.character.add_gift(gift4)

        self.character.add_moment_of_inspiration(moment_of_inspiration)

        self.character.add_facet("intuitive")
        self.character.add_facet("reflective")
        self.character.add_facet("destructive")

        # Check if the character has a template
        self.assertTrue(self.character.has_template())

    def test_add_facet(self):
        self.assertEqual(self.character.inspiration, 1)
        self.assertTrue(self.character.add_facet("Intuitive"))
        self.assertEqual(self.character.intuitive, 1)
        self.assertEqual(self.character.destructive, 0)
        self.assertEqual(self.character.reflective, 0)
        self.assertEqual(self.character.inspiration, 2)
        self.assertTrue(self.character.add_facet("Reflective"))
        self.assertEqual(self.character.intuitive, 1)
        self.assertEqual(self.character.destructive, 0)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 3)
        self.assertTrue(self.character.add_facet("Destructive"))
        self.assertEqual(self.character.intuitive, 1)
        self.assertEqual(self.character.destructive, 1)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 4)
        self.assertTrue(self.character.add_facet("Intuitive"))
        self.assertEqual(self.character.intuitive, 2)
        self.assertEqual(self.character.destructive, 1)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 4)
        self.assertTrue(self.character.add_facet("Destructive"))
        self.assertEqual(self.character.intuitive, 2)
        self.assertEqual(self.character.destructive, 2)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 4)
        self.assertTrue(self.character.add_facet("Intuitive"))
        self.assertEqual(self.character.intuitive, 3)
        self.assertEqual(self.character.destructive, 2)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 5)
        self.assertTrue(self.character.add_facet("Intuitive"))
        self.assertEqual(self.character.intuitive, 4)
        self.assertEqual(self.character.destructive, 2)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 5)
        self.assertTrue(self.character.add_facet("Destructive"))
        self.assertEqual(self.character.intuitive, 4)
        self.assertEqual(self.character.destructive, 3)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 6)
        self.assertTrue(self.character.add_facet("Intuitive"))
        self.assertEqual(self.character.intuitive, 5)
        self.assertEqual(self.character.destructive, 3)
        self.assertEqual(self.character.reflective, 1)
        self.assertEqual(self.character.inspiration, 7)
        self.assertFalse(self.character.add_facet("Intuitive"))
        self.assertEqual(self.character.intuitive, 5)
        self.assertEqual(self.character.destructive, 3)
        self.assertEqual(self.character.reflective, 1)

    def test_has_facets(self):
        self.character.add_facet("Intuitive")
        self.assertFalse(self.character.has_facets())
        self.character.add_facet("Reflective")
        self.assertFalse(self.character.has_facets())
        self.character.add_facet("Reflective")
        self.assertTrue(self.character.has_facets())

    def test_add_gift(self):
        g = TCGift.objects.create(name="Test Gift")
        self.assertEqual(self.character.total_gifts(), 0)
        self.assertTrue(self.character.add_gift(g))
        self.assertEqual(self.character.total_gifts(), 1)
        self.assertFalse(self.character.add_gift(g))
        self.assertEqual(self.character.total_gifts(), 1)

    def test_has_gifts(self):
        p1 = TCPath.objects.create(
            name="Path 1", type="origin", gift_keywords=["science"]
        )
        p2 = TCPath.objects.create(
            name="Path 2", type="role", gift_keywords=["science", "larceny"]
        )
        p3 = TCPath.objects.create(
            name="Path 3", type="society", gift_keywords=["science", "command"]
        )
        self.character.add_path(p1)
        self.character.add_path(p2)
        self.character.add_path(p3)
        g1 = TCGift.objects.create(name="Gift 1", keywords=["science"])
        self.character.add_gift(g1)
        self.assertFalse(self.character.has_gifts())
        g2 = TCGift.objects.create(name="Gift 2", keywords=["larceny"])
        self.character.add_gift(g2)
        self.assertFalse(self.character.has_gifts())
        g3 = TCGift.objects.create(name="Gift 3", keywords=["command"])
        self.character.add_gift(g3)
        self.assertFalse(self.character.has_gifts())
        g4 = TCGift.objects.create(name="Gift 4", keywords=["science"])
        self.character.add_gift(g4)
        self.assertTrue(self.character.has_gifts())

    def test_filter_gifts(self):
        g = TCGift.objects.create(name="Gift 1", keywords=["science"])
        TCGift.objects.create(name="Gift 2", prereqs=[[("might", 3)]])
        TCGift.objects.create(name="Gift 3", keywords=["dexterity"])
        TCGift.objects.create(name="Gift 4", keywords=["luck"])
        TCGift.objects.create(name="Gift 5")
        TCGift.objects.create(name="Gift 6", keywords=["dexterity", "science"])

        p = TCPath.objects.create(name="Path", gift_keywords=["science"])

        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=None)), 4)
        self.character.add_skill("science")
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=None)), 5)
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=p)), 2)
        self.assertEqual(
            len(self.character.filter_gifts(keyword="science", path=None)), 2
        )
        self.assertEqual(len(self.character.filter_gifts(keyword="luck", path=None)), 1)
        self.character.add_gift(g)
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=None)), 4)
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=p)), 1)
        self.assertEqual(
            len(self.character.filter_gifts(keyword="science", path=None)), 1
        )
        self.assertEqual(len(self.character.filter_gifts(keyword="luck", path=None)), 1)

    def test_total_gifts(self):
        gift1 = TCGift.objects.create(name="Gift1")
        gift2 = TCGift.objects.create(name="Gift2")

        self.character.add_gift(gift1)
        self.character.add_gift(gift2)

        self.assertEqual(self.character.total_gifts(), 2)

    def test_total_facets(self):
        self.assertEqual(self.character.total_facets(), 0)

        self.character.add_facet("intuitive")
        self.assertEqual(self.character.total_facets(), 1)

        self.character.add_facet("reflective")
        self.assertEqual(self.character.total_facets(), 2)

        self.character.add_facet("destructive")
        self.assertEqual(self.character.total_facets(), 3)

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
        self.assertEqual(self.character.xp_cost("path gift"), 4)
        self.assertEqual(self.character.xp_cost("gift"), 5)
        self.assertEqual(self.character.xp_cost("facet"), 10)

    def test_spend_xp(self):
        Edge.objects.create(name="XP Edge 1", ratings=[1, 2])
        Edge.objects.create(name="XP Edge 2", ratings=[3])
        pe = Edge.objects.create(name="XP Path Edge", ratings=[2])

        Trick.objects.create(name="XP Trick", skill="science")
        Specialty.objects.create(name="XP Specialty", skill="science")

        EnhancedEdge.objects.create(
            name="XP Enhanced Edge", prereqs=[[("XP Edge 1", 2)]]
        )

        p = TCPath.objects.create(
            name="XP Path",
            skills=["science", "technology", "command", "close_combat"],
            gift_keywords=["science"],
        )
        p.edges.add(pe)
        p.save()

        TCGift.objects.create(name="Test Path Gift", keywords=["science"])
        TCGift.objects.create(name="Test Gift", keywords=["athletics"])

        self.character.approach = "RES"

        self.character.add_path(p)

        self.character.xp = 1000
        self.character.add_skill("science")
        self.assertTrue(self.character.spend_xp("Test Path Gift"))
        self.assertEqual(self.character.xp, 996)
        self.assertEqual(self.character.total_gifts(), 1)
        self.character.add_skill("athletics")
        self.assertTrue(self.character.spend_xp("Test Gift"))
        self.assertEqual(self.character.xp, 991)
        self.assertEqual(self.character.total_gifts(), 2)
        num = self.character.reflective
        self.assertTrue(self.character.spend_xp("Reflective"))
        self.assertEqual(self.character.xp, 981)
        self.assertEqual(self.character.reflective, num + 1)


class TestRandomTalent(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Talent.objects.create(name="", owner=self.player)
        for skill in self.character.get_skills().keys():
            for i in range(5):
                Specialty.objects.create(name=f"{skill} Specialty {i}", skill=skill)
                Trick.objects.create(name=f"{skill} Trick {i}", skill=skill)
                TCGift.objects.create(name=f"{skill} Gift {i}", keywords=[skill])
        for t in ["origin", "role", "society"]:
            for k in range(3):
                p = TCPath.objects.create(name=f"{t} Path {k}", type=t)
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
        MomentOfInspiration.objects.create(
            name="MOI 1", attributes=["might", "dexterity", "stamina"]
        )
        MomentOfInspiration.objects.create(
            name="MOI 2", attributes=["intellect", "cunning", "resolve"]
        )
        MomentOfInspiration.objects.create(
            name="MOI 3", attributes=["presence", "manipulation", "composure"]
        )

    def test_random_facets(self):
        self.assertFalse(self.character.has_facets())
        self.character.random_facets()
        self.assertTrue(self.character.has_facets())

    def test_random_gifts(self):
        self.character.random_paths()
        for skill in self.character.get_skills():
            self.character.add_skill(skill)
        self.assertFalse(self.character.has_gifts())
        self.character.random_gifts()
        self.assertTrue(self.character.has_gifts())

    def test_apply_random_template(self):
        self.character.random_attributes()
        self.character.random_paths()
        for skill in self.character.get_skills():
            self.character.add_skill(skill)
        self.assertFalse(self.character.has_template())
        self.character.apply_random_template()
        self.assertTrue(self.character.has_template())

    def test_random_spend_xp(self):
        self.character.xp = 15
        self.character.random_spend_xp()
        self.assertLess(self.character.xp, 15)

    def test_random_moment_of_inspiration(self):
        self.assertFalse(self.character.has_moment_of_inspiration())
        self.character.random_moment_of_inspiration()
        self.assertTrue(self.character.has_moment_of_inspiration())

    def test_random_path(self):
        self.character.random_path()
        self.assertEqual(self.character.paths.count(), 1)

    def test_random(self):
        character = Talent.objects.create(owner=self.player)
        self.assertFalse(character.has_name())
        self.assertFalse(character.has_concept())
        self.assertFalse(character.has_paths())
        self.assertFalse(character.has_aspirations())
        self.assertFalse(character.has_attributes())
        self.assertFalse(character.has_skills())
        self.assertFalse(character.has_basics())
        self.assertFalse(character.has_gifts())
        self.assertFalse(character.has_facets())
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
        self.assertTrue(character.has_gifts())
        self.assertTrue(character.has_facets())
        self.assertTrue(character.has_template())


class TestTalentDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.character = Talent.objects.create(
            name="Test Character", owner=User.objects.get(username="Test User"),
        )

    def test_talent_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_talent_detail_view_template(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "tc/characters/talent/talent/detail.html")


class TestGift(TestCase):
    def setUp(self):
        self.gift = TCGift.objects.create()
        self.character = Talent.objects.create()

    def test_check_prereqs(self):
        self.gift.prereqs = [[("might", 2), ("aim", 1)]]
        self.assertFalse(self.gift.check_prereqs(self.character))
        self.character.add_attribute("might")
        self.assertFalse(self.gift.check_prereqs(self.character))
        self.character.add_skill("aim")
        self.assertTrue(self.gift.check_prereqs(self.character))

    def test_prereq_satisfied(self):
        # attribute
        prereq = ("might", 3)
        self.assertFalse(self.gift.prereq_satisfied(prereq, self.character))
        self.character.add_attribute("might")
        self.assertFalse(self.gift.prereq_satisfied(prereq, self.character))
        self.character.add_attribute("might")
        self.assertTrue(self.gift.prereq_satisfied(prereq, self.character))
        # skill
        prereq = ("aim", 2)
        self.assertFalse(self.gift.prereq_satisfied(prereq, self.character))
        self.character.add_skill("aim")
        self.assertFalse(self.gift.prereq_satisfied(prereq, self.character))
        self.character.add_skill("aim")
        self.assertTrue(self.gift.prereq_satisfied(prereq, self.character))
        # edge
        edge = Edge.objects.create(name="Test Edge", ratings=[1, 2, 3])
        prereq = ("Test Edge", 2)
        self.assertFalse(self.gift.prereq_satisfied(prereq, self.character))
        self.character.add_edge(edge)
        self.assertFalse(self.gift.prereq_satisfied(prereq, self.character))
        self.character.add_edge(edge)
        self.assertTrue(self.gift.prereq_satisfied(prereq, self.character))
