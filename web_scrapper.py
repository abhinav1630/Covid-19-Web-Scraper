import total as total
from selenium import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

driver = webdriver.Chrome(executable_path='/Users/abhinavagrawal/Downloads/chromedriver')
driver.get("https://www.covid19india.org/")

timeout = 10

try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME,"level-vaccinated")))
except TimeoutException:
    driver.quit()

# Cases current stats

cases_current_stats = driver.find_element(By.CLASS_NAME,"Level").text
# print(cases_current_stats)
cs_list = cases_current_stats.split("\n")
print(cs_list)

print("Today confirmed:", cs_list[1])
print("Total Confirmed:" , cs_list[2])
print("Total Active:" , cs_list[4])
print("Today recovered:", cs_list[6])
print("Total Recovered:" , cs_list[7])
print("Today deceased:", cs_list[9])
print("Total deceased", cs_list[10])

# tested_current_stats = driver.find_element(By.CLASS_NAME , "header-right")
# print(tested_current_stats.text.split('/n'))
#
# tested_current_stats = driver.find_element(By.CLASS_NAME,"header-left")
# print(tested_current_stats.text.split('/n')[1])

# Vaccination current stats

# vaccination_current_stats = driver.find_element(By.CLASS_NAME,"level-vaccinated")
# vcs = vaccination_current_stats.text.split('/n')[0]
#
# vaccination_alo_prog_bar = driver.find_element(By.CLASS_NAME,"progress-bar")
# vaccination_fv_prog_bar = driver.find_element(By.CLASS_NAME, "label")
#
# fvl = vaccination_fv_prog_bar[1].text
# fvl = fvl.split("(")
# fvl = fvl[1].split(")")
#
# print("Total vaccine doses:" , vcs)
# print("At least 1 dose:", vaccination_alo_prog_bar.text)
# print("Fully Vaccinated", fvl[0])


# path = '/Users/abhinavagrawal/Downloads/chromedriver'
# driver = webdriver.Chrome(path)
# driver.get("https://www.covid19india.org/")
#
# timeout = 10
#
# try:
#     WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME,"level-vaccinated")))
# except TimeoutException:
#     driver.quit()

category_element =driver.find_element(By.CLASS_NAME, "Table").text
# print( category_element)
category_list = category_element.split("\n")
temp = category_list[38]

# print(temp)
up_arrow = chr(8593)
down_arrow = chr(8595)

for x in category_list:
    for y in range(len(x)):
        i = x[y]
        if i==up_arrow:
            category_list.remove(x)
        if i == down_arrow:
            category_list.remove(x)


print(category_list)
print(len(category_list))
total_row = ((len(category_list)-2)/7)
print("total_row :", (len(category_list)-2)/7)

data_for_table= []
i = 2
j = 9
num_row = 0
count = 9
while num_row< total_row:
    temp_list =[]
    while i <j:
        temp_list.append(category_list[i])
        i = i+1
        count = count +1
    data_for_table.append(temp_list)
    j = count
    num_row +=1

print(data_for_table)
column_names = data_for_table[0]

data_for_table.pop(0)
print("new data", data_for_table)

df = pd.DataFrame(data_for_table, columns=column_names)

print(df)

df.to_csv("covid_web_scrapping_data.csv")


