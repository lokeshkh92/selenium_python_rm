from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# resource manager ipaddres and port
ipaddress = "10.0.10.36"
rmport = "8088"
# applicationId for which logs to be analyzed
#applicationId = "application_1533123882731_0127"
applicationId = "application_1733123882731_0127"

# launch chrome browser and open resource manager UI
browser = webdriver.Chrome()
browser.get('http://{}:{}/cluster'.format(ipaddress, rmport))
table_id = browser.find_element_by_id("apps")
table_tab = 1

# Function to count row number for the application id
def rownum():
    app_flag = 0
    row_count = 0
    for col in table_id.find_elements(By.CSS_SELECTOR, "td.sorting_1"):
        row_count += 1
        col_value = col.text
        if col_value == applicationId:
            app_flag = 1
            print('Got the applicationId: {}'.format(applicationId))
            print("Hey row {} what's up buddy!!".format(str(row_count - 1)))
            break
    return row_count,app_flag


# Get row number and application found flag status
row_number,app_flag = rownum()

while app_flag == 0:
    table_tab += 1
    tab_path = '//*[@id="apps_paginate"]/span/a[' + str(table_tab) + ']'
    next_table_tab = browser.find_element(By.XPATH, tab_path).click()
    print("Next_table_tab: {}".format(next_table_tab))
    row_number,app_flag = rownum()
    if app_flag == 1:
        break
    if next_table_tab == 'None':
        break
    elif table_tab == 8:
        break

print("application found flag {}".format(app_flag))
print("End of table search")
# create xpath for application id
app_xpath = '//*[@id="apps"]/tbody/tr[' + str(row_number - 1) + ']/td[1]/a'
print(app_xpath)
# perform click action over applicationID to open application history page
click_app = browser.find_element(By.XPATH, app_xpath).click()
print(click_app)

#//*[@id="apps_paginate"]/span/a[2]
#//*[@id="apps_next"]
#//*[@id="apps_paginate"]/a[2]