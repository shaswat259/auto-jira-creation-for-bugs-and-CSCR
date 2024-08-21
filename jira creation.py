from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome() 

# Open a webpage
driver.get("https://pdtzycus.atlassian.net/browse/RM-219100")
driver.maximize_window()
time.sleep(5)

username = "username" #enter your username
password = "password" # enter our password
# Find the element by name and send keys
driver.find_element(By.NAME,"username").click()
driver.find_element(By.NAME,"username").send_keys(username)
driver.find_element(By.ID,"login-submit").click()
time.sleep(5)
driver.find_element(By.NAME,"password").click()
driver.find_element(By.NAME,"password").send_keys(password)

driver.find_element(By.ID,"login-submit").click()
time.sleep(10)
driver.find_element(By.ID,"createGlobalItem").click()
time.sleep(10)
driver.find_element(By.NAME,"summary").click()
driver.find_element(By.NAME,"summary").send_keys('demo cscr')


driver.find_element(By.CSS_SELECTOR,"#customfield_10301-container > div > div > div > div > div.select-customfield_10301__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_10301-field").send_keys("24.06.1.0")
driver.find_element(By.ID,"customfield_10301-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_10128-container > div > div._1bsbuo76._19pknek2._n3td11zn > div > div > div.select-customfield_10128__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_10128-field").send_keys("iSave")
driver.find_element(By.ID,"customfield_10128-field").send_keys(Keys.DOWN)
driver.find_element(By.ID,"customfield_10128-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_27704-field").click()
driver.find_element(By.ID,"customfield_27704-field").send_keys("isave-backend-api")

driver.find_element(By.CSS_SELECTOR,"#customfield_17102-container > div > div > div > div > div.select-customfield_17102__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_17102-field").send_keys("1")
driver.find_element(By.ID,"customfield_17102-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_27705-field").click()
driver.find_element(By.ID,"customfield_27705-field").send_keys("iSave")

driver.find_element(By.CSS_SELECTOR,"#customfield_25945-container > div > div > div > div > div.select-customfield_25945__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_25945-field").send_keys("Weekday")
time.sleep(3)
driver.find_element(By.ID,"customfield_25945-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_25085-container > div > div > div > div > div.select-customfield_25085__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_25085-field").send_keys("Oak")
driver.find_element(By.ID,"customfield_25085-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_25974-container > div > div > div > div > div.select-customfield_25974__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_25974-field").send_keys("P4")
driver.find_element(By.ID,"customfield_25974-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_17117-field").click()
driver.find_element(By.ID,"customfield_17117-field").send_keys("NA")

driver.find_element(By.CSS_SELECTOR,"#customfield_25200-container > div > div._1bsbuo76._19pknek2._n3td11zn > div > div > div.select-customfield_25200__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_25200-field").send_keys("USST")
driver.find_element(By.ID,"customfield_25200-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_26403-container > div > div > div > div > div.select-customfield_26403__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_26403-field").send_keys("Customer")
driver.find_element(By.ID,"customfield_26403-field").send_keys(Keys.RETURN)


driver.find_element(By.CSS_SELECTOR,"#customfield_25898-field").click()
driver.find_element(By.ID,"customfield_25898-field").send_keys("SANITY")


driver.find_element(By.CSS_SELECTOR,"#customfield_25899-field").click()
driver.find_element(By.ID,"customfield_25899-field").send_keys("tenant id")

driver.find_element(By.CSS_SELECTOR,"#customfield_25681-field").click()
driver.find_element(By.ID,"customfield_25681-field").send_keys("nexus url")

driver.find_element(By.CSS_SELECTOR,"#customfield_25901-field").click()
driver.find_element(By.ID,"customfield_25901-field").send_keys("NA")

driver.find_element(By.CSS_SELECTOR,"#customfield_25902-container > div > div > div > div > div.select-customfield_25902__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_25902-field").send_keys("NA")
driver.find_element(By.ID,"customfield_25902-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_17105-container > div > div > div > div > div.select-customfield_17105__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_17105-field").send_keys("NO")
driver.find_element(By.ID,"customfield_17105-field").send_keys(Keys.RETURN)


driver.find_element(By.CSS_SELECTOR,"#customfield_25873-container > div > div > div > div > div.select-customfield_25873__indicators.css-2egbai").click()
driver.find_element(By.ID,"customfield_25873-field").send_keys("NO")
driver.find_element(By.ID,"customfield_25873-field").send_keys(Keys.RETURN)

driver.find_element(By.CSS_SELECTOR,"#customfield_25917-container > div > div._1bsbuo76._19pknek2._n3td11zn > div > div > div.fabric-user-picker__value-container.css-17gq658").click()
driver.find_element(By.ID,"customfield_25917-field").send_keys("shaswat srivastava")
time.sleep(3)
driver.find_element(By.ID,"customfield_25917-field").send_keys(Keys.RETURN)


driver.find_element(By.CSS_SELECTOR,"#customfield_25187-container > div > div > div > div > div > div.css-101nbls > span").click()
driver.find_element(By.ID,"customfield_25187-field").send_keys("8/18/2024")
driver.find_element(By.ID,"customfield_25187-field").send_keys(Keys.RETURN)


driver.find_element(By.CSS_SELECTOR,"#customfield_26436-field").click()
driver.find_element(By.ID,"customfield_26436-field").send_keys("NA")

driver.find_element(By.CSS_SELECTOR,"#customfield_26437-field").click()
driver.find_element(By.ID,"customfield_26437-field").send_keys("NA")

driver.find_element(By.CSS_SELECTOR,"#customfield_26438-field").click()
driver.find_element(By.ID,"customfield_26438-field").send_keys("NA")

driver.find_element(By.CSS_SELECTOR,"#customfield_13601-field").click()
driver.find_element(By.ID,"customfield_13601-field").send_keys("SANITY")

driver.find_element(By.CSS_SELECTOR,"#customfield_27816-field").click()
driver.find_element(By.ID,"customfield_27816-field").send_keys("setup_1")






time.sleep(15)



