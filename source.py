from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# WebScraper class is created for better organization
class WebScraper:
    
    # __init__ is defined in case it needs to be used in later versions
    def __init__(self): 
        pass

    # Function that obtains the links from the google scholar pages
    def getLinks(self, searchTerm, numberOfPages):
        
        # webdriver object is initialized
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://scholar.google.com/")

        # Search is set to the search bar on the google scholar page
        search = driver.find_element(By.ID, 'gs_hdr_tsi')
        
        search.send_keys(searchTerm)
        search.send_keys(Keys.RETURN)

        # This variable is used to navigate through different pages
        count = 1

        listOfLinks = []

        # For loop iterates through number of pages that user desires
        for page in range(0, numberOfPages):
            
            try:
                
                # This statement makes sure that the page has loaded before it is searched
                mainPage = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'gs_top'))
                )

                # The html code is obtained
                pageToBeSearched = driver.page_source

                # For loop iterates through the html code to look for links
                for i in range(0, len(pageToBeSearched)):

                    if (pageToBeSearched[i:i+11] == 'href="https'):
                        
                        iterator = i+6

                        currentString = ""

                        while (pageToBeSearched[iterator] != '"'):

                            currentString += pageToBeSearched[iterator]
                            iterator += 1

                        listOfLinks.append(currentString)

            except:
                print("An Error Occurred Loading Website!")
                driver.quit()

            count += 1

            # The next page is obtained through seleniums click functionality and the count variable
            nextPage = driver.find_element(By.LINK_TEXT, str(count))
            nextPage.click()


        driver.quit()

        return listOfLinks



# Test code that can be uncommented to test program
"""

testObject = WebScraper()

listOfLinks = testObject.getLinks("astronomy", 2)

for i in listOfLinks:
    print(i)

"""

