from selenium import webdriver
import json 

with open('config.json') as f:
    config = json.load(f)
    
HEADLESS = config['HEADLESS']

class Chrome:
    def driver(self):
        chromeOptions = webdriver.ChromeOptions()

        if HEADLESS:
            chromeOptions.add_argument("--headless")
            chromeOptions.add_argument("--disable-gpu")
            chromeOptions.add_argument("--no-sandbox")
            chromeOptions.add_argument("--disable-dev-shm-usage")
        else:
            chromeOptions.add_argument("--start-maximized")
        
        return webdriver.Chrome(options=chromeOptions)
    

