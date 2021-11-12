import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, URL_lm, caps, consentAndExponeaBanner

def LM_isDisplayed(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    wait = WebDriverWait(driver, 1500)
    driver.get(URL_lm)
    driver.maximize_window()
    time.sleep(2.5)
    consentAndExponeaBanner(driver)

    try:
        zajezdyLMsingle = driver.find_element_by_xpath("//*[@class='page-tour']")
        zajezdyLMall = driver.find_elements_by_xpath("//*[@class='page-tour']")
        wait.until(EC.visibility_of(zajezdyLMsingle))
        if zajezdyLMsingle.is_displayed():
            for WebElement in zajezdyLMall:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = "Problem s LM  zajezdy se neukazuji " + url

                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s LM  zajezdy se neukazuji " + url
        sendEmail(msg)

    try:
        rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
        wait.until(EC.visibility_of(rozbal))
        driver.execute_script("arguments[0].click();", rozbal)
        time.sleep(2)

    except NoSuchElementException:
        url = driver.current_url
        msg = " Nepodarilo se rozbalit LM zajezd " + url
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
    except NoSuchElementException:
        url = driver.current_url
        msg = "Nenasel se zadny zajezd pri rozbaleni zajezdu v last minute " + url
        sendEmail(msg)


    driver.quit()

for cap in caps:
        Thread(target=LM_isDisplayed, args=(cap,)).start()