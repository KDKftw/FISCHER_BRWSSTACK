from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

##URL = "https://www.eximtours.cz"
URL = "https://www.fischer.cz"
URL_faq = URL+"/faq"
URL_stat = URL+"/recko"
URL_lm = URL+"/last-minute"
URL_fm = URL+"/first-minute"
URL_fmExotika = URL+"/first-minute/zima"
URL_detail = URL+"/spanelsko/mallorca/cala-san-vicente/globales-simar?DS=1&GIATA=89104&D=953|1108|592|611|610|612|590|726|609|621|1009|680|622|669|1086|1194|670|978|594|675|1010|683&HID=153030&MT=5&DI=13&RT=15&NN=7&RD=2022-08-27&DD=2022-08-20&DP=4312&MNN=7|8|9&TT=1&PID=MSIM&DPR=Fischer&TTM=1&DF=2022-08-20|2022-09-20&ERM=0&NNM=7|8|9&ac1=2&kc1=0&ic1=0"
URL_covidInfo = URL+"/covid-info"

caps=[{
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
      }]

caps3 = [{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'ie',
      'browser_version': '11.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      }]

caps2 = [   {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '94.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      }]

def acceptConsent(driver):
    def expand_shadow_element(element):
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root
    try:
        outer = expand_shadow_element(driver.find_element_by_css_selector("div#usercentrics-root"))
        inner = outer.find_element_by_css_selector("button[data-testid='uc-accept-all-button']")
        inner.click()
    except NoSuchElementException:
        pass

def closeExponeaBanner(driver):
    time.sleep(1.5)
    wait = WebDriverWait(driver, 150000)
    driver.maximize_window()
    try:
        exponeaBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']")
        if exponeaBanner.is_displayed():

            wait.until(EC.visibility_of(exponeaBanner))
            exponeaCrossAndBanner = driver.find_element_by_xpath("//*[@class='exponea-popup-banner']//*[@class='exponea-close']")
            exponeaCrossAndBanner.click()
            time.sleep(2)

    except NoSuchElementException:
        print( "nenasle se exponea banner")

def consentAndExponeaBanner(driver):
    time.sleep(3)
    acceptConsent(driver)

    time.sleep(2)
    closeExponeaBanner(driver)
    time.sleep(1)