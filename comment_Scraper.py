from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def check_element_exists(driver):
    try:
        elem = parent_card.find_element_by_link_text("View more comments")
        return elem
    except Exception as e:
        return None


driver = webdriver.Chrome(executable_path="chromedriver.exe")

#Define a wait to be used
wait = WebDriverWait(driver, 10)

#Go to the facebook page
driver.get("https://www.facebook.com/CNC3Television/posts/10158767485687996")
#Get rid of stupid sign-in popup

element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Not Now')))
element.click()
parent_card = driver.find_element_by_id("contentArea")
# Load intial set of comments
parent_card.find_element_by_partial_link_text("Comments").click()
#Select All Comments
sleep(2)
parent_card.find_element_by_link_text("Most Relevant").click()
driver.find_elements_by_class_name("_54ni")[2].click()
js = "var aa=document.getElementById('headerArea');aa.parentNode.removeChild(aa)"
driver.execute_script(js)
sleep(1)
#Keep clicking "View more comments" to load all comments
while check_element_exists(parent_card):
    parent_card.find_element_by_link_text("View more comments").click()
    sleep(3)
comments=[]
elements = parent_card.find_elements_by_tag_name("li")
for element in elements :
    comment_data = {}
    comment_data['text']= element.find_element_by_xpath("//span[@dir]").text
    comment_data['author']= element.find_element_by_xpath("//span[@dir]/preceding-sibling::*").text
    comments.append(comment_data)
print(comments)
#Now scrape all the comments
driver.close()