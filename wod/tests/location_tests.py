from django.contrib.auth.models import User
from django.test import TestCase
from wod.models.characters.mage import Mage, Resonance
from wod.models.locations.mage import (City, Location, Node, NodeMeritFlaw,
                                       NodeResRating)


# Create your tests here.
class TestNode(TestCase):
    """Manage Tests for Node"""

    def setUp(self) -> None:
        Resonance.objects.create(name="Res1")
        Resonance.objects.create(name="Res2")
        Resonance.objects.create(name="Res3")
        Resonance.objects.create(name="Res4")
        Resonance.objects.create(name="Res5")
        Resonance.objects.create(name="Res6")
        NodeMeritFlaw.objects.create(name="MF1", value=2)
        NodeMeritFlaw.objects.create(name="MF2", value=-2)
        NodeMeritFlaw.objects.create(name="MF3", value=1)
        NodeMeritFlaw.objects.create(name="MF4", value=-1)

        self.node = Node()
        self.node.save()
        self.res1 = Resonance(name="Intense")
        self.res1.save()
        self.res2 = Resonance(name="Fiery")
        self.res2.save()

    def tearDown(self) -> None:
        self.node.delete()
        self.res1.delete()
        self.res2.delete()

    def test_random_resonance(self):
        node = Node.objects.create(name="Test")
        node.random_resonance()
        self.assertEqual(node.total_resonance(), 1)
        node.random_resonance()
        self.assertEqual(node.total_resonance(), 2)

    def test_merits_and_flaws(self):
        node = Node.objects.create(name="Test")
        points = node.random_merits_and_flaws(3)
        rem = sum([x.value for x in node.merits_and_flaws.all()])
        self.assertEqual(points, 3 - rem)

    def test_random_rank(self):
        node = Node.objects.create(name="Test")
        node.random_rank(None)
        node.save()
        self.assertNotEqual(node.rank, 0)
        node = Node.objects.create(name="Test")
        node.random_rank(3)
        node.save()
        self.assertEqual(node.rank, 3)

    def test_total_resonance(self):
        NodeResRating.objects.create(node=self.node, resonance=self.res1, rating=2)
        NodeResRating.objects.create(node=self.node, resonance=self.res2, rating=2)
        self.assertEqual(self.node.total_resonance(), 4)
        self.assertNotEqual(self.node.total_resonance(), 5)
        self.node.add_resonance_dot()
        self.assertEqual(self.node.total_resonance(), 5)

    def test_new_resonance_trait(self):
        node = Node.objects.create(name="Test")
        node.new_resonance_trait()
        self.assertEqual(node.total_resonance(), 1)

    def test_add_resonance_dot(self):
        node = Node.objects.create(name="Test")
        with self.assertRaises(IndexError):
            node.add_resonance_dot()
        NodeResRating.objects.create(node=node, resonance=self.res1, rating=1)
        node.add_resonance_dot()
        self.assertEqual(node.total_resonance(), 2)
        node.add_resonance_dot()
        self.assertEqual(node.total_resonance(), 3)

    def test_description(self):
        self.node.random(rank=3)
        self.assertNotEqual(self.node.basic_description(), "")

    def test_full_random(self):
        node = Node.objects.create(name="Test")
        node.random(rank=3)
        node.save()
        points = 9
        points -= node.ratio_cost
        points -= node.size
        for merit_flaw in node.merits_and_flaws.all():
            points -= merit_flaw.value
        if "Corrupted" in [x.name for x in node.merits_and_flaws.all()]:
            points += 2
        if "Sphere Attuned" in [x.name for x in node.merits_and_flaws.all()]:
            points += 1
        points -= node.total_resonance() - 3
        points -= node.quintessence_per_week
        points -= node.tass_per_week
        self.assertEqual(points, 0)


class TestLocationIndexView(TestCase):
    """Manage Tests for Location"""

    def test_correct_template(self):
        response = self.client.get("/wod/locations/")
        self.assertTemplateUsed(response, "wod/locations/index.html")

    def test_gets_list_of_locations(self):
        for i in range(5):
            Location.objects.create(name=f"Location {i}")
            City.objects.create(name=f"City {i}")
            Node.objects.create(name=f"Node {i}")
        response = self.client.get("/wod/locations/")
        for i in range(5):
            self.assertContains(response, f"Location {i}")
            self.assertContains(response, f"City {i}")
            self.assertContains(response, f"Node {i}")


class TestNodeView(TestCase):
    """Manage Tests for NodeView"""

    def test_correct_template(self):
        location = Node.objects.create(name="Node")
        response = self.client.get(f"/wod/locations/{location.id}/")
        self.assertTemplateUsed(response, "wod/locations/mage/node.html")


class TestLocationView(TestCase):
    """Manage Tests for LocationView"""

    def setUp(self) -> None:
        self.location = Location.objects.create(name="Location 1")
        self.child = Location.objects.create(name="Location 2", parent=self.location)

    def test_correct_template(self):
        location = Location.objects.create(name="Location")
        response = self.client.get(f"/wod/locations/{location.id}/")
        self.assertTemplateUsed(response, "wod/locations/location.html")

    def test_location_str(self):
        self.assertEqual(str(self.location), "Location 1")

    def test_location_parent(self):
        self.assertEqual(self.child.parent, self.location)
        self.assertIn(self.child, self.location.children.all())

    # def test_scenes_created_at_locations(self):
    #     self.fail()


class CityTests(TestCase):
    """Manage Tests for City"""

    def test_populate_with_characters(self):
        city = City.objects.create(name="New York City", population=28000000)
        player = User.objects.create_user(username="User")
        mage_npc = Mage.objects.create(name="Mage NPC 1", player=player.wod_profile)
        city.mages.add(mage_npc)
        self.assertIn(mage_npc, city.mages.all())
