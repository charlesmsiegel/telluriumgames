from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.characters.aberrant import (
    Aberrant,
    MegaEdge,
    MegaEdgeRating,
    Power,
    PowerRating,
    Tag,
    Transformation,
)
from tc.models.characters.human import (
    Edge,
    EnhancedEdge,
    PathConnection,
    PathRating,
    Specialty,
    TCPath,
    Trick,
)


# Create your tests here.
class TestPower(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(
            name="", owner=self.player, might=3, dexterity=2, science=1
        )
        self.power = Power.objects.create(name="Test", cost=4)
        self.tag = Tag.objects.create(name="Reduced Cost", ratings=[2, 4, 6, 8, 10])
        self.tag.permitted_powers.add(self.power)
        self.tag.save()
        for i in range(10):
            Transformation.objects.create(name=f"Low Transformation {i}", level="low")
            Transformation.objects.create(
                name=f"Medium Transformation {i}", level="medium"
            )
            Transformation.objects.create(name=f"High Transformation {i}", level="high")

    def test_set_action_type(self):
        self.assertTrue(self.power.set_action_type("reflexive"))
        self.assertEqual(self.power.action_type, "reflexive")
        self.assertTrue(self.power.set_action_type("ordinary"))
        self.assertEqual(self.power.action_type, "ordinary")

    def test_dice_pool(self):
        self.assertTrue(self.power.set_dicepool("might+science"))
        self.assertEqual(self.power.dicepool, "might+science")
        self.assertEqual(self.power.dicepool_traits(), ["might", "science"])
        self.assertEqual(self.power.num_dice(self.character), 4)
        self.assertTrue(self.power.add_to_dicepool("dexterity"))
        self.assertEqual(self.power.dicepool, "might+science+dexterity")
        self.assertEqual(
            self.power.dicepool_traits(), ["might", "science", "dexterity"]
        )
        self.assertEqual(self.power.num_dice(self.character), 6)

    def test_set_range(self):
        self.assertTrue(self.power.set_range("personal"))
        self.assertEqual(self.power.range, "personal")
        self.assertTrue(self.power.set_range("close"))
        self.assertEqual(self.power.range, "close")
        self.assertTrue(self.power.set_range("short"))
        self.assertEqual(self.power.range, "short")
        self.assertTrue(self.power.set_range("medium"))
        self.assertEqual(self.power.range, "medium")
        self.assertTrue(self.power.set_range("long"))
        self.assertEqual(self.power.range, "long")
        self.assertTrue(self.power.set_range("extreme"))
        self.assertEqual(self.power.range, "extreme")
        self.assertTrue(self.power.set_range("visual"))
        self.assertEqual(self.power.range, "visual")

    def test_duration_choices(self):
        self.assertTrue(self.power.set_duration("instantaneous"))
        self.assertEqual(self.power.duration, "instantaneous")
        self.assertTrue(self.power.set_duration("concentration"))
        self.assertEqual(self.power.duration, "concentration")
        self.assertTrue(self.power.set_duration("maintained"))
        self.assertEqual(self.power.duration, "maintained")
        self.assertTrue(self.power.set_duration("continuous"))
        self.assertEqual(self.power.duration, "continuous")

    def test_cost_and_reduced_price_tag(self):
        self.assertTrue(self.character.add_power(self.power))
        self.assertEqual(self.character.power_cost(self.power), 4)
        self.assertTrue(self.character.add_tag(self.power, self.tag))
        self.assertEqual(self.character.power_cost(self.power), 2)
        self.assertTrue(self.character.add_tag(self.power, self.tag))
        self.assertEqual(self.character.power_cost(self.power), 0)
        self.assertFalse(self.character.add_tag(self.power, self.tag))
        self.assertEqual(self.character.power_cost(self.power), 0)

    def test_minimum_quantum_for_next_dot(self):
        aberrant = Aberrant.objects.create(name="Test Aberrant")
        power = Power.objects.create(
            name="Test Power", quantum_minimum=2, quantum_offset=1
        )
        power_rating = PowerRating.objects.create(
            character=aberrant, power=power, rating=2
        )

        self.assertEqual(power_rating.minimum_quantum_for_next_dot(), 2)
        power.quantum_minimum = -1
        power.save()
        self.assertEqual(power_rating.minimum_quantum_for_next_dot(), 3)


class TestAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", owner=self.player)
        for i in range(1, 5):
            for j in range(5):
                MegaEdge.objects.create(name=f"MegaEdge {5*i+j}", ratings=[i, i + 1])
        MegaEdge.objects.create(
            name="MegaEdge with Prereq", ratings=[2, 4], prereqs=[[("MegaEdge 5", 2)]]
        )

    def test_add_mega_edge(self):
        megaedge_5 = MegaEdge.objects.get(name="MegaEdge 5")
        self.assertEqual(self.character.total_mega_edges(), 0)
        self.assertEqual(self.character.mega_edges.count(), 0)
        self.assertTrue(self.character.add_mega_edge(megaedge_5))
        self.assertEqual(self.character.total_mega_edges(), 1)
        self.assertEqual(self.character.mega_edges.count(), 1)
        self.assertFalse(
            MegaEdge.objects.get(name="MegaEdge with Prereq").check_prereqs(
                self.character
            )
        )
        self.assertTrue(self.character.add_mega_edge(megaedge_5))
        self.assertEqual(self.character.total_mega_edges(), 2)
        self.assertEqual(self.character.mega_edges.count(), 1)
        self.assertIn(megaedge_5, self.character.mega_edges.all())
        self.assertEqual(2, self.character.mega_edge_rating(megaedge_5))
        self.assertTrue(
            MegaEdge.objects.get(name="MegaEdge with Prereq").check_prereqs(
                self.character
            )
        )

    def test_filter_mega_edges(self):
        MegaEdge.objects.create(
            name="MegaEdge 100", ratings=[1, 2], prereqs=[[("mega_might", 2)]]
        )
        e2 = MegaEdge.objects.create(
            name="MegaEdge 101", ratings=[1, 2], prereqs=[[("science", 2)]]
        )
        e3 = MegaEdge.objects.create(name="MegaEdge 102", ratings=[1, 2])
        MegaEdge.objects.create(
            name="MegaEdge 103", ratings=[1, 2], prereqs=[[("MegaEdge 102", 2)]]
        )

        self.assertEqual(len(self.character.filter_mega_edges()), 21)
        self.character.add_mega_edge(e3)
        self.assertEqual(len(self.character.filter_mega_edges()), 21)
        self.assertEqual(len(self.character.filter_mega_edges(dots=1)), 6)
        self.character.mega_might = 2
        self.assertEqual(len(self.character.filter_mega_edges()), 22)
        self.character.science = 2
        self.assertEqual(len(self.character.filter_mega_edges()), 23)
        self.character.add_mega_edge(e2)
        self.assertEqual(len(self.character.filter_mega_edges()), 23)
        self.character.add_mega_edge(e3)
        self.assertEqual(len(self.character.filter_mega_edges()), 23)
        self.assertNotIn(e3, self.character.filter_mega_edges())
        m4 = MegaEdge.objects.create(
            name="MegaEdge 104",
            ratings=[1, 2, 3, 4, 5],
            prereqs=[[("quantum", "dots")]],
        )
        self.character.quantum = 1
        self.assertIn(m4, self.character.filter_mega_edges())
        self.character.add_mega_edge(m4)
        self.assertNotIn(m4, self.character.filter_mega_edges())
        self.character.quantum = 2
        self.assertIn(m4, self.character.filter_mega_edges())

    def test_add_mega_attribute(self):
        self.assertEqual(self.character.mega_might, 0)
        self.assertTrue(self.character.add_mega_attribute("might"))
        self.assertEqual(self.character.mega_might, 1)

    def set_attributes(self):
        self.character.might = 5
        self.character.dexterity = 4
        self.character.stamina = 3
        self.character.intellect = 2
        self.character.cunning = 1
        self.character.resolve = 2
        self.character.presence = 3
        self.character.manipulation = 4
        self.character.composure = 5

    def set_mega_attributes(self):
        self.character.mega_might = 0
        self.character.mega_dexterity = 2
        self.character.mega_stamina = 2
        self.character.mega_intellect = 2
        self.character.mega_cunning = 0
        self.character.mega_resolve = 0
        self.character.mega_presence = 0
        self.character.mega_manipulation = 1
        self.character.mega_composure = 2

    def test_get_megaattributes(self):
        self.assertEqual(
            self.character.get_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 0,
                "mega_stamina": 0,
                "mega_intellect": 0,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 0,
                "mega_composure": 0,
            },
        )
        self.set_mega_attributes()
        self.assertEqual(
            self.character.get_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 2,
                "mega_stamina": 2,
                "mega_intellect": 2,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 1,
                "mega_composure": 2,
            },
        )

    def test_filter_mega_attribute(self):
        self.set_attributes()
        self.character.quantum = 2
        self.assertEqual(
            self.character.filter_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 0,
                "mega_stamina": 0,
                "mega_intellect": 0,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 0,
                "mega_composure": 0,
            },
        )
        self.set_mega_attributes()
        self.assertEqual(
            self.character.filter_mega_attributes(),
            {
                "mega_might": 0,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 1,
            },
        )
        self.character.quantum = 3
        self.assertEqual(
            self.character.filter_mega_attributes(),
            {
                "mega_might": 0,
                "mega_dexterity": 2,
                "mega_stamina": 2,
                "mega_cunning": 0,
                "mega_resolve": 0,
                "mega_presence": 0,
                "mega_manipulation": 1,
                "mega_composure": 2,
            },
        )

    def test_add_power(self):
        p = Power.objects.create(name="Test Power 1", quantum_minimum=0)
        self.assertEqual(self.character.total_powers(), 0)
        self.assertTrue(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 1)
        p = Power.objects.create(name="Test Power 2", quantum_minimum=3)
        self.assertFalse(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 1)
        self.character.quantum = 3
        self.assertTrue(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 2)
        self.assertTrue(self.character.add_power(p))
        self.assertEqual(self.character.total_powers(), 3)

    def test_filter_tags(self):
        p = Power.objects.create(name="Test Power")
        self.character.add_power(p)
        t1 = Tag.objects.create(name="Tag 1", ratings=[1, 2])
        t1.permitted_powers.add(p)
        t1.save()
        t2 = Tag.objects.create(name="Tag 2", ratings=[1, 2])
        t2.permitted_powers.add(p)
        t2.save()
        t3 = Tag.objects.create(name="Tag 3", ratings=[1, 2])
        t3.permitted_powers.add(p)
        t3.save()
        Tag.objects.create(name="Tag 4", ratings=[1, 2])
        self.assertEqual(len(self.character.filter_tags(p)), 3)
        self.character.add_tag(p, t1)
        self.assertEqual(len(self.character.filter_tags(p)), 3)
        self.character.add_tag(p, t1)
        self.assertEqual(len(self.character.filter_tags(p)), 2)

    def test_add_tag(self):
        p = Power.objects.create(name="Test Power")
        self.assertTrue(self.character.add_power(p))
        t1 = Tag.objects.create(name="Tag 1", ratings=[1, 2])
        t1.permitted_powers.add(p)
        t1.save()
        t2 = Tag.objects.create(name="Tag 2", ratings=[1, 2])
        t2.permitted_powers.add(p)
        t2.save()
        t3 = Tag.objects.create(name="Tag 3", ratings=[1, 2])
        t3.permitted_powers.add(p)
        t3.save()
        t4 = Tag.objects.create(name="Tag 4", ratings=[1, 2])
        self.assertFalse(self.character.add_tag(p, t4))
        self.assertTrue(self.character.add_tag(p, t1))
        self.assertEqual(self.character.tag_rating(p, t1), 1)
        self.assertTrue(self.character.add_tag(p, t1))
        self.assertEqual(self.character.tag_rating(p, t1), 2)
        self.assertFalse(self.character.add_tag(p, t1))

    def test_add_transcendance(self):
        for i in range(3):
            for level in ["low", "medium", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )
        low_level = Transformation.objects.create(
            name="Low Transformation 5", level="low"
        )
        self.assertEqual(self.character.transcendence, 0)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 1)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 2)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 3)
        self.assertTrue(self.character.add_transcendence(transformation=low_level))
        self.assertEqual(self.character.transcendence, 4)
        self.assertEqual(self.character.transformations.count(), 1)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 5)
        self.assertEqual(self.character.transformations.filter(level="low").count(), 2)
        self.assertEqual(self.character.transformations.count(), 2)
        self.character.quantum = 3
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 6)
        self.assertEqual(
            self.character.transformations.filter(level="medium").count(), 1
        )
        self.assertEqual(self.character.transformations.count(), 3)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 7)
        self.assertEqual(
            self.character.transformations.filter(level="medium").count(), 2
        )
        self.assertEqual(self.character.transformations.count(), 4)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 8)
        self.assertEqual(self.character.transformations.filter(level="high").count(), 1)
        self.assertEqual(self.character.transformations.count(), 5)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 9)
        self.assertEqual(self.character.transformations.filter(level="high").count(), 2)
        self.assertEqual(self.character.transformations.count(), 6)
        self.assertTrue(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 10)
        self.assertFalse(self.character.add_transcendence())
        self.assertEqual(self.character.transcendence, 10)

    def test_add_quantum(self):
        t = Transformation.objects.create(name="Test Transformation", level="medium")
        for i in range(10):
            for level in ["low", "medium", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )

        self.character.quantum = 3
        self.character.update_quantum_points()
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.transcendence, 1)
        self.assertEqual(self.character.quantum, 4)
        self.assertEqual(self.character.quantum_points, 30)
        self.assertTrue(self.character.add_quantum())
        self.assertEqual(self.character.transcendence, 2)
        self.assertEqual(self.character.quantum, 5)
        self.assertEqual(self.character.quantum_points, 35)
        self.assertFalse(self.character.add_quantum())
        self.assertEqual(self.character.quantum, 5)
        self.assertEqual(self.character.quantum_points, 35)
        self.assertTrue(self.character.add_quantum(start=False))
        self.assertEqual(self.character.transcendence, 3)
        self.assertEqual(self.character.quantum, 6)
        self.assertEqual(self.character.quantum_points, 40)
        self.assertTrue(self.character.add_quantum(start=False, transformation=t))
        self.assertEqual(self.character.transcendence, 4)
        self.assertEqual(self.character.quantum, 7)
        self.assertIn(t, self.character.transformations.all())

    def test_add_flux(self):
        self.assertEqual(self.character.flux, 0)
        self.assertTrue(self.character.add_flux())
        self.assertEqual(self.character.flux, 1)
        self.assertTrue(self.character.reset_flux())
        self.assertEqual(self.character.flux, 0)

    def test_add_transformation(self):
        for i in range(10):
            for level in ["low", "medium", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )

        self.character.quantum = 3
        all_transformations = list(Transformation.objects.order_by("?"))
        for i in range(6):
            self.assertTrue(self.character.add_transformation(all_transformations[i]))
        self.assertEqual(self.character.transformations.count(), 6)

    def test_filter_transformation(self):
        transformation_dict = {"low": [], "medium": [], "high": []}
        for i in range(10):
            for level in ["low", "medium", "high"]:
                transformation_dict[level].append(
                    Transformation.objects.create(
                        name=f"{level.title()} Transformation {i}", level=level
                    )
                )
        self.character.quantum = 3
        self.character.add_transformation(transformation_dict["low"][0])
        self.character.add_transformation(transformation_dict["low"][1])
        self.character.add_transformation(transformation_dict["medium"][0])
        self.assertEqual(len(self.character.filter_transformations()), 27)
        self.assertEqual(len(self.character.filter_transformations(level="low")), 8)
        self.assertEqual(len(self.character.filter_transformations(level="medium")), 9)
        self.assertEqual(len(self.character.filter_transformations(level="high")), 10)

    def test_has_template(self):
        self.character.approach = "RES"
        self.character.might = 3
        self.character.dexterity = 3
        self.character.stamina = 4
        self.character.intellect = 3
        self.character.cunning = 2
        self.character.resolve = 3
        self.character.presence = 2
        self.character.manipulation = 2
        self.character.composure = 2
        e = Edge.objects.create(name="Fame", ratings=[1])
        self.assertFalse(self.character.has_template())
        self.character.quantum = 1
        self.assertFalse(self.character.has_template())
        self.character.resolve = 4
        self.assertFalse(self.character.has_template())
        self.character.add_edge(e)
        self.character.xp = 150
        self.assertTrue(self.character.has_template())

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("mega attribute"), 12)
        self.assertEqual(self.character.xp_cost("mega edge"), 12)
        self.assertEqual(self.character.xp_cost("power tag"), 12)
        self.assertEqual(self.character.xp_cost("quantum<=5"), 16)
        self.assertEqual(self.character.xp_cost("quantum>5"), 32)
        self.assertEqual(self.character.xp_cost("quantum power"), 12)
        self.assertEqual(
            self.character.xp_cost("mega attribute", transcendence=True), 6
        )
        self.assertEqual(self.character.xp_cost("mega edge", transcendence=True), 6)
        self.assertEqual(self.character.xp_cost("quantum power", transcendence=True), 6)

        self.assertEqual(
            self.character.xp_cost("mega attribute", transformation="low"), 9
        )
        self.assertEqual(self.character.xp_cost("mega edge", transformation="low"), 9)
        self.assertEqual(self.character.xp_cost("power tag", transformation="low"), 9)
        self.assertEqual(self.character.xp_cost("quantum<=5", transformation="low"), 13)
        self.assertEqual(self.character.xp_cost("quantum>5", transformation="low"), 29)
        self.assertEqual(
            self.character.xp_cost("quantum power", transformation="low"), 9
        )
        self.assertEqual(
            self.character.xp_cost(
                "mega attribute", transcendence=True, transformation="low"
            ),
            3,
        )
        self.assertEqual(
            self.character.xp_cost(
                "mega edge", transcendence=True, transformation="low"
            ),
            3,
        )
        self.assertEqual(
            self.character.xp_cost(
                "quantum power", transcendence=True, transformation="low"
            ),
            3,
        )

        self.assertEqual(
            self.character.xp_cost("mega attribute", transformation="medium"), 6
        )
        self.assertEqual(
            self.character.xp_cost("mega edge", transformation="medium"), 6
        )
        self.assertEqual(
            self.character.xp_cost("power tag", transformation="medium"), 6
        )
        self.assertEqual(
            self.character.xp_cost("quantum<=5", transformation="medium"), 10
        )
        self.assertEqual(
            self.character.xp_cost("quantum>5", transformation="medium"), 26
        )
        self.assertEqual(
            self.character.xp_cost("quantum power", transformation="medium"), 6
        )
        self.assertEqual(
            self.character.xp_cost(
                "mega attribute", transcendence=True, transformation="medium"
            ),
            0,
        )
        self.assertEqual(
            self.character.xp_cost(
                "mega edge", transcendence=True, transformation="medium"
            ),
            0,
        )
        self.assertEqual(
            self.character.xp_cost(
                "quantum power", transcendence=True, transformation="medium"
            ),
            0,
        )

    def test_spend_xp(self):
        MegaEdge.objects.create(name="MegaEdge 1", ratings=[1, 2, 3])
        p = Power.objects.create(name="Power 1")
        t = Tag.objects.create(name="Power Tag 1", ratings=[1, 2])
        t.permitted_powers.add(p)
        t.save()

        self.character.might = 4
        self.character.quantum = 4
        self.character.xp = 1000
        self.assertTrue(self.character.spend_xp("mega_might"))
        self.assertEqual(self.character.xp, 988)
        self.assertEqual(self.character.total_mega_attributes(), 1)
        self.assertTrue(self.character.spend_xp("MegaEdge 1"))
        self.assertEqual(self.character.xp, 976)
        self.assertEqual(self.character.total_mega_edges(), 1)
        self.assertTrue(self.character.spend_xp("Power 1"))
        self.assertEqual(self.character.xp, 964)
        self.assertEqual(self.character.total_powers(), 1)
        self.assertIn(Power.objects.get(name="Power 1"), self.character.powers.all())
        self.assertTrue(self.character.spend_xp("Power Tag 1", power="Power 1"))
        self.assertEqual(self.character.xp, 952)
        self.assertEqual(
            len(self.character.get_tags(Power.objects.get(name="Power 1"))), 1
        )
        self.assertTrue(self.character.spend_xp("quantum"))
        self.assertEqual(self.character.xp, 936)
        self.assertEqual(self.character.quantum, 5)
        self.assertTrue(self.character.spend_xp("quantum"))
        self.assertEqual(self.character.xp, 904)
        self.assertEqual(self.character.quantum, 6)
        starting_transcendence = self.character.transcendence
        self.assertTrue(self.character.spend_xp("mega_might", transcendence=True))
        self.assertEqual(self.character.transcendence, starting_transcendence + 1)
        self.assertEqual(self.character.xp, 898)
        self.assertEqual(self.character.total_mega_attributes(), 2)
        self.assertTrue(self.character.spend_xp("MegaEdge 1", transcendence=True))
        self.assertEqual(self.character.transcendence, starting_transcendence + 2)
        self.assertEqual(self.character.xp, 892)
        self.assertEqual(self.character.total_mega_edges(), 2)
        self.assertTrue(self.character.spend_xp("Power 1", transcendence=True))
        self.assertEqual(self.character.transcendence, starting_transcendence + 3)
        self.assertEqual(self.character.xp, 886)
        self.assertEqual(self.character.total_powers(), 2)
        self.character.quantum = 1
        self.assertTrue(self.character.spend_xp("Power 1", transformation="low"))
        self.assertEqual(self.character.xp, 877)
        self.assertTrue(self.character.spend_xp("Power 1", transformation="medium"))
        self.assertEqual(self.character.xp, 871)
        self.assertTrue(self.character.spend_xp("Power 1", transformation="low"))
        self.assertEqual(self.character.xp, 859)
        self.character.quantum = 2
        self.assertTrue(self.character.spend_xp("Power 1", transformation="low"))
        self.assertEqual(self.character.xp, 850)

    def test_mega_intellect_add(self):
        edges = [
            "Iron Will",
            "Lightning Calculator",
            "Photographic Memory",
            "Speed Reading",
        ]
        for name in edges:
            Edge.objects.create(name=name, ratings=[1, 2, 3])

        num = sum(self.character.edge_rating(x) for x in edges)
        self.character.add_mega_attribute("intellect")
        self.assertEqual(sum(self.character.edge_rating(x) for x in edges), num + 1)

    def test_mega_cunning_add(self):
        keen_sense_sight = Edge.objects.create(name="Keen Sense (Sight)", ratings=[1],)
        keen_sense_hearing = Edge.objects.create(
            name="Keen Sense (Hearing)", ratings=[1],
        )
        keen_sense_touch = Edge.objects.create(name="Keen Sense (Touch)", ratings=[1],)
        keen_sense_smell_and_taste = Edge.objects.create(
            name="Keen Sense (Smell and Taste)", ratings=[1],
        )
        keen_senses = [
            keen_sense_sight,
            keen_sense_hearing,
            keen_sense_smell_and_taste,
            keen_sense_touch,
        ]
        self.character.mega_cunning = 0
        for sense in keen_senses:
            self.assertNotIn(sense, self.character.edges.all())
        self.character.add_mega_attribute("cunning")
        for sense in keen_senses:
            self.assertIn(sense, self.character.edges.all())

    def test_mega_manipulation_add(self):
        edges = ["Animal Ken", "Skilled Liar", "Striking", "Wealth"]
        for name in edges:
            Edge.objects.create(name=name, ratings=[1, 2, 3])

        num = sum(self.character.edge_rating(x) for x in edges)
        self.character.add_mega_attribute("manipulation")
        self.assertEqual(sum(self.character.edge_rating(x) for x in edges), num + 1)

    def test_mega_composure_add(self):
        edges = ["Always Prepared", "Covert", "Danger Sense", "Iron Will"]
        for name in edges:
            Edge.objects.create(name=name, ratings=[1, 2, 3])

        ee = EnhancedEdge.objects.create(
            name="Indomitable", prereqs=[[("Iron Will", 3)]]
        )

        num = sum(self.character.edge_rating(x) for x in edges)
        self.character.add_mega_attribute("composure")
        self.assertEqual(sum(self.character.edge_rating(x) for x in edges), num + 1)

        self.character.composure = 5
        self.character.quantum = 5
        while self.character.edge_rating("Iron Will") < 3:
            e = Edge.objects.get(name="Iron Will")
            self.character.add_edge(e)
        self.character.add_mega_attribute("composure")
        self.character.add_mega_attribute("composure")
        self.assertIn(ee, self.character.enhanced_edges.all())

    def test_total_mega_attribute(self):
        self.fail()

    def test_total_mega_edges(self):
        self.fail()

    def test_mega_edge_rating(self):
        self.fail()

    def test_total_powers(self):
        self.fail()

    def test_power_rating(self):
        self.fail()

    def test_get_tags(self):
        self.fail()

    def test_tag_rating(self):
        self.fail()

    def test_update_quantum_points(self):
        self.fail()

    def test_reset_flux(self):
        self.fail()

    def test_spend_xp_mega_attribute(self):
        self.fail()

    def test_spend_xp_mega_edge(self):
        self.fail()

    def test_spend_xp_power(self):
        self.fail()

    def test_spend_xp_tag(self):
        self.fail()

    def test_spend_xp_quantum(self):
        self.fail()


class TestRandomAberrant(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Aberrant.objects.create(name="", owner=self.player)
        for skill in self.character.get_skills().keys():
            for i in range(5):
                Specialty.objects.create(name=f"{skill} Specialty {i}", skill=skill)
                Trick.objects.create(name=f"{skill} Trick {i}", skill=skill)
        for t in ["origin", "role", "society"]:
            for k in range(3):
                p = TCPath.objects.create(name=f"{t} Path {k}", type=t)
                for i in range(4):
                    for j in range(4):
                        p.skills.append(
                            list(self.character.get_skills().keys())[4 * i + j]
                        )
                        p.gift_keywords.append(
                            list(self.character.get_skills().keys())[4 * i + j]
                        )
                        p.edges.add(
                            Edge.objects.create(
                                name=f"{t} Edge {4*j+i}, {k}", ratings=[i + 1, i + 2]
                            )
                        )
                    p.save()
        for i in range(10):
            for level in ["low", "medium", "high"]:
                Transformation.objects.create(
                    name=f"{level.title()} Transformation {i}", level=level
                )

        p1 = Power.objects.create(name="Power Test 1", quantum_minimum=0)
        p2 = Power.objects.create(name="Power Test 2", quantum_minimum=2)
        p3 = Power.objects.create(name="Power Test 3", quantum_minimum=3)
        p4 = Power.objects.create(name="Power Test 4", quantum_minimum=1)

        p = [p1, p2, p3, p4]

        for i, ratings in enumerate([[1, 2], [2, 4], [2], [1]]):
            t = Tag.objects.create(name=f"Tag {i}", ratings=ratings)
            for j in ratings:
                t.permitted_powers.add(p[j - 1])
                t.save()

        for i in range(10):
            p = Power.objects.create(name=f"Test Power {i}")
            t = Tag.objects.order_by("?").first()
            t.permitted_powers.add(p)
            t.save()

        for i in range(1, 5):
            for j in range(1, 5):
                if i != j:
                    MegaEdge.objects.create(name=f"MegaEdge{4*i+j}", ratings=[i, j])
                else:
                    MegaEdge.objects.create(name=f"MegaEdge{4*i+j}", ratings=[i])

        Edge.objects.create(name="Fame", ratings=[1, 2, 3])
        Edge.objects.create(name="Alternate Identity", ratings=[1, 2, 3])

        t = Tag.objects.create(name="Universal Tag", ratings=[1, 2, 3, 4, 5])
        t.permitted_powers.set(Power.objects.all())
        t.save()

        edges = [
            "Lightning Calculator",
            "Photographic Memory",
            "Speed Reading",
        ]
        for name in edges:
            Edge.objects.create(name=name, ratings=[1, 2, 3])

        edges = ["Always Prepared", "Covert", "Danger Sense", "Iron Will"]
        for name in edges:
            Edge.objects.create(name=name, ratings=[1, 2, 3])

        EnhancedEdge.objects.create(name="Indomitable", prereqs=[[("Iron Will", 3)]])

        edges = ["Animal Ken", "Skilled Liar", "Striking", "Wealth"]
        for name in edges:
            Edge.objects.create(name=name, ratings=[1, 2, 3])

        Edge.objects.create(
            name="Keen Sense (Sight)", ratings=[1],
        )
        Edge.objects.create(
            name="Keen Sense (Hearing)", ratings=[1],
        )
        Edge.objects.create(
            name="Keen Sense (Touch)", ratings=[1],
        )
        Edge.objects.create(
            name="Keen Sense (Smell and Taste)", ratings=[1],
        )

    def test_random_mega_attribute(self):
        num = self.character.total_mega_attributes()
        self.character.random_mega_attribute()
        self.assertEqual(self.character.total_mega_attributes(), num + 1)

    def test_random_mega_edge(self):
        num = self.character.total_mega_edges()
        self.character.random_mega_edge(dots=1)
        self.assertEqual(self.character.total_mega_edges(), num + 1)

    def test_random_tag(self):
        self.character.random_power()
        p = self.character.powers.first()
        self.assertEqual(len(self.character.get_tags(p)), 0)
        self.character.random_tag(p)
        self.assertEqual(len(self.character.get_tags(p)), 1)

    def test_random_power(self):
        num = self.character.total_powers()
        self.character.random_power()
        self.assertEqual(self.character.total_powers(), num + 1)

    def test_apply_random_template(self):
        self.character.random_attributes()
        self.character.random_paths()
        self.assertFalse(self.character.has_template())
        self.character.apply_random_template()
        self.assertTrue(self.character.has_template())

    def test_random_transformation(self):
        aberrant = Aberrant.objects.create(name="Test Aberrant")
        transform1 = Transformation.objects.create(name="Test Transform 1", level=1)
        Transformation.objects.create(name="Test Transform 2", level=2)
        Transformation.objects.create(name="Test Transform 3", level=3)
        aberrant.transformations.add(transform1)
        # Test adding a transformation
        self.assertTrue(aberrant.random_transformation())
        self.assertEqual(aberrant.transformations.count(), 2)

        # Test adding a transformation with a specific level
        self.assertTrue(aberrant.random_transformation(level=2))
        self.assertEqual(aberrant.transformations.count(), 3)

        # Test not adding a transformation when all at a certain level are already added
        aberrant.transformations.add(*aberrant.filter_transformations(level=3))
        n = aberrant.transformations.count()
        aberrant.random_transformation(level=3)
        self.assertFalse(aberrant.random_transformation(level=3))
        self.assertEqual(aberrant.transformations.count(), n)

        # Test not adding a transformation when all are already added
        aberrant.transformations.add(*aberrant.filter_transformations())
        n = aberrant.transformations.count()
        self.assertFalse(aberrant.random_transformation())
        self.assertEqual(aberrant.transformations.count(), n)

    def test_random_spend_xp(self):
        self.character.xp = 15
        self.character.random_spend_xp()
        self.assertLess(self.character.xp, 15)

    def test_random(self):
        character = Aberrant.objects.create(owner=self.player)
        self.assertFalse(character.has_name())
        self.assertFalse(character.has_concept())
        self.assertFalse(character.has_paths())
        self.assertFalse(character.has_aspirations())
        self.assertFalse(character.has_attributes())
        self.assertFalse(character.has_skills())
        self.assertFalse(character.has_basics())
        self.assertFalse(character.has_template())
        character.xp = 0
        character.random(xp=0)
        self.assertTrue(character.has_name())
        self.assertTrue(character.has_concept())
        self.assertTrue(character.has_paths())
        self.assertTrue(character.has_aspirations())
        self.assertTrue(character.has_attributes(template=True))
        self.assertTrue(character.has_skills())
        self.assertTrue(character.has_specialties())
        self.assertTrue(character.has_tricks())
        self.assertTrue(character.has_basics())
        self.assertTrue(character.has_template(xp=0))


class TestAberrantDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.character = Aberrant.objects.create(
            name="Test Character", owner=User.objects.get(username="Test User"),
        )

    def test_mortal_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mortal_detail_view_template(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "tc/characters/aberrant/aberrant/detail.html")


class TestMegaEdge(TestCase):
    def setUp(self):
        self.character = Aberrant.objects.create(name="Test Character", quantum=4)
        self.edge = Edge.objects.create(name="Test Edge", ratings=[3])
        self.mega_edge = MegaEdge.objects.create(name="Test Mega Edge", ratings=[5, 6])
        self.mega_edge_rating = MegaEdgeRating.objects.create(
            mega_edge=self.mega_edge, character=self.character, rating=3
        )
        self.path = TCPath.objects.create(name="Test Path")
        self.path.edges.add(self.mega_edge)
        self.path_connection = PathConnection.objects.create(path=self.path)
        self.path_rating = PathRating.objects.create(
            path=self.path, character=self.character, rating=4
        )

    def test_check_prereqs(self):
        # Test with attribute prereq that is not satisfied
        prereq = ("might", 4)
        self.assertFalse(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with attribute prereq that is satisfied
        self.character.might = 5
        self.character.save()
        self.assertTrue(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with skill prereq that is not satisfied
        prereq = ("aim", 3)
        self.assertFalse(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with skill prereq that is satisfied
        setattr(self.character, "aim", 4)
        self.assertTrue(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with edge prereq that is not satisfied
        prereq = ("Test Edge", 2)
        self.assertFalse(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with edge prereq that is satisfied
        self.character.add_edge(self.edge)
        self.assertTrue(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with mega edge prereq that is not satisfied
        prereq = ("Test Mega Edge", 4)
        self.assertFalse(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with mega edge prereq that is satisfied
        self.character.add_mega_edge(self.mega_edge)
        self.assertTrue(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with path prereq that is not satisfied
        prereq = ("path", 5)
        self.assertFalse(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with path prereq that is satisfied
        self.character.add_path(self.path)
        self.assertTrue(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with quantum prereq that is not satisfied
        prereq = ("quantum", 5)
        self.assertFalse(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with quantum prereq that is satisfied
        self.character.quantum = 5
        self.assertTrue(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with mega attribute prereq that is not satisfied
        prereq = ("mega_might", 3)
        self.assertFalse(self.mega_edge.prereq_satisfied(prereq, self.character))

        # Test with mega attribute prereq that is satisfied
        setattr(self.character, "mega_might", 4)
        self.assertTrue(self.mega_edge.prereq_satisfied(prereq, self.character))


class TestTag(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(ratings=[1, 2, 3])

    def test_save_method_updates_max_rating_field(self):
        self.assertEqual(self.tag.max_rating, 3)
        self.tag.ratings = [4, 5, 6]
        self.tag.save()
        self.assertEqual(self.tag.max_rating, 6)
