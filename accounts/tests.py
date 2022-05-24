from django.contrib.auth.models import User
from django.test import TestCase

from cod.models.characters.mortal import Mortal


# Create your tests here.
class TestSignUpView(TestCase):
    """Class that Tests SignUpView"""

    def test_correct_template(self):
        self.client.get("/accounts/")
        self.assertTemplateUsed("registration/login.html")


class TestProfileView(TestCase):
    """Class that Tests the ProfileView"""

    def setUp(self) -> None:
        self.user1 = User.objects.create_user(
            "Test User 1", "test@user1.com", "testpass"
        )
        self.user2 = User.objects.create_user(
            "Test User 2", "test@user2.com", "testpass"
        )
        self.storyteller = User.objects.create_user(
            "Test Storyteller", "test@st.com", "testpass"
        )
        self.storyteller.cod_profile.storyteller = True
        self.storyteller.cod_profile.save()
        self.char1 = Mortal.objects.create(
            name="Test Character 1", player=self.user1.cod_profile
        )
        self.char2 = Mortal.objects.create(
            name="Test Character 2", player=self.user2.cod_profile
        )

    def test_template_logged_out(self):
        response = self.client.get("/accounts/", follow=True)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_template_logged_in(self):
        self.client.login(username="Test User 1", password="testpass")
        response = self.client.get("/accounts/")
        self.assertTemplateUsed(response, "accounts/index.html")

    def test_character_list(self):
        self.client.login(username="Test User 1", password="testpass")
        response = self.client.get("/accounts/")
        self.assertTemplateUsed(response, "accounts/index.html")
        # Check that character appears on user page
        self.assertContains(response, "Test Character 1")
        self.assertNotContains(response, "Test Character 2")
        self.assertContains(response, f"/cod/characters/{self.char1.id}/")

    def test_approval_list(self):
        self.client.login(username="Test Storyteller", password="testpass")
        response = self.client.get("/accounts/")
        self.assertContains(response, "Test Character 2")
        self.assertContains(response, "To Approve")

    # def test_temporary_trait_tracking(self):
    #     self.fail()

    # def test_only_see_correct_scenes(self):
    #     self.fail()

    # def test_only_st_and_player_sees_xp_request(self):
    #     self.fail()
