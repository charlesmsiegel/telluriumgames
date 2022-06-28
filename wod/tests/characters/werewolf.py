from glob import glob1

from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.human import Archetype, MeritFlaw, Specialty
from wod.models.characters.werewolf import (
    Camp,
    Gift,
    Pack,
    RenownIncident,
    Rite,
    Totem,
    Tribe,
    Werewolf,
)


# Create your tests here.
def werewolf_setup(player):
    for i in range(5):
        w = Werewolf.objects.create(name=f"Character {i}", player=player.wod_profile)
    for i in range(5):
        Totem.objects.create(name=f"Totem {i}", cost=(10 + i))
    for i in range(1, 6):
        Gift.objects.create(name=f"Gift {i}", rank=i, allowed={"garou": []})
        Gift.objects.create(name=f"Gift {5+i}", rank=i, allowed={"garou": []})
    t = Tribe.objects.create(name="Test Tribe", willpower=5)
    Tribe.objects.create(name="Test Tribe 2", willpower=3)
    Camp.objects.create(name="Test Camp", tribe=t)
    for t in Tribe.objects.all():
        Gift.objects.create(name=f"{t.name} Gift", rank=1, allowed={"garou": [t.name]})
    for auspice in ["ragabash", "theurge", "philodox", "galliard", "ahroun"]:
        Gift.objects.create(
            name=f"{auspice.title()} Gift", rank=1, allowed={"garou": [auspice]}
        )
    for breed in ["homid", "metis", "lupus"]:
        Gift.objects.create(
            name=f"{breed.title()} Gift", rank=1, allowed={"garou": [breed]}
        )
    for i in range(6):
        Rite.objects.create(name=f"Rite {i}", level=i)
        Rite.objects.create(name=f"Rite {6+i}", level=i)
    for i in range(5):
        MeritFlaw.objects.create(
            name=f"Merit {i}", ratings=[i], allowed_types=["garou"]
        )
        MeritFlaw.objects.create(
            name=f"Flaw {i}", ratings=[-i], allowed_types=["garou"]
        )
    for i in range(10):
        for trait in w.get_attributes():
            Specialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )

        for trait in w.get_abilities():
            Specialty.objects.create(
                name=f"{trait.replace('_', ' ').title()} {i}", stat=trait
            )
    for i in range(20):
        Archetype.objects.create(name=f"Archetype {i}")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                RenownIncident.objects.create(
                    name=f"Incident {i}, {j}, {k}",
                    glory=i - 1,
                    honor=j - 1,
                    wisdom=k - 1,
                )


class TestWerewolf(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = Werewolf.objects.create(
            name="Test Werewolf", player=self.player.wod_profile
        )
        werewolf_setup(self.player)

    def set_abilities(self):
        self.character.brawl = 1
        self.character.expression = 3
        self.character.intimidation = 2
        self.character.subterfuge = 1
        self.character.leadership = 4
        self.character.crafts = 2
        self.character.etiquette = 1
        self.character.animal_ken = 5
        self.character.larceny = 2
        self.character.survival = 1
        self.character.computer = 4
        self.character.science = 5
        self.character.law = 3
        self.character.rituals = 2
        self.character.technology = 1

    def test_get_abilities(self):
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "expression": 0,
                "intimidation": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "leadership": 0,
                "primal_urge": 0,
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 0,
                "larceny": 0,
                "performance": 0,
                "survival": 0,
                "academics": 0,
                "computer": 0,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
                "enigmas": 0,
                "law": 0,
                "occult": 0,
                "rituals": 0,
                "technology": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_abilities(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 1,
                "empathy": 0,
                "expression": 3,
                "intimidation": 2,
                "streetwise": 0,
                "subterfuge": 1,
                "leadership": 4,
                "primal_urge": 0,
                "crafts": 2,
                "drive": 0,
                "etiquette": 1,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 5,
                "larceny": 2,
                "performance": 0,
                "survival": 1,
                "academics": 0,
                "computer": 4,
                "investigation": 0,
                "medicine": 0,
                "science": 5,
                "enigmas": 0,
                "law": 3,
                "occult": 0,
                "rituals": 2,
                "technology": 1,
            },
        )

    def test_get_talents(self):
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 0,
                "empathy": 0,
                "expression": 0,
                "intimidation": 0,
                "streetwise": 0,
                "subterfuge": 0,
                "leadership": 0,
                "primal_urge": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
            {
                "alertness": 0,
                "athletics": 0,
                "brawl": 1,
                "empathy": 0,
                "expression": 3,
                "intimidation": 2,
                "streetwise": 0,
                "subterfuge": 1,
                "leadership": 4,
                "primal_urge": 0,
            },
        )

    def test_get_skills(self):
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 0,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 0,
                "larceny": 0,
                "performance": 0,
                "survival": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_skills(),
            {
                "crafts": 2,
                "drive": 0,
                "etiquette": 1,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 5,
                "larceny": 2,
                "performance": 0,
                "survival": 1,
            },
        )

    def test_get_knowledges(self):
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
                "enigmas": 0,
                "law": 0,
                "occult": 0,
                "rituals": 0,
                "technology": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 4,
                "investigation": 0,
                "medicine": 0,
                "science": 5,
                "enigmas": 0,
                "law": 3,
                "occult": 0,
                "rituals": 2,
                "technology": 1,
            },
        )

    def test_add_gift(self):
        g = Gift.objects.get(name="Gift 1")
        self.assertEqual(self.character.gifts.count(), 0)
        self.assertTrue(self.character.add_gift(g))
        self.assertEqual(self.character.gifts.count(), 1)
        self.assertIn(g, self.character.gifts.all())

    def test_filter_gifts(self):
        self.character.rank = 2
        self.assertEqual(len(self.character.filter_gifts()), 14)
        self.character.add_gift(Gift.objects.get(name="Gift 1"))
        self.character.add_gift(Gift.objects.get(name="Gift 2"))
        self.assertEqual(len(self.character.filter_gifts()), 12)

    def test_has_gifts(self):
        t = Tribe.objects.get(name="Test Tribe", willpower=5)
        self.character.set_tribe(t)
        self.character.set_breed("homid")
        self.character.set_auspice("ragabash")
        g1 = Gift.objects.get(name="Test Tribe Gift")
        g2 = Gift.objects.get(name="Ragabash Gift")
        g3 = Gift.objects.get(name="Homid Gift")
        self.assertFalse(self.character.has_gifts())
        self.character.add_gift(g1)
        self.assertFalse(self.character.has_gifts())
        self.character.add_gift(g2)
        self.assertFalse(self.character.has_gifts())
        self.character.add_gift(g3)
        self.assertTrue(self.character.has_gifts())

    def test_add_rite(self):
        r = Rite.objects.get(name="Rite 1", level=1)
        self.assertEqual(self.character.rites_known.count(), 0)
        self.assertTrue(self.character.add_rite(r))
        self.assertEqual(self.character.rites_known.count(), 1)
        self.assertIn(r, self.character.rites_known.all())

    def test_filter_rites(self):
        self.assertEqual(len(self.character.filter_rites()), 12)
        self.character.add_rite(Rite.objects.get(name="Rite 1"))
        self.character.add_rite(Rite.objects.get(name="Rite 2"))
        self.assertEqual(len(self.character.filter_rites()), 10)

    def test_has_rites(self):
        self.character.rites = 3
        self.assertFalse(self.character.has_rites())
        self.character.add_rite(Rite.objects.get(name="Rite 3"))
        self.assertTrue(self.character.has_rites())

    def test_set_tribe(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.assertFalse(self.character.has_tribe())
        self.assertTrue(self.character.set_tribe(t))
        self.assertTrue(self.character.has_tribe())

    def test_has_tribe(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.assertFalse(self.character.has_tribe())
        self.character.set_tribe(t)
        self.assertTrue(self.character.has_tribe())

    def test_set_breed(self):
        self.assertFalse(self.character.has_breed())
        self.assertTrue(self.character.set_breed("homid"))
        self.assertTrue(self.character.has_breed())

    def test_has_breed(self):
        self.assertFalse(self.character.has_breed())
        self.character.set_breed("homid")
        self.assertTrue(self.character.has_breed())

    def test_breed_sets_gnosis(self):
        self.character.set_breed("homid")
        self.assertEqual(self.character.gnosis, 1)
        self.character.set_breed("metis")
        self.assertEqual(self.character.gnosis, 3)
        self.character.set_breed("lupus")
        self.assertEqual(self.character.gnosis, 5)

    def test_set_camp(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        c = Camp.objects.get(name="Test Camp")
        self.assertFalse(self.character.has_camp())
        self.assertTrue(self.character.set_camp(c))
        self.assertTrue(self.character.has_camp())

    def test_has_camp(self):
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        c = Camp.objects.get(name="Test Camp", tribe=t)
        self.assertFalse(self.character.has_camp())
        self.character.set_camp(c)
        self.assertTrue(self.character.has_camp())

    def test_add_gnosis(self):
        self.assertEqual(self.character.gnosis, 0)
        self.assertTrue(self.character.add_gnosis())
        self.assertEqual(self.character.gnosis, 1)
        self.character.gnosis = 10
        self.assertFalse(self.character.add_gnosis())

    def test_add_rage(self):
        self.assertEqual(self.character.rage, 0)
        self.assertTrue(self.character.add_rage())
        self.assertEqual(self.character.rage, 1)
        self.character.rage = 10
        self.assertFalse(self.character.add_rage())

    def test_tribe_sets_willpower(self):
        t = Tribe.objects.get(name="Test Tribe 2")
        self.character.set_tribe(t)
        self.assertEqual(self.character.willpower, 3)
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        self.assertEqual(self.character.willpower, 5)

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 0,
                "ancestors": 0,
                "fate": 0,
                "fetish": 0,
                "kinfolk": 0,
                "pure_breed": 0,
                "contacts": 0,
                "rites": 0,
                "spirit_heritage": 0,
                "mentor": 0,
                "resources": 0,
                "totem": 0,
            },
        )
        self.character.allies = 1
        self.character.ancestors = 3
        self.character.kinfolk = 3
        self.character.pure_breed = 2
        self.character.mentor = 2
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "allies": 1,
                "ancestors": 3,
                "fate": 0,
                "fetish": 0,
                "kinfolk": 3,
                "pure_breed": 2,
                "contacts": 0,
                "rites": 0,
                "spirit_heritage": 0,
                "mentor": 2,
                "resources": 0,
                "totem": 0,
            },
        )

    def test_total_backgrounds(self):
        self.character.allies = 3
        self.character.ancestors = 4
        self.character.resources = 1
        self.character.fetish = 2
        self.assertEqual(self.character.total_backgrounds(), 10)
        self.character.spirit_heritage = 2
        self.assertEqual(self.character.total_backgrounds(), 12)

    def test_set_glory(self):
        self.assertEqual(self.character.glory, 0)
        self.assertTrue(self.character.set_glory(3))
        self.assertEqual(self.character.glory, 3)

    def test_set_honor(self):
        self.assertEqual(self.character.honor, 0)
        self.assertTrue(self.character.set_honor(3))
        self.assertEqual(self.character.honor, 3)

    def test_set_wisdom(self):
        self.assertEqual(self.character.wisdom, 0)
        self.assertTrue(self.character.set_wisdom(3))
        self.assertEqual(self.character.wisdom, 3)

    def test_has_renown(self):
        self.assertFalse(self.character.has_renown())
        self.character.set_auspice("ragabash")
        self.assertEqual(
            self.character.glory + self.character.honor + self.character.wisdom, 3
        )
        self.assertTrue(self.character.has_renown())

    def test_set_auspice(self):
        self.assertFalse(self.character.has_auspice())
        self.assertTrue(self.character.set_auspice("ragabash"))
        self.assertTrue(self.character.has_auspice())

    def test_has_auspice(self):
        self.assertFalse(self.character.has_breed())
        self.character.set_breed("homid")
        self.assertTrue(self.character.has_breed())

    def test_auspice_sets_rage(self):
        self.assertEqual(self.character.rage, 0)
        self.character.set_auspice("ragabash")
        self.assertEqual(self.character.rage, 1)
        self.character.set_auspice("theurge")
        self.assertEqual(self.character.rage, 2)
        self.character.set_auspice("philodox")
        self.assertEqual(self.character.rage, 3)
        self.character.set_auspice("galliard")
        self.assertEqual(self.character.rage, 4)
        self.character.set_auspice("ahroun")
        self.assertEqual(self.character.rage, 5)

    def test_auspice_sets_renown(self):
        self.assertEqual(
            self.character.glory + self.character.honor + self.character.wisdom, 0
        )
        self.character.set_auspice("ragabash")
        self.assertEqual(
            self.character.glory + self.character.honor + self.character.wisdom, 3
        )
        self.character.set_auspice("theurge")
        self.assertEqual(self.character.glory, 0)
        self.assertEqual(self.character.honor, 0)
        self.assertEqual(self.character.wisdom, 3)
        self.character.set_auspice("philodox")
        self.assertEqual(self.character.glory, 0)
        self.assertEqual(self.character.honor, 3)
        self.assertEqual(self.character.wisdom, 0)
        self.character.set_auspice("galliard")
        self.assertEqual(self.character.glory, 2)
        self.assertEqual(self.character.honor, 0)
        self.assertEqual(self.character.wisdom, 1)
        self.character.set_auspice("ahroun")
        self.assertEqual(self.character.glory, 2)
        self.assertEqual(self.character.honor, 1)
        self.assertEqual(self.character.wisdom, 0)

    def test_set_rank(self):
        self.assertEqual(self.character.rank, 1)
        self.character.set_rank(3)
        self.assertEqual(self.character.rank, 3)

    def test_increase_rank(self):
        self.assertEqual(self.character.rank, 1)
        self.character.set_auspice("ragabash")
        self.assertFalse(self.character.increase_rank())
        self.character.set_glory(3)
        self.character.set_honor(3)
        self.character.set_wisdom(1)
        self.assertTrue(self.character.increase_rank())

    def test_freebie_cost(self):
        self.assertEqual(self.character.freebie_cost("attribute"), 5)
        self.assertEqual(self.character.freebie_cost("ability"), 2)
        self.assertEqual(self.character.freebie_cost("background"), 1)
        self.assertEqual(self.character.freebie_cost("willpower"), 1)
        self.assertEqual(self.character.freebie_cost("meritflaw"), 1)
        self.assertEqual(self.character.freebie_cost("gift"), 7)
        self.assertEqual(self.character.freebie_cost("rage"), 1)
        self.assertEqual(self.character.freebie_cost("gnosis"), 2)

    def test_spend_freebies(self):
        self.character.set_tribe(Tribe.objects.get(name="Test Tribe"))
        self.assertEqual(self.character.freebies, 15)
        self.assertTrue(self.character.spend_freebies("strength"))
        self.assertEqual(self.character.freebies, 10)
        self.assertTrue(self.character.spend_freebies("occult"))
        self.assertEqual(self.character.freebies, 8)
        self.assertTrue(self.character.spend_freebies("mentor"))
        self.assertEqual(self.character.freebies, 7)
        self.assertTrue(self.character.spend_freebies("willpower"))
        self.assertEqual(self.character.freebies, 6)
        self.assertTrue(self.character.spend_freebies("Merit 1"))
        self.assertEqual(self.character.freebies, 5)
        self.character.freebies = 15
        self.assertEqual(self.character.freebies, 15)
        self.assertTrue(self.character.spend_freebies("Test Tribe Gift"))
        self.assertEqual(self.character.freebies, 8)
        self.assertTrue(self.character.spend_freebies("rage"))
        self.assertEqual(self.character.freebies, 7)
        self.assertTrue(self.character.spend_freebies("gnosis"))
        self.assertEqual(self.character.freebies, 5)

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("ability"), 2)
        self.assertEqual(self.character.xp_cost("background"), 3)
        self.assertEqual(self.character.xp_cost("new background"), 5)
        self.assertEqual(self.character.xp_cost("willpower"), 1)
        self.assertEqual(self.character.xp_cost("new ability"), 3)

        self.assertEqual(self.character.xp_cost("gift"), 3)
        self.assertEqual(self.character.xp_cost("outside gift"), 5)
        self.assertEqual(self.character.xp_cost("rage"), 1)
        self.assertEqual(self.character.xp_cost("gnosis"), 2)

    def test_spend_xp(self):
        self.character.xp = 100
        t = Tribe.objects.get(name="Test Tribe")
        self.character.set_tribe(t)
        self.character.set_auspice("ragabash")
        self.character.set_breed("homid")
        self.assertTrue(self.character.spend_xp("strength"))
        self.assertEqual(self.character.xp, 96)
        self.assertTrue(self.character.spend_xp("occult"))
        self.assertEqual(self.character.xp, 93)
        self.assertTrue(self.character.spend_xp("occult"))
        self.assertEqual(self.character.xp, 91)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 86)
        self.assertTrue(self.character.spend_xp("mentor"))
        self.assertEqual(self.character.xp, 83)
        self.assertTrue(self.character.spend_xp("willpower"))
        self.assertEqual(self.character.xp, 78)
        self.assertTrue(self.character.spend_xp("Test Tribe Gift"))
        self.assertEqual(self.character.xp, 75)
        self.assertTrue(self.character.spend_xp("rage"))
        self.assertEqual(self.character.xp, 74)
        self.assertTrue(self.character.spend_xp("gnosis"))
        self.assertEqual(self.character.xp, 72)
        self.assertTrue(self.character.spend_xp("Gift 1"))
        self.assertEqual(self.character.xp, 67)

    def test_has_werewolf_history(self):
        self.assertFalse(self.character.has_werewolf_history())
        self.character.first_change = "Young"
        self.assertFalse(self.character.has_werewolf_history())
        self.character.battle_scars = "Several"
        self.assertFalse(self.character.has_werewolf_history())
        self.character.age_of_first_change = 13
        self.assertTrue(self.character.has_werewolf_history())

    def test_no_homid_red_talons(self):
        self.character.breed = "homid"
        self.assertFalse(
            self.character.set_tribe(Tribe.objects.create(name="Red Talons"))
        )

    def test_no_male_black_furies(self):
        self.character.sex = "Male"
        self.assertFalse(
            self.character.set_tribe(Tribe.objects.create(name="Black Furies"))
        )

    def test_silver_fangs_have_pure_breed_three(self):
        self.character.set_tribe(Tribe.objects.create(name="Silver Fangs"))
        self.assertEqual(self.character.pure_breed, 3)

    def test_add_renown_incident(self):
        r = RenownIncident.objects.create(
            name="Test Renown Incident", glory=1, honor=1, wisdom=1
        )
        self.assertTrue(self.character.add_renown_incident(r))
        self.assertEqual(self.character.num_renown_incidents(), 1)
        self.assertIn("Test Renown Incident", self.character.renown_incidents)
        self.assertEqual(self.character.temporary_glory, 1)
        self.assertEqual(self.character.temporary_honor, 1)
        self.assertEqual(self.character.temporary_wisdom, 1)

    def test_update_renown(self):
        self.character.glory = 2
        self.character.temporary_glory = 10
        self.character.update_renown()
        self.assertEqual(self.character.glory, 3)
        self.assertEqual(self.character.temporary_glory, 0)

    def test_achieved_age_only_once(self):
        r = RenownIncident.objects.create(
            name="One Off", glory=1, wisdom=2, only_once=True
        )
        self.assertTrue(self.character.add_renown_incident(r))
        self.assertFalse(self.character.add_renown_incident(r))

    def test_breed_renown_correct(self):
        r = RenownIncident.objects.create(name="Lupus Award", breed="lupus")
        self.character.set_breed("homid")
        self.assertFalse(self.character.add_renown_incident(r))

    def test_renown_check_if_has_rite(self):
        rite = Rite.objects.create(name="Test Rite for Renown")
        renown = RenownIncident.objects.create(
            name="Used Test Rite for Renown", rite=rite
        )
        self.assertFalse(self.character.add_renown_incident(renown))
        self.character.add_rite(rite)
        self.assertTrue(self.character.add_renown_incident(renown))

    def test_wont_add_if_last_is_posthumous(self):
        r1 = RenownIncident.objects.create(
            name="Award (posthumous)", glory=3, honor=3, wisdom=0, posthumous=True
        )
        r2 = RenownIncident.objects.create(name="Award", glory=3, honor=3, wisdom=0)
        self.assertTrue(self.character.add_renown_incident(r1))
        self.assertFalse(self.character.add_renown_incident(r2))

    def test_learn_a_new_rite(self):
        r = RenownIncident.objects.create(name="Learning a new rite")
        num = self.character.rites_known.count()
        self.character.add_renown_incident(r)
        self.assertEqual(self.character.rites_known.count(), num + 1)


class TestTotem(TestCase):
    pass


class TestRandomTotem(TestCase):
    # Cost 1 - 3 points for WP, Rage, and Gnosis
    # Cost 1 - Totem can speak to pack without Spirit Speech
    # Cost 1 - Totam can always find pack members
    # Cost 2 - Totem is nearly always with pack members
    # Cost 2 - Totem is respected by other spirits
    # Cost 2 - Per charm
    # Cost 3 - Per extra pack member who can use the totem's powers in same turn
    # Cost 4 - Totem connected mystically to all pack maembers allowing communication
    # Cost 5 - Totem is feared by the Wyrm
    pass


class TestRandomWerewolf(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = Werewolf.objects.create(
            name="", player=self.player.wod_profile
        )
        werewolf_setup(self.player)

    def test_random_tribe(self):
        self.assertFalse(self.character.has_tribe())
        self.character.random_tribe()
        self.assertTrue(self.character.has_tribe())

    def test_random_auspice(self):
        self.assertFalse(self.character.has_auspice())
        self.character.random_auspice()
        self.assertTrue(self.character.has_auspice())

    def test_random_gifts(self):
        self.character.random_tribe()
        self.character.random_auspice()
        self.character.random_breed()
        self.assertFalse(self.character.has_gifts())
        self.character.random_gifts()
        self.assertTrue(self.character.has_gifts())

    def test_random_rites(self):
        self.character.rites = 3
        self.assertFalse(self.character.has_rites())
        self.character.random_rites()
        self.assertTrue(self.character.has_rites())

    def test_random_spend_xp(self):
        self.character.random_tribe()
        self.character.random_auspice()
        self.character.science = 1
        self.character.xp = 15
        self.character.random_xp()
        self.assertLess(self.character.xp, 15)

    def test_random_freebies(self):
        self.character.random_tribe()
        self.assertEqual(self.character.freebies, 15)
        self.character.random_freebies()
        self.assertEqual(self.character.freebies, 0)

    def test_random_renown_incident(self):
        self.character.auspice = "ahroun"
        num = self.character.num_renown_incidents()
        self.character.random_renown_incident()
        self.assertEqual(self.character.num_renown_incidents(), num + 1)

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        self.assertFalse(self.character.has_archetypes())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_backgrounds())
        self.assertFalse(self.character.has_finishing_touches())
        self.assertFalse(self.character.has_history())
        self.assertFalse(self.character.has_gifts())
        self.assertFalse(self.character.has_tribe())
        self.assertFalse(self.character.has_auspice())
        self.assertFalse(self.character.has_camp())
        self.assertFalse(self.character.has_renown())
        self.assertFalse(self.character.has_werewolf_history())
        self.character.random(freebies=0, xp=0)
        self.assertTrue(self.character.has_name())
        self.assertTrue(self.character.has_concept())
        self.assertTrue(self.character.has_archetypes())
        self.assertTrue(self.character.has_attributes())
        self.assertTrue(self.character.has_abilities())
        self.assertTrue(self.character.has_specialties())
        self.assertTrue(self.character.has_backgrounds())
        self.assertTrue(self.character.has_finishing_touches())
        self.assertTrue(self.character.has_history())
        self.assertTrue(self.character.has_gifts())
        self.assertTrue(self.character.has_rites())
        self.assertTrue(self.character.has_tribe())
        self.assertTrue(self.character.has_auspice())
        self.assertTrue(self.character.has_renown())
        self.assertTrue(self.character.has_werewolf_history())


class TestPack(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        werewolf_setup(self.player)

    def test_pack_creation(self):
        pack = Pack.objects.create(name="Pack 1")
        pack.members.set(Werewolf.objects.all())
        pack.leader = Werewolf.objects.first()
        pack.save()
        self.assertEqual(pack.members.count(), 5)
        self.assertIsNotNone(pack.leader)

    def test_random_pack(self):
        pack = Pack.objects.create(name="Pack 1")
        pack.random(num_chars=5, new_characters=False)
        self.assertEqual(pack.members.count(), 5)
        for werewolf in Werewolf.objects.all():
            self.assertIn(werewolf, pack.members.all())
        pack = Pack.objects.create(name="Pack 2")
        pack.random(num_chars=5, new_characters=True)
        self.assertEqual(pack.members.count(), 5)

    def test_exception(self):
        pack = Pack.objects.create(name="Pack 10")
        with self.assertRaises(ValueError):
            pack.random(num_chars=10, new_characters=False)

    def test_totem_total(self):
        p = Pack.objects.create(name="Pack")
        self.assertEqual(p.total_totem(), 0)
        for i in range(4):
            w = Werewolf.objects.create(
                name=f"Werewolf {i}", player=self.player.wod_profile
            )
            w.totem = i + 1
            w.save()
            p.members.add(w)
            p.save()
        self.assertEqual(p.total_totem(), 10)

    def test_set_totem(self):
        pack = Pack.objects.create(name="Pack 1")
        t = Totem.objects.first()
        self.assertFalse(pack.has_totem())
        self.assertTrue(pack.set_totem(t))
        self.assertTrue(pack.has_totem())

    def test_has_totem(self):
        pack = Pack.objects.create(name="Pack 1")
        t = Totem.objects.first()
        self.assertFalse(pack.has_totem())
        pack.set_totem(t)
        self.assertTrue(pack.has_totem())

    def test_random_totem(self):
        p = Pack.objects.create(name="Pack")
        for i in range(4):
            w = Werewolf.objects.create(
                name=f"Werewolf {i}", player=self.player.wod_profile
            )
            w.totem = i + 1
            w.save()
            p.members.add(w)
            p.save()
        self.assertFalse(p.has_totem())
        self.assertTrue(p.random_totem())
        self.assertTrue(p.has_totem())

    def test_str(self):
        pack = Pack.objects.create(name="Pack 1")
        self.assertEqual(str(pack), "Pack 1")


class TestWerewolfDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.werewolf = Werewolf.objects.create(
            name="Test Werewolf", player=self.player.wod_profile
        )

    def test_werewolf_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.werewolf.id}/")
        self.assertEqual(response.status_code, 200)

    def test_werewolf_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.werewolf.id}/")
        self.assertTemplateUsed(response, "wod/characters/werewolf/detail.html")
