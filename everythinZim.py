import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# initialize webdriver
service_obj = Service("/Users/TendayiKunaka/Documents/geckodriver")
driver = webdriver.Firefox(service=service_obj)

# open url & maximize window
driver.get("https://everythingzimbabwean.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
time.sleep(2)

# search for a smart-watch
search = driver.find_element(By.XPATH, "//input[@class='search-field']")
search.click()
# search.send_keys("iphone")
search.send_keys("Bluetooth Smart Watch")
time.sleep(2)
click_search = driver.find_element(By.XPATH, "//button[@name='search-products']")
click_search.click()
time.sleep(3)

#view = driver.find_element(By.XPATH, "//li[10]//a[1]//div[1]//img[1]")
#view.location_once_scrolled_into_view
#time.sleep(2)

# select_phone = driver.find_element(By.XPATH, "//div[normalize-space()='Q18 Bluetooth Smart Watch']")
#select_phone = driver.find_element(By.XPATH, "//div[@class='name'][.='Q18 Bluetooth Smart Watch']")
time.sleep(2)
#select_phone.click()

# view smart-watch images
watch = driver.find_element(By.XPATH, "//img[@class='wp-post-image']")
watch.click()
time.sleep(2)
select_nextpic = driver.find_element(By.XPATH, "//button[@class='pswp__button pswp__button--arrow--right']")
time.sleep(2)
for i in range(0, 2):
    select_nextpic.click()
    time.sleep(2)
driver.save_screenshot("everything#" + str(random.randint(0, 99)) + ".png")
time.sleep(2)
close = driver.find_element(By.XPATH, "//button[@class='pswp__button pswp__button--close']")
close.click()

# select quantity
quantity = driver.find_element(By.ID, "quantity_6369020d445f7")
quantity.click()
quantity.clear()
quantity.send_keys(2)
stock = driver.find_element(By.XPATH, "//div[text()='9 in stock']")
print(stock.text)
time.sleep(2)
add_to_basket = driver.find_element(By.XPATH, "//button[@name='add-to-cart']")
add_to_basket.click()

# add a laptop to cart
search = driver.find_element(By.XPATH, "//input[@class='search-field']")
search.click()
search.send_keys("laptop")
time.sleep(2)

click_search = driver.find_element(By.XPATH, "//button[@name='search-products']")
click_search.click()
time.sleep(3)

hp = driver.find_element(By.XPATH, "//div[normalize-space()='Hp 250 G8 Dual Core Laptop']")
hp.click()
time.sleep(2)
add_to_basket2 = driver.find_element(By.XPATH, "//button[@name='add-to-cart']")
add_to_basket2.click()
time.sleep(2)

# open basket
open_basket = driver.find_element(By.ID, "cart-link")
open_basket.click()
time.sleep(2)

# here u should validate the transactions
# code comes here
# add the totals & assert in tests

# proceed to checkout
view2 = driver.find_element(By.XPATH, "//a[@href='https://everythingzimbabwean.com/checkout/']")
view2.location_once_scrolled_into_view
time.sleep(2)
proceed_checkout = driver.find_element(By.XPATH, "//a[@href='https://everythingzimbabwean.com/checkout/']")
proceed_checkout.click()

# fill in the Billing Information
first_name = driver.find_element(By.ID, "billing_first_name")
first_name.send_keys("Trust")
last_name = driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Livingstone")
email_add = driver.find_element(By.ID, "billing_email")
email_add.send_keys("trust@gmail.com")
phone = driver.find_element(By.ID, "billing_phone")
phone.send_keys("227-555-287")
# assert totals again
# verify that you can view shop details
time.sleep(2)
check_box1 = driver.find_element(By.XPATH, "//input[@id='terms']")
check_box1.click()
check_box2 = driver.find_element(By.XPATH, "//input[@id='automatewoo_optin']")
check_box2.click()
