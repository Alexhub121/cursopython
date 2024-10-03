from selenium import webdriver

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.youtube.com/")

driver.close()