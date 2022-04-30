import time

from django.contrib.auth.models import User
from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select

MAX_WAIT = 10
# Create your tests here.
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

    def test_create_account(self):
        # User arrives on front page
        self.browser.get(self.live_server_url)

        # User sees login/signup links
        links = self.browser.find_elements_by_tag_name("a")
        links = [
            (self.clean_url(link.get_attribute("href")), link.text) for link in links
        ]

        self.assertIn(("accounts/login/", "Log In"), links)
        self.assertIn(("accounts/signup/", "Sign Up"), links)

        # User clicks signup
        self.client.get("/accounts/signup/")
        self.assertTemplateUsed(
            self.client.get("/accounts/signup/"), "accounts/signup.html"
        )

        # User creates credentials
        #     First attempt at credentials fails
        self.browser.get(self.live_server_url + "/accounts/signup/")
        namebox = self.browser.find_element_by_id("id_username")
        namebox.send_keys("test_user")
        pw1 = self.browser.find_element_by_id("id_password1")
        pw1.send_keys("pw123456")
        pw2 = self.browser.find_element_by_id("id_password2")
        pw2.send_keys("pw123454")
        submit_button = self.browser.find_element_by_id("signup_button")
        submit_button.click()

        username = "test_user"
        password = "pw123456"

        pw1 = self.browser.find_element_by_id("id_password1")
        pw1.send_keys(password)
        pw2 = self.browser.find_element_by_id("id_password2")
        pw2.send_keys(password)
        submit_button = self.browser.find_element_by_id("signup_button")
        submit_button.click()

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
