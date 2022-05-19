from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character.human import Edge, EnhancedEdge, Path, Specialty, Trick
from tc.models.character.talent import Gift, Talent


# Create your tests here.
class TestTalent(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Talent.objects.create(name="", player=self.player.tc_profile)

    def test_add_moment_of_inspiration(self):
        self.assertFalse(self.character.has_moment_of_inspiration())
        self.assertTrue(self.character.add_moment_of_inspiration("Got Inspired"))
        self.assertTrue(self.character.has_moment_of_inspiration())

    def test_has_moment_of_inspiration(self):
        self.character.moment_of_inspiration = ""
        self.assertFalse(self.character.has_moment_of_inspiration())
        self.character.moment_of_inspiration = "Inspired!"
        self.assertTrue(self.character.has_moment_of_inspiration())

    def test_add_inspiration(self):
        self.assertEqual(self.character.inspiration, 1)
        self.assertTrue(self.character.add_inspiration())
        self.assertEqual(self.character.inspiration, 2)
        self.character.inspiration = 10
        self.assertFalse(self.character.add_inspiration())
        self.assertEqual(self.character.inspiration, 10)

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
        g1 = Gift.objects.create(name="Gift 1", keywords=["science"])
        self.character.add_gift(g1)
        self.assertFalse(self.character.has_gifts())
        g2 = Gift.objects.create(name="Gift 1", keywords=["larcey"])
        self.character.add_gift(g2)
        self.assertFalse(self.character.has_gifts())
        g3 = Gift.objects.create(name="Gift 1", keywords=["command"])
        self.character.add_gift(g3)
        self.assertFalse(self.character.has_gifts())
        g4 = Gift.objects.create(name="Gift 1", keywords=["science"])
        self.character.add_gift(g4)
        self.assertTrue(self.character.has_gifts())

    def test_filter_gifts(self):
        # Filter by keyword the gifts a character doesn't have
        # Filter by Path using its keywords
        self.fail()
        # Gifts are name, keyword, prereqs
        # aptitude in skill or attribute require 1 dot
        # perhaps keyword should just be Constant or Momentary, and aptitude should be managed via prereq?
        # aptitude is tied to path
        # Eh, just use keywords

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
            name="XP Path", skills=["science", "technology", "command", "close_combat"]
        )
        p.edges.add(pe)
        p.save()

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
        # Buy path gift
        # buy regular gift
        # buy a facet


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
