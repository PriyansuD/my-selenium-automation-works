import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

excel_file = 'test_for_oD.xlsx'  
data = pd.read_excel(excel_file)

driver = webdriver.Chrome()

driver.get("http://pipetrackerlive.com/admin/login/?next=/admin/")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("safakat")
password.send_keys("Mozi@2020")

login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
login_button.click()

WebDriverWait(driver, 10).until(#check point
    EC.presence_of_element_located((By.XPATH, '//a[@href="/admin/api/pressuretypespecification/"]'))#/admin/api/standardtypeclassification/
)
WebDriverWait(driver, 10).until(#check point
    EC.presence_of_element_located((By.XPATH, '//a[@href="/admin/api/standardtypeclassification/"]'))#
)

for index, row in data.iterrows():
    driver.get("http://pipetrackerlive.com/admin/api/standardtypeclassification/add/")

    WebDriverWait(driver, 10).until(#check point
        EC.presence_of_element_located((By.ID, 'standardtypeclassification_form'))
    )
    
    select = Select(driver.find_element(By.ID,'id_basic_metarial'))

    # select by visible text
    select.select_by_visible_text('PVC-STANDARD')
    
    id_field = driver.find_element(By.ID, "id_standard_type_classification")
    distributor_name = driver.find_element(By.ID, "id_code")
   

    id_field.send_keys(str(row[0]))  
    distributor_name.send_keys(row[1])


    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()

    # Wait to ensure the form is submitted and processed
    WebDriverWait(driver, 10).until(#check point
        EC.presence_of_element_located((By.CLASS_NAME, "success"))
    )

input("Press Enter to close the browser...")
# # Close the WebDriver
driver.quit()
