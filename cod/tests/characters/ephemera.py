from django.test import TestCase

from cod.models.characters.ephemera import Ephemera


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
        self.fail()

    def test_total_attributes(self):
        self.fail()

    def test_other_traits(self):
        self.fail()

    def test_add_numina(self):
        self.fail()

    def test_add_filter_numina(self):
        self.fail()

    def test_total_numina(self):
        self.fail()


class TestRandomEphemera(TestCase):
    def test_random_rank(self):
        self.fail()

    def test_random_rank(self):
        self.fail()

    def test_random_type(self):
        self.fail()

    def test_random_attributes(self):
        self.fail()

    def test_random_numina(self):
        self.fail()

    def test_random_name(self):
        self.fail()

    def test_random(self):
        self.fail()
