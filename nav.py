from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

web = webdriver.Chrome(options=options)
wait = WebDriverWait(web,10)


web.get('https://www.google.com/recaptcha/api2/demo')

time.sleep(2)

wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@id='recaptcha-anchor']"))).click()

time.sleep(2)

web.save_screenshot("page.png")

time.sleep(2)
