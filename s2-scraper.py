#This is built for a rpi4 with chromium and chromium-driver installed

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import sqlite3
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
c_mo = datetime.now().strftime("%B")
c_yr = datetime.now().strftime("%Y")
c_day = datetime.now().strftime("%d")
url = """https://publish.obsidian.md/s2underground/S2+Underground+PUBLISH/02+Wire+Reports/"""+c_mo+"/The+Wire+-+"+c_mo+"+"+c_day+"""%2C+"""+c_yr
pathpath = "/usr/bin/chromedriver"

try:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(executable_path=pathpath)
    driver = webdriver.Chrome(service=service,options=options)
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
    
    #You can add other elements here to scrape. comma separated
    selectors = [
        "div.el-p"
    ]
    
    for selector in selectors:
        try:
            c = driver.find_element(By.CSS_SELECTOR, selector)
            wire_text = c.text.strip()
        except:
            continue
    driver.quit()

except Exception as e:
    #print(e)
    pass

try:
    db_name = '/home/pi/Desktop/s2_reports.db'
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reports (date TEXT NOT NULL,content TEXT NOT NULL,url TEXT NOT NULL)''')
    conn.commit()
    conn.close()

    conn = sqlite3.connect('/home/pi/Desktop/s2_reports.db')
    c = conn.cursor()
    c.execute('''INSERT OR REPLACE INTO reports (date,content,url) VALUES (?,?,?)''',(today,wire_text,url))
    conn.commit()
    conn.close()

except Exception as e:
    #print(e)
    pass