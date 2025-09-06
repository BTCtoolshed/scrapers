from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import subprocess
import time

import sqlite3

from datetime import datetime, timedelta


url = """https://spotcrime.com/map?lat=38.9071923&lon=-77.0368707&address=Washington,%20DC,%20USA""" #change within the triple quotes to the area you are trying to monitor through SpotCrime.com

pathpath = "/usr/bin/chromedriver"

j=0

try:
    options = Options()
    options.add_argument("--headless=new") #=new
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(executable_path=pathpath)
    driver = webdriver.Chrome(service=service,options=options)
    driver.get(url)


    try:
        db_name = '/home/pi/Desktop/crime_reports.db'
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS reports (date TEXT NOT NULL,type TEXT NOT NULL,loc TEXT NOT NULL,fullrow PRIMARY KEY)''')
        conn.commit()
        conn.close()
        
        view_crime = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, """/html/body/main/div[3]/div/button[1]""")))
        view_crime.click()
        #print("a")
        popup = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, """/html/body/main/div[3]/div/button[1]""")))
        #print("b")
        j==0;
        while j < 101:
            j=j+1
            try:
                crime_items = driver.find_elements(By.XPATH, """/html/body/main/div[3]/div/div[2]/div/a["""+str(j)+"""]""") #
                #print("Item Accessed!")
                #print(len(crime_items))
                for i, item in enumerate(crime_items,1):
                    #item.get_attribute('outerHTML')[:500])
                    crime_type = item.find_element(By.XPATH,"""./div[2]/span[1]""").text.strip()
                    crime_loc = item.find_element(By.XPATH,"""./div[2]/span[2]""").text.strip()
                    crime_date = item.find_element(By.XPATH,"""./div[2]/span[3]""").text.strip()
                    dt = datetime.strptime(crime_date,'%m/%d/%Y %I:%M %p')
                    thisrow = dt.strftime('%Y-%m-%d %H:%M')+" "+crime_loc+" "+crime_type
                    #print(f"{thisrow}")
                    
                    conn = sqlite3.connect('/home/pi/Desktop/crime_reports.db')
                    c = conn.cursor()
                    c.execute('''INSERT OR REPLACE INTO reports (date,type,loc,fullrow) VALUES (?,?,?,?)''',(dt.strftime('%Y-%m-%d %H:%M'),crime_type,crime_loc,thisrow))
                    conn.commit()
                    conn.close()

                    crime_type = None
                    crime_loc = None
                    crime_date = None
                    dt = None
                    
            except Exception:
                pass
    except Exception as e:
        print(e)

    driver.quit()

except Exception as e:
    print(f"{e}")
    
conn = sqlite3.connect('/home/pi/Desktop/crime_reports.db')
c = conn.cursor()
#c.execute('''SELECT * FROM reports ORDER BY 1 DESC''') #view all
c.execute('''SELECT date(date, 'weekday 0','-7 days') as WEEK, COUNT(*) AS CRIMES FROM reports GROUP BY 1 ORDER BY 1 DESC''') #view by week
rows = c.fetchall()
for row in rows:
    print("Wk:"+str(row[0])+" C: "+str(row[1]))
conn.commit()
conn.close()