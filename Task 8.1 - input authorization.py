from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
 
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу http://the-internet.herokuapp.com/login
driver.get('http://the-internet.herokuapp.com/login')

#В поле uername ввести значение tomsmith
search_lokator_Username = '#username'
search_input_Username = driver.find_element(By.CSS_SELECTOR, search_lokator_Username)
search_input_Username.send_keys("tomsmith")

#В поле password ввести значение SuperSecretPassword!
search_lokator_Password = '#password'
search_input_Password = driver.find_element(By.CSS_SELECTOR, search_lokator_Password)
search_input_Password.send_keys("SuperSecretPassword!")

#Нажмите кнопку Login
search_lokator_Login = '[class="fa fa-2x fa-sign-in"]'

search_input_Login = driver.find_element(By.CSS_SELECTOR, search_lokator_Login)

search_input_Login.click()