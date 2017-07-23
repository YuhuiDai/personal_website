from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import httplib
import unittest

class TestLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/daiyuhui/Desktop/PortfolioTemplate/test/chromedriver")
        self.driver.get("http://localhost:8000/views/landingPage.html")

    def test_title(self):
        self.assertTrue("Landing Page" in self.driver.title)

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

    def test_hover_animation_coding(self):
        hoverLink = self.driver.find_element_by_link_text("coding")
        ActionChains(self.driver).move_to_element(hoverLink).perform()
        canvas = self.driver.find_element_by_id("myCanvas")
        visibility = canvas.value_of_css_property("visibility")
        # print visibility
        self.assertFalse("hidden" in visibility)

    def test_hover_animation_dataVisualization(self):
        hoverLink = self.driver.find_element_by_link_text("data visualization")
        ActionChains(self.driver).move_to_element(hoverLink).perform()
        bubbles = self.driver.find_element_by_id("bubbles")
        visibility = bubbles.value_of_css_property("visibility")
        # print visibility
        self.assertFalse("hidden" in visibility)

    def test_hover_animation_dataVisualization_after_coding(self):
        hoverLink1 = self.driver.find_element_by_link_text("coding")
        ActionChains(self.driver).move_to_element(hoverLink1).perform()
        hoverLink2 = self.driver.find_element_by_link_text("data visualization")
        ActionChains(self.driver).move_to_element(hoverLink2).perform()
        bubbles = self.driver.find_element_by_id("bubbles")
        visibility_data = bubbles.value_of_css_property("visibility")
        self.assertFalse("hidden" in visibility_data)

        canvas = self.driver.find_element_by_id("myCanvas")
        visibility_coding = canvas.value_of_css_property("visibility")
        self.assertFalse("visible" in visibility_coding)
    
    def test_hover_animation_coding_after_dataVisualization(self):
        hoverLink1 = self.driver.find_element_by_link_text("data visualization")
        ActionChains(self.driver).move_to_element(hoverLink1).perform()
        hoverLink2 = self.driver.find_element_by_link_text("coding")
        ActionChains(self.driver).move_to_element(hoverLink2).perform()
        bubbles = self.driver.find_element_by_id("bubbles")
        visibility_data = bubbles.value_of_css_property("visibility")
        self.assertFalse("visible" in visibility_data)

        canvas = self.driver.find_element_by_id("myCanvas")
        visibility_coding = canvas.value_of_css_property("visibility")
        self.assertFalse("hidden" in visibility_coding)

    def tearDown(self):
        self.driver.close();

if __name__ == '__main__':

    unittest.main()
