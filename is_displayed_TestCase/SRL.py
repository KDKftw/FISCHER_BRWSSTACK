import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, caps



def proklikNaSRLzHP(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    time.sleep(2.5)
    acceptConsent(driver)

    try:
        lmZajezdNej = driver.find_element_by_xpath(
            "//*[@class='fshr-lm-table-item-content']")
        wait.until(EC.visibility_of(lmZajezdNej))
        ##lmZajezdNej.click()
        driver.execute_script("arguments[0].click();", lmZajezdNej)  ####.click nefunguje na fischer NNN LM/FM, chrome
    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem HP-Nej. nabidka - nenasel se LM zajezd" + url
        sendEmail(msg)

    time.sleep(2)

def test_SRL(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    wait = WebDriverWait(driver, 150000)
    proklikNaSRLzHP(driver)

    try:
        hotelySingle = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")        ##
        hotelyAll = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
        wait.until(EC.visibility_of(hotelySingle))
        ##print(hotelyAll)
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                ##print(jdouvidet)
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = " Problem s hotely v searchi - hotelCard " +url
                    sendEmail(msg)
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s hotely v searchi - hotelCard " + url
        sendEmail(msg)


    try:
        fotkyAll = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_tileGallery']")         ##
        fotkaSingle = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_tileGallery']")
        wait.until(EC.visibility_of(fotkaSingle))
        ##print(fotkaSingle)
        if fotkaSingle.is_displayed():
            for WebElement in fotkyAll:
                jdouvidet = WebElement.is_displayed()
                ##print(jdouvidet)
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = " Problem s fotkami hotelu v searchi " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = " Problem s fotkami hotelu v searchi " + url
        sendEmail(msg)


    try:
        cenaAll = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_price']")     ##
        cenaSingle = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_price']")
        wait.until(EC.visibility_of(cenaSingle))
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = " Problem s cenami hotelu v searchi " +url
                    sendEmail(msg)


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg)


    driver.quit()

for cap in caps:
        Thread(target=test_SRL, args=(cap,)).start()