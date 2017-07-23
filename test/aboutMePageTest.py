from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import httplib
import unittest
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAboutMePage(unittest.TestCase):

    def setUp(self):
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ALL'}
        self.driver = webdriver.Chrome("/Users/daiyuhui/Desktop/PortfolioTemplate/test/chromedriver", desired_capabilities=d)
        self.driver.get("http://localhost:8000/views/aboutMePage.html")

    def test_title(self):
        self.assertTrue("About Me" in self.driver.title)

    def test_author(self):
        # print (self.driver.find_element_by_name("author").get_attribute("content"))
        self.assertTrue("Yuhui Dai" in self.driver.find_element_by_name("author").get_attribute("content"))
        self.assertTrue("Ting-Che Lin" in self.driver.find_element_by_name("author").get_attribute("content"))

    def test_portfolio_lnk(self):
        portfolioLink = self.driver.find_element_by_link_text("Portfolio")
        link = str(portfolioLink.get_attribute("href"))
        # print(link)
        ActionChains(self.driver).move_to_element(portfolioLink).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText)

    def test_contact_lnk(self):
        portfolioLink = self.driver.find_element_by_link_text("Contact")
        link = str(portfolioLink.get_attribute("href"))
        # print(link)
        ActionChains(self.driver).move_to_element(portfolioLink).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText)

    def test_about_me_lnk(self):
        portfolioLink = self.driver.find_element_by_link_text("About Me")
        link = str(portfolioLink.get_attribute("href"))
        # print(link)
        ActionChains(self.driver).move_to_element(portfolioLink).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText)

    def test_centralBubble_animation_initialization(self):
        text = "calling move to central"
        for entry in self.driver.get_log('browser'):
            self.assertTrue(text in entry["message"])


    def test_centralBubble_animation(self):
        centralBubble = self.driver.find_element_by_class_name('active')
        ActionChains(self.driver).move_to_element(centralBubble).click().perform()
        time.sleep(5)
        text = "calling move to reflection"
        string = ""
        for entry in self.driver.get_log('browser'):
            string = string + entry["message"] + " "
        self.assertTrue(text in string)

    def test_smallBubbles_animation(self):
        smallBubbles = self.driver.find_element_by_class_name('node:not(.active)')
        ActionChains(self.driver).move_to_element(smallBubbles).click().perform()
        time.sleep(5)
        text = "calling move to reflection"
        string = ""
        for entry in self.driver.get_log('browser'):
            string = string + entry["message"] + " "
        self.assertTrue(text in string)
  

    def tearDown(self):
        self.driver.close();

if __name__ == '__main__':

    unittest.main()
