from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.human import Edge, EnhancedEdge, Path, Specialty, Trick
from tc.models.character.talent import Gift, MomentOfInspiration, Talent


# Create your tests here.
class TestTalent(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Talent.objects.create(name="", player=self.player.tc_profile)

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
        g = Gift.objects.create(name="Test Gift", keywords=[], prereqs=[])
        self.assertEqual(self.character.total_gifts(), 0)
        self.assertTrue(self.character.add_gift(g))
        self.assertEqual(self.character.total_gifts(), 1)
        self.assertFalse(self.character.add_gift(g))
        self.assertEqual(self.character.total_gifts(), 1)

    def test_has_gifts(self):
        p1 = Path.objects.create(
            name="Path 1", type="origin", gift_keywords=["science"]
        )
        p2 = Path.objects.create(
            name="Path 2", type="role", gift_keywords=["science", "larceny"]
        )
        p3 = Path.objects.create(
            name="Path 3", type="society", gift_keywords=["science", "command"]
        )
        self.character.add_path(p1)
        self.character.add_path(p2)
        self.character.add_path(p3)
        g1 = Gift.objects.create(name="Gift 1", keywords=["science"])
        self.character.add_gift(g1)
        self.assertFalse(self.character.has_gifts())
        g2 = Gift.objects.create(name="Gift 2", keywords=["larceny"])
        self.character.add_gift(g2)
        self.assertFalse(self.character.has_gifts())
        g3 = Gift.objects.create(name="Gift 3", keywords=["command"])
        self.character.add_gift(g3)
        self.assertFalse(self.character.has_gifts())
        g4 = Gift.objects.create(name="Gift 4", keywords=["science"])
        self.character.add_gift(g4)
        self.assertTrue(self.character.has_gifts())

    def test_filter_gifts(self):
        g = Gift.objects.create(name="Gift 1", keywords=["science"], prereqs=[])
        Gift.objects.create(name="Gift 2", keywords=[], prereqs=[("might", 3)])
        Gift.objects.create(name="Gift 3", keywords=["dexterity"], prereqs=[])
        Gift.objects.create(name="Gift 4", keywords=["luck"], prereqs=[])
        Gift.objects.create(name="Gift 5", keywords=[], prereqs=[])
        Gift.objects.create(
            name="Gift 6", keywords=["dexterity", "science"], prereqs=[]
        )

        p = Path.objects.create(name="Path", gift_keywords=["science"])

        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=None)), 2)
        self.character.add_skill("science")
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=None)), 4)
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=p)), 2)
        self.assertEqual(
            len(self.character.filter_gifts(keyword="science", path=None)), 2
        )
        self.assertEqual(len(self.character.filter_gifts(keyword="luck", path=None)), 1)
        self.character.add_gift(g)
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=None)), 3)
        self.assertEqual(len(self.character.filter_gifts(keyword=None, path=p)), 1)
        self.assertEqual(
            len(self.character.filter_gifts(keyword="science", path=None)), 1
        )
        self.assertEqual(len(self.character.filter_gifts(keyword="luck", path=None)), 1)

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

        ee = EnhancedEdge.objects.create(
            name="XP Enhanced Edge", prereqs=[("XP Edge 1", 2)]
        )

        p = Path.objects.create(
            name="XP Path",
            skills=["science", "technology", "command", "close_combat"],
            gift_keywords=["science"],
        )
        p.edges.add(pe)
        p.save()

        Gift.objects.create(name="Test Path Gift", keywords=["science"])
        Gift.objects.create(name="Test Gift", keywords=["athletics"])

        self.character.approach = "RES"

        self.character.add_path(p)

        self.character.xp = 1000
        self.assertTrue(self.character.spend_xp("might"))
        self.assertEqual(self.character.xp, 990)
        self.assertEqual(self.character.might, 2)
        self.assertTrue(self.character.spend_xp("XP Edge 1"))
        self.assertEqual(self.character.xp, 987)
        self.assertEqual(self.character.edge_rating("XP Edge 1"), 1)
        self.assertTrue(self.character.spend_xp("XP Edge 2"))
        self.assertEqual(self.character.xp, 978)
        self.assertEqual(self.character.edge_rating("XP Edge 2"), 3)
        self.assertTrue(self.character.spend_xp("XP Edge 1"))
        self.assertEqual(self.character.xp, 975)
        self.assertEqual(self.character.edge_rating("XP Edge 1"), 2)
        self.assertTrue(self.character.spend_xp("XP Path Edge"))
        self.assertEqual(self.character.xp, 971)
        self.assertEqual(self.character.edge_rating("XP Path Edge"), 2)
        self.assertTrue(self.character.spend_xp("XP Enhanced Edge"))
        self.assertEqual(self.character.xp, 965)
        self.assertEqual(self.character.enhanced_edges.first(), ee)
        self.assertTrue(self.character.spend_xp("science"))
        self.assertEqual(self.character.xp, 960)
        self.assertEqual(self.character.science, 1)
        self.assertTrue(self.character.spend_xp("XP Trick"))
        self.assertEqual(self.character.xp, 957)
        self.assertEqual(self.character.tricks.count(), 1)
        self.assertTrue(self.character.spend_xp("XP Specialty"))
        self.assertEqual(self.character.xp, 954)
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertTrue(self.character.spend_xp("XP Path"))
        self.assertEqual(self.character.xp, 936)
        self.assertEqual(self.character.path_rating("XP Path"), 2)
        self.assertTrue(self.character.spend_xp("Favor FIN"))
        self.assertEqual(self.character.xp, 921)
        self.assertEqual(self.character.approach, "FIN")
        self.assertTrue(self.character.spend_xp("Test Path Gift"))
        self.assertEqual(self.character.xp, 917)
        self.assertEqual(self.character.total_gifts(), 1)
        self.assertTrue(self.character.spend_xp("Test Gift"))
        self.assertEqual(self.character.xp, 912)
        self.assertEqual(self.character.total_gifts(), 2)
        num = self.character.reflective
        self.assertTrue(self.character.spend_xp("Reflective"))
        self.assertEqual(self.character.xp, 902)
        self.assertEqual(self.character.reflective, num + 1)


class TestRandomTalent(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Talent.objects.create(name="", player=self.player.tc_profile)
        for skill in self.character.get_skills().keys():
            for i in range(5):
                Specialty.objects.create(name=f"{skill} Specialty {i}", skill=skill)
                Trick.objects.create(name=f"{skill} Trick {i}", skill=skill)
                Gift.objects.create(name=f"{skill} Gift {i}", keywords=[skill])
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

    def test_random_template_choices(self):
        self.character.random_paths()
        for skill in self.character.get_skills():
            self.character.add_skill(skill)
        self.assertFalse(self.character.has_template())
        self.character.apply_random_template()
        self.assertTrue(self.character.has_template())

    def test_random_xp_spend(self):
        self.character.xp = 15
        self.character.random_xp_spend()
        self.assertLess(self.character.xp, 15)

    def test_random_moment_of_inspiration(self):
        self.assertFalse(self.character.has_moment_of_inspiration())
        self.character.random_moment_of_inspiration()
        self.assertTrue(self.character.has_moment_of_inspiration())

    def test_random(self):
        character = Talent.objects.create(player=self.player.tc_profile)
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
            name="Test Character",
            player=User.objects.get(username="Test User").tc_profile,
        )

    def test_talent_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_talent_detail_view_template(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "tc/characters/talent/detail.html")
