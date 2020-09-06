import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Creds
URL = "http://ec2-3-128-160-151.us-east-2.compute.amazonaws.com/"

# Registration Details
FirstName = "Test"
LastName = "Account"
Email = "test@gmail.com"
UserName = "test"
Password = "password@123"


# LOCATORS
email_id = "username"
pwd_id = "passwrod"
loginBtn_xpath = "//button[contains(text(), 'Login')]"
registerLink_xpath = "//a[contains(text(), 'Register Yourself')]"
logoutLink_xpath = "//a[@href='/logout']"
welcomeMsg_xpath = "//h1[contains(text(), 'Welcome test')]"

search_xpath = "//input[@name = 'query']"
searchBtn_xpath = "//button[ contains(text(),'Search')]"


# TEST DATA
firstName_id = "fname"
lastName_id = "lname"
emailReg_id = "email"
username_id = "username"
password_id = "passwrod"
registerBtn_xpath = "//button[contains(text(), 'Submit')]"
successMsg_xpath = "//strong[contains(text(), 'Registration Successful , Login Now')]"

@pytest.fixture(scope="function")
def env_setup(request):
    chromeDriver = webdriver.Chrome(
        executable_path=r"C:\Users\spatil\PycharmProjects\AWSautomate\driver\chromedriver.exe")
    request.cls.driver = chromeDriver
    yield
    chromeDriver.close()


@pytest.mark.usefixtures("env_setup")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_registration(self):
        self.driver.get(URL)
        self.driver.find_element_by_xpath(registerLink_xpath).click()
        time.sleep(3)
        # self.driver.find_element_by_id(firstName_id).send_keys(FirstName)
        # self.driver.find_element_by_id(lastName_id).send_keys(LastName)
        # self.driver.find_element_by_id(emailReg_id).send_keys(Email)
        # self.driver.find_element_by_id(username_id).send_keys(UserName)
        # self.driver.find_element_by_id(password_id).send_keys(Password)
        # self.driver.find_element_by_xpath(registerBtn_xpath).click()

        # Test Code
        self.driver.find_element_by_id(firstName_id).send_keys('Test1')
        self.driver.find_element_by_id(lastName_id).send_keys('Account1')
        self.driver.find_element_by_id(emailReg_id).send_keys('test1@gmail.com')
        self.driver.find_element_by_id(username_id).send_keys('test1')
        self.driver.find_element_by_id(password_id).send_keys('password1')
        self.driver.find_element_by_xpath(registerBtn_xpath).click()

        time.sleep(3)
        actual_val = self.driver.find_element_by_xpath(successMsg_xpath).text
        if actual_val != "Registration Successful , Login Now":
            pytest.fail("Registration success message not displayed")


    def test_login(self):
        self.driver.get(URL)
        self.driver.find_element_by_id(email_id).send_keys(UserName)
        self.driver.find_element_by_id(pwd_id).send_keys(Password)
        self.driver.find_element_by_xpath(loginBtn_xpath).click()
        time.sleep(3)
        actual_welcomeMsg = self.driver.find_element_by_xpath(welcomeMsg_xpath).text
        if actual_welcomeMsg != "Welcome test":
            pytest.fail("Login was not successful")
        self.driver.find_element_by_xpath(logoutLink_xpath).click()
        time.sleep(3)


    def test_search(self):
        self.driver.get(URL)
        self.driver.find_element_by_id(email_id).send_keys(UserName)
        self.driver.find_element_by_id(pwd_id).send_keys(Password)
        self.driver.find_element_by_xpath(loginBtn_xpath).click()
        time.sleep(3)
        actual_welcomeMsg = self.driver.find_element_by_xpath(welcomeMsg_xpath).text
        if actual_welcomeMsg != "Welcome test":
            pytest.fail("Login was not successful")
        self.driver.find_element_by_xpath(search_xpath).send_keys("Earth")
        self.driver.find_element_by_xpath(searchBtn_xpath).click()
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, searchBtn_xpath)))
        if not element:
            pytest.fail("Searched")
        self.driver.find_element_by_xpath(logoutLink_xpath).click()
        time.sleep(3)