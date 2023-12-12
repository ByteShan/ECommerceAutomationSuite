import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome WebDriver with options
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)

# Navigate to the website
driver.get("https://automationexercise.com/")
driver.implicitly_wait(15)
driver.maximize_window()

# Click on Login or Sign up
driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a").click()

# Enter Name and E-Mail Address
driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("Shan")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(f"amulbaby{random.randint(30, 500)}@gmail.com")

# Click on Sign Up Button to Create the account
driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()

# Enter Personal Details
driver.find_element(By.XPATH, "//input[@id='id_gender1']").click()  # Select Title
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("9876543210")  # Enter Password
time.sleep(10)  # Add sleep for better synchronization
driver.find_element(By.XPATH, "//select[@id='days']").click()  # Click on Day
driver.find_element(By.XPATH, "//option[normalize-space()='2']").click()  # Select the Date
driver.find_element(By.XPATH, "//select[@id='months']").click()  # Click on Month
driver.find_element(By.XPATH, "//option[normalize-space()='November']").click()  # Select the Month
driver.find_element(By.XPATH, "//select[@id='years']").click()  # Click on Year
driver.find_element(By.XPATH, "//option[@value='1989']").click()  # Select the Year

driver.find_element(By.XPATH, "//input[@id='newsletter']").click()

driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Shanmugarajan")  # Enter F Name
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("K")  # Enter L Name

# Enter Address
driver.find_element(By.XPATH, "//input[@id='address1']").send_keys("33, Times Square, Guindy")  # Enter Address
driver.find_element(By.XPATH, "//input[@id='state']").send_keys("Tamil Nadu")
driver.find_element(By.XPATH, "//input[@id='city']").send_keys("Chennai")
driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys("600 063")
driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys("9876543210")

# Create account
driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()

# Verify the result
exp_res = "Automation Exercise - Account Created"
act_res = driver.title

if exp_res == act_res:
    print("The Project is Successful")
else:
    print("Try Again!")

# Add a delay for better visibility before quitting the browser
time.sleep(5)
print(driver.title)

# Quit the WebDriver
driver.quit()