from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу http://the-internet.herokuapp.com/add_remove_elements/
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

# 5 раз кликнуть на кнопку Add Element
search_lokator_button = "button"

search_input_button = driver.find_element(By.CSS_SELECTOR, search_lokator_button)

for click in range(1,6):
    search_input_button.click()

# Собрать со страницы список кнопок Delete
search_lokator_delete = '[class="added-manually"]'
search_input_delete = driver.find_elements(By.CSS_SELECTOR, search_lokator_delete)

# Вывести на экран размер списка
print(len(search_input_delete))



 
