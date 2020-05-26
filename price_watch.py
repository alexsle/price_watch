from selenium import webdriver
import re
import ctypes

driver = webdriver.Chrome(executable_path="c:\selenium browser drivers\chromedriver.exe")
driver.implicitly_wait(2)

driver.get("https://store.google.com/us/?hl=en-US&regionRedirect=true")
driver.maximize_window()

#Getting to the phone, capturing the current price as a string
driver.find_element_by_xpath("//*[@id='desktop-products']/button[1]").click()
driver.find_element_by_link_text("Pixel 3a").click()
cost_string = driver.find_element_by_class_name("is-price").text

driver.close()

#Separating a number from a price string
cost_number = re.findall(r'\d+', cost_string)

#Converting the price from list to integer
strings = [str(integer) for integer in cost_number]
a_string = "". join(strings)
cost_integer = int(a_string)

#If the price has changed showing a dialog box with results
if cost_integer < 279:
    ctypes.windll.user32.MessageBoxW(0, "Pixel 3a just went down $" + str(279 - cost_integer) + ". It is " + cost_string + " now!", "Price Change Alert", 1)
if cost_integer > 279:
    ctypes.windll.user32.MessageBoxW(0, "Pixel 3a just went up $" + str(cost_integer - 279) + ". It is " + cost_string + " now.", "Price Change Alert", 1)