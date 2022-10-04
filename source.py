from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class webScraper:
    
    def __init__(self):
        pass

    def getLinks(self, searchTerm, numberOfPages):
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://scholar.google.com/")

        search = driver.find_element(By.ID, 'gs_hdr_tsi')
        
        search.send_keys(searchTerm)

        count = 0

        listOfLinks = []

        for page in range(0, numberOfPages):

            try:
                
                mainPage = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'gs_top'))
                )

                pageToBeSearched = driver.page_source

                for i in range(0, len(pageToBeSearched)):

                    if (pageToBeSearched[i:i+11] == 'href="https'):
                        
                        iterator = i+7

                        currentString = ""

                        while (pageToBeSearched[i] != '"'):

                            currentString += pageToBeSearched[i]
                            iterator += 1

                        listOfLinks.append(currentString)

            except:
                print("An Error Occurred Loading Website!")
                driver.quit()

        

        

        driver.quit()

    def obtainDataFromLinks(self, listOfLinks):
        pass




