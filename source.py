# Important Links:
# - https://pandas.pydata.org/docs/user_guide/index.html#user-guide
# - https://docs.python.org/3/library/re.html

from bs4 import BeautifulSoup
import requests

websiteObject = requests.get('https://www.quora.com/Has-anyone-ever-tried-to-build-a-spaceship-of-their-own')

if websiteObject.status_code >= 200 and websiteObject.status_code <= 400:
    print("Successful load!")
    print("Status Code: " + str(websiteObject.status_code))

    soup = BeautifulSoup(websiteObject.content, "html.parser")

    listOfElements = ['h1', 'h2', 'h3', 'p', 'h4', 'li', 'span']

    for i in listOfElements:
        pTags = soup.find_all(i)

        for x in range(1, len(pTags)):
            print(i + ": " + pTags[x].get_text())
            print("\n\n\n")

else:
    print("Fuck you")