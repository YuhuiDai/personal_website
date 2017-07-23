from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import httplib
import unittest

class TestDescriptionPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/views/portfolioDescriptionPage.html")

    def test_title(self):
        self.assertTrue("Portfolio Description Page" in self.driver.title)

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
        self.assertFalse(text in bodyText);

    def test_contact_lnk(self):
        portfolioLink = self.driver.find_element_by_link_text("Contact")
        link = str(portfolioLink.get_attribute("href"))
        # print(link)
        ActionChains(self.driver).move_to_element(portfolioLink).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText);

    def test_about_me_lnk(self):
        portfolioLink = self.driver.find_element_by_link_text("About Me")
        link = str(portfolioLink.get_attribute("href"))
        # print(link)
        ActionChains(self.driver).move_to_element(portfolioLink).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText);

    def test_related_work_1(self):
        portfolioLink = self.driver.find_elements_by_css_selector(".row.relatedWork .col-md-4")
        # link = str(portfolioLink.get_attribute("href"))
        print(link[0])
        ActionChains(self.driver).move_to_element(portfolioLink[0]).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText);

    def test_related_work_2(self):
        portfolioLink = self.driver.find_elements_by_css_selector(".row.relatedWork .col-md-4")
        # link = str(portfolioLink.get_attribute("href"))
        # print(link)
        ActionChains(self.driver).move_to_element(portfolioLink[1]).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText);

    def test_related_work_3(self):
        portfolioLink = self.driver.find_elements_by_css_selector(".row.relatedWork .col-md-4")
        # link = str(portfolioLink.get_attribute("href"))
        # print(link)
        ActionChains(self.driver).move_to_element(portfolioLink[2]).click().perform()
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertFalse(text in bodyText);

    def tearDown(self):
        self.driver.close();

if __name__ == '__main__':

    unittest.main()
