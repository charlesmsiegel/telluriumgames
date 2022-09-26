from django.contrib.auth.models import User
from django.test import TestCase

from cod.models.characters.mortal import Mortal
from tc.models.characters.aberrant import Aberrant
from wod.models.characters.mage import Mage
from game.models import Chronicle


# Create your tests here.
class TestSignUpView(TestCase):
    """Class that Tests SignUpView"""

    def test_correct_template(self):
        self.client.get("/accounts/")
        self.assertTemplateUsed("registration/login.html")


class TestProfileView(TestCase):
    """Class that Tests the ProfileView"""

    def setUp(self) -> None:
        chronicle = Chronicle.objects.create(name="Test Chronicle")
        self.user1 = User.objects.create_user(
            "Test User 1", "test@user1.com", "testpass"
        )
        self.user2 = User.objects.create_user(
            "Test User 2", "test@user2.com", "testpass"
        )
        self.storyteller = User.objects.create_user(
            "Test Storyteller", "test@st.com", "testpass"
        )
        chronicle.storytellers.add(self.storyteller)
        self.storyteller.profile.cod_st = True
        self.storyteller.profile.save()
        self.char1 = Mortal.objects.create(name="Test Character 1", owner=self.user1)
        self.char2 = Mortal.objects.create(name="Test Character 2", owner=self.user2, chronicle=chronicle)
        self.char3 = Mage.objects.create(name="Test Character 3", owner=self.user1)
        self.char4 = Mage.objects.create(name="Test Character 4", owner=self.user2)
        self.char5 = Aberrant.objects.create(name="Test Character 5", owner=self.user1)
        self.char6 = Aberrant.objects.create(name="Test Character 6", owner=self.user2)

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

        self.assertContains(response, "Test Character 3")
        self.assertNotContains(response, "Test Character 4")
        self.assertContains(response, f"/wod/characters/{self.char3.id}/")

        self.assertContains(response, "Test Character 5")
        self.assertNotContains(response, "Test Character 6")
        self.assertContains(response, f"/tc/characters/{self.char5.id}/")

    def test_approval_list(self):
        self.client.login(username="Test Storyteller", password="testpass")
        response = self.client.get("/accounts/")
        self.assertContains(response, "Test Character 2")
        self.assertContains(response, "To Approve")
