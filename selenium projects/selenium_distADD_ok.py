import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

excel_file = 'test3exe.xlsx'  
data = pd.read_excel(excel_file)

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/admin/login/")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("priyansudey215@gmail.com")
password.send_keys("Levi@1017")

login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
login_button.click()

WebDriverWait(driver, 10).until(#check point
    EC.presence_of_element_located((By.XPATH, '//a[@href="/admin/shipper_distribution/distributordetails/"]'))
)

for index, row in data.iterrows():
    driver.get("http://127.0.0.1:8000/admin/shipper_distribution/distributordetails/add/")

    WebDriverWait(driver, 10).until(#check point
        EC.presence_of_element_located((By.ID, 'distributordetails_form'))
    )

    id_field = driver.find_element(By.ID, "id_id")
    distributor_name = driver.find_element(By.ID, "id_distributor_name")
   

    id_field.send_keys(str(row[0]))  
    distributor_name.send_keys(row[1])


    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()

    # Wait to ensure the form is submitted and processed
    WebDriverWait(driver, 10).until(#check point
        EC.presence_of_element_located((By.CLASS_NAME, "success"))
    )

input("Press Enter to close the browser...")
# Close the WebDriver
driver.quit()
