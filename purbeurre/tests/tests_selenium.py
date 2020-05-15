# coding: utf-8
"""[summary]Fonctionals tests on the Heroku platform for
nutella_project.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from ..config import TESTS


class TestUserTakesTheTest(LiveServerTestCase):
    """Class LiveServerTestCase for tests functions.
    Functions:
    -setUp(self)
    -tearDown(self)
    -test_user_unlog(self)
    -test_user_add_product(self)
    -test_user_log(self)

    """
    def setUp(self):
        """Create self objects for running tests
        """
        self.driver = webdriver.Firefox()

    def tearDown(self):
        """delete self objects after the running tests
        """
        self.driver.quit()

    def test_user_unlog(self):
        """[summary]Tests the user's route starting with
        the index page, the a research on an substitute and
        a click for more information on the result.
        The user then go to the account_creation page and quit.
        """
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS['UrlApp'])
        driver.find_element(
            By.NAME, "item_name").send_keys("cassoulet" + Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.ID, "resultBox")))
        first_url = driver.current_url
        driver.find_element_by_class_name('itemResult').click()
        wait.until(EC.presence_of_element_located((By.ID, "itemBox")))
        second_url = driver.current_url
        driver.find_element(By.ID, "create").click()
        WebDriverWait(self.driver, 2)
        third_url = driver.current_url
        wait.until(EC.presence_of_element_located((By.ID, "creationBox")))
        driver.find_element(By.ID, "index").click()
        last_url = driver.current_url
        self.assertEqual(TESTS['UrlResult'], first_url)
        self.assertEqual(TESTS['UrlItem'], second_url)
        self.assertEqual(TESTS['UrlCreation'], third_url)
        self.assertEqual(TESTS['UrlApp'], last_url)

    def test_user_add_product(self):
        """[summary]Tests the user's loging route starting with
        the index page, then a loging on the page connexion and
        a click for consulting the page 'myaccount'.
        The user then runs a research and save the result.
        """
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS['UrlApp'])
        wait.until(EC.presence_of_element_located((By.ID, "login")))
        driver.find_element(By.ID, 'login').click()
        wait.until(EC.presence_of_element_located((By.ID, "connectionBox")))
        driver.find_element(By.NAME, "email").send_keys("azerty@gmail.com")
        driver.find_element(
            By.NAME, "password").send_keys("azerty" + Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.ID, "myaccount")))
        first_url = driver.current_url

        driver.find_element(
            By.NAME, "item_name").send_keys("cassoulet" + Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "saveItem")))
        second_url = driver.current_url

        driver.find_element(By.CLASS_NAME, "saveItem").click()
        wait.until(EC.presence_of_element_located((By.ID, "saveBox")))
        third_url = driver.current_url

        driver.find_element(By.ID, "logout").click()
        wait.until(EC.presence_of_element_located((By.ID, "portfolio")))
        forth_url = driver.current_url

        self.assertEqual(TESTS['UrlConnexion'], first_url)
        self.assertEqual(TESTS['UrlResult'], second_url)
        self.assertEqual(TESTS['UrlSave'], third_url)
        self.assertEqual(TESTS['UrlDeconnexion'], forth_url)

    def test_user_log(self):
        """[summary]Tests the user's loging route starting with
        the index page, then a loging on the page connexion and
        and consult one's account and one's history pages.
        """
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get(TESTS['UrlApp'])
        wait.until(EC.presence_of_element_located((By.ID, "login")))
        driver.find_element(By.ID, 'login').click()
        wait.until(EC.presence_of_element_located((By.ID, "connectionBox")))
        first_url = driver.current_url

        driver.find_element(By.NAME, "email").send_keys("azerty@gmail.com")
        driver.find_element(
            By.NAME, "password").send_keys("azerty" + Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.ID, "myaccount")))
        driver.find_element(By.ID, 'myaccount').click()
        wait.until(EC.presence_of_element_located((By.ID, "accountBox")))
        second_url = driver.current_url

        driver.find_element(By.ID, 'historical').click()
        wait.until(EC.presence_of_element_located((By.ID, "historyBox")))
        third_url = driver.current_url

        self.assertEqual(TESTS['UrlConnexion'], first_url)
        self.assertEqual(TESTS['UrlAccount'], second_url)
        self.assertEqual(TESTS['UrlHistory'], third_url)
