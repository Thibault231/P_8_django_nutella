from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import RequestFactory, TestCase, LiveServerTestCase

class TestUserTakesTheTest(LiveServerTestCase):
    # Méthode exécutée avant chaque test
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
    
    def test_user_unlog(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get("https://djangonutella.herokuapp.com/")
        driver.find_element(By.NAME, "item_name").send_keys("cassoulet" + Keys.RETURN)
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
        self.assertEquals("https://djangonutella.herokuapp.com/purbeurre/result/", first_url)
        self.assertEquals("https://djangonutella.herokuapp.com/purbeurre/item/21/", second_url)
        self.assertEquals("https://djangonutella.herokuapp.com/connection/count_creation/", third_url)
        self.assertEquals("https://djangonutella.herokuapp.com/", last_url)
 
    def test_user_add_product(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get("https://djangonutella.herokuapp.com/")
        wait.until(EC.presence_of_element_located((By.ID, "login")))
        driver.find_element(By.ID,'login').click()
        wait.until(EC.presence_of_element_located((By.ID, "connectionBox")))
        driver.find_element(By.NAME, "email").send_keys("azerty@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("azerty" + Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.ID, "myaccount")))
        first_url = driver.current_url
        
        driver.find_element(By.NAME, "item_name").send_keys("cassoulet" + Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "saveItem")))
        second_url = driver.current_url
        
        driver.find_element(By.CLASS_NAME, "saveItem").click()
        wait.until(EC.presence_of_element_located((By.ID, "saveBox")))
        third_url = driver.current_url

        driver.find_element(By.ID, "logout").click()
        wait.until(EC.presence_of_element_located((By.ID, "portfolio")))
        forth_url = driver.current_url

        self.assertEquals("https://djangonutella.herokuapp.com/connection/connexion/", first_url)
        self.assertEquals("https://djangonutella.herokuapp.com/purbeurre/result/", second_url)
        self.assertEquals("https://djangonutella.herokuapp.com/purbeurre/save/21/", third_url)
        self.assertEquals("https://djangonutella.herokuapp.com/connection/deconnexion/", forth_url)
   
    def test_user_log(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get("https://djangonutella.herokuapp.com/")
        wait.until(EC.presence_of_element_located((By.ID, "login")))
        driver.find_element(By.ID,'login').click()
        wait.until(EC.presence_of_element_located((By.ID, "connectionBox")))
        first_url = driver.current_url
        
        driver.find_element(By.NAME, "email").send_keys("azerty@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("azerty" + Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.ID, "myaccount")))
        driver.find_element(By.ID, 'myaccount').click()
        wait.until(EC.presence_of_element_located((By.ID, "accountBox")))
        second_url = driver.current_url

        driver.find_element(By.ID, 'historical').click()
        wait.until(EC.presence_of_element_located((By.ID, "historyBox")))
        third_url = driver.current_url

        self.assertEquals("https://djangonutella.herokuapp.com/connection/connexion/", first_url)
        self.assertEquals("https://djangonutella.herokuapp.com/connection/myaccount/", second_url)
        self.assertEquals("https://djangonutella.herokuapp.com/purbeurre/history/", third_url)
