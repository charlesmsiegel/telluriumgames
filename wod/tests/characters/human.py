from django.contrib.auth.models import User
from django.test import TestCase

from wod.models.characters.human import Character, Human
from wod.models.characters.mage import Mage


# Create your tests here.
class TestCharacter(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Character.objects.create(
            player=self.player.wod_profile, name=""
        )

    def test_has_name(self):
        self.assertFalse(self.character.has_name())
        self.character.set_name("Test")
        self.assertTrue(self.character.has_name())

    def test_set_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.set_name("Test"))
        self.assertNotEqual(self.character.name, "")

    def test_has_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.set_concept("Test")
        self.assertTrue(self.character.has_concept())

    def test_set_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.set_concept("Test"))
        self.assertNotEqual(self.character.concept, "")


class TestHuman(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="Test")
        self.character = Human.objects.create(name="", player=self.user.wod_profile)

    def test_has_archetypes(self):
        self.fail()

    def test_archetypes(self):
        self.fail()

    def test_get_attributes(self):
        self.fail()

    def test_get_physical_attributes(self):
        self.fail()

    def test_get_mental_attributes(self):
        self.fail()

    def test_get_social_attributes(self):
        self.fail()

    def test_add_attribute(self):
        self.character.strength = 1
        self.assertTrue(self.character.add_attribute("strength"))
        self.assertEqual(self.character.strength, 2)
        self.character.strength = 5
        self.assertFalse(self.character.add_attribute("strength", maximum=5))
        self.assertEqual(self.character.strength, 5)
        self.assertTrue(self.character.add_attribute("strength", maximum=6))
        self.assertEqual(self.character.strength, 6)

    def test_filter_attributes(self):
        self.character.strength = 5
        self.assertEqual(
            self.character.filter_attributes(maximum=4),
            {
                "dexterity": 1,
                "stamina": 1,
                "intelligence": 1,
                "wits": 1,
                "perception": 1,
                "appearance": 1,
                "manipulation": 1,
                "charisma": 1,
            },
        )
        self.assertEqual(
            self.character.filter_attributes(maximum=5),
            {
                "strength": 5,
                "dexterity": 1,
                "stamina": 1,
                "intelligence": 1,
                "wits": 1,
                "perception": 1,
                "appearance": 1,
                "manipulation": 1,
                "charisma": 1,
            },
        )
        self.character.strength = 4
        self.assertEqual(self.character.filter_attributes(minimum=3), {"strength": 4})
        self.assertEqual(
            self.character.filter_attributes(minimum=3, maximum=5), {"strength": 4}
        )
        self.assertEqual(self.character.filter_attributes(minimum=5, maximum=6), {})

    def test_has_attributes(self):
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 8, 10])
        self.character.strength = 3
        self.character.dexterity = 4
        self.character.stamina = 3
        self.character.intelligence = 3
        self.character.wits = 3
        self.character.perception = 2
        self.character.charisma = 2
        self.character.manipulation = 2
        self.character.appearance = 2
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertEqual(triple, [6, 8, 10])
        self.character.perception = 3
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 8, 10])

    def test_get_abilities(self):
        self.fail()

    def test_get_talents(self):
        self.fail()

    def test_get_skills(self):
        self.fail()

    def test_get_knowledges(self):
        self.fail()

    def test_add_ability(self):
        self.character.occult = 0
        self.assertTrue(self.character.add_attribute("occult"))
        self.assertEqual(self.character.occult, 1)
        self.character.occult = 5
        self.assertFalse(self.character.add_attribute("occult", maximum=5))
        self.assertEqual(self.character.occult, 5)
        self.assertTrue(self.character.add_attribute("occult", maximum=6))
        self.assertEqual(self.character.occult, 6)

    def test_filter_abilities(self):
        self.fail()

    def set_skills(self):
        pass

    def test_has_abilities(self):
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [5, 9, 13])
        self.set_skills()
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertEqual(triple, [5, 9, 13])
        self.character.subterfuge = 1
        triple = [
            self.character.total_talents(),
            self.character.total_skills(),
            self.character.total_knowledges(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [5, 9, 13])

    def test_add_specialty(self):
        # TODO: Include Well-Skilled Craftman rule, M20 page 279, to allow multiple specialties for some abilities
        self.fail()

    def test_filter_specialties(self):
        self.fail()

    def test_has_specialties(self):
        self.fail()

    def test_get_backgrounds(self):
        self.fail()

    def test_add_background(self):
        self.fail()

    def test_filter_backgrounds(self):
        self.fail()

    def test_has_backgrounds(self):
        self.fail()

    def test_add_willpower(self):
        self.fail()

    def test_add_mf(self):
        self.fail()

    def test_has_mfs(self):
        self.fail()

    def test_filter_mfs(self):
        self.fail()

    def test_freebie_cost(self):
        self.fail()

    def test_spend_freebies(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()


class TestRandomHuman(TestCase):
    def test_random_name(self):
        self.fail()

    def test_random_concept(self):
        self.fail()

    def test_random_archetypes(self):
        self.fail()

    def test_random_attribute(self):
        self.fail()

    def test_random_attributes(self):
        self.fail()

    def test_random_ability(self):
        self.fail()

    def test_random_abilities(self):
        self.fail()

    def test_random_specialty(self):
        self.fail()

    def test_random_specialties(self):
        self.fail()

    def test_random_freebies(self):
        self.fail()

    def test_random_spend_xp(self):
        self.fail()

    def test_random(self):
        self.fail()


class TestCharacterIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/wod/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/characters/")
        self.assertTemplateUsed(response, "wod/characters/index.html")

    def test_index_content(self):
        player = User.objects.create_user(username="User1", password="12345")
        for i in range(10):
            Human.objects.create(name=f"Human {i}", player=player.wod_profile)
        response = self.client.post("/wod/characters/")
        for i in range(10):
            self.assertContains(response, f"Human {i}")


class TestHumanDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.human = Human.objects.create(
            name="Test Human", player=self.player.wod_profile
        )

    def test_mage_detail_view_status_code(self):
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/human/detail.html")

class TestCharacterDetailViews(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.character = Character.objects.create(name="Test Character", player=self.player.wod_profile)
        self.human = Human.objects.create(
            name="Test Human", player=self.player.wod_profile
        )
        self.mage = Mage.objects.create(name="Test Mage", player=self.player.wod_profile)
        
    def test_mage_detail_view_templates(self):
        response = self.client.get(f"/wod/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "wod/characters/character/detail.html")
        response = self.client.get(f"/wod/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "wod/characters/human/detail.html")
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/detail.html")
