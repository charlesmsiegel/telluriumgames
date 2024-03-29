import time
from collections import Counter
from unittest import mock
from unittest.mock import Mock

from django.contrib.auth.models import User
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

from cod.models.characters.mortal import Mortal
from core.models import CharacterModel, filepath
from core.templatetags.dots import dots
from core.utils import wod_dice

# from game.models import Scene, Story

MAX_WAIT = 10
# Create your tests here.
class FunctionalTest(LiveServerTestCase):
    """Base case for Functional Tests"""

    def setUp(self) -> None:
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):  # pragma: no cover
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id("id_character_table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as exception:
                if time.time() - start_time > MAX_WAIT:
                    raise exception
                time.sleep(0.5)

    def clean_url(self, url):
        return url.replace(self.live_server_url + "/", "")


class TestHomeView(TestCase):
    """Manages Tests for the HomeView and Template"""

    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        User.objects.create_superuser("Test Admin", "admin@admin.com", "testadmin")

    def test_home_status_code(self):
        """Tests that the page exists"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        """Tests that the correct template is loaded"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "core/index.html")

    def test_content_null_user(self):
        """Tests what users who are not logged in see on front page"""
        response = self.client.get("/")
        self.assertContains(response, "Tellurium Games")
        self.assertContains(response, "navbar")
        self.assertContains(response, "Log In")
        self.assertContains(response, "Sign Up")

    def test_content_logged_in(self):
        """Tests what logged in users see"""
        self.client.login(username="Test User", password="testpass")
        response = self.client.get("/")
        self.assertContains(response, "Tellurium Games")
        self.assertContains(response, "navbar")
        self.assertContains(response, "Log Out")
        self.assertContains(response, "Account")

    def test_content_staff(self):
        """Tests what admins see"""
        self.client.login(username="Test Admin", password="testadmin")
        response = self.client.get("/")
        self.assertContains(response, "Tellurium Games")
        self.assertContains(response, "navbar")
        self.assertContains(response, "Log Out")
        self.assertContains(response, "Admin")
        self.assertContains(response, "Account")

    def test_includes_patreon(self):
        """Tests site contains link to Patreon"""
        response = self.client.get("/")
        self.assertContains(response, "Patron")
        self.assertContains(response, "https://www.patreon.com/bePatron?u=62722820")

    def test_includes_storytellers_vault(self):
        """Tests site contains Stoyteller's Vault logo"""
        response = self.client.get("/")
        self.assertContains(response, "Storyteller's Vault")
        self.assertContains(response, "stv.png")

    def test_includes_dark_pack(self):
        """Tests site contains Dark Pack Logo"""
        response = self.client.get("/")
        self.assertContains(response, "Dark Pack")
        self.assertContains(response, "dark_pack.png")

    def test_includes_storypath_nexus(self):
        """Tests site contains Storypath Nexus logo"""
        response = self.client.get("/")
        self.assertContains(response, "Storypath Nexus")
        self.assertContains(response, "spn.jpg")


class NewUserTest(FunctionalTest):
    """Test creating a new user with interface"""

    def test_homepage_has_login(self):
        self.browser.get(self.live_server_url)
        links = self.browser.find_elements_by_tag_name("a")
        links = [
            (self.clean_url(link.get_attribute("href")), link.text) for link in links
        ]

        self.assertIn(("accounts/login/", "Log In"), links)
        self.assertIn(("accounts/signup/", "Sign Up"), links)

    def credential_creation_fail(self):
        self.browser.get(self.live_server_url + "/accounts/signup/")
        namebox = self.browser.find_element_by_id("id_username")
        namebox.send_keys("test_user")
        pw1 = self.browser.find_element_by_id("id_password1")
        pw1.send_keys("pw123456")
        pw2 = self.browser.find_element_by_id("id_password2")
        pw2.send_keys("pw123454")
        submit_button = self.browser.find_element_by_id("signup_button")
        submit_button.click()

    def credential_creation_succeed(self, username, password):
        self.browser.get(self.live_server_url + "/accounts/signup/")
        namebox = self.browser.find_element_by_id("id_username")
        namebox.send_keys(username)
        pw1 = self.browser.find_element_by_id("id_password1")
        pw1.send_keys(password)
        pw2 = self.browser.find_element_by_id("id_password2")
        pw2.send_keys(password)
        submit_button = self.browser.find_element_by_id("signup_button")
        submit_button.click()

    def test_create_account(self):
        # User arrives on front page
        self.browser.get(self.live_server_url)

        # User clicks signup
        self.client.get("/accounts/signup/")
        self.assertTemplateUsed(
            self.client.get("/accounts/signup/"), "accounts/signup.html"
        )

        # User creates credentials
        self.credential_creation_fail()

        username = "test_user"
        password = "pw123456"

        self.credential_creation_succeed(username, password)
        self.assertEqual(User.objects.count(), 1)

        # User inputs credentials
        self.browser.get(self.live_server_url + "/accounts/login/")
        namebox = self.browser.find_element_by_id("id_username")
        namebox.send_keys(username)
        pw1 = self.browser.find_element_by_id("id_password")
        pw1.send_keys(password)
        submit_button = self.browser.find_element_by_id("login_button_id")
        submit_button.click()

        # User is forwarded to account page
        # Account page has user name on it
        links = self.browser.find_elements_by_tag_name("a")
        links = [
            (self.clean_url(link.get_attribute("href")), link.text) for link in links
        ]
        self.assertIn("test_user", self.browser.title)


class TestHomepage(FunctionalTest):
    """Test seeing the appropriate content on Homepage"""

    def test_homepage_structure(self):
        self.browser.get(self.live_server_url)

        self.assertIn("Tellurium Games", self.browser.title)

        links = self.browser.find_elements_by_tag_name("a")
        links = [
            (self.clean_url(link.get_attribute("href")), link.text) for link in links
        ]

        self.assertIn(("accounts/login/", "Log In"), links)
        self.assertIn(("accounts/signup/", "Sign Up"), links)


class TestDots(TestCase):
    def test_length(self):
        output_5 = dots(4)
        output_10 = dots(4, maximum=10)
        output_10_2 = dots(6)
        self.assertEqual(len(output_5), 5)
        self.assertEqual(len(output_10), 10)
        self.assertEqual(len(output_10_2), 10)

    def test_correct_ratio(self):
        self.assertEqual(Counter(dots(3))["●"], 3)
        self.assertEqual(Counter(dots(3))["○"], 2)
        self.assertEqual(Counter(dots(3, maximum=10))["●"], 3)
        self.assertEqual(Counter(dots(3, maximum=10))["○"], 7)
        self.assertEqual(Counter(dots(6))["●"], 6)
        self.assertEqual(Counter(dots(6))["○"], 4)


class TestFilePath(TestCase):
    def test_filepath_parsing(self):
        m = Mortal.objects.create(name="Test Mortal from CoD")
        self.assertEqual(
            filepath(m, "test.jpg"),
            "cod/characters/mortal/mortal/test_mortal_from_cod.jpg",
        )


class TestModel(TestCase):
    def setUp(self):
        # Model is abstract, using a descendant class to test methods
        self.model = CharacterModel.objects.create(name="")
        self.user = User.objects.create_user(username="Test User")

    def test_get_gameline(self):
        m = Mortal.objects.create(name="Test Mortal from CoD")
        self.assertEqual(m.get_gameline(), "Chronicles of Darkness")

    def test_has_name(self):
        self.assertFalse(self.model.has_name())
        self.model.set_name("Test")
        self.assertTrue(self.model.has_name())

    def test_set_name(self):
        self.assertFalse(self.model.has_name())
        self.assertTrue(self.model.set_name("Test"))
        self.assertTrue(self.model.has_name())

    def test_has_description(self):
        self.assertFalse(self.model.has_description())
        self.model.set_description("Test")
        self.assertTrue(self.model.has_description())

    def test_set_description(self):
        self.assertFalse(self.model.has_description())
        self.assertTrue(self.model.set_description("Test"))
        self.assertTrue(self.model.has_description())

    def test_has_owner(self):
        self.assertFalse(self.model.has_owner())
        self.model.set_owner(self.user)
        self.assertTrue(self.model.has_owner())

    def test_set_owner(self):
        self.assertFalse(self.model.has_owner())
        self.assertTrue(self.model.set_owner(self.user))
        self.assertTrue(self.model.has_owner())

    def test_update_status(self):
        self.assertEqual(self.model.status, "Un")
        self.assertEqual(self.model.get_status_display(), "Unfinished")
        self.assertTrue(self.model.update_status("App"))
        self.assertEqual(self.model.status, "App")
        self.assertEqual(self.model.get_status_display(), "Approved")

    def test_toggle_display(self):
        self.assertTrue(self.model.display)
        self.assertTrue(self.model.toggle_display())
        self.assertFalse(self.model.display)

    def test_has_source(self):
        self.assertFalse(self.model.has_source())
        self.model.add_source("Test Book", 1)
        self.assertTrue(self.model.has_source())

    def test_add_source(self):
        self.assertFalse(self.model.has_source())
        self.assertTrue(self.model.add_source("Test Book", 1))
        self.assertTrue(self.model.has_source())


class TestWoDDice(TestCase):
    """Manage tests for Diceroller"""

    def test_botch(self):
        mocker = Mock()
        mocker.side_effect = [1, 1, 3, 4, 5]
        with mock.patch("random.randint", mocker):
            _, successes = wod_dice(5)
            self.assertEqual(successes, -2)

    def test_failure_with_1s(self):
        mocker = Mock()
        mocker.side_effect = [1, 1, 7, 4, 5]
        with mock.patch("random.randint", mocker):
            _, successes = wod_dice(5)
            self.assertEqual(successes, 0)

    def test_failure(self):
        mocker = Mock()
        mocker.side_effect = [4, 2, 3, 4, 5]
        with mock.patch("random.randint", mocker):
            _, successes = wod_dice(5)
            self.assertEqual(successes, 0)

    def test_success(self):
        mocker = Mock()
        mocker.side_effect = [6, 7, 3, 4, 5]
        with mock.patch("random.randint", mocker):
            _, successes = wod_dice(5)
            self.assertEqual(successes, 2)

    def test_specialty(self):
        mocker = Mock()
        mocker.side_effect = [10, 10, 3, 6, 5]
        with mock.patch("random.randint", mocker):
            _, successes = wod_dice(5, specialty=True)
            self.assertEqual(successes, 5)

    def test_difficulty(self):
        mocker = Mock()
        mocker.side_effect = [4, 2, 3, 4, 5]
        with mock.patch("random.randint", mocker):
            _, successes = wod_dice(5, difficulty=5)
            self.assertEqual(successes, 1)
