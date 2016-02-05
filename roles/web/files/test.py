from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://reddit.com')
driver.save_screenshot('reddit.png')
driver.quit()
