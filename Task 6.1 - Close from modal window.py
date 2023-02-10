from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep 

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу http://the-internet.herokuapp.com/entry_ad
driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(2)

# В модальном окне нажать на кнопку Сlose
search_lokator_close_button = "//body/div/div/div/div/div[3]/p"

search_input_close_button = driver.find_element(By.XPATH, search_lokator_close_button)

search_input_close_button.click()

