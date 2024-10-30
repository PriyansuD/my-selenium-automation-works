from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Optionally, install the driver automatically
# service = Service(ChromeDriverManager().install())

# Set up the WebDriver
service = Service('C:/Users/PRIYANSU/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')  # Specify the path to your chromedriver if not in PATH
driver = webdriver.Chrome(service=service)

# Open a website
driver.get('https://www.google.com')

# Perform actions on the website (example: print the title of the page)
print(driver.title)

# Close the browser
# driver.quit()
