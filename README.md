#PortfolioTemplate

The objective of this project is to create an aesthetically pleasing portfolio website template for people interested in product (software/hardware/graphic) design. The template should be easily modifiable with extensive commenting and well-named variables.

##Unit test notes:

###Steps to test locally:

1. If you have not download chromedriver, you need that to facilitate test-run.

2. change the setUp(self) function. Specifically:
        self.driver = webdriver.Chrome("/Users/YOUR_DIRECTORY_TO_CHROMEDRIVER")
      
3. Open your simple local host via python, and add the url to:
		self.driver.get(URL)

4. run the test :)

##How to make this code your code?

###Changes
1. Change HTML text field to adjust to your needs
2. If you have more than two characteristics/areas of expertise that you want to display on your introduction page. You can add another div, and format it as the two examples: coding, data visualization;
You can also add your own animation for the code.
3. To change the skill sets. You need to change the object, data.item, in the ../public/js/bubble/index.js. Specifically, change the text to your desired skill set. You can also change the description attribute to include some relevant work title using that skill. The category attribute needs to be a number. For instance, we can denote all the fron-end language skills to 2; all the back-end to 1.
4. When creating a new project portfolio. You need to specify which category your project fit into with respect to the areas of expertise that have been mentioned in the landing page. For instance, if a project demonstrate your "data visualization" ability, you should create a project in the same way that the template provide you and specify the class to "dataVisualization."
