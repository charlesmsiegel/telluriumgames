from django.test import TestCase
from django.contrib.auth.models import User

from wod.models.characters.werewolf import Werewolf, Pack, Totem, Tribe, Camp

# Create your tests here.
def werewolf_setup(player):
    for i in range(5):
        Totem.objects.create(name=f"Totem {i}", cost=(10 + i))


class TestWerewolf(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = Werewolf.objects.create(name="Test Werewolf", player=self.player.wod_profile)
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
            }
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
            }
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
            }
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
            }
        )

    def test_get_skills(self):
        self.assertEqual(
            self.character.get_talents(),
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
            }
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
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
            }
        )

    def test_get_knowledges(self):
        self.assertEqual(
            self.character.get_talents(),
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
            }
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_talents(),
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
            }
        )

    def test_set_gifts(self):
        self.fail()

    def test_add_gift(self):
        self.fail()

    def test_filter_gifts(self):
        self.fail()

    def test_has_gifts(self):
        self.fail()

    def test_set_rites(self):
        self.fail()

    def test_add_rites(self):
        self.fail()

    def test_filter_rites(self):
        self.fail()

    def test_has_rites(self):
        self.fail()

    def test_set_tribe(self):
        t = Tribe.objects.create(name="Test Tribe")
        self.assertFalse(self.character.has_tribe())
        self.assertTrue(self.character.set_tribe(t))
        self.assertTrue(self.character.has_tribe())

    def test_has_tribe(self):
        t = Tribe.objects.create(name="Test Tribe")
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

    def test_set_camp(self):
        t = Tribe.objects.create(name="Test Tribe")
        self.character.set_tribe(t)
        c = Camp.objects.create(name="Test Camp", tribe=t)
        self.assertFalse(self.character.has_camp())
        self.assertTrue(self.character.set_camp(c))
        self.assertTrue(self.character.has_camp())

    def test_has_camp(self):
        t = Tribe.objects.create(name="Test Tribe")
        self.character.set_tribe(t)
        c = Camp.objects.create(name="Test Camp", tribe=t)
        self.assertFalse(self.character.has_camp())
        self.character.set_camp(c)
        self.assertTrue(self.character.has_camp())

    def test_add_gnosis(self):
        self.fail()

    def test_add_rage(self):
        self.fail()

    def test_tribe_sets_willpower(self):
        self.fail()

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
        self.assertEqual(self.character.total_backgrounds(), 12)
        self.character.spirit_heritage = 2
        self.assertEqual(self.character.total_backgrounds(), 14)

    def test_set_permanent_glory(self):
        self.fail()

    def test_set_permanent_honor(self):
        self.fail()

    def test_set_permanent_wisdom(self):
        self.fail()

    def test_set_temporary_glory(self):
        self.fail()

    def test_set_temporary_honor(self):
        self.fail()

    def test_set_temporary_wisdom(self):
        self.fail()
        
    def test_has_renown(self):
        self.fail()

    def test_set_auspice(self):
        self.fail()

    def test_has_auspice(self):
        self.fail()

    def test_auspice_sets_rage(self):
        self.fail()

    def test_auspice_sets_renown(self):
        self.fail()

    def test_set_rank(self):
        self.fail()

    def test_increase_rank(self):
        self.fail()

    def test_freebie_cost(self):
        self.fail()

    def test_spend_freebies(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()

    def test_has_werewolf_history(self):
        self.fail()


class TestRandomWerewolf(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
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
        self.fail()

    def test_random_spend_xp(self):
        self.character.science = 1
        self.character.xp = 15
        self.character.random_xp()
        self.assertLess(self.character.xp, 15)


    def test_random_freebies(self):
        self.assertEqual(self.character.freebies, 15)
        self.character.random_freebies()
        self.assertEqual(self.character.freebies, 0)

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
        self.assertFalse(self.character.has_rites())
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
        self.assertTrue(self.character.has_camp())
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
        pack.random(5, new_characters=False)
        self.assertEqual(pack.members.count(), 5)
        for werewolf in Werewolf.objects.all():
            self.assertIn(werewolf, pack.members.all())
        pack = Pack.objects.create(name="Pack 2")
        pack.random(5, new_characters=True)
        self.assertEqual(pack.members.count(), 5)

    def test_exception(self):
        pack = Pack.objects.create(name="Pack 10")
        with self.assertRaises(ValueError):
            pack.random(10, new_characters=False)

    def test_totem_total(self):
        p = Pack.objects.create(name="Pack")
        self.assertEqual(p.total_totem(), 0)
        for i in range(4):
            w = Werewolf.objects.create(
                name=f"Werewolf {i}", player=self.player.wod_profile
            )
            w.totem = i + 1
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

