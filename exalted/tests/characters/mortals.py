from django.test import TestCase
from exalted.models.characters.mortals import Mortal
from django.contrib.auth.models import User

# Create your tests here.
def setup():
    pass

class TestMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="", player=self.player.exalted_profile)
        setup()
        
    def test_absolute_url(self):
        self.assertEqual(
            self.character.get_absolute_url(), f"/exalted/characters/{self.character.id}/"
        )
        
    def test_has_name(self):
        self.character.name = ""
        self.assertFalse(self.character.has_name())
        self.character.name = "Test"
        self.assertTrue(self.character.has_name())
    
    def test_set_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.set_name("Test"))
        self.assertNotEqual(self.character.name, "")
    
    def test_has_concept(self):
        self.character.concept = ""
        self.assertFalse(self.character.has_concept())
        self.character.concept = "Test"
        self.assertTrue(self.character.has_concept())

    def test_set_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.set_concept("Test Concept"))
        self.assertEqual(self.character.concept, "Test Concept")

    def test_add_attribute(self):
        self.character.strength = 1
        self.assertTrue(self.character.add_attribute("strength"))
        self.assertEqual(self.character.strength, 2)
        self.character.strength = 5
        self.assertFalse(self.character.add_attribute("strength", maximum=5))
        self.assertEqual(self.character.strength, 5)
        self.assertTrue(self.character.add_attribute("strength", maximum=6))
        self.assertEqual(self.character.strength, 6)

    def set_attributes(self):
        self.character.strength = 5
        self.character.dexterity = 4
        self.character.stamina = 3
        self.character.perception = 2
        self.character.intelligence = 1
        self.character.wits = 2
        self.character.charisma = 3
        self.character.manipulation = 4
        self.character.appearance = 5

    def test_get_attributes(self):
        self.assertEqual(
            self.character.get_attributes(),
            {
                "strength": 1,
                "dexterity": 1,
                "stamina": 1,
                "perception": 1,
                "intelligence": 1,
                "wits": 1,
                "charisma": 1,
                "manipulation": 1,
                "appearance": 1,
            },
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_attributes(),
            {
                "strength": 5,
                "dexterity": 4,
                "stamina": 3,
                "perception": 2,
                "intelligence": 1,
                "wits": 2,
                "charisma": 3,
                "manipulation": 4,
                "appearance": 5,
            },
        )

    def test_get_physical_attributes(self):
        self.assertEqual(
            self.character.get_physical_attributes(),
            {"strength": 1, "dexterity": 1, "stamina": 1,},
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_physical_attributes(),
            {"strength": 5, "dexterity": 4, "stamina": 3,},
        )

    def test_get_mental_attributes(self):
        self.assertEqual(
            self.character.get_mental_attributes(),
            {"perception": 1, "intelligence": 1, "wits": 1,},
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_mental_attributes(),
            {"perception": 2, "intelligence": 1, "wits": 2,},
        )

    def test_get_social_attributes(self):
        self.assertEqual(
            self.character.get_social_attributes(),
            {"charisma": 1, "manipulation": 1, "appearance": 1,},
        )
        self.set_attributes()
        self.assertEqual(
            self.character.get_social_attributes(),
            {"charisma": 3, "manipulation": 4, "appearance": 5,},
        )

    def test_has_attributes(self):
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 7, 9])
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
        self.assertEqual(triple, [6, 7, 9])
        self.character.perception = 3
        triple = [
            self.character.total_physical_attributes(),
            self.character.total_mental_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort()
        self.assertNotEqual(triple, [6, 7, 9])

    def test_total_physical_attribute(self):
        self.character.strength = 1
        self.character.dexterity = 2
        self.character.stamina = 3
        self.assertEqual(self.character.total_physical_attributes(), 6)
        self.character.stamina = 2
        self.assertEqual(self.character.total_physical_attributes(), 5)

    def test_total_mental_attribute(self):
        self.character.perception = 1
        self.character.intelligence = 2
        self.character.wits = 3
        self.assertEqual(self.character.total_mental_attributes(), 6)
        self.character.wits = 2
        self.assertEqual(self.character.total_mental_attributes(), 5)

    def test_total_social_attribute(self):
        self.character.charisma = 1
        self.character.manipulation = 2
        self.character.appearance = 3
        self.assertEqual(self.character.total_social_attributes(), 6)
        self.character.appearance = 2
        self.assertEqual(self.character.total_social_attributes(), 5)

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

    def test_add_ability(self):
        self.character.occult = 0
        self.assertTrue(self.character.add_ability("occult"))
        self.assertEqual(self.character.occult, 1)
        self.character.occult = 5
        self.assertFalse(self.character.add_ability("occult", maximum=5))
        self.assertEqual(self.character.occult, 5)
        self.assertTrue(self.character.add_ability("occult", maximum=6))
        self.assertEqual(self.character.occult, 6)

    def set_abilities(self):
        self.character.archery = 3
        self.character.melee = 2
        self.character.awareness = 1
        self.character.dodge = 1
        self.character.craft = 1
        self.character.presence = 2
        self.character.martial_arts = 3
        self.character.linguistics = 3
        self.character.lore = 2
        self.character.bureaucracy = 2
        self.character.socialize = 3
        self.character.sail = 1
        self.character.ride = 1
        self.character.war = 3

    def test_get_abilities(self):
        self.assertEqual(self.character.get_abilities(), {
            "archery": 0,
            "athletics": 0,
            "awareness": 0,
            "brawl": 0,
            "bureaucracy": 0,
            "craft": 0,
            "dodge": 0,
            "integrity": 0,
            "investigation": 0,
            "larceny": 0,
            "linguistics": 0,
            "lore": 0,
            "martial_arts": 0,
            "medicine": 0,
            "melee": 0,
            "occult": 0,
            "performance": 0,
            "presence": 0,
            "resistance": 0,
            "ride": 0,
            "sail": 0,
            "socialize": 0,
            "stealth": 0,
            "survival": 0,
            "thrown": 0,
            "war": 0,
        })
        self.set_abilities()
        self.assertEqual(self.character.get_abilities(), {
            "archery": 3,
            "athletics": 0,
            "awareness": 1,
            "brawl": 0,
            "bureaucracy": 2,
            "craft": 1,
            "dodge": 1,
            "integrity": 0,
            "investigation": 0,
            "larceny": 0,
            "linguistics": 3,
            "lore": 2,
            "martial_arts": 3,
            "medicine": 0,
            "melee": 2,
            "occult": 0,
            "performance": 0,
            "presence": 2,
            "resistance": 0,
            "ride": 1,
            "sail": 1,
            "socialize": 3,
            "stealth": 0,
            "survival": 0,
            "thrown": 0,
            "war": 3,
        })

    def test_has_abilities(self):
        self.assertFalse(self.character.has_abilities())
        self.set_abilities()
        self.assertTrue(self.character.has_abilities())

    def test_filter_abilities(self):
        self.fail()

    def test_add_specialty(self):
        self.fail()

    def test_has_specialties(self):
        self.fail()

    def test_filter_specialties(self):
        self.fail()

    def test_add_merit(self):
        self.fail()

    def test_filter_merits(self):
        self.fail()

    def test_has_intimacies(self):
        self.fail()

    def test_add_intimacy(self):
        self.fail()

    def test_bonus_point_costs(self):
        self.fail()

    def test_spend_bonus_points(self):
        self.fail()

    def test_xp_costs(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()


class TestRandomMortal(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Mortal.objects.create(name="", player=self.player.exalted_profile)
        setup()

    def test_random_name(self):
        self.assertFalse(self.character.has_name())
        self.character.random_name()
        self.assertTrue(self.character.has_name())

    def test_random_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.random_concept()
        self.assertTrue(self.character.has_concept())

    def test_random_attribute(self):
        num = self.character.total_attributes()
        self.character.random_attribute()
        self.assertEqual(self.character.total_attributes(), num + 1)

    def test_random_attributes(self):
        self.character.random_attributes()
        triple = [
            self.character.total_mental_attributes(),
            self.character.total_physical_attributes(),
            self.character.total_social_attributes(),
        ]
        triple.sort(key=lambda x: -x)
        self.assertEqual(triple, [9, 7, 6])

    def test_random_ability(self):
        num = self.character.total_abilities()
        self.character.random_ability()
        self.assertEqual(self.character.total_abilities(), num + 1)
        
    def test_random_abilities(self):
        self.assertFalse(self.character.has_abilities())
        self.assertTrue(self.character.random_abilities())
        self.assertTrue(self.character.has_abilities())

    def test_random_specialty(self):
        self.fail()

    def test_random_specialties(self):
        self.fail()

    def test_random_merit(self):
        self.fail()

    def test_random_intimacy(self):
        self.fail()

    def test_random_spend_bonus_points(self):
        self.fail()

    def test_random_spend_xp(self):
        self.fail()

    def test_random(self):
        self.fail()


class TestCharacterIndexView(TestCase):
    def test_index_status_code(self):
        response = self.client.get("/exalted/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/exalted/characters/")
        self.assertTemplateUsed(response, "exalted/characters/index.html")

    def test_index_content(self):
        player = User.objects.create_user(username="User1", password="12345")
        for i in range(10):
            Mortal.objects.create(name=f"Mortal {i}", player=player.exalted_profile)
        response = self.client.post("/exalted/characters/")
        for i in range(10):
            self.assertContains(response, f"Mortal {i}")

class TestMortalDetailView(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.human = Mortal.objects.create(
            name="Test Mortal", player=self.player.exalted_profile
        )

    def test_mortal_detail_view_status_code(self):
        response = self.client.get(f"/exalted/characters/{self.human.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mortal_detail_view_template(self):
        response = self.client.get(f"/exalted/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "exalted/characters/mortal/detail.html")

class TestGenericCharacterDetailViews(TestCase):
    def setUp(self) -> None:
        self.player = User.objects.create_user(username="Test")
        self.mortal = Mortal.objects.create(
            name="Test Mortal", player=self.player.exalted_profile
        )

    def test_character_detail_view_templates(self):
        response = self.client.get(f"/exalted/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "exalted/characters/mortal/detail.html")
