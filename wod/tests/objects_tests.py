from unittest import mock
from unittest.mock import Mock

from django.test import TestCase

from characters.models import (
    Instrument,
    Language,
    Mage,
    MageFaction,
    Material,
    Medium,
    Paradigm,
    Practice,
    Rote,
)
from objects.models import Grimoire, Library, Wonder


# Create your tests here.
class GrimoireTest(TestCase):
    """Manage Tests for Grimoire"""

    def test_random_rank(self):
        grimoire = Grimoire()
        mocker = Mock()
        mocker.side_effect = [0.0001, 0.00001]
        with mock.patch("random.random", mocker):
            self.assertEqual(grimoire.random_rank(None), 4)
            self.assertEqual(grimoire.random_rank(None), 5)
            self.assertEqual(grimoire.random_rank(2), 2)

    def test_random_primer(self):
        grimoire = Grimoire()
        mocker = Mock()
        mocker.side_effect = [0.01, 0.11]
        with mock.patch("random.random", mocker):
            self.assertTrue(grimoire.random_primer(None))
            self.assertFalse(grimoire.random_primer(None))
            self.assertTrue(grimoire.random_primer(True))

    def test_random_faction(self):
        grimoire = Grimoire()
        faction = MageFaction.objects.create(name="Test Faction")
        self.assertTrue(grimoire.random_faction(None) is not None)
        self.assertTrue(grimoire.random_faction(faction) is not None)

    def test_random_focus(self):
        instrument_1 = Instrument.objects.create(name="Test Instrument 1")
        instrument_2 = Instrument.objects.create(name="Test Instrument 2")
        instrument_3 = Instrument.objects.create(name="Test Instrument 3")
        instrument_4 = Instrument.objects.create(name="Test Instrument 4")
        instrument_5 = Instrument.objects.create(name="Test Instrument 5")
        practice_1 = Practice.objects.create(name="Test Practice 1")
        practice_1.instruments.add(instrument_1)
        practice_1.instruments.add(instrument_2)
        practice_1.instruments.add(instrument_3)
        practice_2 = Practice.objects.create(name="Test Practice 2")
        practice_2.instruments.add(instrument_4)
        practice_2.instruments.add(instrument_5)
        practice_1.save()
        practice_2.save()
        paradigm = Paradigm.objects.create(name="Test Paradigm")
        paradigm.practices.add(practice_1)
        paradigm.practices.add(practice_2)
        paradigm.save()
        faction = MageFaction.objects.create(name="Test Faction")
        faction.paradigms.add(paradigm)
        faction.practices.add(practice_1)
        faction.practices.add(practice_2)
        faction.save()
        grimoire = Grimoire.objects.create(faction=faction)
        paradigms, practices, instruments = grimoire.random_focus(None, None, None)
        self.assertGreater(len(paradigms), 0)
        self.assertGreater(len(practices), 0)
        self.assertGreater(len(instruments), 0)

    def test_random_abilities(self):
        practice = Practice.objects.create(
            name="Test Practice", abilities=["awareness", "alertness", "science"]
        )
        grimoire = Grimoire.objects.create(name="Test Grimoire")
        grimoire.practices.add(practice)
        grimoire.save()
        abilities = grimoire.random_abilities(None)
        self.assertGreater(len(abilities), 0)

    def test_random_materials(self):
        material = Material.objects.create(name="Test Material")
        faction = MageFaction.objects.create(name="Test Faction")
        faction.materials.add(material)
        faction.save()
        grimoire = Grimoire(faction=faction)
        self.assertTrue(grimoire.random_material(None) is not None)
        self.assertTrue(grimoire.random_material(material) is not None)

    def test_random_language(self):
        language_1 = Language.objects.create(name="Test Language 1")
        language_2 = Language.objects.create(name="Test Language 2")
        faction = MageFaction.objects.create(name="Test Faction")
        faction.languages.set([language_1, language_2])
        faction.save()
        grimoire = Grimoire(name="Test Grimoire", faction=faction)
        self.assertIsNotNone(grimoire.random_language(None))

    def test_random_medium(self):
        medium = Medium.objects.create(
            name="Test Medium", length_modifier_type="division", length_modifier=1
        )
        faction = MageFaction.objects.create(name="Test Faction")
        faction.media.add(medium)
        faction.save()
        grimoire = Grimoire(faction=faction)
        self.assertTrue(grimoire.random_medium(None) is not None)
        self.assertTrue(grimoire.random_medium(medium) is not None)

    def test_random_length(self):
        medium_1 = Medium.objects.create(
            name="Test Medium", length_modifier_type="division", length_modifier=20
        )
        medium_2 = Medium.objects.create(
            name="Test Medium 2", length_modifier_type="addition", length_modifier=20
        )
        medium_3 = Medium.objects.create(
            name="Test Medium 2", length_modifier_type="subtraction", length_modifier=20
        )
        faction = MageFaction.objects.create(name="Test Faction")
        faction.media.add(medium_1)
        faction.save()
        grimoire_1 = Grimoire(faction=faction, medium=medium_1)
        grimoire_2 = Grimoire(medium=medium_2)
        grimoire_3 = Grimoire(medium=medium_3)
        grimoire_4 = Grimoire(medium=medium_1, primer=True)
        self.assertTrue(grimoire_1.random_length(None) is not None)
        self.assertEqual(grimoire_1.random_length(20), 20)
        self.assertTrue(grimoire_2.random_length(None) is not None)
        with self.assertRaises(ValueError):
            grimoire_3.random_length(None)
        self.assertTrue(grimoire_4.random_length(None) is not None)

    def test_time_written(self):
        faction = MageFaction.objects.create(name="Test Faction", founded=1466)
        grimoire = Grimoire.objects.create(faction=faction)
        self.assertIsNotNone(grimoire.random_time_written(None))

    def test_random_spheres(self):
        faction = MageFaction.objects.create(
            name="Test Faction", affinities=["Cor", "For"]
        )
        grimoire = Grimoire.objects.create(faction=faction, name="Test Grimoire")
        spheres = grimoire.random_spheres(None)
        self.assertGreater(len(spheres), 0)

    def test_random_rotes(self):
        grimoire = Grimoire.objects.create(
            name="Test Grimoire", spheres=["correspondence", "forces"], rank=3
        )
        Rote.objects.create(name="Test Rote 1", forces=3, prime=2)
        Rote.objects.create(name="Test Rote 2", correspondence=2, time=2)
        Rote.objects.create(name="Test Rote 3", life=3)
        Rote.objects.create(name="Test Rote 4", forces=5)
        Rote.objects.create(name="Test Rote 5", matter=5, prime=3)
        rotes = grimoire.random_rotes(None)
        self.assertGreater(len(rotes), 0)


class TestLibrary(TestCase):
    """Manage Tests for Library"""

    def test_has_books(self):
        library = Library.objects.create(name="Test Library")
        self.assertEqual(library.books.count(), 0)
        library.books.add(Grimoire.objects.create(name="Test Grimoire"))
        self.assertEqual(library.books.count(), 1)

    def test_increase_library(self):
        medium = Medium.objects.create(name="Test")
        instrument_1 = Instrument.objects.create(name="Test Instrument 1")
        instrument_2 = Instrument.objects.create(name="Test Instrument 2")
        instrument_3 = Instrument.objects.create(name="Test Instrument 3")
        instrument_4 = Instrument.objects.create(name="Test Instrument 4")
        instrument_5 = Instrument.objects.create(name="Test Instrument 5")
        practice_1 = Practice.objects.create(name="Test Practice 1")
        practice_1.instruments.add(instrument_1)
        practice_1.instruments.add(instrument_2)
        practice_1.instruments.add(instrument_3)
        practice_2 = Practice.objects.create(name="Test Practice 2")
        practice_2.instruments.add(instrument_4)
        practice_2.instruments.add(instrument_5)
        practice_1.save()
        practice_2.save()
        para = Paradigm.objects.create(name="Test Paradigm")
        para.practices.add(practice_1)
        para.practices.add(practice_2)
        para.save()
        faction = MageFaction.objects.create(name="Test Faction")
        faction.paradigms.add(para)
        faction.practices.add(practice_1)
        faction.practices.add(practice_2)
        faction.media.add(medium)
        faction.save()
        library = Library.objects.create(name="Test Library", rank=0)
        self.assertEqual(len(library), 0)
        library.increase_size(None)
        library.increase_size(None)
        self.assertEqual(len(library), 2)


class TestWonderView(TestCase):
    """Manage Tests for Wonder View"""

    def test_correct_template(self):
        wonder = Wonder.objects.create(
            name="Test Wonder",
            rank=3,
            background_cost=6,
            quintessence_max=15,
            description="Test Description",
        )
        response = self.client.get(f"/objects/{wonder.id}/")
        self.assertTemplateUsed(response, "objects/wonders/detail.html")


class TestGrimoireView(TestCase):
    """Manage Tests for Grimoire View"""

    def test_correct_template(self):
        faction = MageFaction.objects.create(name="Test Faction")
        wonder = Grimoire.objects.create(
            name="Test Wonder",
            rank=3,
            background_cost=6,
            quintessence_max=15,
            description="Test Description",
            faction=faction,
        )
        response = self.client.get(f"/objects/{wonder.id}/")
        self.assertTemplateUsed(response, "objects/grimoires/detail.html")
