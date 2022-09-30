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

PATH = "/home/blaise/Downloads/chromeDriver/chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.tiktok.com/")

search = driver.find_elements(By.TAG_NAME, 'strong')

for i in search:
    print(i.text)


