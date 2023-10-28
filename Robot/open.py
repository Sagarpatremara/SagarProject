# Python program to demonstrate
# selenium
#hello
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
# create webdriver object
driver = webdriver.Chrome()
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# get element
element = driver.find_element(By.ID, "gcse-search-input")
 
# send keys
element.send_keys("Arrays")