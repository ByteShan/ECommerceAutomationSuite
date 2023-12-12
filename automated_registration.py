import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def click_element(xpath):
    driver.find_element(By.XPATH, xpath).click()

def enter_text(xpath, text):
    driver.find_element(By.XPATH, xpath).send_keys(text)

def select_option(xpath, option):
    click_element(xpath)
    click_element(f"//option[normalize-space()='{option}']")

def create_account():
    click_element("//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")  # Click on Login/Sign up
    enter_text("//input[@placeholder='Name']", "Shanmugarajan")  # Enter Name
    enter_text("//input[@data-qa='signup-email']", "amulbaby18@gmail.com")  # Enter Email
    click_element("//button[normalize-space()='Signup']")  # Click Signup

def enter_personal_details():
    click_element("//input[@id='id_gender1']")  # Select Title
    enter_text("//input[@id='password']", "9876543210")  # Enter Password
    select_option("//select[@id='days']", "2")  # Select Day
    select_option("//select[@id='months']", "November")  # Select Month
    select_option("//select[@id='years']", "1989")  # Select Year
    click_element("//input[@id='newsletter']")  # Subscribe to newsletter
    enter_text("//input[@id='first_name']", "Shanmugarajan")  # Enter First Name
    enter_text("//input[@id='last_name']", "K")  # Enter Last Name

def enter_address():
    enter_text("//input[@id='address1']", "24, Valluvar Nagar, Perumagalur")
    enter_text("//input[@id='state']", "Tamil Nadu")
    enter_text("//input[@id='city']", "Chennai")
    enter_text("//input[@id='zipcode']", "600 063")
    enter_text("//input[@id='mobile_number']", "7695934823")

def create_account_final():
    click_element("//button[normalize-space()='Create Account']")

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=ops)
driver.get("https://automationexercise.com/")
driver.implicitly_wait(15)
driver.maximize_window()

create_account()
enter_personal_details()
enter_address()
create_account_final()

expected_result = "Automation Exercise - Account Created"
actual_result = driver.title

if expected_result == actual_result:
    print("The Project is Successful")
else:
    print("Try Again!")

time.sleep(5)
print(driver.title)

driver.quit()
