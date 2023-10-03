from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# Test Case-1 : Whether the URL/webpage is working correctly or not
class Suman:
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def login(self):
        self.driver.get(self.url)

url = "https://www.guvi.in"

Suman(url).login()

