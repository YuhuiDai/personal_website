from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import httplib
import unittest
import time

class TestPortfolioPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/views/portfolioPage.html")

    def test_title(self):
        self.assertTrue("Portfolio Page" in self.driver.title)

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

    def test_portfolio_description_links(self):
        allLinkValid = True
        portfolioDescriptionLinks = self.driver.find_elements_by_css_selector('div.portfolioDeck a')
        for i in range(0,len(portfolioDescriptionLinks)):
            ActionChains(self.driver).move_to_element(portfolioDescriptionLinks[i]).click().perform()
            self.driver.back();
            portfolioDescriptionLinks = self.driver.find_elements_by_css_selector('div.portfolioDeck a')
            text = "Error code 404"
            bodyText = self.driver.find_element_by_tag_name("body").text
            if text in bodyText:
                allLinkValid = False;
            # print bodyText
        text = "Error code 404"
        bodyText = self.driver.find_element_by_tag_name("body").text
        self.assertTrue(allLinkValid)

    def test_tab_coding(self):
        notHiding = False;
        hoverLink = self.driver.find_element_by_id("codeTab")
        # print hoverLink.get_attribute("class")
        ActionChains(self.driver).move_to_element(hoverLink).click().perform()
        # time.sleep(10)
        cards = self.driver.find_elements_by_class_name("portfolioDeck")
        for i in range(0,len(cards)):
            classList = cards[i].get_attribute("class")
            if ("dataVisualization" in classList) and not("hide" in classList):
                notHiding = True
            # print classList
        self.assertFalse(notHiding)

    def test_tab_data_visualization(self):
        notHiding = False
        hoverLink = self.driver.find_element_by_id("dataVisualizationTab")
        # print hoverLink.get_attribute("class")
        ActionChains(self.driver).move_to_element(hoverLink).click().perform()
        # time.sleep(10)
        cards = self.driver.find_elements_by_class_name("portfolioDeck")
        for i in range(0,len(cards)):
            classList = cards[i].get_attribute("class")
            if ("code" in classList) and (not("hide" in classList)):
                notHiding = True
            # print classList
        self.assertFalse(notHiding)

    def test_tab_data_visualization(self):
        hidding = False
        hoverLink = self.driver.find_element_by_id("allTab")
        # print hoverLink.get_attribute("class")
        ActionChains(self.driver).move_to_element(hoverLink).click().perform()
        # time.sleep(10)
        cards = self.driver.find_elements_by_class_name("portfolioDeck")
        for i in range(0,len(cards)):
            classList = cards[i].get_attribute("class")
            if ("hide" in classList):
                hidding = True
            # print classList
        self.assertFalse(hidding)


    def tearDown(self):
        self.driver.close();

if __name__ == '__main__':

    unittest.main()
