from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу http://the-internet.herokuapp.com/inputs
driver.get('http://the-internet.herokuapp.com/inputs')

#Введите в поле текст 1000
search_lokator_place = '[type="number"]'
search_input_place = driver.find_element(By.CSS_SELECTOR, search_lokator_place)
search_input_place.send_keys("1000")

#Очистите это поле (метод clear)
search_input_place.clear()

#введите в это же поле текст SkyPro
search_input_place.send_keys("2000") #поле не принимает буквы SkyPro