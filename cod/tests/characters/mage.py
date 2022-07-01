from django.contrib.auth.models import User
from django.test import TestCase
from cod.models.characters.mage import Path, Mage, Order, Legacy, Spell, Rote
from cod.models.characters.mortal import Merit


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


def mage_setup():
    for i in range(5):
        Path.objects.create(
            name=f"Path {i}",
            ruling_arcana=[ARCANA[2 * i], ARCANA[2 * i + 1]],
            inferior_arcanum=ARCANA[(3 * i + 2) % 10],
        )
        Order.objects.create(
            name=f"Order {i}",
            rote_skills=[]
        )
    for path in Path.objects.all():
        for order in Order.objects.all():
            Legacy.objects.create(name=f"{path.name} {order.name} Legacy", path=path, order=order)
    for arcana in ARCANA:
        for level, practice in [(1, "compelling"), (2, "ruling"), (3, "fraying"), (4, "patterning"), (5, "making")]:
            s = Spell.objects.create(name=f"{practice.title()} {arcana.title()} Spell", practice=practice, arcanum=arcana, level=level)
            Rote.objects.create(name=f"{practice.title()} {arcana.title()} Rote", spell=s)
    for i in range(1, 5):
        Merit.objects.create(name=f"Merit {i}", ratings=[i, i+1])
        Merit.objects.create(name=f"Merit {i + 5}", ratings=[i, i+1])
        Merit.objects.create(name=f"Merit {i + 10}", ratings=[i, i+1])

class TestMage(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", player=self.player.cod_profile)
        mage_setup()

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
        self.mage.legacy = Legacy.objects.get(name="Path 0 Order 0 Legacy")
        self.mage.save()
        self.assertTrue(self.mage.has_legacy())

    def test_set_legacy(self):
        self.mage.set_order(Order.objects.get(name="Order 0"))
        self.mage.set_path(Path.objects.get(name="Path 0"))
        self.assertFalse(self.mage.has_order())
        self.assertTrue(self.mage.set_order(Order.objects.get(name="Order 0")))
        self.assertTrue(self.mage.has_order())
        
    def test_filter_legacy(self):
        both_wrong = Mage.objects.create(name="Neither Character", player=self.player.cod_profile)
        path_right = Mage.objects.create(name="Path Character", player=self.player.cod_profile)
        order_right = Mage.objects.create(name="Order Character", player=self.player.cod_profile)
        legacy = Legacy.objects.get(name="Path 0 Order 0 Legacy")
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

    def test_get_arcana(self):
        self.assertEqual(self.mage.get_arcana(), {
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
        })
        self.mage.matter = 2
        self.mage.spirit = 3
        self.assertEqual(self.mage.get_arcana(), {
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
        })

    def test_has_arcana(self):
        self.assertFalse(self.mage.has_arcana())
        self.mage.set_path(Path.objects.get(name="Path 0"))
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

    def test_xp_cost(self):
        self.assertEqual(self.mage.xp_cost("arcanum (to limit)"), 4)
        self.assertEqual(self.mage.xp_cost("arcanum (above limit)"), 5)
        self.assertEqual(self.mage.xp_cost("gnosis"), 5)
        self.assertEqual(self.mage.xp_cost("rote"), 1)
        self.assertEqual(self.mage.xp_cost("praxis"), 1)
        self.assertEqual(self.mage.xp_cost("wisdom"), 2)
        self.assertEqual(self.mage.xp_cost("willpower"),14)
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
        self.mage.add_rote(Rote.objects.get(name="Compelling Death Rote"))
        self.mage.add_rote(Rote.objects.get(name="Compelling Matter Rote"))
        self.mage.add_rote(Rote.objects.get(name="Compelling Life Rote"))
        self.assertTrue(self.mage.has_rotes())

    def test_add_rote(self):
        self.mage.death = 3
        self.mage.save()
        num = self.mage.rotes.count()
        self.assertTrue(self.mage.add_rote(Rote.objects.get(name="Compelling Death Rote")))
        self.assertFalse(self.mage.add_rote(Rote.objects.get(name="Compelling Matter Rote")))
        self.assertEqual(self.mage.rotes.count(), num + 1)

    def test_total_rotes(self):
        self.mage.death = 3
        self.mage.matter = 2
        self.mage.life = 1
        self.assertEqual(self.mage.total_rotes(), 0)
        self.mage.add_rote(Rote.objects.get(name="Compelling Death Rote"))
        self.assertEqual(self.mage.total_rotes(), 1)
        self.mage.add_rote(Rote.objects.get(name="Compelling Matter Rote"))
        self.assertEqual(self.mage.total_rotes(), 2)
        self.mage.add_rote(Rote.objects.get(name="Compelling Life Rote"))
        self.assertEqual(self.mage.total_rotes(), 3)

    def test_filter_rotes(self):
        self.assertEqual(len(self.mage.filter_rotes()), 0)
        self.mage.death = 3
        self.assertEqual(len(self.mage.filter_rotes()), 3)
        self.mage.fate = 2
        self.assertEqual(len(self.mage.filter_rotes()), 5)
        self.mage.spirit = 1
        self.assertEqual(len(self.mage.filter_rotes()), 6)
        r = Rote.objects.get(name="Compelling Death Rote")
        self.assertIn(r, self.mage.filter_rotes())
        self.mage.add_rote(r)
        self.assertNotIn(r, self.mage.filter_rotes())
        self.assertEqual(len(self.mage.filter_rotes()), 5)

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
        
        self.assertEqual(self.mage.practices_at_level(1), ["compelling", "knowing", "unveiling"])
        self.assertEqual(self.mage.practices_at_level(2), ["ruling", "shielding", "veiling"])
        self.assertEqual(self.mage.practices_at_level(3), ["fraying", "perfecting", "weaving"])
        self.assertEqual(self.mage.practices_at_level(4), ["patterning", "unraveling"])
        self.assertEqual(self.mage.practices_at_level(5), ["making", "unmaking"])

class TestRandomMage(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", player=self.player.cod_profile)
        mage_setup()

    def test_random_path(self):
        self.assertFalse(self.mage.has_path())
        self.assertTrue(self.mage.random_path())
        self.assertTrue(self.mage.has_path())

    def test_random_order(self):
        self.assertFalse(self.mage.has_order())
        self.assertTrue(self.mage.random_order())
        self.assertTrue(self.mage.has_order())

    def test_random_legacy(self):
        self.assertFalse(self.mage.has_legacy())
        self.assertTrue(self.mage.random_legacy())
        self.assertTrue(self.mage.has_legacy())

    def test_random_arcanum(self):
        num = self.mage.total_arcana()
        self.assertTrue(self.mage.random_arcanum())
        self.assertEqual(self.mage.total_arcana(), num + 1)

    def test_random_arcana(self):
        self.assertFalse(self.mage.has_arcana())
        self.assertTrue(self.mage.random_arcana())
        self.assertTrue(self.mage.has_arcana())

    def test_random_rote(self):
        self.mage.death = 3
        num = self.mage.rotes.count()
        self.assertTrue(self.mage.random_rote())
        self.assertEqual(self.mage.rotes.count(), num + 1)
        
    def test_random_rotes(self):
        self.assertFalse(self.mage.has_rotes())
        self.assertTrue(self.mage.random_rotes())
        self.assertTrue(self.mage.has_rotes())

    def test_random_nimbus(self):
        self.assertFalse(self.mage.has_nimbus())
        self.assertTrue(self.mage.random_nimbus())
        self.assertTrue(self.mage.has_nimbus())

    def test_random_spend_xp(self):
        self.mage.science = 1
        self.mage.xp = 15
        self.mage.random_spend_xp()
        self.assertLess(self.mage.xp, 15)
        self.mage.arcane_xp = 15
        self.mage.random_spend_xp()
        self.assertLess(self.mage.arcane_xp, 15)

    def test_random(self):
        self.assertFalse(self.mage.has_path())
        self.assertFalse(self.mage.has_order())
        self.assertFalse(self.mage.has_rote_skills())
        self.assertFalse(self.mage.has_arcana())
        self.assertFalse(self.mage.has_gnosis())
        self.assertFalse(self.mage.has_mana())
        self.assertFalse(self.mage.has_rotes())
        self.assertFalse(self.mage.has_nimbus())
        self.mage.random(xp=0)
        self.assertTrue(self.mage.has_path())
        self.assertTrue(self.mage.has_order())
        self.assertTrue(self.mage.has_rote_skills())
        self.assertTrue(self.mage.has_arcana())
        self.assertTrue(self.mage.has_gnosis())
        self.assertTrue(self.mage.has_mana())
        self.assertTrue(self.mage.has_rotes())
        self.assertTrue(self.mage.has_nimbus())

class TestMageDetailView(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.mage = Mage.objects.create(name="", player=self.player.cod_profile)

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/cod/characters/{self.mage.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/cod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "cod/characters/mage/detail.html")
