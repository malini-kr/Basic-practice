from selenium.webdriver import Chrome
from time import sleep
driver = Chrome()
driver.maximize_window()

driver.get("https://www.w3schools.com/")
sleep(5)
a=driver.find_elements("tag name", "h1")
print(len(a))
for i in a:
    print(i.text)