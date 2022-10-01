# Important Links:
# - https://pandas.pydata.org/docs/user_guide/index.html#user-guide
# - https://docs.python.org/3/library/re.html

"""
from bs4 import BeautifulSoup
import requests

websiteObject = requests.get('https://www.reddit.com/')

if websiteObject.status_code >= 200 and websiteObject.status_code <= 400:
    print("Successful load!")
    print("Status Code: " + str(websiteObject.status_code))

    soup = BeautifulSoup(websiteObject.text, "html.parser")

    listOfElements = ['h1', 'h2', 'h3', 'p', 'h4', 'li']

    for i in listOfElements:
        pTags = soup.find_all(i)

        for x in range(1, len(pTags)):
            print(i + ": " + pTags[x].get_text())
            print("\n")

else:
    print("Connection Failed")
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""

#PATH = "/home/blaise/Downloads/chromeDriver/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.tiktok.com/")
driver.refresh()
driver.refresh()
driver.refresh()

search = driver.find_elements(By.TAG_NAME, 'strong')

time.sleep(10)

for i in search:
    print(i.text)

"""

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.techwithtim.net/")

### This Block of Code finds the search bar and searches for test
"""
search = driver.find_element(By.NAME, 's')
search.send_keys("test")
search.send_keys(Keys.RETURN)
"""
###

#print(driver.page_source) Will return all source code for page

### This block of Code waits until 10 seconds have passed or it detects that it has 
# entered the web page that id: main resides in. It then collects the articles by tag name.
"""
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements(By.TAG_NAME, 'article')

    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        #print(header.text)

finally:
    driver.quit()
"""
###