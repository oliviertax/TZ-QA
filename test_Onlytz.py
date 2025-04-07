import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


def test_web_navigation():
  
    driver.get("https://only.digital/")
    time.sleep(3)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    footer = driver.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed(), "Футер не отображается"
   
    button = driver.find_element(By.XPATH, "//footer//button[contains(text(),'Начать проект')]")
    assert button.is_displayed(), "Кнопка не отображается"
    
    be = driver.find_element(By.XPATH, "//footer//a[@href='https://www.behance.net/onlydigitalagency']")
    assert be.is_displayed(), "Кнопка не отображается"
    be.click()
   
    dp = driver.find_element(By.XPATH, "//footer//a[@href='https://dprofile.ru/only']")
    assert dp.is_displayed(), "Кнопка не отображается"
    dp.click()
    
  
