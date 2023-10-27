import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from symbiot_lib.tool_kits.tool_kit import ToolKit


class GoogleSearcher(ToolKit):

    GET_QUERY_DESCRIPTION = """
    Function search some phrases in google search engine 
    and returns a list of query with a short summary.
    Use this function when you don't have enough information 
    or when your information is outdated.'  
    """

    PHRASE_DESCRIPTION = """
    Topic search phrases in google search engine
    """

    @ToolKit.tool_function(GET_QUERY_DESCRIPTION,
                           parameters=[dict(
                               name="query",
                               type="string",
                               description=PHRASE_DESCRIPTION)])
    def get_query(self, phrase: str):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.google.pl/?hl=pl")

        accept = driver.find_element(By.ID, "L2AGLb")
        accept.click()

        google_search_box = driver.find_element(By.ID, "APjFqb")
        google_search_box.send_keys(phrase)
        google_search_box.send_keys(Keys.ENTER)

        time.sleep(10)
        return driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc")
