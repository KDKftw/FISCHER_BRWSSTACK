import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, URL_stat, caps



def test_SDO(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    driver.get(URL_stat)
    driver.maximize_window()
    time.sleep(2.5)
    acceptConsent(driver)


    try:
        destinaceAll = driver.find_elements_by_xpath("//*[@class='fshr-listTable-content-part']")
        destinaceSingle = driver.find_element_by_xpath("//*[@class='fshr-listTable-content-part']")
        if destinaceSingle.is_displayed():
            for WebElement in destinaceAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = "Nenasli se destinace v /stat " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Nenasli se destinace v /stat " + url
        sendEmail(msg)

    try:
        dlazdiceFotoSingle = driver.find_element_by_xpath("//*[@class='f_tile-image']")
        dlazdiceFotoAll = driver.find_elements_by_xpath("//*[@class='f_tile-image']")
        if dlazdiceFotoSingle.is_displayed():
            for WebElement in dlazdiceFotoAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = "Nenasli se fotky v dlazdicich v /stat " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Nenasli se fotky v dlazdicich v /stat " + url
        sendEmail(msg)

    try:
        mapa = driver.find_element_by_xpath("//*[@id='google-map']")
        if mapa.is_displayed():
            pass
        else:
            url = driver.current_url
            msg = "Nenasli se mapa v /stat " + url
            sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Nenasli se mapa v /stat " + url
        sendEmail(msg)

    driver.quit()

for cap in caps:
        Thread(target=test_SDO, args=(cap,)).start()