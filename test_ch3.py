from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    # 1. Go to statsroyale.com
    driver.get('https://statsroyale.com')
    # 2. Go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    # 3. Assert Ice Spirit is diplayed
    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert ice_spirit_card.is_displayed
 