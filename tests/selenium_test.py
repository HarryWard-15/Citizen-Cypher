# Basic import statements to initialise required Selenium packages.

import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class ProjectTest(unittest.TestCase):
    # Initialise flask process and open Chrome (v113) web driver.
    def setUp(self):
        self.flask_process = subprocess.Popen(["flask", "run"])
        time.sleep(2)
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.get("http://127.0.0.1:5000/index")

    def tearDown(self):
        self.driver.quit()
        self.flask_process.terminate()

    # Tests login and signup methods, and ensures that previous game data still exists.
    # After opening browser to index page of local flask environment:
    # 1. Log into Sample user A test account to ensure credentials have been imported and work. Log in should succeed.
    # 2. Log out of Sample user A test account, attempt to sign up for new account using Sample user A credentials. Sign up should fail.
    # 3. Once sign up fails, attempt to sign up for new account using new credentials. Sign up should succeed.
    # 4. Sign into new account. Log in should succeed.
    # 5. Sign out of new account, sign into Sample user A test account again. Check for game history - should succeed if death reason string found.

    def login_gamehistory_test(self):
        login_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'LOG IN')]"
        )
        login_button.click()

        email_input = self.driver.find_element("id", "email")
        password_input = self.driver.find_element("id", "password")

        email = "a@a.a"
        password = "a"

        email_input.send_keys(email)
        password_input.send_keys(password)

        login_screen_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'LOG IN')]"
        )
        login_screen_button.click()

        expected_string = "Thanks for logging in, Sample user A!"

        welcome_string = self.driver.find_element(
            "xpath", "//h2[contains(text(), 'Thanks for logging in, Sample user A!')]"
        ).text

        self.assertEqual(expected_string, welcome_string)

        print("Login was successful! HTML read correctly")

        logout_button = self.driver.find_element(
            "xpath", "//a[contains(text(), 'Not you?')]"
        )
        logout_button.click()

        print("Logout successful")

        signup_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'SIGN UP')]"
        )
        signup_button.click()

        realname_input = self.driver.find_element("id", "realname")
        realname = "Test user C"

        email_input = self.driver.find_element("id", "email")
        password_input = self.driver.find_element("id", "password")

        realname_input.send_keys(realname)
        email_input.send_keys(email)
        password_input.send_keys(password)

        signup_screen_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'SIGN UP')]"
        )
        signup_screen_button.click()

        error_msg = self.driver.find_element("id", "msg").text

        expected_msg = "This email already exists in the database!"

        self.assertEqual(expected_msg, error_msg)

        print("Sign up with existing details failed - successful credential check")

        realname = "Test user d"
        email = "d@d.d"
        password = "d"

        realname_input = self.driver.find_element("id", "realname")
        email_input = self.driver.find_element("id", "email")
        password_input = self.driver.find_element("id", "password")

        realname_input.send_keys(realname)
        email_input.send_keys(email)
        password_input.send_keys(password)

        signup_screen_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'SIGN UP')]"
        )
        signup_screen_button.click()

        print("Sign up with new details successful!")

        print("Logged in with new details successfully!")

        logout_button = self.driver.find_element(
            "xpath", "//a[contains(text(), 'Not you?')]"
        )
        logout_button.click()

        print("Logged out of new user successfully")

        login_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'LOG IN')]"
        )
        login_button.click()

        email_input = self.driver.find_element("id", "email")
        password_input = self.driver.find_element("id", "password")

        email = "a@a.a"
        password = "a"

        email_input.send_keys(email)
        password_input.send_keys(password)

        login_screen_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'LOG IN')]"
        )
        login_screen_button.click()

        print("Signed back into sample user A successfully")

        show_history_button = self.driver.find_element(
            "xpath", "//button[contains(text(), 'SHOW GAME HISTORY')]"
        )
        show_history_button.click()

        reason_string = self.driver.find_element("id", "death_reason").text

        expected_reason = "Death reason: Died because of low Happiness"

        self.assertEqual(reason_string, expected_reason)

        print("Successful game history found!")


if __name__ == "__main__":
    unittest.main()
