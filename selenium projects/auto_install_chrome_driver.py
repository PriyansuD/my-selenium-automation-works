from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Automatically install the driver
service = Service(ChromeDriverManager().install())

# Set up the WebDriver
driver = webdriver.Chrome(service=service)

# Open a website
driver.get('http://127.0.0.1:8000/admin/shipper_distribution/distributordetails/add/')
print(driver.title)

input("Press Enter to close the browser...")

driver.quit()
