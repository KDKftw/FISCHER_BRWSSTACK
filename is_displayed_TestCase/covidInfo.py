import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, URL_stat, caps, URL_covidInfo, closeExponeaBanner



def covidInfo_isDisplayed(desired_cap):
    driver = webdriver.Remote(
    command_executor=comandExecutor,
        desired_capabilities=desired_cap)

    wait = WebDriverWait(driver, 150000)
    driver.get(URL_covidInfo)
    time.sleep(1)
    acceptConsent(driver)
    time.sleep(1)
    closeExponeaBanner(driver)


    wholeGridsAll = driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
    wholeGridsSingle = driver.find_element_by_xpath("//*[@class='f_tileGrid-item']")
    try:
        wait.until(EC.visibility_of(wholeGridsSingle))
        for WebElement in wholeGridsAll:
            jdouvidet = WebElement.is_displayed()
            if jdouvidet == True:
                pass
                print("gridy jdou videt")
            else:
                url = driver.current_url
                msg = " Problem s gridy cocid info wholeGridsAll " + url
                sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s gridy covid info wholeGridsAll " + url
        sendEmail(msg)

    contentItemsAll = driver.find_elements_by_xpath("//*[@class='f_tile-content-item']")
    contentItemsSingle = driver.find_element_by_xpath("//*[@class='f_tile-content-item']")

    try:
        wait.until(EC.visibility_of(contentItemsSingle))
        for WebElement in contentItemsAll:
            jdouvidet = WebElement.is_displayed()
            if jdouvidet == True:
                pass
                ##print("content jdou videt")
            else:
                url = driver.current_url
                msg = " Problem s content vocid info " + url
                sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s content covid info contentItemsAll " + url
        sendEmail(msg)

    driver.quit()

for cap in caps:
        Thread(target=covidInfo_isDisplayed, args=(cap,)).start()