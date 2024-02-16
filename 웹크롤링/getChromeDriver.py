from selenium import webdriver

import chromedriver_autoinstaller

import os



# Check if chrome driver is installed or not

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

# driver_path = f'./{chrome_ver}/chromedriver.exe'

driver_path = 'Z:/999_sjbang/웹크롤링/120/chromedriver.exe'



if os.path.exists(driver_path):

    print(f"chrom driver is insatlled: {driver_path}")

else:

    print(f"install the chrome driver(ver: {chrome_ver})")

    chromedriver_autoinstaller.install(True)



# Get driver and open url

driver = webdriver.Chrome()