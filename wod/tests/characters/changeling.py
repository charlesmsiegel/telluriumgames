from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.changeling import Changeling, Kith, House, Legacy, Motley


# Create your tests here.
def changeling_setup(player):
    for i in range(5):
        Kith.objects.create(
            name=f"Kith {i}",
            birthrights=["Birthright 1", "Birthright 2"],
            frailty="",
            description="",
        )
        House.objects.create(
            name=f"House {i}",
            court=["seelie", "unseelie"][i % 2],
            boon="",
            flaw="",
            factions=[],
        )
        Legacy.objects.create(
            name=f"Legacy {i}", court=["seelie", "unseelie"][i % 2],
        )


class TestCtDHuman(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")
        changeling_setup(self.player)

    def set_abilities(self):
        self.character.kenning = 3
        self.character.leadership = 2
        self.character.crafts = 3
        self.character.animal_ken = 2
        self.character.larceny = 2
        self.character.enigmas = 2
        self.character.gremayre = 3

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
                "kenning": 0,
                "leadership": 0,
            },
        )
        self.set_abilities()
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
                "kenning": 3,
                "leadership": 2,
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
                "crafts": 3,
                "drive": 0,
                "etiquette": 0,
                "firearms": 0,
                "melee": 0,
                "stealth": 0,
                "animal_ken": 2,
                "larceny": 2,
                "performance": 3,
                "survival": 2,
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
                "gremayre": 0,
                "law": 0,
                "politics": 0,
                "technology": 0,
            },
        )
        self.set_abilities()
        self.assertEqual(
            self.character.get_knowledges(),
            {
                "academics": 0,
                "computer": 0,
                "investigation": 0,
                "medicine": 0,
                "science": 0,
                "enigmas": 2,
                "gremayre": 3,
                "law": 0,
                "politics": 0,
                "technology": 0,
            },
        )

    def test_get_backgrounds(self):
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "contacts": 0,
                "mentor": 0,
                "chimera": 0,
                "dreamers": 0,
                "holdings": 0,
                "remembrance": 0,
                "resources": 0,
                "retinue": 0,
                "title": 0,
                "treasure": 0,
            },
        )
        self.character.contacts = 2
        self.character.title = 3
        self.character.dreamers = 4
        self.character.resources = 5
        self.assertEqual(
            self.character.get_backgrounds(),
            {
                "contacts": 2,
                "mentor": 0,
                "chimera": 0,
                "dreamers": 4,
                "holdings": 0,
                "remembrance": 0,
                "resources": 5,
                "retinue": 0,
                "title": 3,
                "treasure": 0,
            },
        )


class TestChangeling(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")
        changeling_setup(self.player)

    def test_set_seeming(self):
        self.assertFalse(self.character.has_seeming())
        glamour = self.character.glamour
        willpower = self.character.willpower
        self.assertTrue(self.character.set_seeming("childer"))
        self.assertEqual(self.character.glamour, glamour + 1)
        self.assertTrue(self.character.has_seeming())
        self.assertTrue(self.character.set_seeming("wilder"))
        self.assertEqual(
            self.character.glamour + self.character.willpower, glamour + willpower + 1
        )
        self.assertTrue(self.character.set_seeming("grump"))
        self.assertEqual(self.character.willpower, willpower + 1)

    def test_has_seeming(self):
        self.assertFalse(self.character.has_seeming())
        self.character.set_seeming("childer")
        self.assertTrue(self.character.has_seeming())

    def test_set_court(self):
        self.assertFalse(self.character.has_court())
        self.assertTrue(self.character.set_court("seelie"))
        self.assertTrue(self.character.has_court())

    def test_has_court(self):
        self.assertFalse(self.character.has_court())
        self.character.set_court("seelie")
        self.assertTrue(self.character.has_court())

    def test_set_seelie_legacy(self):
        self.fail()

    def test_has_seelie_legacy(self):
        self.fail()

    def test_set_unseelie_legacy(self):
        self.fail()

    def test_has_unseelie_legacy(self):
        self.fail()

    def test_add_art(self):
        self.fail()

    def test_get_arts(self):
        self.fail()

    def test_has_arts(self):
        # Arts 3
        self.fail()

    def test_total_arts(self):
        self.fail()

    def test_filter_arts(self):
        self.fail()

    def test_add_realm(self):
        self.fail()

    def test_get_realms(self):
        self.fail()

    def test_has_realms(self):
        # Realms 5
        self.fail()

    def test_total_realms(self):
        self.fail()

    def test_filter_realms(self):
        self.fail()

    def test_set_musing_threshold(self):
        self.fail()

    def test_has_musing_threshold(self):
        self.fail()

    def test_set_ravaging_threshold(self):
        self.fail()

    def test_has_ravaging_threshold(self):
        self.fail()

    def test_set_antithesis(self):
        self.fail()

    def test_has_antithesis(self):
        self.fail()

    def test_add_glamour(self):
        self.fail()

    def test_add_banality(self):
        self.fail()

    def test_changeling_numbers(self):
        self.assertEqual(self.character.background_points, 5)
        self.assertEqual(self.character.willpower, 4)
        self.assertEqual(self.character.glamour, 4)
        self.assertEqual(self.character.banality, 3)

    def test_freebie_cost(self):
        self.assertEqual(self.character.freebie_cost("attribute"), 5)
        self.assertEqual(self.character.freebie_cost("ability"), 2)
        self.assertEqual(self.character.freebie_cost("background"), 1)
        self.assertEqual(self.character.freebie_cost("willpower"), 1)
        self.assertEqual(self.character.freebie_cost("meritflaw"), 1)
        self.assertEqual(self.character.freebie_cost("art"), 5)
        self.assertEqual(self.character.freebie_cost("glamour"), 3)
        self.assertEqual(self.character.freebie_cost("realm"), 2)

    def test_spend_freebies(self):
        self.fail()

    def test_xp_cost(self):
        self.assertEqual(self.character.xp_cost("attribute"), 4)
        self.assertEqual(self.character.xp_cost("ability"), 2)
        self.assertEqual(self.character.xp_cost("background"), 3)
        self.assertEqual(self.character.xp_cost("new background"), 5)
        self.assertEqual(self.character.xp_cost("willpower"), 2)
        self.assertEqual(self.character.xp_cost("new ability"), 3)

        self.assertEqual(self.character.xp_cost("art"), 4)
        self.assertEqual(self.character.xp_cost("new art"), 7)
        self.assertEqual(self.character.xp_cost("realm"), 3)
        self.assertEqual(self.character.xp_cost("new realm"), 5)
        self.assertEqual(self.character.xp_cost("glamour"), 3)

    def test_spend_xp(self):
        self.fail()

    def test_birthright_corrections(self):
        self.fail()

    def test_changeling_history(self):
        self.fail()

    def test_changeling_appearance(self):
        self.fail()


class TestRandomChangeling(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Changeling.objects.create(owner=self.player, name="")
        changeling_setup(self.player)

    def test_random_seeming(self):
        self.assertFalse(self.character.has_seeming())
        self.assertTrue(self.character.random_seeming())
        self.assertTrue(self.character.has_seeming())

    def test_random_court(self):
        self.assertFalse(self.character.has_court())
        self.assertTrue(self.character.random_court())
        self.assertTrue(self.character.has_court())

    def test_random_seelie_legacy(self):
        self.fail()

    def test_random_unseelie_legacy(self):
        self.fail()

    def test_random_art(self):
        self.fail()

    def test_random_arts(self):
        self.fail()

    def test_random_realm(self):
        self.fail()

    def test_random_realms(self):
        self.fail()

    def test_random_musing_threshold(self):
        self.fail()

    def test_random_ravaging_threshold(self):
        self.fail()

    def test_random(self):
        self.fail()

    def test_random_freebies(self):
        self.fail()

    def test_random_spend_xp(self):
        self.fail()

    def test_random(self):
        self.assertFalse(self.character.has_name())
        self.assertFalse(self.character.has_concept())
        # self.assertFalse(self.character.has_archetypes())
        self.assertFalse(self.character.has_attributes())
        self.assertFalse(self.character.has_abilities())
        self.assertFalse(self.character.has_backgrounds())
        self.assertFalse(self.character.has_finishing_touches())
        self.assertFalse(self.character.has_history())
        # self.assertFalse(self.character.has_spheres())
        # self.assertFalse(self.character.has_affinity_sphere())
        # self.assertFalse(self.character.has_faction())
        # self.assertFalse(self.character.has_focus())
        # self.assertFalse(self.character.has_essence())
        # self.assertFalse(self.character.has_effects())
        self.assertFalse(self.character.has_changeling_history())
        self.character.random(freebies=0, xp=0)
        self.assertTrue(self.character.has_name())
        self.assertTrue(self.character.has_concept())
        # self.assertTrue(self.character.has_archetypes())
        self.assertTrue(self.character.has_attributes())
        self.assertTrue(self.character.has_abilities())
        self.assertTrue(self.character.has_specialties())
        self.assertTrue(self.character.has_backgrounds())
        self.assertTrue(self.character.has_finishing_touches())
        self.assertTrue(self.character.has_history())
        # self.assertTrue(self.character.has_spheres())
        # self.assertTrue(self.character.has_affinity_sphere())
        # self.assertTrue(self.character.has_faction())
        # self.assertTrue(self.character.has_focus())
        # self.assertTrue(self.character.has_essence())
        # self.assertTrue(self.character.has_effects())
        self.assertTrue(self.character.has_changeling_history())


class TestMotley(TestCase):
    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        changeling_setup(self.player)

    def test_motley_creation(self):
        motley = Motley.objects.create(name="Motley 1")
        motley.members.set(Changeling.objects.all())
        motley.leader = Changeling.objects.first()
        motley.save()
        self.assertEqual(motley.members.count(), 5)
        self.assertIsNotNone(motley.leader)

    def test_random_motley(self):
        motley = Motley.objects.create(name="Motley 1")
        motley.random(num_chars=5, new_characters=False)
        self.assertEqual(motley.members.count(), 5)
        for changeling in Changeling.objects.all():
            self.assertIn(changeling, motley.members.all())
        motley = motley.objects.create(name="Motley 2")
        motley.random(num_chars=5, new_characters=True)
        self.assertEqual(motley.members.count(), 5)

    def test_exception(self):
        motley = Motley.objects.create(name="Motley 10")
        with self.assertRaises(ValueError):
            motley.random(num_chars=10, new_characters=False)

    def test_str(self):
        motley = Motley.objects.create(name="Motley 1")
        self.assertEqual(str(motley), "Motley 1")


class TestChangelingDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.changeling = Changeling.objects.create(
            name="Test Changeling", owner=self.player
        )

    def test_changeling_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.changeling.id}/")
        self.assertEqual(response.status_code, 200)

    def test_changeling_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.changeling.id}/")
        self.assertTemplateUsed(
            response, "wod/characters/changeling/changeling/detail.html"
        )


class TestMotleyDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.motley = Motley.objects.create(name="Test Motley")

    def test_motley_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/groups/{self.motley.id}/")
        self.assertEqual(response.status_code, 200)

    def test_motley_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/groups/{self.motley.id}/")
        self.assertTemplateUsed(
            response, "wod/characters/changeling/motley/detail.html"
        )
