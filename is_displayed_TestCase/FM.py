import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, URL_fmExotika, caps



def FM_isDisplayed(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    driver.get(URL_fmExotika)
    wait = WebDriverWait(driver, 1500)
    driver.maximize_window()
    time.sleep(2)
    acceptConsent(driver)
    time.sleep(1.5)
    try:
        zajezdyFMsingle = driver.find_element_by_xpath("//*[@class='page-tour']")
        zajezdyFMall = driver.find_elements_by_xpath("//*[@class='page-tour']")
        wait.until(EC.visibility_of(zajezdyFMsingle))
        if zajezdyFMsingle.is_displayed():
            for WebElement in zajezdyFMall:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = "Problem s FM - zajezdy se neukazuji " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s FM - zajezdy se neukazuji " + url
        sendEmail(msg)

    try:
        rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
        wait.until(EC.visibility_of(rozbal))
        driver.execute_script("arguments[0].click();", rozbal)
        time.sleep(2)

    except NoSuchElementException:
        url = driver.current_url
        msg = " Nepodarilo se rozbalit FM zajezd " + url
        sendEmail(msg)

    try:
        rozbalenyZajezd = driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
        rozbalenyZajezdAll = driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
        wait.until(EC.visibility_of(rozbalenyZajezd))
        if rozbalenyZajezd.is_displayed():
            for WebElement in rozbalenyZajezdAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu ve FM " + url
        sendEmail(msg)

    driver.quit()

for cap in caps:
        Thread(target=FM_isDisplayed, args=(cap,)).start()

