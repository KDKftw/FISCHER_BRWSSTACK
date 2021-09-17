import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL, URL_faq, caps


def HomePage(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    wait = WebDriverWait(driver, 1500)
    driver.get(URL)
    driver.maximize_window()
    time.sleep(2.5)
    acceptConsent(driver)
    try:
        bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
        bannerAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
        wait.until(EC.visibility_of(bannerSingle))
        if bannerSingle.is_displayed():
            for WebElement in bannerAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
                else:
                    url = driver.current_url
                    msg = "Problem na HP s bannery " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem na HP s bannery " + url
        sendEmail(msg)

    time.sleep(1.5)

    try:
        nejnabidkyLMsingle = driver.find_element_by_xpath("//*[@class='fshr-lm-table-item-content']")
        nejnabidkyLMall = driver.find_elements_by_xpath("//*[@class='fshr-lm-table-item-content']")
        wait.until(EC.visibility_of(nejnabidkyLMsingle))
        if nejnabidkyLMsingle.is_displayed():
            for WebElement in nejnabidkyLMall:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass

                else:
                    url = driver.current_url
                    msg = "Problem na HP s nej. nabidky LM " + url
                    sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem na HP s nej. nabidky LM " + url
        sendEmail(msg)

    driver.get(URL_faq)

    try:
        faqSingle = driver.find_element_by_xpath("//*[@class='f_faq-item']")
        faqAll = driver.find_elements_by_xpath("//*[@class='f_faq-item']")
        if faqSingle.is_displayed():
            for WebElement in faqAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    pass
        else:
            url = driver.current_url
            msg = "Problem FAQ " + url
            sendEmail(msg)

    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem FAQ " + url
        sendEmail(msg)



    driver.quit()

for cap in caps:
        Thread(target=HomePage, args=(cap,)).start()