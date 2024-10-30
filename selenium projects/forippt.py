import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

excel_file = 'mapping.xlsx'  
data = pd.read_excel(excel_file)

driver = webdriver.Chrome()

driver.get("https://pipetracker.live/admin/login/?next=/admin/")

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

username.send_keys("admin")
password.send_keys("password")

login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
login_button.click()

WebDriverWait(driver, 10).until(#check point
    EC.presence_of_element_located((By.XPATH, '//a[@href="/admin/api/pipeouterdiameter/"]'))#/admin/api/standardtypeclassification/
)
WebDriverWait(driver, 10).until(#check point
    EC.presence_of_element_located((By.XPATH, '//a[@href="/admin/api/pipeouterdiameter/"]'))#
)
i = 1
for index, row in data.iterrows():
    print("sdfgh")
    driver.get("https://pipetracker.live/admin/api/pipeouterdiameter/add/")
    print("here")

    WebDriverWait(driver, 10).until(#check point
        EC.presence_of_element_located((By.ID,'pipeouterdiameter_form'))
    )
    
    # select_stc = Select(driver.find_element(By.ID,'id_standard_type_classification'))

    # select by visible text
    # select_stc.select_by_visible_text(f'P-{5+i}')
    # select_stc.select_by_visible_text(f'P-{5+i}')#changeS
    # i+=1
    
    select_bm = Select(driver.find_element(By.ID,'id_unit'))
    # select by visible text
    
    
    select_stc = driver.find_element(By.ID,'id_standard_type_classification')
    select_bm.select_by_visible_text('mm')#changeS
    pts = driver.find_element(By.ID, "id_outer_diameter")
    code = driver.find_element(By.ID, "id_code")
   
    select_stc.send_keys(str(row[0]))
    print(str(row[0]))
    pts.send_keys(str(row[1]))  
    code.send_keys(str(row[2]))


    save_button = driver.find_element(By.NAME, "_save")
    save_button.click()

    # Wait to ensure the form is submitted and processed
    WebDriverWait(driver, 10).until(#check point
        EC.presence_of_element_located((By.CLASS_NAME, "success"))
    )

input("Press Enter to close the browser...")
# # Close the WebDriver
driver.quit()
