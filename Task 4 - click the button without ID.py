from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу http://uitestingplayground.com/dynamicid
driver.get('http://uitestingplayground.com/dynamicid')

# Кликнуть на синюю кнопку
search_lokator_blue_button = '[class="btn btn-primary"]'

search_input_blue_button = driver.find_element(By.CSS_SELECTOR, search_lokator_blue_button)

# Убедиться, что скрипт отрабатывает 3 раза подряд (код не требуется редактировать)
x = 0
for click in range(1,4):
    search_input_blue_button.click()
    x = x+1

assert x == 3
