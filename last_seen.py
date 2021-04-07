from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


# XPath selectors

ONLINE_STATUS_LABEL = '//span[@class=\'_7yrSq _3-8er selectable-text copyable-text\']'

# Replace below with the list of targets to be tracked
TARGETS = {'"Name"': '+123456789'}

# Replace below path with the absolute path
browser = webdriver.Chrome(r'C:\path\chromedriver.exe')

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)
statusFlag = 'offline'
while True:
    # Clear screen
    #os.system('cls')

    # For each target
    
    for target in TARGETS:
        tryAgain = True

        # Wait untill new chat button is visible
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"side\"]/div[1]/div/label/div/div[2]")))

        #new_chat_title.click()
        

        while (tryAgain):
            try:
                # Click on new chat button
                new_chat_title.click()

                # Wait untill input text box is visible
                #input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))

                time.sleep(0.5)

                # Write phone number
                #input_box.send_keys(TARGETS[target])
                new_chat_title.send_keys(TARGETS[target])

                time.sleep(1)

                # Press enter to confirm the phone number
                new_chat_title.send_keys(Keys.ENTER)

                time.sleep(5)
                tryAgain = False
                                
                try:
                    try:
                        if (browser.find_element_by_xpath(ONLINE_STATUS_LABEL).text == 'online'):
                            if(statusFlag != 'online'):
                                statusFlag = "online"
                                startTime = datetime.now().strftime("%H:%M:%S")
                    except:
                        if(statusFlag!= 'offline'):
                            endTime = datetime.now().strftime("%H:%M:%S")
                            statusFlag="offline"
                            print(target + ' is online from {} to  {}'.format(startTime, endTime))
                        pass
                    time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)