import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Edge()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    # Ждем, когда цена станет $100
    wait = WebDriverWait(browser, 12)
    price = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    # Нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    
    # Решаем математическую задачу
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)
    
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()
    
finally:
    time.sleep(10)
    browser.quit()
