from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.eximtours.cz"
URL_faq = URL+"/faq"
URL_stat = URL+"/recko"
URL_lm = URL+"/last-minute"
URL_fm = URL+"/first-minute"
URL_fmExotika = URL+"/first-minute/zima"
URL_detail = URL+"/turecko/turecka-riviera/alanya/kleopatra-royal-palm?DS=1&GIATA=38694&D=627|974|596|712|684|955&HID=129375&MT=5&DI=13&RT=15&NN=7&RD=2021-09-25&DD=2021-09-18&DP=4305&TO=4305|4309|2682|4308|4312&MNN=7&TT=1&PID=AYPAL&DPR=Fischer&TTM=1&TOM=4305|4309|2682|4308|4312&DF=2021-09-18|2021-10-19&ERM=0&NNM=7&ac1=2&kc1=0&ic1=0"

caps=[{
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
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

def closePopupBanner(driver):
    try:
        wait = WebDriverWait(driver, 150000)
        bannerClose = driver.find_element_by_xpath('//*[@class="close"]')
        wait.until(EC.visibility_of(bannerClose))
        bannerClose.click()

    except NoSuchElementException:
        pass