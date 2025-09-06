#This is built for a rpi4 with chromium and chromium-driver installed

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import sqlite3
from datetime import datetime,timedelta

wire_text = None
today = None
#CURRENT YEAR LOOP
date1=datetime(2025,1,1) #when the archive began
date2=datetime.now()
delta=date2-date1
i=delta.days

while i >= 0:
    loopdate = datetime.now() - timedelta(days=i)
    today = loopdate.strftime('%Y-%m-%d')
    c_mo = loopdate.strftime("%B")
    c_yr = loopdate.strftime("%Y")
    c_day2 = loopdate.strftime("%e")
    c_moO = loopdate.strftime("%m")
    c_day = c_day2.replace(" ","")
    
    #URL for archive
    url = """https://publish.obsidian.md/s2underground/S2+Underground+PUBLISH/02+Wire+Reports/Wire+Archive/"""+c_moO+"+"+c_mo+"+"+c_yr+"/The+Wire+-+"+c_mo+"+"+c_day+"""%2C+"""+c_yr
    #print(url)
    i = i-1

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
        #driver.quit()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        
        selectors = [
            "div.el-p"
        ]
        
        for selector in selectors:
            try:
                c = driver.find_element(By.CSS_SELECTOR, selector)
                wire_text = c.text.strip()
                print(f"{wire_text}")
            except Exception as e:
                #print(e)
                continue
        #print(text)
        driver.quit()

    except Exception as e:
        #print(e)
        pass

    #print(wire_text)
    try:
        db_name = '/home/pi/Desktop/s2_reports.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS reports (date TEXT PRIMARY KEY NOT NULL,content TEXT NOT NULL,url TEXT NOT NULL, read TEXT NOT NULL)''')
        conn.commit()
        conn.close()

        conn = sqlite3.connect('/home/pi/Desktop/s2_reports.db')
        c = conn.cursor()
        c.execute('''INSERT OR REPLACE INTO reports (date,content,url,read) VALUES (?,?,?,?)''',(today,wire_text,url,"U"))
        conn.commit()
        conn.close()
        wire_text = None

    except Exception as e:
        #print(e)
        wire_text=None
        today=None
        pass


#CURRENT MONTH LOOP 1
today = None
wire_text = None
i=31
while i >= 0:
    loopdate = datetime.now() - timedelta(days=i)
    today = loopdate.strftime('%Y-%m-%d')
    c_mo = loopdate.strftime("%B")
    c_yr = loopdate.strftime("%Y")
    c_day2 = loopdate.strftime("%e")
    c_moO = loopdate.strftime("%m")
    c_day = c_day2.replace(" ","")
    
    #URL for current month
    url = """https://publish.obsidian.md/s2underground/S2+Underground+PUBLISH/02+Wire+Reports/"""+c_mo+"+"+c_yr+"/The+Wire+-+"+c_mo+"+"+c_day+"""%2C+"""+c_yr
    #print(url)
    i = i-1

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
        #driver.quit()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        
        selectors = [
            "div.el-p"
        ]
        
        for selector in selectors:
            try:
                c = driver.find_element(By.CSS_SELECTOR, selector)
                wire_text = c.text.strip()
                print(f"{wire_text}")
            except Exception as e:
                #print(e)
                continue
        #print(text)
        driver.quit()

    except Exception as e:
        #print(e)
        pass

    #print(wire_text)
    try:
        db_name = '/home/pi/Desktop/s2_reports.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS reports (date TEXT PRIMARY KEY NOT NULL,content TEXT NOT NULL,url TEXT NOT NULL, read TEXT NOT NULL)''')
        conn.commit()
        conn.close()

        conn = sqlite3.connect('/home/pi/Desktop/s2_reports.db')
        c = conn.cursor()
        c.execute('''INSERT OR REPLACE INTO reports (date,content,url,read) VALUES (?,?,?,?)''',(today,wire_text,url,"U"))
        conn.commit()
        conn.close()
        wire_text = None

    except Exception as e:
        #print(e)
        wire_text=None
        today=None
        pass




#CURRENT MONTH LOOP 2
today = None
wire_text = None
i=31
while i >= 0:
    loopdate = datetime.now() - timedelta(days=i)
    today = loopdate.strftime('%Y-%m-%d')
    c_mo = loopdate.strftime("%B")
    c_yr = loopdate.strftime("%Y")
    c_day2 = loopdate.strftime("%e")
    c_moO = loopdate.strftime("%m")
    c_day = c_day2.replace(" ","")
    
    #URL for current month
    url = """https://publish.obsidian.md/s2underground/S2+Underground+PUBLISH/02+Wire+Reports/"""+c_mo+"+"+c_yr+"/The+Wire+-+"+c_mo+"+"+c_day+"""%2C+"""+c_yr
    #print(url)
    i = i-1

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
        #driver.quit()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        
        selectors = [
            "div.el-p"
        ]
        
        for selector in selectors:
            try:
                c = driver.find_element(By.CSS_SELECTOR, selector)
                wire_text = c.text.strip()
                print(f"{wire_text}")
            except Exception as e:
                #print(e)
                continue
        #print(text)
        driver.quit()

    except Exception as e:
        #print(e)
        pass

    #print(wire_text)
    try:
        db_name = '/home/pi/Desktop/s2_reports.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS reports (date TEXT PRIMARY KEY NOT NULL,content TEXT NOT NULL,url TEXT NOT NULL, read TEXT NOT NULL)''')
        conn.commit()
        conn.close()

        conn = sqlite3.connect('/home/pi/Desktop/s2_reports.db')
        c = conn.cursor()
        c.execute('''INSERT OR REPLACE INTO reports (date,content,url,read) VALUES (?,?,?,?)''',(today,wire_text,url,"U"))
        conn.commit()
        conn.close()
        wire_text = None

    except Exception as e:
        #print(e)
        wire_text=None
        today=None
        pass


wire_text=None
today=None    

#CURRENT DAY
today = datetime.today().strftime('%Y-%m-%d')
c_mo = datetime.now().strftime("%B")
c_yr = datetime.now().strftime("%Y")
c_day_pre = datetime.now().strftime("%e")
c_day = c_day_pre.replace(" ","")
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
    c.execute('''CREATE TABLE IF NOT EXISTS reports (date TEXT PRIMARY KEY NOT NULL,content TEXT NOT NULL,url TEXT NOT NULL)''')
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

conn = sqlite3.connect('/home/pi/Desktop/s2_reports.db')
c = conn.cursor()
c.execute('''SELECT * FROM reports ORDER BY 1 DESC LIMIT 15''') #view last 15
rows = c.fetchall()
for row in rows:
    print("Wk:"+str(row[0])+" C: "+str(row[1]))
conn.commit()