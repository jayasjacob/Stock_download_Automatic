#Author: Jayas P Jacob
#Finkraft Data Downloader


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse as urlparse
from selenium.webdriver.chrome.options import Options
import time
import webbrowser
import numpy as np
import pandas as pd
from kiteconnect import KiteTicker
from kiteconnect import KiteConnect
from datetime import datetime
api_key = '7zb683rvaw0n95th'
#Getting stock list
col = ['Symbol']
stk_list1= pd.read_csv('list/list_working.csv', names=col)

list1 =stk_list1.Symbol.tolist()
print(list1)



api_secret = '6nuty3s4wjcisxx4ncnxauvz0ubj13y8'
date = datetime.today().strftime('%Y-%m-%d')
class ZerodhaAccessToken:
    def __init__(self):
        self.apiKey = '7zb683rvaw0n95th'
        self.apiSecret = '6nuty3s4wjcisxx4ncnxauvz0ubj13y8'
        self.accountUserName = 'DM1362'
        self.accountPassword = '05JUNE1991'
        self.securityPin = '973186'

    def getaccesstoken(self):
        try:
            login_url = "https://kite.trade/connect/login?v=3&api_key={apiKey}".format(apiKey=self.apiKey)

            ##change the chrome driver path
            # chrome_driver_path = "C:\Users\jayas\PycharmProjects\CHRIST_Consultancy_Project\HIST_DATA_FETCH\chromedriver.exe"
            options = Options()

            ### By enabling below option you can run chrome without UI
            #options.add_argument('--headless')


            ## chrome driver object
            driver = webdriver.Chrome()

            ## load the url into chrome
            driver.get(login_url)

            ## wait to load the site
            wait = WebDriverWait(driver, 20)

            ## Find User Id field and set user id
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))\
                .send_keys(self.accountUserName)

            ## Find password field and set user password
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))\
                .send_keys(self.accountPassword)

            ## Find submit button and click
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))\
                .submit()

            ## Find pin field and set  pin value
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).click()
            time.sleep(1)
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.securityPin)

            ## Final Submit
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).submit()

            ## wait for redirection
            wait.until(EC.url_contains('status=success'))

            ## get the token url after success
            tokenurl = driver.current_url
            parsed = urlparse.urlparse(tokenurl)
            driver.close()
            return urlparse.parse_qs(parsed.query)['request_token'][0]
        except Exception as ex:
            print(ex)


## Initialise the class object with required parameters
_ztoken = ZerodhaAccessToken()
actual_token = _ztoken.getaccesstoken()
## Final Token valid for the day ===========>
kite = KiteConnect(api_key=api_key)
data = kite.generate_session(
    actual_token, api_secret)
kite.set_access_token(data["access_token"])
print(" \n ")
print(" \n ")

#  inputs

while (True):
    print(" \n ")
    while (True):
        zde = 'NO'
        if zde:
            if "YES" == zde:
                break
            if "NO" in zde:
                break
    print("\n")
    if "YES" in zde:
        while (True):
            k = str(input("ENTER SYMBOL''S ex:-'sunpharma,sbin':=")).upper()
            if k:
                z = k.split(',')
                break
    if "NO" in zde:
        while (True):
            a = ['ACC']
            if a:
                z = a
                break
    while (True):
        eexchange = str('NSE')
        if eexchange:
            break
    while (True):
        time_frame = str('minute')
        if time_frame:
            break
    while (True):
        print(" \n ")
        zd = str('NO')
        if zd:
            if "YES" == zd:
                break
            if "NO" == zd:
                break
    if "YES" in zd:
        while (True):
            sdate = str(input("Starting Date in formatof '2019-07-23' :=")).lower()
            if sdate:
                break
        while (True):
            todate = str(input("Ending Date in format of '2019-10-23' :=")).lower()
            if todate:
                break
    if "NO" in zd:
        sdate = "2020-06-20"
        todate = date
    print(" \n ")
    while (True):
        st = str('YES')
        if st:
            if "YES" == st:
                break
            else:
                pass
    if "YES" == st:
        break
tokenall = []
symbl = []
aa = 0
print(" \n ")
print("Processing.....")

while (True):
    ttoken = int(pd.DataFrame(kite.ltp(eexchange + ":" + z[aa])).iloc[-2, 0])
    tokenall.append(ttoken)  # fetching tokens
    symbl.append(z[aa])
    aa = aa + 1
    if aa == len(z):
        break

print("Processing.....")
ee = 0

# downloading data

while (True):
    dff = kite.historical_data(tokenall[ee], sdate, todate, interval='minute', continuous=False)
    time.sleep(1)
    dfw = pd.DataFrame(dff)
    s = 'DATAS/'f"{symbl[ee]}.csv"  # writing to csv
    dfw.to_csv(s)
    ee = ee + 1
    if ee == len(z):
        print("\n")
        print("Download Complete")
        break
