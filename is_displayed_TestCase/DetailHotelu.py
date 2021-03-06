import time
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from to_import_secret import sendEmail, comandExecutor
from to_import import acceptConsent, URL_detail, caps

##there is new SRL rn so gotta prepare that, for now I created this test just for the detail of hotel it self, hard url


def Detail_isDisplayed(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    driver.get("https://www.fischer.cz/hotely/recko/kreta/panorrmo/apollo?DS=2&GIATA=7855&D=826|623|741|735|618|619|624|973|993|595|972|648|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122|620&HID=487851&MT=0&RT=22&NN=7&RD=2021-10-27&DD=2021-10-20&DP=3789&MNN=7|8|9&TT=1&PID=AMTSGR2504&DPR=OTSCKF&TTM=1&DF=2021-10-20|2021-11-20&ERM=0&NNM=7|8|9&ac1=2&kc1=1&ka1=10&ic1=0")
    driver.maximize_window()
    time.sleep(5)
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
        Thread(target=Detail_isDisplayed, args=(cap,)).start()

