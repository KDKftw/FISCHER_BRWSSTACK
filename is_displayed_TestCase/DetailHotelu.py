import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL_detail, caps, closePopupBanner

##there is new SRL rn so gotta prepare that, for now I created this test just for the detail of hotel it self, hard url


def test_Detail(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    driver.get(URL_detail)
    driver.maximize_window()
    time.sleep(2.5)
    acceptConsent(driver)
    wait = WebDriverWait(driver, 150000)
    try:
        detailFotka = driver.find_element_by_xpath("//*[@class='fshr-detailGallery']")
        wait.until(EC.visibility_of(detailFotka))
        if detailFotka.is_displayed():
            pass
    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s fotkami na detailu hotelu " + url
        sendEmail(msg)

    try:
        sedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
        wait.until(EC.visibility_of(sedivka))
        if sedivka.is_displayed():
            pass


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem se sedivkou na detailu hotelu " + url
        sendEmail(msg)

    closePopupBanner(driver)

    try:
        terminyCeny = driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
        wait.until(EC.visibility_of(terminyCeny))
        terminyCeny.click()
        try:
            potvrdit = driver.find_element_by_xpath("//*[@data-testid='popup-closeButton']")
            driver.execute_script("arguments[0].click();", potvrdit)

        except NoSuchElementException:
            pass


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem prepnuti na terminy a ceny na detailu hotelu " + url
        sendEmail(msg)

    try:
        terminySingle = driver.find_element_by_xpath("//*[@data-hotel]")
        wait.until(EC.visibility_of(terminySingle))

        if terminySingle.is_displayed():
            pass
        else:
            url = driver.current_url
            msg = "Problem s terminy a ceny na detailu hotelu " + url
            sendEmail(msg)


    except NoSuchElementException:
        url = driver.current_url
        msg = "Problem s terminy a ceny na detailu hotelu " + url
        sendEmail(msg)

    driver.quit()

for cap in caps:
        Thread(target=test_Detail, args=(cap,)).start()

