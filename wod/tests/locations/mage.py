from unittest import mock
from unittest.mock import Mock, patch

from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Language, Material, Medium, Noun
from wod.models.characters.human import Human
from wod.models.characters.mage import (
    Effect,
    Instrument,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
)
from wod.models.characters.mage.cabal import Cabal
from wod.models.characters.mage.utils import ABILITY_LIST, SPHERE_LIST
from wod.models.items.mage import Grimoire
from wod.models.locations.mage import Chantry, Library, Node, NodeMeritFlaw
from wod.models.locations.mage.nodes import NodeMeritFlawRating, NodeResonanceRating
from wod.tests.characters.mage import mage_setup
from wod.tests.items.mage import grimoire_setup


# Create your tests here.
class TestNode(TestCase):
    def setUp(self):
        for i in range(1, 11):
            Resonance.objects.create(name=f"Resonance {i}")
        for i in range(1, 6):
            for j in [1, -1]:
                if j == 1:
                    t = "Merit"
                else:
                    t = "Flaw"
                NodeMeritFlaw.objects.create(name=f"Node {t} {i}", ratings=[i * j])
        self.node = Node.objects.create(name="Test Node")
        for i in range(10):
            Noun.objects.create(name=f"Node Noun {i}")

    # def test_gauntlet_rating(self):
    #     self.assertEqual(self.node.gauntlet, 3)

    def test_add_resonance(self):
        res = Resonance.objects.order_by("?").first()
        self.assertEqual(self.node.resonance_rating(res), 0)
        self.assertTrue(self.node.add_resonance(res))
        self.assertEqual(self.node.resonance_rating(res), 1)

    def test_filter_resonance(self):
        self.assertEqual(len(self.node.filter_resonance()), 10)
        for res in Resonance.objects.order_by("?")[:3]:
            self.assertTrue(self.node.add_resonance(res))
        self.assertEqual(len(self.node.filter_resonance(maximum=0)), 7)

    def test_total_resonance(self):
        resonance = Resonance.objects.order_by("?")[:2]
        for res in resonance:
            self.node.add_resonance(res)
            self.node.add_resonance(res)
        self.assertEqual(self.node.total_resonance(), 4)
        self.assertNotEqual(self.node.total_resonance(), 5)
        self.node.add_resonance(resonance[1])
        self.assertEqual(self.node.total_resonance(), 5)

    def test_check_resonance(self):
        r = Resonance.objects.create(name="Test Res")
        self.assertTrue(self.node.check_resonance(r))
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.node.add_resonance(r)
        self.assertFalse(self.node.check_resonance(r))
        r2 = Resonance.objects.create(name="Test Res 2", forces=True)
        self.assertFalse(self.node.check_resonance(r2, sphere="life"))
        self.assertTrue(self.node.check_resonance(r2, sphere="forces"))
        self.assertTrue(self.node.check_resonance(r2))
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.node.add_resonance(r2)
        self.assertFalse(self.node.check_resonance(r2, sphere="forces"))

    def test_has_resonance(self):
        self.node.rank = 1
        resonance = Resonance.objects.create(name="Test Resonance")
        self.node.add_resonance(resonance)
        self.assertTrue(self.node.has_resonance())

    def test_resonance_rating(self):
        resonance = Resonance.objects.create(name="Test Resonance")
        rating = 3
        NodeResonanceRating.objects.create(
            node=self.node, resonance=resonance, rating=rating
        )
        self.assertEqual(self.node.resonance_rating(resonance), rating)

    def test_set_rank(self):
        self.assertEqual(self.node.rank, 0)
        self.assertTrue(self.node.set_rank(3))
        self.assertEqual(self.node.rank, 3)
        self.assertEqual(self.node.points, 9)

    def test_resonance_postprocessing(self):
        merit1 = NodeMeritFlaw.objects.create(name="Corrupted", ratings=[0])
        merit2 = NodeMeritFlaw.objects.create(name="Sphere Attuned", ratings=[0])
        Resonance.objects.create(name="Corrupted")
        Resonance.objects.create(
            name="Sphered",
            correspondence=True,
            entropy=True,
            forces=True,
            matter=True,
            life=True,
            time=True,
            prime=True,
            spirit=True,
            mind=True,
        )
        self.node.merits_and_flaws.add(merit1)
        self.node.merits_and_flaws.add(merit2)
        self.node.save()
        self.node.resonance_postprocessing()
        self.assertEqual(self.node.total_resonance(), 3)
        self.assertIn("Corrupted", [x.name for x in self.node.resonance.all()])
        self.assertIn("Sphered", [x.name for x in self.node.resonance.all()])

    def test_add_mf(self):
        num = self.node.total_mf()
        self.assertFalse(
            self.node.add_mf(NodeMeritFlaw.objects.get(name="Node Merit 3"), 4)
        )
        self.assertTrue(
            self.node.add_mf(NodeMeritFlaw.objects.get(name="Node Merit 3"), 3)
        )
        self.assertEqual(self.node.total_mf(), num + 3)

    def test_filter_mf(self):
        self.assertEqual(len(self.node.filter_mf()), 10)
        self.assertEqual(len(self.node.filter_mf(minimum=0)), 5)
        for mf in NodeMeritFlaw.objects.all():
            if "Merit" in mf.name:
                self.node.add_mf(mf, mf.ratings[0])
        self.assertEqual(len(self.node.filter_mf()), 5)
        self.assertEqual(len(self.node.filter_mf(maximum=0)), 5)
        for mf in NodeMeritFlaw.objects.all():
            if "Flaw" in mf.name:
                self.node.add_mf(mf, mf.ratings[0])
        self.assertEqual(len(self.node.filter_mf()), 0)

    def test_total_mf(self):
        self.assertEqual(self.node.total_mf(), 0)
        self.node.add_mf(NodeMeritFlaw.objects.get(name="Node Merit 3"), 3)
        self.assertEqual(self.node.total_mf(), 3)
        self.node.add_mf(NodeMeritFlaw.objects.get(name="Node Flaw 2"), -2)
        self.assertEqual(self.node.total_mf(), 1)

    def test_mf_rating(self):
        mf = NodeMeritFlaw.objects.create(name="Test MF", ratings=[1, 2, 3])
        rating = 2
        NodeMeritFlawRating.objects.create(node=self.node, mf=mf, rating=rating)
        self.assertEqual(self.node.mf_rating(mf), rating)

    def test_set_size(self):
        self.assertEqual(self.node.size, 0)
        self.assertEqual(self.node.get_size_display(), "Average Room")
        self.assertTrue(self.node.set_size(2))
        self.assertEqual(self.node.size, 2)
        self.assertEqual(self.node.get_size_display(), "Large Building")
        self.assertTrue(self.node.set_size(-2))
        self.assertEqual(self.node.size, -2)
        self.assertEqual(self.node.get_size_display(), "Household Object")

    def test_set_ratio(self):
        self.assertEqual(self.node.ratio, 0)
        self.assertEqual(self.node.get_ratio_display(), "0.5")
        self.assertTrue(self.node.set_ratio(2))
        self.assertEqual(self.node.ratio, 2)
        self.assertEqual(self.node.get_ratio_display(), "1.0")
        self.assertTrue(self.node.set_ratio(-2))
        self.assertEqual(self.node.ratio, -2)
        self.assertEqual(self.node.get_ratio_display(), "0.0")

    def test_update_output(self):
        self.node.set_rank(2)
        self.assertEqual(self.node.ratio, 0)
        self.node.update_output()
        self.assertEqual(self.node.quintessence_per_week, 3)
        self.assertEqual(self.node.tass_per_week, 3)
        self.node.set_ratio(1)
        self.assertEqual(self.node.ratio, 1)
        self.node.update_output()
        self.assertEqual(self.node.quintessence_per_week, 4)
        self.assertEqual(self.node.tass_per_week, 2)

    def test_has_output_forms(self):
        self.assertFalse(self.node.has_output_forms())
        self.node.set_output_forms("Quintessence", "Tass")
        self.assertTrue(self.node.has_output_forms())

    def test_set_output_forms(self):
        self.assertFalse(self.node.has_output_forms())
        self.assertTrue(self.node.set_output_forms("Quintessence", "Tass"))
        self.assertTrue(self.node.has_output_forms())

    def test_has_output(self):
        self.node.random_rank()
        self.assertFalse(self.node.has_output())
        self.node.update_output()
        self.assertTrue(self.node.has_output())


class TestRandomNode(TestCase):
    def setUp(self):
        for i in range(1, 11):
            Resonance.objects.create(name=f"Resonance {i}")
        for i in range(1, 6):
            for j in [1, -1]:
                if j == 1:
                    t = "Merit"
                else:
                    t = "Flaw"
                NodeMeritFlaw.objects.create(name=f"Node {t} {i}", ratings=[i * j])
        self.node = Node.objects.create(name="")
        for i in range(10):
            Noun.objects.create(name=f"Node Noun {i}")

    def test_random_name(self):
        self.assertFalse(self.node.has_name())
        self.node.random_name()
        self.assertTrue(self.node.has_name())

    def test_random_rank(self):
        self.assertEqual(self.node.rank, 0)
        self.node.random_rank()
        self.assertNotEqual(self.node.rank, 0)

    def test_random_resonance(self):
        self.assertEqual(self.node.total_resonance(), 0)
        self.node.random_resonance()
        self.assertEqual(self.node.total_resonance(), 1)

    def test_random_mf(self):
        num = self.node.total_mf()
        while not self.node.random_mf(minimum=0):
            assert False
        self.assertGreater(self.node.total_mf(), num)

    def test_random_size(self):
        mocker = Mock()
        mocker.side_effect = [0, 2]
        with mock.patch("random.choice", mocker):
            self.node.random_size()
            self.assertEqual(self.node.size, 0)
            self.node.random_size()
            self.assertEqual(self.node.size, 2)

    def test_random_ratio(self):
        mocker = Mock()
        mocker.side_effect = [0, 2]
        with mock.patch("random.choice", mocker):
            self.node.random_ratio()
            self.assertEqual(self.node.ratio, 0)
            self.node.random_ratio()
            self.assertEqual(self.node.ratio, 2)

    def test_random_forms(self):
        self.assertFalse(self.node.has_output_forms())
        self.node.random_forms()
        self.assertTrue(self.node.has_output_forms())

    def test_random(self):
        self.assertEqual(self.node.points, 0)
        self.node.random()
        self.assertGreaterEqual(self.node.total_resonance(), self.node.rank)
        self.assertNotEqual(self.node.rank, 0)
        self.assertEqual(self.node.points, 0)
        self.assertTrue(self.node.has_resonance())
        self.assertTrue(self.node.has_output_forms())
        self.assertTrue(self.node.has_output())


class TestNodeMeritFlaw(TestCase):
    def test_save(self):
        m = NodeMeritFlaw.objects.create(name="TestMF", ratings=[2, 3])
        self.assertEqual(m.max_rating, 3)


class TestChantry(TestCase):
    def setUp(self) -> None:
        self.chantry = Chantry.objects.create(name="")
        self.library = Library.objects.create(rank=3)
        self.grimoire1 = Grimoire.objects.create()
        self.grimoire2 = Grimoire.objects.create()
        self.grimoire3 = Grimoire.objects.create()
        self.library.add_book(self.grimoire1)
        self.library.add_book(self.grimoire2)
        self.library.add_book(self.grimoire3)
        self.node1 = Node.objects.create(name="node1", rank=1)
        self.node2 = Node.objects.create(name="node2", rank=1)
        self.human = Human.objects.create(name="human")
        self.cabal = Cabal.objects.create(name="cabal")
        self.faction = MageFaction.objects.create(name="faction")
        self.player = User.objects.create_user(username="Test")
        mage_setup(self.player)
        grimoire_setup()

    def test_trait_cost(self):
        self.assertEqual(self.chantry.trait_cost("allies"), 2)
        self.assertEqual(self.chantry.trait_cost("arcane"), 2)
        self.assertEqual(self.chantry.trait_cost("backup"), 2)
        self.assertEqual(self.chantry.trait_cost("cult"), 2)
        self.assertEqual(self.chantry.trait_cost("elders"), 2)
        self.assertEqual(self.chantry.trait_cost("integrated_effects"), 2)
        self.assertEqual(self.chantry.trait_cost("library_rating"), 2)
        self.assertEqual(self.chantry.trait_cost("retainers"), 2)
        self.assertEqual(self.chantry.trait_cost("spies"), 2)
        self.assertEqual(self.chantry.trait_cost("node_rating"), 3)
        self.assertEqual(self.chantry.trait_cost("resources"), 3)
        self.assertEqual(self.chantry.trait_cost("enhancement"), 4)
        self.assertEqual(self.chantry.trait_cost("requisitions"), 4)
        self.assertEqual(self.chantry.trait_cost("reality_zone_rating"), 5)

    def test_has_node(self):
        self.chantry.node_rating = 1
        self.assertFalse(self.chantry.has_node())
        self.chantry.nodes.add(self.node1)
        self.assertTrue(self.chantry.has_node())

    def test_total_node(self):
        self.assertEqual(self.chantry.total_node(), 0)
        self.chantry.nodes.add(self.node1)
        self.assertEqual(self.chantry.total_node(), 1)
        self.chantry.nodes.add(self.node2)
        self.assertEqual(self.chantry.total_node(), 2)

    def test_create_nodes(self):
        self.chantry.random_faction()
        self.chantry.random_name()
        self.chantry.node_rating = 0
        self.chantry.create_nodes()
        self.assertEqual(self.chantry.nodes.count(), 0)
        self.assertEqual(self.chantry.total_node(), 0)
        self.chantry.node_rating = 12
        self.chantry.create_nodes()
        self.assertGreater(self.chantry.nodes.count(), 0)
        self.assertEqual(self.chantry.total_node(), 12)
        for node in self.chantry.nodes.all():
            self.assertEqual(node.parent, self.chantry)

    def test_has_library(self):
        self.chantry.library_rating = 3
        self.assertFalse(self.chantry.has_library())
        self.chantry.chantry_library = self.library
        self.chantry.save()
        self.assertTrue(self.chantry.has_library())

    def test_create_library(self):
        self.chantry.library_rating = 0
        self.assertFalse(self.chantry.has_library())
        self.chantry.create_library()
        self.assertTrue(self.chantry.has_library())
        self.assertEqual(self.chantry.chantry_library.num_books(), 0)
        self.chantry.library_rating = 4
        self.chantry.create_library()
        self.assertTrue(self.chantry.has_library())
        self.assertEqual(self.chantry.chantry_library.num_books(), 4)

    def test_set_library(self):
        library = Library.objects.create(name="Test Library", rank=0)
        self.assertFalse(self.chantry.has_library())
        self.chantry.set_library(library)
        self.assertTrue(self.chantry.has_library())

    def test_add_node(self):
        node = Node.objects.create(name="Test Node", rank=3)
        self.chantry.node_rating = 3
        self.assertFalse(self.chantry.has_node())
        self.chantry.add_node(node)
        self.assertTrue(self.chantry.has_node())

    def test_points_spent(self):
        self.assertEqual(self.chantry.points_spent(), 0)
        self.chantry.requisitions = 3
        self.assertEqual(self.chantry.points_spent(), 12)
        self.chantry.node_rating = 8
        self.assertEqual(self.chantry.points_spent(), 36)
        self.chantry.arcane = 1
        self.assertEqual(self.chantry.points_spent(), 38)

    def test_set_rank(self):
        self.chantry.set_rank(5)
        self.assertEqual(self.chantry.rank, 5)

    def test_has_faction(self):
        faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.chantry.has_faction())
        self.chantry.faction = faction
        self.chantry.save()
        self.assertTrue(self.chantry.has_faction())

    def test_set_faction(self):
        faction = MageFaction.objects.get(name="Test Faction 0")
        self.assertFalse(self.chantry.has_faction())
        self.assertTrue(self.chantry.set_faction(faction))
        self.assertEqual(self.chantry.faction, faction)
        self.assertTrue(self.chantry.has_faction())

    def test_has_name(self):
        self.assertFalse(self.chantry.has_name())
        self.chantry.name = "Test"
        self.assertTrue(self.chantry.has_name())

    def test_set_name(self):
        self.assertFalse(self.chantry.has_name())
        self.assertTrue(self.chantry.set_name("Test Chantry"))
        self.assertTrue(self.chantry.has_name())

    def test_has_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.chantry_type = "war"
        self.assertTrue(self.chantry.has_chantry_type())

    def test_set_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.set_chantry_type("war")
        self.assertTrue(self.chantry.has_chantry_type())

    def test_has_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.season = "spring"
        self.assertTrue(self.chantry.has_season())

    def test_set_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.set_season("spring")
        self.assertTrue(self.chantry.has_season())

    def test_get_traits(self):
        self.chantry.allies = 2
        self.chantry.arcane = 3
        self.chantry.backup = 4
        self.chantry.cult = 5
        self.chantry.elders = 6
        self.chantry.integrated_effects = 7
        self.chantry.retainers = 8
        self.chantry.spies = 9
        self.chantry.resources = 10
        self.chantry.enhancement = 11
        self.chantry.requisitions = 12
        self.chantry.reality_zone_rating = 13
        self.chantry.node_rating = 14
        self.chantry.library_rating = 15
        self.chantry.save()

        result = self.chantry.get_traits()
        expected = {
            "allies": 2,
            "arcane": 3,
            "backup": 4,
            "cult": 5,
            "elders": 6,
            "integrated_effects": 7,
            "retainers": 8,
            "spies": 9,
            "resources": 10,
            "enhancement": 11,
            "requisitions": 12,
            "reality_zone": 13,
            "node_rating": 14,
            "library_rating": 15,
        }

        self.assertEqual(result, expected)


class TestRandomChantry(TestCase):
    def setUp(self) -> None:
        self.chantry = Chantry.objects.create(name="")
        self.player = User.objects.create_user(username="Test")
        mage_setup(self.player)
        grimoire_setup()

    def test_random_points(self):
        self.chantry.rank = 1
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 10)
        self.assertLessEqual(self.chantry.points, 20)
        self.chantry.rank = 2
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 21)
        self.assertLessEqual(self.chantry.points, 30)
        self.chantry.rank = 3
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 31)
        self.assertLessEqual(self.chantry.points, 70)
        self.chantry.rank = 4
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 71)
        self.assertLessEqual(self.chantry.points, 100)
        self.chantry.rank = 5
        self.chantry.random_points()
        self.assertGreaterEqual(self.chantry.points, 101)
        self.assertLessEqual(self.chantry.points, 200)

    def test_random_rank(self):
        self.assertEqual(self.chantry.rank, 0)
        self.chantry.random_rank()
        self.assertNotEqual(self.chantry.rank, 0)

    def test_random(self):
        self.assertFalse(self.chantry.has_faction())
        self.assertFalse(self.chantry.has_name())
        self.assertFalse(self.chantry.has_library())
        self.assertFalse(self.chantry.has_season())
        self.assertFalse(self.chantry.has_chantry_type())
        self.assertTrue(self.chantry.has_node())
        self.chantry.random()
        self.assertTrue(self.chantry.has_season())
        self.assertTrue(self.chantry.has_chantry_type())
        self.assertTrue(self.chantry.has_faction())
        self.assertTrue(self.chantry.has_name())
        self.assertGreater(self.chantry.points, 0)
        self.assertLessEqual(self.chantry.points - self.chantry.points_spent(), 1)

    def test_random_faction(self):
        self.assertFalse(self.chantry.has_faction())
        self.assertTrue(self.chantry.random_faction())
        self.assertTrue(self.chantry.has_faction())

    def test_random_name(self):
        self.assertEqual(self.chantry.name, "")
        m, _ = MageFaction.objects.get_or_create(name="Society of Ether")
        self.chantry.set_faction(m)
        self.assertTrue(self.chantry.random_name())
        self.assertIn("Laboratory", self.chantry.name)

    def test_random_chantry_type(self):
        self.assertFalse(self.chantry.has_chantry_type())
        self.chantry.random_chantry_type()
        self.assertTrue(self.chantry.has_chantry_type())

    def test_random_season(self):
        self.assertFalse(self.chantry.has_season())
        self.chantry.random_season()
        self.assertTrue(self.chantry.has_season())

    def test_random_populate(self):
        chantry = Chantry.objects.create(
            name="Test Chantry",
            season="spring",
            chantry_type="college",
            leadership_type="anarchy",
            rank=1,
        )
        chantry.random_points()
        chantry.random_faction()
        chantry.random_populate()

        # Check that the number of members in the chantry is at least 3.
        self.assertGreaterEqual(chantry.members.count(), 3)

        # Check that the total number of points of the cabals' members
        # is less than or equal to the chantry's points.
        total_cabal_points = sum(
            sum(x.chantry for x in cabal.members.all())
            for cabal in self.chantry.cabals.all()
        )
        self.assertLessEqual(total_cabal_points, chantry.points)

        # Check that each cabal has at least 3 members.
        for cabal in chantry.cabals.all():
            self.assertGreaterEqual(cabal.members.count(), 3)

    def test_random_leadership_type(self):
        chantry = Chantry.objects.create()
        chantry.random_leadership_type()

        leadership_choices = [choice[0] for choice in Chantry.LEADERSHIP_CHOICES]

        self.assertIn(chantry.leadership_type, leadership_choices)


class TestNodeDetailView(TestCase):
    def setUp(self) -> None:
        self.location = Node.objects.create(name="Test Node")

    def test_location_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "wod/locations/mage/node/detail.html")


class TestChantryDetailView(TestCase):
    def setUp(self) -> None:
        self.location = Chantry.objects.create(name="Test Chantry")

    def test_chantry_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_chantry_detail_view_templates(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "wod/locations/mage/chantry/detail.html")


class TestLibrary(TestCase):
    def setUp(self):
        self.grimoire = Grimoire()
        grimoire_setup()
        self.library = Library.objects.create(name="Test Library")

    def test_add_book(self):
        g = Grimoire.objects.create(name="Book To Add")
        g.random()
        count = self.library.num_books()
        self.assertTrue(self.library.add_book(g))
        self.assertEqual(self.library.num_books(), count + 1)

    def test_set_faction(self):
        faction = MageFaction.objects.create(name="Test Faction")
        self.assertFalse(self.library.has_faction())
        self.assertTrue(self.library.set_faction(faction))
        self.assertTrue(self.library.has_faction())

    def test_has_faction(self):
        faction = MageFaction.objects.create(name="Test Faction")
        self.assertFalse(self.library.has_faction())
        self.library.set_faction(faction)
        self.assertTrue(self.library.has_faction())

    def test_has_books(self):
        self.library.rank = 3
        self.assertEqual(self.library.books.count(), 0)
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 1", rank=1))
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 2", rank=2))
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 3", rank=3))
        self.assertEqual(self.library.books.count(), 3)

    def test_increase_rank(self):
        self.assertEqual(self.library.num_books(), 0)
        self.library.increase_rank()
        self.library.increase_rank()
        self.assertEqual(self.library.num_books(), 2)

    def test_num_books(self):
        self.assertEqual(self.library.num_books(), 0)
        self.library.rank = 3
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 1", rank=1))
        self.assertEqual(self.library.num_books(), 1)
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 2", rank=2))
        self.assertEqual(self.library.num_books(), 2)
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 3", rank=3))
        self.assertEqual(self.library.num_books(), 3)


class TestRandomLibrary(TestCase):
    def setUp(self):
        self.library = Library.objects.create(rank=2)
        self.faction = MageFaction.objects.create(name="Test Faction")
        self.grimoire = Grimoire.objects.create(name="Test Grimoire")
        grimoire_setup()

    def test_random_faction(self):
        self.library.random_faction()
        self.assertIsNotNone(self.library.faction)

    def test_random_book(self):
        num_books = self.library.num_books()
        self.library.faction = self.faction
        self.library.save()
        self.library.random_book()
        self.assertEqual(num_books + 1, self.library.num_books())

    def test_random(self):
        self.library.random()
        self.assertEqual(self.library.status, "Ran")
        self.assertIsNotNone(self.library.faction)
        self.assertEqual(self.library.num_books(), self.library.rank)


class TestLibraryDetailView(TestCase):
    def setUp(self):
        self.library = Library.objects.create(name="Test Library")

    def test_library_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.library.id}/")
        self.assertEqual(response.status_code, 200)

    def test_library_detail_view_template(self):
        response = self.client.get(f"/wod/locations/{self.library.id}/")
        self.assertTemplateUsed(response, "wod/locations/mage/library/detail.html")
