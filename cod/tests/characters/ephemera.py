from django.test import TestCase

from cod.models.characters.ephemera import Ephemera, Numina


# Create your tests here.
class TestEphemera(TestCase):
    def setUp(self):
        self.ephemera = Ephemera.objects.create()

    def test_has_rank(self):
        self.assertFalse(self.ephemera.has_rank())
        self.ephemera.set_rank(2)
        self.assertTrue(self.ephemera.has_rank())

    def test_set_rank(self):
        self.assertFalse(self.ephemera.has_rank())
        self.assertTrue(self.ephemera.set_rank(2))
        self.assertTrue(self.ephemera.has_rank())

    def test_has_type(self):
        self.assertFalse(self.ephemera.has_type())
        self.ephemera.set_type("ghost")
        self.assertTrue(self.ephemera.has_type())

    def test_set_type(self):
        self.assertFalse(self.ephemera.has_type())
        self.assertTrue(self.ephemera.set_type("ghost"))
        self.assertTrue(self.ephemera.has_type())

    def test_compute_maximum_essence(self):
        self.ephemera.set_rank(1)
        self.ephemera.compute_maximum_essence()
        self.assertEqual(self.ephemera.maximum_essence, 10)
        self.ephemera.set_rank(2)
        self.ephemera.compute_maximum_essence()
        self.assertEqual(self.ephemera.maximum_essence, 15)
        self.ephemera.set_rank(3)
        self.ephemera.compute_maximum_essence()
        self.assertEqual(self.ephemera.maximum_essence, 20)
        self.ephemera.set_rank(4)
        self.ephemera.compute_maximum_essence()
        self.assertEqual(self.ephemera.maximum_essence, 25)
        self.ephemera.set_rank(5)
        self.ephemera.compute_maximum_essence()
        self.assertEqual(self.ephemera.maximum_essence, 50)

    def test_get_attributes(self):
        self.ephemera.power = 2
        self.ephemera.finesse = 3
        self.ephemera.resistance = 4
        expected_attributes = {"power": 2, "finesse": 3, "resistance": 4}
        self.assertEqual(self.ephemera.get_attributes(), expected_attributes)

    def test_total_attributes(self):
        self.ephemera.power = 2
        self.ephemera.finesse = 3
        self.ephemera.resistance = 4
        self.assertEqual(self.ephemera.total_attributes(), 9)

    def test_other_traits(self):
        self.ephemera.rank = 1
        self.ephemera.power = 2
        self.ephemera.finesse = 3
        self.ephemera.resistance = 4
        self.ephemera.other_traits()
        self.assertEqual(self.ephemera.corpus, 9)
        self.assertEqual(self.ephemera.willpower, 7)
        self.assertEqual(self.ephemera.initiative, 7)
        self.assertEqual(self.ephemera.defense, 2)
        self.assertEqual(self.ephemera.speed, 5)

    def test_add_numina(self):
        numina = Numina.objects.create()
        self.ephemera.add_numina(numina)
        self.assertEqual(self.ephemera.numina.count(), 1)
        self.assertIn(numina, self.ephemera.numina.all())

    def test_filter_numina(self):
        numina1 = Numina.objects.create()
        Numina.objects.create()
        num = self.ephemera.filter_numina().count()
        self.ephemera.add_numina(numina1)
        self.assertEqual(self.ephemera.filter_numina().count(), num - 1)

    def test_total_numina(self):
        numina1 = Numina.objects.create()
        numina2 = Numina.objects.create()
        self.ephemera.add_numina(numina1)
        self.assertEqual(self.ephemera.total_numina(), 1)
        self.ephemera.add_numina(numina2)
        self.assertEqual(self.ephemera.total_numina(), 2)


class TestRandomEphemera(TestCase):
    def setUp(self):
        self.ephemera = Ephemera.objects.create()

    def test_random_rank(self):
        ranks = [1, 2, 3, 4, 5]
        self.ephemera.random_rank()
        self.assertIn(self.ephemera.rank, ranks)

    def test_random_type(self):
        types = ["spirit", "goetia", "ghost", "supernal being"]
        self.ephemera.random_type()
        self.assertIn(self.ephemera.ephemera_type, types)

    def test_random_attributes(self):
        self.ephemera.rank = 2
        self.ephemera.random_attributes()
        total_dots = self.ephemera.total_attributes()
        rank_to_dots = {
            1: list(range(5, 8 + 1)),
            2: list(range(9, 14 + 1)),
            3: list(range(15, 25 + 1)),
            4: list(range(26, 35 + 1)),
            5: list(range(36, 45 + 1)),
        }
        rank = self.ephemera.rank
        self.assertGreaterEqual(total_dots, rank_to_dots[rank][0])
        self.assertLessEqual(total_dots, rank_to_dots[rank][-1])

    def test_random_numina(self):
        Numina.objects.create(name="Test Numina")
        self.ephemera.random_numina()
        self.assertGreaterEqual(self.ephemera.total_numina(), 0)

    def test_random_name(self):
        name = "Test Ephemera"
        self.ephemera.random_name(name)
        self.assertEqual(self.ephemera.name, name)

    def test_random(self):
        ranks = [1, 2, 3, 4, 5]
        types = ["spirit", "goetia", "ghost", "supernal being"]
        for i in range(10):
            Numina.objects.create(name=f"Test Numina {i}")
        self.ephemera.random()
        self.assertIn(self.ephemera.rank, ranks)
        self.assertIn(self.ephemera.ephemera_type, types)
        self.assertGreaterEqual(self.ephemera.total_attributes(), self.ephemera.rank)
        self.assertGreaterEqual(self.ephemera.total_numina(), 0)
