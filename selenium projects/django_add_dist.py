from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

# Enable cookies and navigate to the login page
driver.get("http://127.0.0.1:8000/admin/login/")

# Find and fill in the username and password fields
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("priyansudey215@gmail.com")
password.send_keys("Levi@1017")

# Submit the login form
login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
login_button.click()

# Wait for the admin index page to be displayed
WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/admin/shipper_distribution/distributordetails/"]'))
)

# Navigate to the add page
driver.get("http://127.0.0.1:8000/admin/shipper_distribution/distributordetails/add/")

# Wait for the add form page to be displayed
WebDriverWait(driver, 1000).until(
    # EC.presence_of_element_located((By.ID, 'id')), # Replace 'id_field_name1' with the actual ID of the first field
    EC.presence_of_element_located((By.ID, 'distributordetails_form')) 
)

# Fill in the form fields
id = driver.find_element(By.ID, "id_id")
distributor_name = driver.find_element(By.ID, "id_distributor_name")
# Continue for other fields...

id.send_keys("306")
distributor_name.send_keys("Madara Uchiha")
# Continue for other fields...

# Submit the form
save_button = driver.find_element(By.NAME, "_save")
save_button.click()

# Wait to ensure the form is submitted and processed
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "success"))
)

input("Press Enter to close the browser...")
# Close the WebDriver
driver.quit()
