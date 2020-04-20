from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROME_PATH = "./chromedriver.exe"
CHROME_OPTIONS = Options()
BASE_URL = "https://www.thegioididong.com"
TYPES = ["dtdd","laptop",""]
wd = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=CHROME_OPTIONS)

def getProductLinks(internal_url=None):
    if (internal_url==None):
        wd.get(BASE_URL+"")
        # go online to seek for url
        return ["https://www.thegioididong.com/dtdd/xiaomi-redmi-note-9s","https://www.thegioididong.com/dtdd/samsung-galaxy-a51"]
    else:
        # read urls from file 
        pass

def getCommentInfoFromElement(elem):
    # get name

    # get star

    # get comment content
    return 

def getCommentsFromLink(link):
    wd.get(link)
    ratingList = wd.find_element_by_class_name("ratingLst")
    ratings = ratingList.find_elements_by_xpath(".//*")
    print(ratings[0].get_attribute("innerHTML"))

    
    return ""


productLinks = getProductLinks()

for link in productLinks:
    getCommentsFromLink(link)
    body = wd.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
