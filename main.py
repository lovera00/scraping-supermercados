import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import time

load_dotenv()



def setup_webdriver():
    """
    Set up the Chrome WebDriver with options.
    """
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def main():
    driver = setup_webdriver()
    lista_urls = ["https://www.stock.com.py/default.aspx", "https://www.superseis.com.py/default.aspx", "https://www.casarica.com.py/","https://www.arete.com.py/","https://www.realonline.com.py/","https://losjardinesonline.com.py/","https://supermas.com.py/","https://supermercadolabomba.com/index.php?class=Inicio"]

    for url in lista_urls:
        driver.get(url)
        time.sleep(5)
    time.sleep(60)
    driver.quit()

if __name__ == "__main__":
    main()