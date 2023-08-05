import random

from django.contrib.auth.models import User
from django.test import TestCase

from cod.models.characters.ephemera import Ephemera, Numina
from cod.models.characters.mage import (
    Attainment,
    CoDRote,
    Legacy,
    Mage,
    Order,
    Path,
    Proximi,
    ProximiFamily,
)
from cod.models.characters.mortal import CoDMerit, CoDSpecialty, Condition
from core.models import Material

# Create your tests here.
ARCANA = [
    "space",
    "time",
    "death",
    "fate",
    "life",
    "matter",
    "forces",
    "prime",
    "mind",
    "spirit",
]


def mage_setup(mage):
    for i in range(5):
        x = Path.objects.create(
            name=f"Path {i}",
            ruling_arcana=[ARCANA[2 * i], ARCANA[2 * i + 1]],
            inferior_arcanum=ARCANA[(3 * i + 2) % 10],
        )
        x.path_materials.add(Material.objects.create(name=f"{x.name} material"))
        x.save()
        Order.objects.create(
            name=f"Order {i}", rote_skills=["athletics", "science", "occult"]
        )
    for path in Path.objects.all():
        for order in Order.objects.all():
            for arcanum in ARCANA:
                Legacy.objects.create(
                    name=f"{path.name} {order.name} {arcanum.title()} Legacy",
                    path=path,
                    order=order,
                    ruling_arcanum=arcanum,
                )
    for arcana in ARCANA:
        for level, practice in [
            (1, "compelling"),
            (2, "ruling"),
            (3, "fraying"),
            (4, "patterning"),
            (5, "making"),
        ]:
            for i in range(10):
                CoDRote.objects.create(
                    name=f"{practice.title()} {arcana.title()} Rote {i}",
                    practice=practice,
                    arcanum=arcana,
                    level=level,
                )

    for i in range(1, 5):
        for merit_type in ["Physical", "Social", "Mental", "Fighting", "Mage"]:
            CoDMerit.objects.create(
                name=f"{merit_type} Merit {i}",
                ratings=[i, i + 1],
                merit_type=merit_type,
            )
            CoDMerit.objects.create(
                name=f"{merit_type} Merit {i + 5}",
                ratings=[i, i + 1],
                merit_type=merit_type,
            )
            CoDMerit.objects.create(
                name=f"{merit_type} Merit {i + 10}",
                ratings=[i, i + 1],
                merit_type=merit_type,
            )

    for skill in mage.get_skills():
        for i in range(5):
            CoDSpecialty.objects.create(name=f"{skill.title()} {i}", skill=skill)

    for i in range(10):
        Numina.objects.create(name=f"Numina {i}")


class TestMage(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.mage)

    # def test_wisdom(self):
    #     self.assertEqual(self.mage.morality_name, "Wisdom")

    def test_has_path(self):
        self.assertFalse(self.mage.has_path())
        self.mage.path = Path.objects.get(name="Path 0")
        self.mage.save()
        self.assertTrue(self.mage.has_path())

    def test_set_path(self):
        self.assertFalse(self.mage.has_path())
        self.assertTrue(self.mage.set_path(Path.objects.get(name="Path 0")))
        self.assertTrue(self.mage.has_path())

    def test_has_order(self):
        self.assertFalse(self.mage.has_order())
        self.mage.order = Order.objects.get(name="Order 0")
        self.mage.save()
        self.assertTrue(self.mage.has_order())

    def test_set_order(self):
        self.assertFalse(self.mage.has_order())
        self.assertTrue(self.mage.set_order(Order.objects.get(name="Order 0")))
        self.assertTrue(self.mage.has_order())

    def test_has_legacy(self):
        self.assertFalse(self.mage.has_legacy())
        self.mage.legacy = Legacy.objects.get(name="Path 0 Order 0 Death Legacy")
        self.mage.save()
        self.assertTrue(self.mage.has_legacy())

    def test_set_legacy(self):
        self.mage.set_order(Order.objects.get(name="Order 0"))
        self.mage.set_path(Path.objects.get(name="Path 0"))
        self.mage.death = 2
        self.assertFalse(self.mage.has_legacy())
        self.assertTrue(
            self.mage.set_legacy(Legacy.objects.get(name="Path 0 Order 0 Death Legacy"))
        )
        self.assertTrue(self.mage.has_legacy())

    def test_filter_legacies(self):
        both_wrong = Mage.objects.create(name="Neither Character", owner=self.player)
        path_right = Mage.objects.create(name="Path Character", owner=self.player)
        order_right = Mage.objects.create(name="Order Character", owner=self.player)
        legacy = Legacy.objects.get(name="Path 0 Order 0 Death Legacy")
        right_order = Order.objects.get(name="Order 0")
        wrong_order = Order.objects.get(name="Order 1")
        right_path = Path.objects.get(name="Path 0")
        wrong_path = Path.objects.get(name="Path 1")
        both_wrong.set_order(wrong_order)
        both_wrong.set_path(wrong_path)
        path_right.set_order(wrong_order)
        path_right.set_path(right_path)
        order_right.set_order(right_order)
        order_right.set_path(wrong_path)
        self.assertNotIn(legacy, both_wrong.filter_legacies())
        self.assertNotIn(legacy, path_right.filter_legacies())
        self.assertNotIn(legacy, order_right.filter_legacies())
        both_wrong.death = 2
        path_right.death = 2
        order_right.death = 2
        self.assertNotIn(legacy, both_wrong.filter_legacies())
        self.assertIn(legacy, path_right.filter_legacies())
        self.assertIn(legacy, order_right.filter_legacies())

    def test_has_rote_skills(self):
        self.assertFalse(self.mage.has_rote_skills())
        self.mage.rote_skills = ["occult", "science", "athletics"]
        self.assertTrue(self.mage.has_rote_skills())

    def test_set_rote_skills(self):
        self.assertFalse(self.mage.has_rote_skills())
        self.assertTrue(self.mage.set_rote_skills(["occult", "science", "athletics"]))
        self.assertTrue(self.mage.has_rote_skills())

    def test_has_merits(self):
        self.assertFalse(self.mage.has_merits())
        self.mage.gnosis = 3
        self.assertTrue(self.mage.has_merits())
        self.mage.gnosis = 2
        self.assertFalse(self.mage.has_merits())
        m1 = CoDMerit.objects.get(name="Mage Merit 3")
        m2 = CoDMerit.objects.get(name="Mage Merit 2")
        self.mage.add_merit(m1)
        self.mage.add_merit(m2)
        self.assertTrue(self.mage.has_merits())
        self.mage.gnosis = 1
        self.assertFalse(self.mage.has_merits())
        m3 = CoDMerit.objects.get(name="Physical Merit 3")
        m4 = CoDMerit.objects.get(name="Physical Merit 2")
        self.mage.add_merit(m3)
        self.mage.add_merit(m4)
        self.assertTrue(self.mage.has_merits())

    def test_get_arcana(self):
        self.assertEqual(
            self.mage.get_arcana(),
            {
                "death": 0,
                "matter": 0,
                "life": 0,
                "spirit": 0,
                "forces": 0,
                "prime": 0,
                "fate": 0,
                "time": 0,
                "mind": 0,
                "space": 0,
            },
        )
        self.mage.matter = 2
        self.mage.spirit = 3
        self.assertEqual(
            self.mage.get_arcana(),
            {
                "death": 0,
                "matter": 2,
                "life": 0,
                "spirit": 3,
                "forces": 0,
                "prime": 0,
                "fate": 0,
                "time": 0,
                "mind": 0,
                "space": 0,
            },
        )

    def test_has_arcana(self):
        self.assertFalse(self.mage.has_arcana())
        p = Path.objects.get(name="Path 0")
        self.mage.set_path(p)
        self.mage.space = 3
        self.assertFalse(self.mage.has_arcana())
        self.mage.time = 1
        self.assertFalse(self.mage.has_arcana())
        self.mage.matter = 1
        self.assertFalse(self.mage.has_arcana())
        self.mage.spirit = 1
        self.assertTrue(self.mage.has_arcana())

    def test_add_arcanum(self):
        self.assertEqual(self.mage.death, 0)
        self.assertTrue(self.mage.add_arcanum("death"))
        self.assertEqual(self.mage.death, 1)

    def test_filter_arcana(self):
        self.mage.gnosis = 1
        self.assertEqual(len(self.mage.filter_arcana(minimum=0, maximum=5)), 10)
        self.mage.death = 3
        self.assertEqual(len(self.mage.filter_arcana(minimum=0, maximum=2)), 9)
        self.assertEqual(len(self.mage.filter_arcana(minimum=0, maximum=3)), 10)
        self.mage.matter = 2
        self.mage.spirit = 1
        self.assertEqual(len(self.mage.filter_arcana(minimum=1, maximum=5)), 3)
        self.assertEqual(len(self.mage.filter_arcana(minimum=2, maximum=5)), 2)
        self.assertEqual(len(self.mage.filter_arcana(minimum=3, maximum=5)), 1)
        self.assertEqual(len(self.mage.filter_arcana(minimum=4, maximum=5)), 0)

    def test_total_arcana(self):
        self.mage.gnosis = 1
        self.assertEqual(self.mage.total_arcana(), 0)
        self.mage.death = 3
        self.assertEqual(self.mage.total_arcana(), 3)
        self.mage.matter = 2
        self.assertEqual(self.mage.total_arcana(), 5)
        self.mage.spirit = 1
        self.assertEqual(self.mage.total_arcana(), 6)

    def test_add_attainment(self):
        att = Attainment.objects.create(name="test attainment")
        self.assertTrue(self.mage.add_attainment(att))
        self.assertTrue(att in self.mage.attainments.all())

    def test_set_dedicated_tool(self):
        tool = "test tool"
        self.assertTrue(self.mage.set_dedicated_tool(tool))
        self.assertEqual(self.mage.dedicated_tool, tool)

    def test_has_dedicated_tool(self):
        self.assertFalse(self.mage.has_dedicated_tool())
        self.mage.dedicated_tool = "test tool"
        self.assertTrue(self.mage.has_dedicated_tool())

    def test_set_obsession(self):
        obs = "test obsession"
        index = 0
        self.assertTrue(self.mage.set_obsession(obs, index))
        self.assertEqual(self.mage.obsessions[index], obs)

    def test_has_obsession(self):
        self.assertFalse(self.mage.has_obsessions())
        self.mage.gnosis = 3
        self.assertFalse(self.mage.has_obsessions())
        self.mage.obsessions = [None, "test obsession", None, "test 2"]
        self.assertTrue(self.mage.has_obsessions())

    def test_add_wisdom(self):
        self.assertEqual(self.mage.wisdom, 7)
        self.assertTrue(self.mage.add_wisdom())
        self.assertEqual(self.mage.wisdom, 8)

    def test_xp_cost(self):
        self.assertEqual(self.mage.xp_cost("arcanum (to limit)"), 4)
        self.assertEqual(self.mage.xp_cost("arcanum (above limit)"), 5)
        self.assertEqual(self.mage.xp_cost("gnosis"), 5)
        self.assertEqual(self.mage.xp_cost("rote"), 1)
        self.assertEqual(self.mage.xp_cost("praxis"), 1)
        self.assertEqual(self.mage.xp_cost("wisdom"), 2)
        self.assertEqual(self.mage.xp_cost("willpower"), 1)
        self.assertEqual(self.mage.xp_cost("legacy attainment (tutored)"), 1)
        self.assertEqual(self.mage.xp_cost("legacy attainment (untutored)"), 1)

    def test_add_gnosis(self):
        self.mage.gnosis = 1
        self.assertTrue(self.mage.add_gnosis())
        self.assertEqual(self.mage.gnosis, 2)
        self.mage.gnosis = 10
        self.assertFalse(self.mage.add_gnosis())
        self.assertEqual(self.mage.gnosis, 10)

    def test_has_gnosis(self):
        self.assertFalse(self.mage.has_gnosis())
        self.mage.gnosis = 1
        self.assertTrue(self.mage.has_gnosis())

    def test_set_gnosis(self):
        self.mage.gnosis = 1
        self.assertTrue(self.mage.set_gnosis(2))
        self.assertEqual(self.mage.gnosis, 2)
        self.mage.gnosis = 10
        self.assertFalse(self.mage.set_gnosis(11))
        self.assertEqual(self.mage.gnosis, 10)

    def test_has_mana(self):
        self.mage.gnosis = 1
        self.assertFalse(self.mage.has_mana())
        self.mage.mana = 10
        self.assertTrue(self.mage.has_mana())

    def test_set_mana(self):
        self.mage.gnosis = 1
        self.assertEqual(self.mage.mana, 0)
        self.assertTrue(self.mage.set_mana(5))
        self.assertEqual(self.mage.mana, 5)
        self.assertTrue(self.mage.set_mana(15))
        self.assertEqual(self.mage.mana, 10)

    def test_has_rotes(self):
        self.mage.death = 3
        self.mage.matter = 2
        self.mage.life = 1
        self.assertFalse(self.mage.has_rotes())
        self.mage.add_rote(CoDRote.objects.get(name="Compelling Death Rote 0"))
        self.mage.add_rote(CoDRote.objects.get(name="Compelling Matter Rote 0"))
        self.mage.add_rote(CoDRote.objects.get(name="Compelling Life Rote 0"))
        self.assertTrue(self.mage.has_rotes())

    def test_add_rote(self):
        self.mage.death = 3
        self.mage.save()
        num = self.mage.rotes.count()
        self.assertTrue(
            self.mage.add_rote(CoDRote.objects.get(name="Compelling Death Rote 0"))
        )
        self.assertFalse(
            self.mage.add_rote(CoDRote.objects.get(name="Compelling Matter Rote 0"))
        )
        self.assertEqual(self.mage.rotes.count(), num + 1)

    def test_total_rotes(self):
        self.mage.death = 3
        self.mage.matter = 2
        self.mage.life = 1
        self.assertEqual(self.mage.total_rotes(), 0)
        self.mage.add_rote(CoDRote.objects.get(name="Compelling Death Rote 0"))
        self.assertEqual(self.mage.total_rotes(), 1)
        self.mage.add_rote(CoDRote.objects.get(name="Compelling Matter Rote 0"))
        self.assertEqual(self.mage.total_rotes(), 2)
        self.mage.add_rote(CoDRote.objects.get(name="Compelling Life Rote 0"))
        self.assertEqual(self.mage.total_rotes(), 3)

    def test_filter_rotes(self):
        self.assertEqual(len(self.mage.filter_rotes()), 0)
        self.mage.death = 3
        self.assertEqual(len(self.mage.filter_rotes()), 30)
        self.mage.fate = 2
        self.assertEqual(len(self.mage.filter_rotes()), 50)
        self.mage.spirit = 1
        self.assertEqual(len(self.mage.filter_rotes()), 60)
        r = CoDRote.objects.get(name="Compelling Death Rote 0")
        self.assertIn(r, self.mage.filter_rotes())
        self.mage.add_rote(r)
        self.assertNotIn(r, self.mage.filter_rotes())
        self.assertEqual(len(self.mage.filter_rotes()), 59)

    def test_has_nimbus(self):
        self.assertFalse(self.mage.has_nimbus())
        self.mage.nimbus = "It's a Nimbus!"
        self.assertTrue(self.mage.has_nimbus())

    def test_set_nimbus(self):
        self.assertFalse(self.mage.has_nimbus())
        self.mage.set_nimbus("It's a Nimbus!")
        self.assertTrue(self.mage.has_nimbus())

    def test_practice_level_translation(self):
        self.assertEqual(self.mage.practice_level("compelling"), 1)
        self.assertEqual(self.mage.practice_level("knowing"), 1)
        self.assertEqual(self.mage.practice_level("unveiling"), 1)
        self.assertEqual(self.mage.practice_level("ruling"), 2)
        self.assertEqual(self.mage.practice_level("shielding"), 2)
        self.assertEqual(self.mage.practice_level("veiling"), 2)
        self.assertEqual(self.mage.practice_level("fraying"), 3)
        self.assertEqual(self.mage.practice_level("perfecting"), 3)
        self.assertEqual(self.mage.practice_level("weaving"), 3)
        self.assertEqual(self.mage.practice_level("patterning"), 4)
        self.assertEqual(self.mage.practice_level("unraveling"), 4)
        self.assertEqual(self.mage.practice_level("making"), 5)
        self.assertEqual(self.mage.practice_level("unmaking"), 5)

        self.assertEqual(
            self.mage.practices_at_level(1), ["compelling", "knowing", "unveiling"]
        )
        self.assertEqual(
            self.mage.practices_at_level(2), ["ruling", "shielding", "veiling"]
        )
        self.assertEqual(
            self.mage.practices_at_level(3), ["fraying", "perfecting", "weaving"]
        )
        self.assertEqual(self.mage.practices_at_level(4), ["patterning", "unraveling"])
        self.assertEqual(self.mage.practices_at_level(5), ["making", "unmaking"])

    def test_arcane_xp(self):
        self.assertEqual(self.mage.arcane_xp, 0)
        self.mage.arcane_xp = 100
        self.assertTrue(self.mage.spend_xp("gnosis"))
        self.assertEqual(self.mage.arcane_xp, 95)
        self.assertTrue(self.mage.spend_xp("life"))
        self.assertEqual(self.mage.arcane_xp, 91)
        self.assertTrue(self.mage.spend_xp("Compelling Life Rote 0", praxis=True))
        self.assertEqual(self.mage.arcane_xp, 90)
        self.assertTrue(self.mage.spend_xp("wisdom"))
        self.assertEqual(self.mage.arcane_xp, 88)
        # Legacy Attainment should cost 1 Arcane XP both tutored and untutored

        self.mage.xp = 100
        self.mage.arcane_xp = 0
        self.assertFalse(self.mage.spend_xp("Compelling Life Rote 1", praxis=True))
        self.assertFalse(self.mage.spend_xp("wisdom"))
        # Legacy Attainment should fail if untutored and no arcane xp
        self.mage.arcane_xp = 3
        self.assertTrue(self.mage.spend_xp("gnosis"))
        self.assertEqual(self.mage.xp, 98)
        self.assertEqual(self.mage.arcane_xp, 0)
        self.mage.arcane_xp = 3
        self.assertTrue(self.mage.spend_xp("life"))
        self.assertEqual(self.mage.xp, 97)
        self.assertEqual(self.mage.arcane_xp, 0)

    def test_spend_xp(self):
        self.mage.xp = 10
        self.mage.arcane_xp = 10
        self.assertTrue(self.mage.spend_xp("gnosis"))
        self.assertTrue(self.mage.spend_xp("prime"))
        self.assertFalse(self.mage.spend_xp("invalid_trait"))

    def test_random_xp_functions(self):
        random_xp_functions = self.mage.random_xp_functions()
        self.assertIn("attribute", random_xp_functions)
        self.assertIn("merit", random_xp_functions)
        self.assertIn("specialty", random_xp_functions)
        self.assertIn("skill", random_xp_functions)
        self.assertIn("wisdom", random_xp_functions)
        self.assertIn("arcanum", random_xp_functions)
        self.assertIn("gnosis", random_xp_functions)
        self.assertIn("rote", random_xp_functions)
        self.assertIn("attainment", random_xp_functions)

    def test_spend_xp_arcana(self):
        self.mage.gnosis = 1
        self.assertFalse(self.mage.spend_xp_arcana("death"))

        self.mage.death = 3
        self.mage.arcane_xp = 4
        self.assertFalse(self.mage.spend_xp_arcana("death"))
        self.mage.arcane_xp = 5
        self.assertTrue(self.mage.spend_xp_arcana("death"))

        self.mage.gnosis = 5
        self.mage.arcane_xp = 5
        self.assertTrue(self.mage.spend_xp_arcana("death"))
        self.assertEqual(self.mage.death, 5)

    def test_spend_xp_attainment(self):
        attainment = Attainment.objects.create()
        legacy = Legacy.objects.create()
        legacy.attainments.add(attainment)
        self.mage.legacy = legacy
        self.mage.xp = 5

        self.assertFalse(self.mage.spend_xp_attainment(attainment, tutored=False))
        self.assertTrue(self.mage.spend_xp_attainment(attainment))

    def test_spend_xp_rote(self):
        rote = CoDRote.objects.get(name="Compelling Forces Rote 0")
        praxis = CoDRote.objects.get(name="Compelling Forces Rote 1")
        self.mage.gnosis = 1
        self.mage.forces = 1

        # Test failing to spend XP
        self.mage.arcane_xp = 1
        self.assertFalse(self.mage.spend_xp_rote(rote.name))
        self.assertEqual(self.mage.arcane_xp, 1)
        self.assertEqual(self.mage.rotes.count(), 0)
        self.assertEqual(self.mage.praxes.count(), 0)

        # Test spending normal XP
        self.mage.xp = 1
        self.assertTrue(self.mage.spend_xp_rote(rote.name))
        self.assertEqual(self.mage.xp, 0)
        self.assertEqual(self.mage.rotes.count(), 1)
        self.assertEqual(self.mage.praxes.count(), 0)

        # Test spending arcane XP for praxis
        self.assertTrue(self.mage.spend_xp_rote(praxis.name, praxis=True))
        self.assertEqual(self.mage.arcane_xp, 0)
        self.assertEqual(self.mage.rotes.count(), 1)
        self.assertEqual(self.mage.praxes.count(), 1)

    def test_spend_xp_gnosis(self):
        self.mage.gnosis = 1
        self.mage.xp = 6
        self.mage.arcane_xp = 0

        # Test spending normal XP
        self.assertTrue(self.mage.spend_xp_gnosis())
        self.assertEqual(self.mage.xp, 1)
        self.assertEqual(self.mage.gnosis, 2)

        # Test spending mixed XP
        self.mage.xp = 4
        self.mage.arcane_xp = 1
        self.assertTrue(self.mage.spend_xp_gnosis())
        self.assertEqual(self.mage.arcane_xp, 0)
        self.assertEqual(self.mage.xp, 0)
        self.assertEqual(self.mage.gnosis, 3)

        # Test failing to spend XP
        self.mage.xp = 0
        self.mage.arcane_xp = 0
        self.assertFalse(self.mage.spend_xp_gnosis())
        self.assertEqual(self.mage.gnosis, 3)

    def test_spend_xp_wisdom(self):
        self.mage.arcane_xp = 10

        # Test spending arcane XP
        self.assertTrue(self.mage.spend_xp_wisdom())
        self.assertEqual(self.mage.arcane_xp, 8)
        self.assertEqual(self.mage.wisdom, 8)

        # Test failing to spend XP
        self.mage.arcane_xp = 0
        self.mage.xp = 4
        self.assertFalse(self.mage.spend_xp_wisdom())
        self.assertEqual(self.mage.wisdom, 8)

    def test_set_familiar(self):
        familiar = Ephemera.objects.create(name="Test Familiar")
        self.mage.set_familiar(familiar)
        self.assertEqual(self.mage.familiar, familiar)

    def test_assign_advantages(self):
        order = Order.objects.create(name="Test Order")
        merit = CoDMerit.objects.create(name="Test Order Status", ratings=[1, 2, 3])
        high_speech = CoDMerit.objects.create(name="High Speech", ratings=[1])
        self.mage.order = order
        self.mage.assign_advantages()
        self.assertIn(merit, self.mage.merits.all())
        self.assertIn(high_speech, self.mage.merits.all())


class TestRandomMage(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.mage)

    def test_random_path(self):
        self.assertFalse(self.mage.has_path())
        self.assertTrue(self.mage.random_path())
        self.assertTrue(self.mage.has_path())

    def test_random_order(self):
        self.assertFalse(self.mage.has_order())
        self.assertTrue(self.mage.random_order())
        self.assertTrue(self.mage.has_order())

    def test_random_legacy(self):
        self.mage.random_order()
        self.mage.random_path()
        self.mage.random_arcana()
        self.assertFalse(self.mage.has_legacy())
        self.assertTrue(self.mage.random_legacy())
        self.assertTrue(self.mage.has_legacy())

    def test_random_arcanum(self):
        num = self.mage.total_arcana()
        self.assertTrue(self.mage.random_arcanum())
        self.assertEqual(self.mage.total_arcana(), num + 1)

    def test_random_arcana(self):
        self.mage.random_path()
        self.assertFalse(self.mage.has_arcana())
        self.assertTrue(self.mage.random_arcana())
        self.assertTrue(self.mage.has_arcana())

    def test_random_rote(self):
        self.mage.death = 3
        num = self.mage.rotes.count()
        self.assertTrue(self.mage.random_rote(praxis=False))
        self.assertEqual(self.mage.rotes.count(), num + 1)

    def test_random_dedicated_tool(self):
        self.mage.random_path()
        self.mage.random_dedicated_tool()
        self.assertNotEqual(self.mage.dedicated_tool, "")

    def test_random_obsessions(self):
        self.mage.random_obsessions()
        self.assertTrue(self.mage.has_obsessions())

    def test_random_gnosis(self):
        # Mock random value below 0.7
        random.random = lambda: 0.6
        mage = Mage()
        mage.random_gnosis()
        self.assertEqual(mage.gnosis, 1)

        # Mock random value between 0.7 and 0.9
        random.random = lambda: 0.8
        mage = Mage()
        mage.random_gnosis()
        self.assertEqual(mage.gnosis, 2)

        # Mock random value above 0.9
        random.random = lambda: 0.95
        mage = Mage()
        mage.random_gnosis()
        self.assertEqual(mage.gnosis, 3)

    def test_random_rotes(self):
        self.mage.death = 3
        self.mage.matter = 2
        self.mage.spirit = 1
        self.assertFalse(self.mage.has_rotes())
        self.assertTrue(self.mage.random_rotes())
        self.assertTrue(self.mage.has_rotes())

    def test_random_nimbus(self):
        self.assertFalse(self.mage.has_nimbus())
        self.assertTrue(self.mage.random_nimbus())
        self.assertTrue(self.mage.has_nimbus())

    def test_random_spend_xp(self):
        self.mage.gnosis = 1
        self.mage.random_path()
        self.mage.random_order()
        self.mage.random_skills()
        self.mage.random_arcana()
        self.mage.xp = 20
        self.mage.random_spend_xp()
        self.assertLess(self.mage.xp, 20)

    def test_random_xp_attainment(self):
        attainment = Attainment.objects.create()
        legacy = Legacy.objects.create()
        legacy.attainments.add(attainment)
        self.mage.legacy = legacy
        self.mage.xp = 5
        self.mage.arcane_xp = 5
        self.mage.random_xp_attainment()
        self.assertTrue(self.mage.attainments.count() > 0)

    def test_random_xp_wisdom(self):
        self.mage.arcane_xp = 2
        self.mage.random_xp_wisdom()
        self.assertGreater(self.mage.wisdom, 7)

    def test_random_xp_arcanum(self):
        self.mage.gnosis = 1
        num = self.mage.total_arcana()
        self.mage.xp = 5
        self.mage.random_xp_arcanum()
        self.assertGreater(self.mage.total_arcana(), num)

    def test_random_xp_gnosis(self):
        self.mage.gnosis = 1
        self.mage.xp = 5
        self.mage.random_xp_gnosis()
        self.assertGreater(self.mage.gnosis, 1)

    def test_random_xp_rote(self):
        self.mage.gnosis = 3
        self.mage.forces = 3
        self.mage.matter = 3
        self.mage.prime = 2
        self.mage.xp = 1
        self.mage.arcane_xp = 1
        self.mage.random_xp_rote()
        self.assertTrue(self.mage.rotes.count() + self.mage.praxes.count() > 0)

    def test_random_familiar(self):
        # Without the "Familiar" merit, random_familiar should return False
        self.assertFalse(self.mage.random_familiar())

        # Add the "Familiar" merit to the mage
        familiar_merit = CoDMerit.objects.create(
            name="Familiar", ratings=[2, 4, 6, 8, 10]
        )
        self.mage.add_merit(familiar_merit)
        # Try again with the merit - this time random_familiar should succeed
        self.assertTrue(self.mage.random_familiar())
        self.assertIsNotNone(self.mage.familiar)

        # Check that the familiar has the expected rank
        expected_rank = self.mage.merit_rating("Familiar") // 2
        self.assertEqual(self.mage.familiar.rank, expected_rank)

        # Check that the familiar has a name
        self.assertIsNotNone(self.mage.familiar.name)

    def test_random(self):
        self.assertFalse(self.mage.has_path())
        self.assertFalse(self.mage.has_order())
        self.assertFalse(self.mage.has_rote_skills())
        self.assertFalse(self.mage.has_arcana())
        self.assertFalse(self.mage.has_gnosis())
        self.assertFalse(self.mage.has_mana())
        self.assertFalse(self.mage.has_rotes())
        self.assertFalse(self.mage.has_nimbus())
        self.assertFalse(self.mage.has_dedicated_tool())
        self.assertFalse(self.mage.has_obsessions())
        self.mage.random(xp=0)
        self.assertTrue(self.mage.has_path())
        self.assertTrue(self.mage.has_order())
        self.assertTrue(self.mage.has_rote_skills())
        self.assertTrue(self.mage.has_arcana())
        self.assertTrue(self.mage.has_gnosis())
        self.assertTrue(self.mage.has_mana())
        self.assertTrue(self.mage.has_rotes())
        self.assertTrue(self.mage.has_nimbus())
        self.assertTrue(self.mage.has_dedicated_tool())
        self.assertTrue(self.mage.has_obsessions())


class TestMageDetailView(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/cod/characters/{self.mage.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/cod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "cod/characters/mage/mage/detail.html")


class TestProximiFamily(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.mage)
        self.proximi_family = ProximiFamily.objects.create(name="Test Family")
        self.path = Path.objects.create(name="Test Path", ruling_arcana=["mind"])
        self.blessing1 = CoDRote.objects.create(
            name="Test Blessing 1", level=2, arcanum="mind"
        )
        self.blessing2 = CoDRote.objects.create(
            name="Test Blessing 2", level=3, arcanum="mind"
        )
        self.blessing3 = CoDRote.objects.create(
            name="Test Blessing 3", level=1, arcanum="mind"
        )
        self.curse = Condition.objects.create(name="Test Curse", persistent=True)

    def test_has_parent_path(self):
        self.assertFalse(self.proximi_family.has_parent_path())
        self.proximi_family.path = Path.objects.get(name="Path 0")
        self.assertTrue(self.proximi_family.has_parent_path())

    def test_set_parent_path(self):
        self.assertFalse(self.proximi_family.has_parent_path())
        self.assertTrue(
            self.proximi_family.set_parent_path(Path.objects.get(name="Path 0"))
        )
        self.assertTrue(self.proximi_family.has_parent_path())

    def test_has_blessing_arcana(self):
        self.assertFalse(self.proximi_family.has_blessing_arcana())
        self.proximi_family.blessing_arcana = "death"
        self.assertTrue(self.proximi_family.has_blessing_arcana())

    def test_set_blessing_arcana(self):
        self.assertFalse(self.proximi_family.has_blessing_arcana())
        self.proximi_family.set_blessing_arcana("death")
        self.assertTrue(self.proximi_family.has_blessing_arcana())

    def test_has_possible_blessings(self):
        self.assertFalse(self.proximi_family.has_possible_blessings())
        while sum(x.level for x in self.proximi_family.possible_blessings.all()) < 30:
            options = CoDRote.objects.filter(
                level__lte=3, arcanum__in=["death", "space", "time"]
            )
            choice = random.choice(options)
            if (
                choice.level
                + sum(x.level for x in self.proximi_family.possible_blessings.all())
                <= 30
            ):
                self.proximi_family.possible_blessings.add(choice)
        self.assertTrue(self.proximi_family.has_possible_blessings())

    def test_set_possible_blessings(self):
        self.assertFalse(self.proximi_family.has_possible_blessings())
        L = []
        while sum(x.level for x in L) < 30:
            options = CoDRote.objects.filter(
                level__lte=3, arcanum__in=["death", "space", "time"]
            ).exclude(pk__in=[x.id for x in L])
            choice = random.choice(options)
            if choice.level + sum(x.level for x in L) <= 30:
                L.append(choice)
        self.assertTrue(self.proximi_family.set_possible_blessings(L))
        self.assertTrue(self.proximi_family.has_possible_blessings())

    def test_total_possible_blessings(self):
        family = ProximiFamily.objects.create(
            name="Test Family", path=self.path, blessing_arcana="mind"
        )
        family.add_possible_blessing(self.blessing1)
        family.add_possible_blessing(self.blessing2)
        family.add_possible_blessing(self.blessing3)
        self.assertEqual(family.total_possible_blessings(), 6)

    def test_add_possible_blessing(self):
        family = ProximiFamily.objects.create(
            name="Test Family", path=self.path, blessing_arcana="mind"
        )
        family.add_possible_blessing(self.blessing1)
        family.add_possible_blessing(self.blessing2)
        self.assertEqual(family.total_possible_blessings(), 5)
        self.assertTrue(self.blessing1 in family.possible_blessings.all())
        self.assertTrue(self.blessing2 in family.possible_blessings.all())
        self.assertFalse(self.blessing3 in family.possible_blessings.all())

    def test_set_curse(self):
        family = ProximiFamily.objects.create(
            name="Test Family", path=self.path, blessing_arcana="mind"
        )
        family.set_curse(self.curse)
        self.assertEqual(family.curse, self.curse)


class TestProximi(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.mage)
        for path in Path.objects.all():
            for arcana in ARCANA:
                if arcana not in path.ruling_arcana:
                    proximi_family = ProximiFamily.objects.create(
                        name=f"{path.name} {arcana.title()} Family",
                        path=path,
                        blessing_arcana=arcana,
                    )
                    L = []
                    while sum(x.level for x in L) < 30:
                        options = CoDRote.objects.filter(
                            level__lte=3, arcanum__in=["death", "space", "time"]
                        )
                        choice = random.choice(options)
                        if (
                            choice.level
                            + sum(
                                x.level for x in proximi_family.possible_blessings.all()
                            )
                            <= 30
                        ):
                            L.append(choice)
                    proximi_family.set_possible_blessings(L)
        self.proximi = Proximi.objects.create(name="Test Proximi", owner=self.player)

    def test_has_family(self):
        self.assertFalse(self.proximi.has_family())
        self.proximi.family = ProximiFamily.objects.get(name="Path 0 Death Family")
        self.assertTrue(self.proximi.has_family())

    def test_set_family(self):
        self.assertFalse(self.proximi.has_family())
        self.assertTrue(
            self.proximi.set_family(
                ProximiFamily.objects.get(name="Path 0 Death Family")
            )
        )
        self.assertTrue(self.proximi.has_family())

    def test_has_blessings(self):
        self.proximi.set_family(ProximiFamily.objects.get(name="Path 0 Death Family"))
        self.assertFalse(self.proximi.has_blessings())
        self.proximi.blessings.add(self.proximi.family.possible_blessings.first())
        self.assertTrue(self.proximi.has_blessings())

    def test_set_blessings(self):
        self.proximi.set_family(ProximiFamily.objects.get(name="Path 0 Death Family"))
        self.assertFalse(self.proximi.has_blessings())
        blessings = self.proximi.family.possible_blessings.all()[:3]
        self.assertTrue(self.proximi.set_blessings(blessings))
        self.assertTrue(self.proximi.has_blessings())
        for blessing in blessings:
            self.assertIn(blessing, self.proximi.blessings.all())
        self.assertEqual(self.proximi.blessings.count(), 3)

    def test_add_blessing(self):
        self.proximi.set_family(ProximiFamily.objects.get(name="Path 0 Death Family"))
        self.assertFalse(self.proximi.has_blessings())
        b = self.proximi.family.possible_blessings.first()
        self.assertTrue(self.proximi.add_blessing(b))
        self.assertTrue(self.proximi.has_blessings())

    def test_has_mana(self):
        self.assertFalse(self.proximi.has_mana())
        self.proximi.mana = 5
        self.assertTrue(self.proximi.has_mana())

    def test_set_mana(self):
        self.assertFalse(self.proximi.has_mana())
        self.assertTrue(self.proximi.set_mana(5))
        self.assertTrue(self.proximi.has_mana())
        self.assertFalse(self.proximi.set_mana(10))

    def test_random_xp_functions(self):
        xp_functions = self.proximi.random_xp_functions()
        self.assertTrue(callable(xp_functions["blessing"]))

    def test_spend_xp_blessing(self):
        family = ProximiFamily.objects.create()
        family.random()
        blessing = family.possible_blessings.first()
        self.proximi.family = family
        self.proximi.set_mana(5)
        self.proximi.xp = 10
        self.assertTrue(self.proximi.spend_xp_blessing(blessing))
        self.assertEqual(self.proximi.xp, 10 - blessing.level)

    def test_total_merits(self):
        self.assertEqual(self.proximi.total_merits(), 0)
        merit = CoDMerit.objects.create(name="Test Merit", ratings=[2])
        self.proximi.add_merit(merit)
        self.assertEqual(self.proximi.total_merits(), 2)

    def test_total_blessings(self):
        family = ProximiFamily.objects.create()
        family.random()
        self.proximi.family = family
        blessing = family.possible_blessings.first()
        self.assertEqual(self.proximi.total_blessings(), 0)
        self.proximi.add_blessing(blessing)
        self.assertEqual(self.proximi.total_blessings(), blessing.level)


class TestRandomProximiFamily(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.mage)
        self.proximi_family = ProximiFamily.objects.create(name="Test Family")
        self.path = Path.objects.create(
            name="Test Path", ruling_arcana=["mind", "prime"]
        )

    def test_random_name(self):
        pf = ProximiFamily.objects.create(path=self.path)
        pf.random_name()
        self.assertEqual(pf.name, f"Proximi Family {ProximiFamily.objects.count()}")

    def test_random_parent_path(self):
        self.assertFalse(self.proximi_family.has_parent_path())
        self.assertTrue(self.proximi_family.random_parent_path())
        self.assertTrue(self.proximi_family.has_parent_path())

    def test_random_blessing_arcana(self):
        self.proximi_family.set_parent_path(Path.objects.first())
        self.assertFalse(self.proximi_family.has_blessing_arcana())
        self.assertTrue(self.proximi_family.random_blessing_arcana())
        self.assertTrue(self.proximi_family.has_blessing_arcana())

    def test_random_blessing(self):
        pf = ProximiFamily.objects.create(path=self.path)
        CoDRote.objects.create(name="Test Blessing", level=1, arcanum="mind")
        pf.random_blessing(max_rating=1)
        self.assertGreaterEqual(pf.possible_blessings.all().count(), 1)

    def test_random_blessings(self):
        self.proximi_family.set_parent_path(Path.objects.first())
        self.proximi_family.set_blessing_arcana("death")
        self.assertFalse(self.proximi_family.has_possible_blessings())
        self.assertTrue(self.proximi_family.random_blessings())
        self.assertTrue(self.proximi_family.has_possible_blessings())

    def test_random_curse(self):
        pf = ProximiFamily.objects.create(path=self.path)
        pf.random_curse()
        self.assertTrue(pf.curse is not None)

    def test_random(self):
        self.assertFalse(self.proximi_family.has_parent_path())
        self.assertFalse(self.proximi_family.has_blessing_arcana())
        self.assertFalse(self.proximi_family.has_possible_blessings())
        self.assertTrue(self.proximi_family.random())
        self.assertTrue(self.proximi_family.has_possible_blessings())
        self.assertTrue(self.proximi_family.has_blessing_arcana())
        self.assertTrue(self.proximi_family.has_parent_path())


class TestRandomProximi(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.mage)
        for path in Path.objects.all():
            for arcana in ARCANA:
                if arcana not in path.ruling_arcana:
                    proximi_family = ProximiFamily.objects.create(
                        name=f"{path.name} {arcana.title()} Family",
                        path=path,
                        blessing_arcana=arcana,
                    )
                    L = []
                    while sum(x.level for x in L) < 30:
                        options = CoDRote.objects.filter(
                            level__lte=3, arcanum__in=["death", "space", "time"]
                        )
                        choice = random.choice(options)
                        if (
                            choice.level
                            + sum(
                                x.level for x in proximi_family.possible_blessings.all()
                            )
                            <= 30
                        ):
                            L.append(choice)
                    proximi_family.set_possible_blessings(L)
        self.proximi = Proximi.objects.create(name="", owner=self.player)

    def test_random_family(self):
        self.assertFalse(self.proximi.has_family())
        self.assertTrue(self.proximi.random_family())
        self.assertTrue(self.proximi.has_family())

    def test_random_blessing(self):
        family = ProximiFamily.objects.create()
        family.random()
        self.proximi.family = family
        self.proximi.xp = 10
        self.assertFalse(self.proximi.has_blessings())
        self.assertTrue(self.proximi.random_blessing())
        self.assertTrue(self.proximi.has_blessings())
        self.assertEqual(self.proximi.blessings.count(), 1)

    def test_random_xp_blessing(self):
        family = ProximiFamily.objects.create()
        family.random()
        self.proximi.family = family
        self.proximi.set_mana(5)
        self.proximi.xp = 10
        self.proximi.random_xp_blessing()
        blessing = self.proximi.blessings.first()
        self.assertEqual(self.proximi.total_blessings(), blessing.level)
        self.assertEqual(self.proximi.xp, 10 - blessing.level)

    def test_random(self):
        self.assertFalse(self.proximi.has_name())
        self.assertFalse(self.proximi.has_concept())
        self.assertFalse(self.proximi.has_virtue())
        self.assertFalse(self.proximi.has_vice())
        self.assertFalse(self.proximi.has_family())
        self.assertFalse(self.proximi.has_aspirations())
        self.assertFalse(self.proximi.has_attributes())
        self.assertFalse(self.proximi.has_skills())
        self.assertFalse(self.proximi.has_specialties())
        self.assertFalse(self.proximi.has_merits())
        self.assertFalse(self.proximi.has_mana())
        self.assertFalse(self.proximi.has_blessings())
        self.proximi.random()
        self.assertTrue(self.proximi.has_name())
        self.assertTrue(self.proximi.has_concept())
        self.assertTrue(self.proximi.has_virtue())
        self.assertTrue(self.proximi.has_vice())
        self.assertTrue(self.proximi.has_family())
        self.assertTrue(self.proximi.has_aspirations())
        self.assertTrue(self.proximi.has_attributes())
        self.assertTrue(self.proximi.has_skills())
        self.assertTrue(self.proximi.has_specialties())
        self.assertTrue(self.proximi.has_merits())
        self.assertTrue(self.proximi.has_mana())
        self.assertTrue(self.proximi.has_blessings())


class TestProximiFamilyDetailView(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", owner=self.player)
        mage_setup(self.mage)
        self.proximi_family = ProximiFamily.objects.create(name="Test Family")
        self.proximi_family.random()

    def test_proximi_family_detail_view_status_code(self):
        response = self.client.get(
            f"/cod/characters/proximifamily/{self.proximi_family.id}/"
        )
        self.assertEqual(response.status_code, 200)

    def test_proximi_family_detail_view_templates(self):
        response = self.client.get(
            f"/cod/characters/proximifamily/{self.proximi_family.id}/"
        )
        self.assertTemplateUsed(
            response, "cod/characters/mage/proximifamily/detail.html"
        )


class TestProximiDetailView(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.proximi = Proximi.objects.create(name="Test Proximus", owner=self.player)

    def test_proximi_detail_view_status_code(self):
        response = self.client.get(f"/cod/characters/{self.proximi.id}/")
        self.assertEqual(response.status_code, 200)

    def test_proximi_detail_view_templates(self):
        response = self.client.get(f"/cod/characters/{self.proximi.id}/")
        self.assertTemplateUsed(response, "cod/characters/mage/proximi/detail.html")


class TestAttainment(TestCase):
    def setUp(self) -> None:
        self.legacy = Legacy.objects.create()
        self.attainment = Attainment.objects.create(
            name="Test Attainment", legacy=self.legacy
        )
        self.character = Mage.objects.create()

    def test_prereq_satisfied(self):
        # Test when prereq is a skill and is satisfied
        prereq = ("occult", 3)
        self.character.occult = 4
        self.character.weaponry = 2
        self.assertTrue(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is a skill and is not satisfied
        self.character.occult = 2
        self.assertFalse(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is an arcana and is satisfied
        prereq = ("forces", 3)
        self.character.forces = 4
        self.character.life = 2
        self.assertTrue(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is an arcana and is not satisfied
        self.character.forces = 2
        self.assertFalse(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is an attainment and is not satisfied
        prereq = ("attainment", "Test Attainment")
        test_attainment = Attainment.objects.create(name="Test Attainment")
        self.assertFalse(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is an attainment and is satisfied
        prereq = ("attainment", "Test Attainment")
        self.character.attainments.add(test_attainment)
        self.assertTrue(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is a legacy and is not satisfied
        prereq = ("legacy", "Test Legacy")
        test_legacy = Legacy.objects.create(name="Test Legacy")
        self.assertFalse(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is a legacy and is satisfied
        self.character.legacy = test_legacy
        self.assertTrue(self.attainment.prereq_satisfied(prereq, self.character))

        # Test when prereq is invalid
        prereq = ("invalid", "invalid_value")
        self.assertFalse(self.attainment.prereq_satisfied(prereq, self.character))

    def test_check_prereqs(self):
        self.attainment.prereqs = [
            [("occult", 3), ("weaponry", 2), ("forces", 3), ("life", 1)]
        ]
        # Test when all prereqs are satisfied
        self.character.occult = 3
        self.character.weaponry = 2
        self.character.forces = 3
        self.character.life = 1
        self.assertTrue(self.attainment.check_prereqs(self.character))

        # Test when some prereqs are not satisfied
        self.character.forces = 1
        self.assertFalse(self.attainment.check_prereqs(self.character))

    def test_count_prereqs(self):
        self.attainment.prereqs = [[("occult", 3), ("weaponry", 2)]]

        self.character.occult = 4
        self.character.weaponry = 2
        self.assertEqual(self.attainment.count_prereqs(self.character), 2)

        self.character.occult = 2
        self.character.weaponry = 2
        self.assertEqual(self.attainment.count_prereqs(self.character), 1)


class TestLegacy(TestCase):
    def setUp(self) -> None:
        self.path = Path.objects.create(name="Test Path")
        self.order = Order.objects.create(name="Test Order")
        self.attainment = Attainment.objects.create(name="Test Attainment")
        self.legacy = Legacy.objects.create(
            path=self.path,
            order=self.order,
            ruling_arcanum="prime",
            is_left_handed=True,
            prereqs=[[("occult", 3), ("weaponry", 2)]],
        )
        self.character = Mage.objects.create()

    def test_prereq_satisfied(self):
        prereq = ("occult", 3)
        # Test when prereq is not satisfied
        self.character.occult = 2
        self.character.melee = 2
        self.assertFalse(self.legacy.prereq_satisfied(prereq, self.character))

        # Test when prereq is satisfied
        self.character.occult = 4
        self.character.melee = 2
        self.assertTrue(self.legacy.prereq_satisfied(prereq, self.character))

    def test_check_prereqs(self):
        # Test when all prereqs are satisfied
        self.character.occult = 4
        self.character.weaponry = 3
        self.assertTrue(self.legacy.check_prereqs(self.character))

        # Test when some prereqs are not satisfied
        self.character.occult = 2
        self.character.weaponry = 2
        self.assertFalse(self.legacy.check_prereqs(self.character))

    def test_count_prereqs(self):
        self.character.occult = 4
        self.character.weaponry = 2
        self.assertEqual(self.legacy.count_prereqs(self.character), 2)

        self.character.occult = 2
        self.character.weaponry = 2
        self.assertEqual(self.legacy.count_prereqs(self.character), 1)
