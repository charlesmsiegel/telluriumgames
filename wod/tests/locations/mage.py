from django.test import TestCase

from wod.models.characters.mage import Resonance
from wod.models.locations.mage import Node, NodeMeritFlaw


# Create your tests here.
class TestNode(TestCase):
    def setUp(self):
        for i in range(1, 11):
            Resonance.objects.create(name=f"Resonance {i}")
        for i in range(5):
            for j in [1, -1]:
                if j == 1:
                    t = "Merit"
                else:
                    t = "Flaw"
                NodeMeritFlaw.objects.create(name=f"Node {t} {i}", ratings=[i * j])
        self.node = Node.objects.create(name="Test Node")

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

    def test_random_resonance(self):
        self.assertEqual(self.node.total_resonance(), 0)
        self.node.random_resonance()
        self.assertEqual(self.node.total_resonance(), 1)

    def test_total_resonance(self):
        for res in Resonance.objects.order_by("?")[:2]:
            self.node.add_resonance(res)
            self.node.add_resonance(res)
        self.assertEqual(self.node.total_resonance(), 4)
        self.assertNotEqual(self.node.total_resonance(), 5)
        self.node.add_resonance(res)
        self.assertEqual(self.node.total_resonance(), 5)

    def test_set_rank(self):
        self.assertEqual(self.node.rank, 0)
        self.assertTrue(self.node.set_rank(3))
        self.assertEqual(self.node.rank, 3)
        self.assertEqual(self.node.points, 9)

    def test_random_rank(self):
        self.assertEqual(self.node.rank, 0)
        self.node.random_rank()
        self.assertNotEqual(self.node.rank, 0)

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
        self.assertEqual(self.node.filter_mf(), 10)
        for mf in NodeMeritFlaw.objects.all():
            if "Merit" in mf.name:
                self.node.add_mf(mf, mf.ratings[0])
        self.assertEqual(self.node.filter_mf(), 5)
        for mf in NodeMeritFlaw.objects.all():
            if "Flaw" in mf.name:
                self.node.add_mf(mf, mf.ratings[0])
        self.assertEqual(self.node.filter_mf(), 0)

    def test_random_mf(self):
        num = self.node.total_mf()
        self.node.random_mf()
        self.assertGreater(self.node.total_mf(), num)

    def test_total_mf(self):
        self.assertEqual(self.node.total_mf(), 0)
        self.node.add_mf(NodeMeritFlaw.objects.get(name="Node Merit 3"), 3)
        self.assertEqual(self.node.total_mf(), 3)
        self.node.add_mf(NodeMeritFlaw.objects.get(name="Node Flaw 2"), -2)
        self.assertEqual(self.node.total_mf(), 1)

    def test_random(self):
        self.assertEqual(self.node.points, 0)
        self.node.random()
        self.assertGreaterEqual(self.node.total_resonance(), self.node.rank)
        self.assertEqual(self.node.points, 0)


class TestNodeDetailView(TestCase):
    def setUp(self) -> None:
        self.location = Node.objects.create(name="Test Node")

    def test_location_detail_view_status_code(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertEqual(response.status_code, 200)

    def test_location_detail_view_templates(self):
        response = self.client.get(f"/wod/locations/{self.location.id}/")
        self.assertTemplateUsed(response, "wod/locations/node/detail.html")
