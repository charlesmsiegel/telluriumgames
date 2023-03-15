import random
from unittest import mock
from unittest.mock import Mock

from django.db.models.query import QuerySet
from django.test import TestCase

from core.models import Language, Material, Medium, Noun
from wod.models.characters.mage import (
    Effect,
    Instrument,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
)
from wod.models.characters.mage.utils import ABILITY_LIST, SPHERE_LIST
from wod.models.items.mage import Artifact, Charm, Grimoire, Talisman, Wonder


# Create your tests here.
def grimoire_setup():
    for i in range(10):
        Noun.objects.create(name=f"Grimoire Noun {i}")

    abilities = ABILITY_LIST
    spheres = SPHERE_LIST
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
        Material.objects.create(name=f"Test Soft Material {i}", is_hard=False)
        Language.objects.create(name=f"Test Language {i}", frequency=i)
    for i in range(5):
        m = MageFaction.objects.create(
            name=f"Test Faction {i}", affinities=spheres[i : i + 4],
        )
        for j in range(3):
            m1 = MageFaction.objects.create(
                name=f"Test SubFaction {i}, {j}",
                affinities=spheres[i : i + 4],
                parent=m,
            )
            m1.languages.add(Language.objects.get(name=f"Test Language {i}"))
            m1.languages.add(Language.objects.get(name=f"Test Language {5+i}"))
            m1.save()
            m1.paradigms.add(Paradigm.objects.get(name=f"Test Paradigm {i}"))
            m1.paradigms.add(Paradigm.objects.get(name=f"Test Paradigm {5+i}"))
            m1.save()

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
                for i in range(6):
                    for j in range(6):
                        d = {sphere_1: i, sphere_2: j}
                        Effect.objects.create(
                            name=f"{sphere_1}/{sphere_2} Test Effect {5*i+j}", **d
                        )
        for i in range(5):
            Resonance.objects.get_or_create(
                name=f"{sphere_1.title()} Resonance {i}", **{sphere_1: True}
            )


class TestWonder(TestCase):
    def setUp(self):
        grimoire_setup()
        self.wonder = Wonder.objects.create(name="Test Wonder")

    def test_set_rank(self):
        g = Wonder.objects.create(name="")
        self.assertFalse(g.has_rank())
        self.assertTrue(g.set_rank(3))
        self.assertEqual(g.rank, 3)

    def test_has_rank(self):
        g = Wonder.objects.create(name="")
        self.assertFalse(g.has_rank())
        g.set_rank(3)
        self.assertTrue(g.has_rank())

    def test_add_resonance(self):
        res = Resonance.objects.create(name="Test Resonance")
        self.wonder.add_resonance(res)
        self.assertEqual(self.wonder.resonance_rating(res), 1)

    def test_resonance_rating(self):
        res = Resonance.objects.create(name="Test Resonance")
        self.wonder.add_resonance(res)
        self.assertEqual(self.wonder.resonance_rating(res), 1)

    def test_filter_resonance(self):
        res1 = Resonance.objects.create(name="Test Resonance 1")
        res2 = Resonance.objects.create(name="Test Resonance 2")
        res3 = Resonance.objects.create(name="Test Resonance 3")
        self.wonder.add_resonance(res1)
        self.wonder.add_resonance(res2)
        self.wonder.add_resonance(res2)
        self.wonder.add_resonance(res3)
        self.wonder.add_resonance(res3)
        self.wonder.add_resonance(res3)
        res_filtered = self.wonder.filter_resonance(minimum=2, maximum=4)
        self.assertIn(res2, res_filtered)
        self.assertIn(res3, res_filtered)
        self.assertEqual(res_filtered.count(), 2)

    def test_total_resonance(self):
        res1 = Resonance.objects.create(name="Test Resonance 1")
        res2 = Resonance.objects.create(name="Test Resonance 2")
        res3 = Resonance.objects.create(name="Test Resonance 3")
        self.wonder.add_resonance(res1)
        self.wonder.add_resonance(res2)
        self.wonder.add_resonance(res3)
        self.assertEqual(self.wonder.total_resonance(), 3)

    def test_has_resonance(self):
        self.wonder.rank = 2
        self.assertFalse(self.wonder.has_resonance())
        res1 = Resonance.objects.create(name="Test Resonance 1")
        self.wonder.add_resonance(res1)
        self.assertFalse(self.wonder.has_resonance())
        res2 = Resonance.objects.create(name="Test Resonance 2")
        self.wonder.add_resonance(res2)
        self.assertTrue(self.wonder.has_resonance())


class TestRandomWonder(TestCase):
    def setUp(self):
        grimoire_setup()
        self.wonder = Wonder.objects.create(name="Test Wonder")

    def test_random_points(self):
        self.wonder.rank = 2
        points = self.wonder.random_points()
        self.assertGreaterEqual(points, 4)
        self.assertLessEqual(points, 6)

    def test_random_rank(self):
        self.wonder.random_rank()
        self.assertTrue(self.wonder.has_rank())

    def test_random_resonance(self):
        res1 = Resonance.objects.create(name="Test Resonance 1")
        self.wonder.add_resonance(res1)
        self.wonder.random_resonance()
        self.assertGreater(self.wonder.total_resonance(), 1)

    def test_random(self):
        self.wonder.random()
        self.assertTrue(self.wonder.has_name())
        self.assertTrue(self.wonder.has_rank())
        self.assertTrue(self.wonder.has_resonance())
        self.assertGreater(self.wonder.background_cost, 0)


class TestCharm(TestCase):
    def setUp(self):
        self.charm = Charm.objects.create(name="Test Charm")
        self.power = Effect.objects.create(name="Power")

    def test_set_power(self):
        self.assertFalse(self.charm.has_power())
        self.assertTrue(self.charm.set_power(self.power))
        self.assertTrue(self.charm.has_power())

    def test_has_power(self):
        self.assertFalse(self.charm.has_power())
        self.charm.set_power(self.power)
        self.assertTrue(self.charm.has_power())


class TestRandomCharm(TestCase):
    def setUp(self):
        grimoire_setup()

    def test_random_power(self):
        c = Charm.objects.create(name="", rank=3)
        self.assertFalse(c.has_power())
        self.assertTrue(c.random_power())
        self.assertTrue(c.has_power())

    def test_random(self):
        c = Charm.objects.create(name="")
        c.random()
        self.assertEqual(c.status, "Ran")
        self.assertTrue(c.has_name())
        self.assertTrue(c.has_rank())
        self.assertTrue(c.has_resonance())
        self.assertTrue(c.has_power())
        self.assertEqual(c.arete, c.rank)
        self.assertEqual(c.background_cost, c.rank)


class TestArtifact(TestCase):
    def setUp(self):
        self.artifact = Artifact.objects.create(name="Test Artifact")
        self.power = Effect.objects.create(name="Power")

    def test_set_power(self):
        self.assertFalse(self.artifact.has_power())
        self.assertTrue(self.artifact.set_power(self.power))
        self.assertTrue(self.artifact.has_power())

    def test_has_power(self):
        self.assertFalse(self.artifact.has_power())
        self.artifact.set_power(self.power)
        self.assertTrue(self.artifact.has_power())


class TestRandomArtifact(TestCase):
    def setUp(self):
        grimoire_setup()

    def test_random_power(self):
        a = Artifact.objects.create(name="", rank=3)
        self.assertFalse(a.has_power())
        self.assertTrue(a.random_power())
        self.assertTrue(a.has_power())

    def test_random(self):
        a = Artifact.objects.create(name="")
        a.random()
        self.assertEqual(a.status, "Ran")
        self.assertTrue(a.has_name())
        self.assertTrue(a.has_rank())
        self.assertTrue(a.has_resonance())
        self.assertTrue(a.has_power())
        self.assertEqual(a.quintessence_max, a.rank * 5)
        self.assertEqual(a.background_cost, a.rank * 2)


class TestTalisman(TestCase):
    def setUp(self):
        self.effect1 = Effect.objects.create(name="Effect 1", forces=3)
        self.effect2 = Effect.objects.create(name="Effect 2", life=2)
        self.effect3 = Effect.objects.create(name="Effect 3", time=3)

    def test_add_power(self):
        talisman = Talisman.objects.create(rank=2)
        self.assertEqual(talisman.powers.count(), 0)
        talisman.add_power(self.effect1)
        self.assertEqual(talisman.powers.count(), 1)
        talisman.add_power(self.effect2)
        self.assertEqual(talisman.powers.count(), 2)

    def test_has_powers(self):
        talisman = Talisman.objects.create(rank=2)
        self.assertFalse(talisman.has_powers())
        talisman.add_power(self.effect1)
        self.assertFalse(talisman.has_powers())
        talisman.add_power(self.effect2)
        self.assertTrue(talisman.has_powers())


class TestRandomTalisman(TestCase):
    def setUp(self):
        grimoire_setup()
        self.effect1 = Effect.objects.create(name="Effect 1", forces=1)
        self.effect2 = Effect.objects.create(name="Effect 2", life=2)
        self.effect3 = Effect.objects.create(name="Effect 3", time=3)

    def test_random_power(self):
        talisman = Talisman.objects.create(rank=2)
        talisman.random_power(1)
        self.assertEqual(talisman.powers.count(), 1)
        self.assertLessEqual(talisman.powers.first().max_sphere, 1)
        talisman.random_power(2)
        self.assertEqual(talisman.powers.count(), 2)
        max_sphere = max(p.max_sphere for p in talisman.powers.all())
        self.assertLessEqual(max_sphere, 2)

    def test_random_powers(self):
        talisman = Talisman.objects.create(rank=2)
        talisman.random_powers()
        self.assertEqual(talisman.powers.count(), 2)
        max_sphere = max(p.max_sphere for p in talisman.powers.all())
        self.assertLessEqual(max_sphere, 2)

    def test_random(self):
        talisman = Talisman.objects.create()
        mocker = Mock()
        mocker.side_effect = [0.8, 0.5, 0.5, 0.5, 0.5, 0.5]
        with mock.patch("random.random", mocker):
            talisman.random(rank=2)
        self.assertTrue(talisman.has_powers())
        max_sphere = max(p.max_sphere for p in talisman.powers.all())
        self.assertLessEqual(max_sphere, 2)
        self.assertEqual(talisman.quintessence_max, 10)
        self.assertEqual(talisman.background_cost, 4)
        self.assertEqual(talisman.arete, 2)


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
        self.effects = [
            Effect.objects.create(name=f"Test Effect {i}") for i in range(4)
        ]
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

    def test_set_effects(self):
        self.assertEqual(self.grimoire.effects.count(), 0)
        self.assertTrue(self.grimoire.set_effects(self.effects))
        self.assertEqual(set(self.grimoire.effects.all()), set(self.effects))

    def test_has_effects(self):
        self.assertFalse(self.grimoire.has_effects())
        self.grimoire.set_effects(self.effects)
        self.assertTrue(self.grimoire.has_effects())


class TestRandomGrimoire(TestCase):
    def setUp(self):
        self.grimoire = Grimoire.objects.create(name="Random Grimoire")
        grimoire_setup()

    def test_random_name(self):
        g = Grimoire.objects.create(name="")
        g.random_medium()
        g.random_spheres()
        self.assertFalse(g.has_name())
        self.assertTrue(g.random_name())
        self.assertTrue(g.has_name())

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

    def test_random_paradigms(self):
        # Test that random_paradigms() returns a queryset
        self.assertTrue(isinstance(self.grimoire.random_paradigms(None), QuerySet))

        # Test that random_paradigms() returns the correct number of paradigms
        random_num_paradigms = random.randint(1, 3)
        paradigms = Paradigm.objects.order_by("?")[:random_num_paradigms]
        self.grimoire.faction = None
        self.assertEqual(
            len(self.grimoire.random_paradigms(paradigms)), random_num_paradigms
        )

        # Test that random_paradigms() returns at least one paradigm
        self.grimoire.faction = None
        self.assertTrue(len(self.grimoire.random_paradigms(None)) >= 1)

    def test_random_practices(self):
        # Test that random_practices() returns a queryset
        self.assertTrue(isinstance(self.grimoire.random_practices(None), QuerySet))

        # Test that random_practices() returns the correct number of practices
        random_num_practices = random.randint(1, 3)
        practices = Practice.objects.order_by("?")[:random_num_practices]
        self.grimoire.faction = None
        self.assertEqual(
            len(self.grimoire.random_practices(practices)), random_num_practices
        )

        # Test that random_practices() returns at least one practice
        self.grimoire.faction = None
        self.assertTrue(len(self.grimoire.random_practices(None)) >= 1)

    def test_random_instruments(self):
        # Test that random_instruments() returns a queryset
        self.assertTrue(isinstance(self.grimoire.random_instruments(None), QuerySet))

        # Test that random_instruments() returns the correct number of instruments
        random_num_instruments = random.randint(1, 3)
        instruments = Instrument.objects.order_by("?")[:random_num_instruments]
        self.assertEqual(
            len(self.grimoire.random_instruments(instruments)), random_num_instruments
        )

        # Test that random_instruments() returns at least one instrument
        self.assertTrue(len(self.grimoire.random_instruments(None)) >= 1)

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

    def test_random_effects(self):
        self.assertFalse(self.grimoire.has_effects())
        self.grimoire.random_effects()
        self.assertTrue(self.grimoire.has_effects())

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
        self.assertFalse(self.grimoire.has_effects())
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
        self.assertTrue(self.grimoire.has_effects())


class TestGrimoireDetailView(TestCase):
    def setUp(self):
        self.grimoire = Grimoire.objects.create(name="Test Grimoire")

    def test_grimoire_detail_view_status_code(self):
        response = self.client.get(f"/wod/items/{self.grimoire.id}/")
        self.assertEqual(response.status_code, 200)

    def test_grimoire_detail_view_template(self):
        response = self.client.get(f"/wod/items/{self.grimoire.id}/")
        self.assertTemplateUsed(response, "wod/items/mage/grimoire/detail.html")
