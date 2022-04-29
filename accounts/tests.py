from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestSignUpView(TestCase):
    """Class that Tests SignUpView"""

    def test_correct_template(self):
        self.client.get("/accounts/")
        self.assertTemplateUsed("registration/login.html")
