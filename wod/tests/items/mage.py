from unittest import mock
from unittest.mock import Mock

from django.test import TestCase

from core.models import Language, Material, Medium
from wod.models.characters.mage import Instrument, MageFaction, Paradigm, Practice, Rote
from wod.models.items.mage import Grimoire, Library


# Create your tests here.
class TestGrimoire(TestCase):
    def setUp(self):
        self.grimoire = Grimoire.objects.create(name="Test Grimoire")
        self.faction = MageFaction.objects.create(name="Test Faction")
        self.abilities = ["science", "art", "crafts"]
        self.date_written = 1325
        self.language = Language.objects.create(name="Test Language")
        self.length = 100
        self.paradigms = [
            Paradigm.objects.create(name=f"Test Paradigm {i}") for i in range(3)
        ]
        self.practices = [
            Practice.objects.create(name=f"Test Practice {i}") for i in range(3)
        ]
        self.instruments = [
            Instrument.objects.create(name=f"Test Instrument {i}") for i in range(3)
        ]
        self.cover_material = Material.objects.create(name="Test Cover Material")
        self.inner_material = Material.objects.create(name="Test Inner Material")
        self.medium = Medium.objects.create(name="Test Medium")
        self.rotes = [Rote.objects.create(name=f"Test Rote {i}") for i in range(4)]
        self.spheres = ["correspondence", "forces", "matter"]

    def test_set_rank(self):
        self.assertEqual(self.grimoire.rank, 0)
        self.assertTrue(self.grimoire.set_rank(3))
        self.assertEqual(self.grimoire.rank, 3)

    def test_has_rank(self):
        self.assertFalse(self.grimoire.has_rank())
        self.grimoire.set_rank(3)
        self.assertTrue(self.grimoire.has_rank())

    def test_set_is_primer(self):
        self.assertFalse(self.grimoire.is_primer)
        self.assertTrue(self.grimoire.set_is_primer(True))
        self.assertTrue(self.grimoire.is_primer)

    def test_set_faction(self):
        self.assertIsNone(self.grimoire.faction)
        self.assertTrue(self.grimoire.set_faction(self.faction))
        self.assertEqual(self.grimoire.faction, self.faction)

    def test_has_faction(self):
        self.assertFalse(self.grimoire.has_faction())
        self.grimoire.set_faction(self.faction)
        self.assertTrue(self.grimoire.has_faction())

    def test_set_focus(self):
        self.assertEqual(self.grimoire.paradigms.count(), 0)
        self.assertEqual(self.grimoire.practices.count(), 0)
        self.assertEqual(self.grimoire.instruments.count(), 0)
        self.assertTrue(
            self.grimoire.set_focus(self.paradigms, self.practices, self.instruments)
        )
        self.assertEqual(set(self.grimoire.paradigms.all()), set(self.paradigms))
        self.assertEqual(set(self.grimoire.practices.all()), set(self.practices))
        self.assertEqual(set(self.grimoire.instruments.all()), set(self.instruments))

    def test_has_focus(self):
        self.assertFalse(self.grimoire.has_focus())
        self.grimoire.set_focus(self.paradigms, self.practices, self.instruments)
        self.assertTrue(self.grimoire.has_focus())

    def test_set_abilities(self):
        self.assertEqual(self.grimoire.abilities, [])
        self.assertTrue(self.grimoire.set_abilities(self.abilities))
        self.assertEqual(set(self.grimoire.abilities), set(self.abilities))

    def test_has_abilities(self):
        self.assertFalse(self.grimoire.has_abilities())
        self.grimoire.set_abilities(self.abilities)
        self.assertTrue(self.grimoire.has_abilities())

    def test_set_materials(self):
        self.assertIsNone(self.grimoire.cover_material)
        self.assertIsNone(self.grimoire.inner_material)
        self.assertTrue(
            self.grimoire.set_materials(self.cover_material, self.inner_material)
        )
        self.assertEqual(self.grimoire.cover_material, self.cover_material)
        self.assertEqual(self.grimoire.inner_material, self.inner_material)

    def test_has_materials(self):
        self.assertFalse(self.grimoire.has_materials())
        self.grimoire.set_materials(self.cover_material, self.inner_material)
        self.assertTrue(self.grimoire.has_materials())

    def test_set_language(self):
        self.assertIsNone(self.grimoire.language)
        self.assertTrue(self.grimoire.set_language(self.language))
        self.assertEqual(self.grimoire.language, self.language)

    def test_has_language(self):
        self.assertFalse(self.grimoire.has_language())
        self.grimoire.set_language(self.language)
        self.assertTrue(self.grimoire.has_language())

    def test_set_medium(self):
        self.assertIsNone(self.grimoire.medium)
        self.assertTrue(self.grimoire.set_medium(self.medium))
        self.assertEqual(self.grimoire.medium, self.medium)

    def test_has_medium(self):
        self.assertFalse(self.grimoire.has_medium())
        self.grimoire.set_medium(self.medium)
        self.assertTrue(self.grimoire.has_medium())

    def test_set_length(self):
        self.assertEqual(self.grimoire.length, 0)
        self.assertTrue(self.grimoire.set_length(self.length))
        self.assertEqual(self.grimoire.length, self.length)

    def test_has_length(self):
        self.assertFalse(self.grimoire.has_length())
        self.grimoire.set_length(self.length)
        self.assertTrue(self.grimoire.has_length())

    def test_set_date_written(self):
        self.assertEqual(self.grimoire.date_written, -5000)
        self.assertTrue(self.grimoire.set_date_written(self.date_written))
        self.assertEqual(self.grimoire.date_written, self.date_written)

    def test_has_date_written(self):
        self.assertFalse(self.grimoire.has_date_written())
        self.grimoire.set_date_written(self.date_written)
        self.assertTrue(self.grimoire.has_date_written())

    def test_set_spheres(self):
        self.assertEqual(self.grimoire.spheres, [])
        self.assertTrue(self.grimoire.set_spheres(self.spheres))
        self.assertEqual(set(self.grimoire.spheres), set(self.spheres))

    def test_has_spheres(self):
        self.assertFalse(self.grimoire.has_spheres())
        self.grimoire.set_spheres(self.spheres)
        self.assertTrue(self.grimoire.has_spheres())

    def test_set_rotes(self):
        self.assertEqual(self.grimoire.rotes.count(), 0)
        self.assertTrue(self.grimoire.set_rotes(self.rotes))
        self.assertEqual(set(self.grimoire.rotes.all()), set(self.rotes))

    def test_has_rotes(self):
        self.assertFalse(self.grimoire.has_rotes())
        self.grimoire.set_rotes(self.rotes)
        self.assertTrue(self.grimoire.has_rotes())


class TestRandomGrimoire(TestCase):
    def setUp(self):
        self.grimoire = Grimoire.objects.create(name="Random Grimoire")
        abilities = [
            "alertness",
            "art",
            "athletics",
            "awareness",
            "brawl",
            "empathy",
            "expression",
            "intimidation",
            "leadership",
            "streetwise",
            "subterfuge",
            "crafts",
            "drive",
            "etiquette",
            "firearms",
            "martial_arts",
            "meditation",
            "melee",
            "research",
            "stealth",
            "survival",
            "technology",
            "academics",
            "computer",
            "cosmology",
            "enigmas",
            "esoterica",
            "investigation",
            "law",
            "medicine",
            "occult",
            "politics",
            "science",
            "animal_kinship",
            "blatancy",
            "carousing",
            "do",
            "flying",
            "high_ritual",
            "lucid_dreaming",
            "search",
            "seduction",
            "acrobatics",
            "archery",
            "biotech",
            "energy_weapons",
            "hypertech",
            "jetpack",
            "riding",
            "torture",
            "area_knowledge",
            "belief_systems",
            "cryptography",
            "demolitions",
            "finance",
            "lore",
            "media",
            "pharmacopeia",
        ]
        spheres = [
            "correspondence",
            "forces",
            "life",
            "matter",
            "mind",
            "time",
            "spirit",
            "prime",
            "entropy",
        ]

        for i in range(40):
            Instrument.objects.create(name=f"Test Instrument {i}")
        for i in range(20):
            p = Practice.objects.create(
                name=f"Test Practice {i}", abilities=abilities[i : i + 7]
            )
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {i}"))
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {20+i}"))
            p.save()
        for i in range(10):
            p = Paradigm.objects.create(name=f"Test Paradigm {i}")
            p.practices.add(Practice.objects.get(name=f"Test Practice {i}"))
            p.practices.add(Practice.objects.get(name=f"Test Practice {i+10}"))
            p.save()
            Material.objects.create(name=f"Test Material {i}")
            Language.objects.create(name=f"Test Language {i}", frequency=i)
        for i in range(5):
            m = MageFaction.objects.create(
                name=f"Test Faction {i}", affinities=spheres[i : i + 4],
            )
            m.languages.add(Language.objects.get(name=f"Test Language {i}"))
            m.languages.add(Language.objects.get(name=f"Test Language {5+i}"))
            m.save()
            m.paradigms.add(Paradigm.objects.get(name=f"Test Paradigm {i}"))
            m.paradigms.add(Paradigm.objects.get(name=f"Test Paradigm {5+i}"))
            m.save()
            for modifier_type in ["+", "-", "*", "/"]:
                for modifier in [1, 20]:
                    med = Medium.objects.create(
                        name=f"Test {modifier_type} Medium {i, modifier}",
                        length_modifier_type=modifier_type,
                        length_modifier=modifier,
                    )
                    m.media.add(med)
                    m.save()
        for sphere_1 in spheres:
            for sphere_2 in spheres:
                if sphere_1 != sphere_2:
                    for i in range(5):
                        for j in range(5):
                            d = {sphere_1: i, sphere_2: j}
                            Rote.objects.create(
                                name=f"{sphere_1}/{sphere_2} Test Rote {5*i+j}", **d
                            )

    def test_random_rank(self):
        mocker = Mock()
        mocker.side_effect = [0.0001, 0.00001]
        with mock.patch("random.random", mocker):
            self.grimoire.random_rank()
            self.assertEqual(self.grimoire.rank, 4)
            self.grimoire.random_rank()
            self.assertEqual(self.grimoire.rank, 5)

    def test_random_is_primer(self):
        mocker = Mock()
        mocker.side_effect = [0.01, 0.11]
        with mock.patch("random.random", mocker):
            self.grimoire.random_is_primer()
            self.assertTrue(self.grimoire.is_primer)
            self.grimoire.random_is_primer()
            self.assertFalse(self.grimoire.is_primer)

    def test_random_faction(self):
        self.assertFalse(self.grimoire.has_faction())
        self.grimoire.random_faction()
        self.assertTrue(self.grimoire.has_faction())

    def test_random_focus(self):
        self.assertFalse(self.grimoire.has_focus())
        self.grimoire.random_focus()
        self.assertTrue(self.grimoire.has_focus())

    def test_random_abilities(self):
        self.assertFalse(self.grimoire.has_abilities())
        self.grimoire.random_focus()
        self.grimoire.random_abilities()
        self.assertTrue(self.grimoire.has_abilities())

    def test_random_materials(self):
        self.assertFalse(self.grimoire.has_materials())
        self.grimoire.random_faction()
        self.grimoire.random_material()
        self.assertTrue(self.grimoire.has_materials())

    def test_random_language(self):
        self.assertFalse(self.grimoire.has_language())
        self.grimoire.random_language()
        self.assertTrue(self.grimoire.has_language())

    def test_random_medium(self):
        self.assertFalse(self.grimoire.has_medium())
        self.grimoire.random_medium()
        self.assertTrue(self.grimoire.has_medium())

    def test_random_length(self):
        self.assertFalse(self.grimoire.has_length())
        self.grimoire.random_length()
        self.assertTrue(self.grimoire.has_length())

    def test_random_date_written(self):
        self.assertFalse(self.grimoire.has_date_written())
        self.grimoire.random_date_written()
        self.assertTrue(self.grimoire.has_date_written())

    def test_random_spheres(self):
        self.assertFalse(self.grimoire.has_spheres())
        self.grimoire.random_spheres()
        self.assertTrue(self.grimoire.has_spheres())

    def test_random_rotes(self):
        self.assertFalse(self.grimoire.has_rotes())
        self.grimoire.random_rotes()
        self.assertTrue(self.grimoire.has_rotes())

    def test_random(self):
        self.assertFalse(self.grimoire.has_rank())
        self.assertFalse(self.grimoire.has_faction())
        self.assertFalse(self.grimoire.has_medium())
        self.assertFalse(self.grimoire.has_materials())
        self.assertFalse(self.grimoire.has_length())
        self.assertFalse(self.grimoire.has_focus())
        self.assertFalse(self.grimoire.has_date_written())
        self.assertFalse(self.grimoire.has_abilities())
        self.assertFalse(self.grimoire.has_language())
        self.assertFalse(self.grimoire.has_spheres())
        self.assertFalse(self.grimoire.has_rotes())
        self.grimoire.random()
        self.assertTrue(self.grimoire.has_rank())
        self.assertTrue(self.grimoire.has_faction())
        self.assertTrue(self.grimoire.has_medium())
        self.assertTrue(self.grimoire.has_materials())
        self.assertTrue(self.grimoire.has_length())
        self.assertTrue(self.grimoire.has_focus())
        self.assertTrue(self.grimoire.has_date_written())
        self.assertTrue(self.grimoire.has_abilities())
        self.assertTrue(self.grimoire.has_language())
        self.assertTrue(self.grimoire.has_spheres())
        self.assertTrue(self.grimoire.has_rotes())


class TestLibrary(TestCase):
    def setUp(self):
        self.grimoire = Grimoire()
        abilities = [
            "alertness",
            "art",
            "athletics",
            "awareness",
            "brawl",
            "empathy",
            "expression",
            "intimidation",
            "leadership",
            "streetwise",
            "subterfuge",
            "crafts",
            "drive",
            "etiquette",
            "firearms",
            "martial_arts",
            "meditation",
            "melee",
            "research",
            "stealth",
            "survival",
            "technology",
            "academics",
            "computer",
            "cosmology",
            "enigmas",
            "esoterica",
            "investigation",
            "law",
            "medicine",
            "occult",
            "politics",
            "science",
            "animal_kinship",
            "blatancy",
            "carousing",
            "do",
            "flying",
            "high_ritual",
            "lucid_dreaming",
            "search",
            "seduction",
            "acrobatics",
            "archery",
            "biotech",
            "energy_weapons",
            "hypertech",
            "jetpack",
            "riding",
            "torture",
            "area_knowledge",
            "belief_systems",
            "cryptography",
            "demolitions",
            "finance",
            "lore",
            "media",
            "pharmacopeia",
        ]
        spheres = [
            "correspondence",
            "forces",
            "life",
            "matter",
            "mind",
            "time",
            "spirit",
            "prime",
            "entropy",
        ]

        for i in range(40):
            Instrument.objects.create(name=f"Test Instrument {i}")
        for i in range(20):
            p = Practice.objects.create(
                name=f"Test Practice {i}", abilities=abilities[i : i + 7]
            )
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {i}"))
            p.instruments.add(Instrument.objects.get(name=f"Test Instrument {20+i}"))
            p.save()
        for i in range(10):
            p = Paradigm.objects.create(name=f"Test Paradigm {i}")
            p.practices.add(Practice.objects.get(name=f"Test Practice {i}"))
            p.practices.add(Practice.objects.get(name=f"Test Practice {i+10}"))
            p.save()
            Material.objects.create(name=f"Test Material {i}")
            Language.objects.create(name=f"Test Language {i}")
        for i in range(5):
            m = MageFaction.objects.create(
                name=f"Test Faction {i}", affinities=spheres[i : i + 4],
            )
            m.languages.add(Language.objects.get(name=f"Test Language {i}"))
            m.languages.add(Language.objects.get(name=f"Test Language {5+i}"))
            m.save()
            m.paradigms.add(Paradigm.objects.get(name=f"Test Paradigm {i}"))
            m.paradigms.add(Paradigm.objects.get(name=f"Test Paradigm {5+i}"))
            m.save()
            for modifier_type in ["+", "-", "*", "/"]:
                for modifier in [1, 20]:
                    med = Medium.objects.create(
                        name=f"Test {modifier_type} Medium {i, modifier}",
                        length_modifier_type=modifier_type,
                        length_modifier=modifier,
                    )
                    m.media.add(med)
                    m.save()
        for sphere_1 in spheres:
            for sphere_2 in spheres:
                if sphere_1 != sphere_2:
                    for i in range(5):
                        for j in range(5):
                            d = {sphere_1: i, sphere_2: j}
                            Rote.objects.create(
                                name=f"{sphere_1}/{sphere_2} Test Rote {5*i+j}", **d
                            )
        self.library = Library.objects.create(name="Test Library")

    def test_add_book(self):
        g = Grimoire.objects.create(name="Book To Add")
        g.random()
        count = self.library.num_books()
        self.assertTrue(self.library.add_book(g))
        self.assertEqual(self.library.num_books(), count + 1)

    def test_has_books(self):
        self.library.rank = 3
        self.assertEqual(self.library.books.count(), 0)
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 1", rank=1))
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 2", rank=2))
        self.library.books.add(Grimoire.objects.create(name="Test Grimoire 3", rank=3))
        self.assertEqual(self.library.books.count(), 3)

    def test_increase_library_rating(self):
        self.assertEqual(self.library.num_books(), 0)
        self.library.increase_rank()
        self.library.increase_rank()
        self.assertEqual(self.library.num_books(), 2)


class TestGrimoireDetailView(TestCase):
    def setUp(self):
        self.grimoire = Grimoire.objects.create(name="Test Grimoire")

    def test_grimoire_detail_view_status_code(self):
        response = self.client.get(f"/wod/items/{self.grimoire.id}/")
        self.assertEqual(response.status_code, 200)

    def test_grimoire_detail_view_template(self):
        response = self.client.get(f"/wod/items/{self.grimoire.id}/")
        self.assertTemplateUsed(response, "wod/items/grimoire/detail.html")


class TestLibraryDetailView(TestCase):
    def setUp(self):
        self.library = Library.objects.create(name="Test Library")

    def test_library_detail_view_status_code(self):
        response = self.client.get(f"/wod/items/{self.library.id}/")
        self.assertEqual(response.status_code, 200)

    def test_library_detail_view_template(self):
        response = self.client.get(f"/wod/items/{self.library.id}/")
        self.assertTemplateUsed(response, "wod/items/library/detail.html")
