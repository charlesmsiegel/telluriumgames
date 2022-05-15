from django.contrib.auth.models import User
from django.test import TestCase

from tc.models.character import Aberrant, Human, Path, Specialty, Talent


# Create your tests here.
class TestHuman(TestCase):
    def setUp(self):
        self.player = User.objects.create(username="Test User")
        self.character = Human.objects.create(name="", player=self.player.tc_profile)

    def test_add_name(self):
        self.assertEqual(self.character.name, "")
        self.assertTrue(self.character.add_name("Test Name"))
        self.assertEqual(self.character.name, "Test Name")

    def test_has_name(self):
        self.character.name = ""
        self.assertFalse(self.character.has_name())
        self.character.name = "Test"
        self.assertTrue(self.character.has_name())

    def test_add_concept(self):
        self.assertEqual(self.character.concept, "")
        self.assertTrue(self.character.add_concept("Test Concept"))
        self.assertEqual(self.character.concept, "Test Concept")

    def test_has_concept(self):
        self.character.concept = ""
        self.assertFalse(self.character.has_concept())
        self.character.concept = "Test"
        self.assertTrue(self.character.has_concept())

    def test_add_path(self):
        self.assertEqual(self.character.paths.count(), 0)
        path = Path.objects.create(name="Path")
        self.assertTrue(self.character.add_path(path))
        self.assertEqual(self.character.paths.count(), 1)

    def test_has_paths(self):
        path_origin = Path.objects.create(name="Origin Path", type="origin")
        path_role = Path.objects.create(name="Role Path", type="role")
        path_society = Path.objects.create(name="Society Path", type="society")
        self.character.add_path(path_origin)
        self.assertFalse(self.character.has_paths())
        self.character.add_path(path_role)
        self.assertFalse(self.character.has_paths())
        self.character.add_path(path_society)
        self.assertTrue(self.character.has_paths())

    def test_filter_paths(self):
        self.fail()

    def test_add_skill(self):
        self.character.science = 0
        self.assertTrue(self.character.add_attribute("science"))
        self.assertEqual(self.character.science, 1)
        self.character.science = 5
        self.assertFalse(self.character.add_attribute("science", maximum=5))
        self.assertEqual(self.character.science, 5)
        self.assertTrue(self.character.add_attribute("science", maximum=6))
        self.assertEqual(self.character.science, 6)

    def test_filter_skills(self):
        self.character.science = 5
        self.assertEqual(
            self.character.filter_skills(maximum=4),
            {
                "aim": 0,
                "athletics": 0,
                "close_combat": 0,
                "command": 0,
                "culture": 0,
                "empathy": 0,
                "enigmas": 0,
                "humanities": 0,
                "integrity": 0,
                "larceny": 0,
                "medicine": 0,
                "persuasion": 0,
                "pilot": 0,
                "survival": 0,
                "technology": 0,
            },
        )
        self.assertEqual(
            self.character.filter_skills(maximum=6),
            {
                "aim": 0,
                "athletics": 0,
                "close_combat": 0,
                "command": 0,
                "culture": 0,
                "empathy": 0,
                "enigmas": 0,
                "humanities": 0,
                "integrity": 0,
                "larceny": 0,
                "medicine": 0,
                "persuasion": 0,
                "pilot": 0,
                "science": 5,
                "survival": 0,
                "technology": 0,
            },
        )
        self.character.science = 4
        self.assertEqual(self.character.filter_skills(minimum=3), {"science": 4})
        self.assertEqual(
            self.character.filter_skills(minimum=3, maximum=5), {"science": 4}
        )
        self.assertEqual(self.character.filter_skills(minimum=5, maximum=6), {})

    def test_has_skills(self):
        self.assertFalse(self.character.has_skills())
        self.set_skills()
        self.assertTrue(self.character.has_skills())

    def test_add_trick(self):
        self.fail()

    def test_has_tricks(self):
        self.fail()

    def test_filter_tricks(self):
        self.fail()

    def test_add_specialty(self):
        specialty = Specialty.objects.create(name="Biology", skill="science")
        specialty2 = Specialty.objects.create(name="Physics", skill="science")
        self.assertTrue(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertFalse(self.character.add_specialty(specialty))
        self.assertEqual(self.character.specialties.count(), 1)
        self.assertTrue(self.character.add_specialty(specialty2))
        self.assertEqual(self.character.specialties.count(), 2)

    def test_filter_specialties(self):
        specialty = Specialty.objects.create(name="Biology", skill="science")
        Specialty.objects.create(name="Physics", skill="science")
        Specialty.objects.create(name="Dogs", skill="animal_ken")
        Specialty.objects.create(name="Guns", skill="firearms")
        self.character.add_specialty(specialty)
        self.assertEqual(len(self.character.filter_specialties()), 3)
        self.assertEqual(len(self.character.filter_specialties(skill="firearms")), 1)

    def test_has_specialties(self):
        self.fail()

    def test_add_attribute(self):
        self.character.might = 1
        self.assertTrue(self.character.add_attribute("might"))
        self.assertEqual(self.character.might, 2)
        self.character.might = 5
        self.assertFalse(self.character.add_attribute("might", maximum=5))
        self.assertEqual(self.character.might, 5)
        self.assertTrue(self.character.add_attribute("might", maximum=6))
        self.assertEqual(self.character.might, 6)

    def test_filter_attributes(self):
        self.character.might = 5
        self.assertEqual(
            self.character.filter_attributes(maximum=4),
            {
                "dexterity": 1,
                "stamina": 1,
                "intellect": 1,
                "cunning": 1,
                "resolve": 1,
                "presence": 1,
                "manipulation": 1,
                "composure": 1,
            },
        )
        self.assertEqual(
            self.character.filter_attributes(maximum=5),
            {
                "might": 5,
                "dexterity": 1,
                "stamina": 1,
                "intellect": 1,
                "cunning": 1,
                "resolve": 1,
                "presence": 1,
                "manipulation": 1,
                "composure": 1,
            },
        )
        self.character.might = 4
        self.assertEqual(self.character.filter_attributes(minimum=3), {"might": 4})
        self.assertEqual(
            self.character.filter_attributes(minimum=3, maximum=5), {"might": 4}
        )
        self.assertEqual(self.character.filter_attributes(minimum=5, maximum=6), {})

    def test_has_attributes(self):
        self.assertFalse(self.character.has_attributes())
        self.set_sttributes()
        self.assertTrue(self.character.has_attributes())

    def test_apply_human_template(self):
        self.fail()

    def test_assign_advantages(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()

    def test_get_absolute_url(self):
        self.fail()


class TestRandomHuman(TestCase):
    def test_random_basics(self):
        self.fail()

    def test_random_paths(self):
        self.fail()

    def test_random_skills(self):
        self.fail()

    def test_random_tricks(self):
        self.fail()

    def test_random_specialties(self):
        self.fail()

    def test_random_attributes(self):
        self.fail()

    def test_random_template_choices(self):
        self.fail()

    def test_random_xp_spend(self):
        self.fail()

    def test_random(self):
        self.fail()


class TestHumanDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.character = Human.objects.create(
            name="Test Character",
            player=User.objects.get(username="Test User").tc_profile,
        )

    def test_mortal_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mortal_detail_view_template(self):
        response = self.client.get(f"/tc/characters/{self.character.id}/")
        self.assertTemplateUsed(response, "tc/characters/human/detail.html")


class CharacterDetailView(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.human = Human.objects.create(
            name="Test Human", player=User.objects.get(username="Test User").tc_profile,
        )
        self.talent = Talent.objects.create(
            name="Test Talent",
            player=User.objects.get(username="Test User").tc_profile,
        )
        self.aberrant = Aberrant.objects.create(
            name="Test Aberrant",
            player=User.objects.get(username="Test User").tc_profile,
        )

    def test_character_detail_view_status_code(self):
        response = self.client.get(f"/tc/characters/{self.human.id}/")
        response = self.client.get(f"/tc/characters/{self.talent.id}/")
        response = self.client.get(f"/tc/characters/{self.aberrant.id}/")
        self.assertEqual(response.status_code, 200)

    def test_character_detail_view_templates(self):
        response = self.client.get(f"/tc/characters/{self.human.id}/")
        self.assertTemplateUsed(response, "cod/characters/human/detail.html")
        response = self.client.get(f"/tc/characters/{self.talent.id}/")
        self.assertTemplateUsed(response, "cod/characters/talent/detail.html")
        response = self.client.get(f"/tc/characters/{self.aberrant.id}/")
        self.assertTemplateUsed(response, "cod/characters/aberrant/detail.html")


class TestIndexView(TestCase):
    def setUp(self) -> None:
        for i in range(5):
            User.objects.create_user(username=f"Player {i}")

    def test_index_status_code(self):
        response = self.client.get("/tc/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/tc/characters/")
        self.assertTemplateUsed(response, "tc/characters/index.html")

    def test_index_post(self):
        for i in range(5):
            player = User.objects.get(username=f"Player {i}")
            for j in range(3):
                Human.objects.create(
                    name=f"Human {5*j+i}",
                    player=player.tc_profile,
                    status=Human.status_keys[i],
                )
                Talent.objects.create(
                    name=f"Talent {5*j+i}",
                    player=player.tc_profile,
                    status=Talent.status_keys[i],
                )
                Aberrant.objects.create(
                    name=f"Aberrant {5*j+i}",
                    player=player.tc_profile,
                    status=Aberrant.status_keys[i],
                )
        response = self.client.post("/tc/characters/")
        for i in range(15):
            self.assertContains(response, f"Human {i}")
            self.assertContains(response, f"Talent {i}")
            self.assertContains(response, f"Aberrant {i}")
        for i in range(5):
            self.assertContains(response, f"Player {i}")
        for status in Human.statuses:
            self.assertContains(response, status)
