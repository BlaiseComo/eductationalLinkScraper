from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://scholar.google.com/")

search = driver.find_element(By.ID, 'gs_hdr_tsi')
search.send_keys("astronomy")
search.send_keys(Keys.RETURN)


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'gs_top'))
    )

    #for i in webpages:
        #print(i.text)

    #11
        
    stringToBeSearched = driver.page_source

    for i in range(0, len(stringToBeSearched)):

        if (stringToBeSearched[i:i+11] == 'href="https'):
            print(stringToBeSearched[i:i+100])



    #webpages = main.find_element(By.TAG_NAME, 'body')

    #webpagesBody = webpages.find_elements(By.ID, 'gs_bdy')

    #for page in webpages:

        #divs = page.find_elements(By.TAG_NAME, 'div')
        #print(len(divs))

        #h3Tag = divs[1].find_element(By.TAG_NAME, 'h3')



    #articles = main.find_elements(By.TAG_NAME, 'a')

    #for article in articles:
        #header = article.find_element(By.TAG_NAME, 'h3')
        #print(header.text)
        
    #for i in main:
        #print(i.text)
    #print(len(main))

finally:
    driver.quit()







