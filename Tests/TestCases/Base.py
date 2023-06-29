import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Tests.Config import main

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()