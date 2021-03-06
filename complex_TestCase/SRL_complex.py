from is_displayed_TestCase.to_import import acceptConsent, URL, URL_stat, caps, closeExponeaBanner
from is_displayed_TestCase.to_import_secret import comandExecutor, sendEmail
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from threading import Thread


##driver = webdriver.Chrome(executable_path=r"C:\Users\KADOUN\Desktop\Selenium setup\chromedriver94.exe")
##driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\Selenium setup\chromedriver94.exe")
URL_SRL = "https://www.fischer.cz/vysledky-vyhledavani?d=826|623|741|735|618|619|624|973|993|595|972|648|620|746|1126|1129|1124|1128|1059|1118|1119|1121|625|1127|1125|861|1115|1132|1120|709|711|1117|603|1116|1130|1131|614|1123|1093|1198|1114|1122&tt=1&dd=2022-07-01&rd=2022-08-31&nn=7|8|9&ac1=2"
##URL_SRL = "https://www.eximtours.cz/vysledky-vyhledavani?tt=0&ac1=2&dd=2021-08-27&rd=2021-09-26&nn=7&d=63720|63719&pf=0&pt=900000"

def SRLtestV2(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    x=0         ##variable for taking the first hotel, starting at 0
    windowHandle = 1  ##variable for handling windows, gotta start on 1

    driver.get(URL_SRL)
    wait = WebDriverWait(driver, 150000)

    time.sleep(2)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)

    hotelyAllKarty = driver.find_elements_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
    for WebElement in hotelyAllKarty:

        terminZajezdu = driver.find_elements_by_xpath("//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")
        terminZajezduSingle = driver.find_element_by_xpath("//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")

        wait.until(EC.visibility_of(terminZajezduSingle))
        ##print(terminZajezdu[x].text)

        linkDetail = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
        linkDetailActualUrl = linkDetail[x].get_attribute("href")
        ##print(linkDetailActualUrl)

        stravaZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
        stravaZajezduString = stravaZajezdu[x].text

        pokojZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--bed']")
        pokojZajezduString = pokojZajezdu[x].text
        ##print(pokojZajezduString)

        cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
        cenaZajezduAllString = cenaZajezduAll[x].text
        ##print(cenaZajezduAllString)

        cenaZajezduAdult = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']//*[@class='f_tile-priceDetail-note'] //*[@class='f_price']")
        cenaZajezduAdultString = cenaZajezduAdult[x].text
        print(cenaZajezduAdultString)



        driver.execute_script("window.open("");")
        driver.switch_to.window(driver.window_handles[windowHandle])
        driver.get(linkDetailActualUrl)

        closeExponeaBanner(driver)

        time.sleep(1)       ##natvrdo aby se to neposralo

        detailTerminSedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
        ##print(detailTerminSedivka.text)

        detailStravaSedivka = driver.find_elements_by_xpath("//*[@class='fshr-detail-summary-paragraph']")
        detailStravaSedivkaString = detailStravaSedivka[1].text         ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully

        detailPokojSedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title fshr-icon fshr-icon--bed']")
        detailPokojSedivkaString = detailPokojSedivka.text
        detailPokojSedivkaString = detailPokojSedivkaString[:-3]            ##need to be edited cuz there is random spaces and "?" in the element
        ##print(detailPokojSedivkaString)

        detailCenaAll = driver.find_element_by_xpath("//*[@class='fshr-tooltip-underline js-totalPrice']")
        detailCenaAllString = detailCenaAll.text
        ##print(detailCenaAllString)
        try:
            detailCenaAdult = driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
            detailCenaAdultString = detailCenaAdult.text
            print(detailCenaAdultString)

        except NoSuchElementException:
            pass


        if detailPokojSedivkaString == pokojZajezduString:
            print("pokoje sed?? srl vs detail")
        else:
            print(" nesed?? pokoj SRL vs sedivka")

        if detailStravaSedivkaString == stravaZajezduString:
            print("stravy sed?? srl vs detail")

        else:
            print( "nesed?? strava srl vs ssedika")

        if detailCenaAllString == cenaZajezduAllString:
            print ("ceny all sed?? srl vs detail")

        else:
            print("ceny all problem srl vs detail")

        if detailCenaAdultString == cenaZajezduAdultString:
            print(" cena adult sed?? srl vs detail")

        else:
            print("cena adult nesedi srl vs detail")

        driver.switch_to.window(driver.window_handles[0])   ##this gotta be adjusted based on what test is executed
        ##for daily test needs to be set on 1 so it gets on the SRL

        x = x +1
        print(x)
        windowHandle = windowHandle + 1
        print(windowHandle)

def SRL_sort_cheapest(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)

    driver.get(URL_SRL)
    wait = WebDriverWait(driver, 150000)
    time.sleep(2)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)

    cenaZajezduAllList = []                     ##one list that takes prices from the srl
    cenaZajezduAllListSorted = []               ##second list takes the values too, then sorts it low to high

    sortByCheapest = driver.find_element_by_xpath("//*[contains(text(), 'od nejlevn??j????ho')]")
    sortByCheapest.click()

    hotelyKarty = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
    wait.until(EC.visibility_of(hotelyKarty))
    time.sleep(10)
    x=0
    cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")

    for WebElement in cenaZajezduAll:
        cenaZajezduAllString = cenaZajezduAll[x].text
        cenaZajezduAllString = cenaZajezduAllString[:-3]
        cenaZajezduAllString = ''.join(cenaZajezduAllString.split())        ##delete spaces
        cenaZajezduAllString = int(cenaZajezduAllString)        ##convert to int to do sort easily
        x=x+1
        cenaZajezduAllList.append(cenaZajezduAllString)
        cenaZajezduAllListSorted.append(cenaZajezduAllString)

    cenaZajezduAllListSorted.sort()     ##sorting second list low to high


    if cenaZajezduAllListSorted == cenaZajezduAllList:          ##compare first list to second list, if is equal = good
        print("Razeni od nejlevnejsiho je OK")

    else:
        print("Razeni od nejlevnejsiho je spatne")



    print(cenaZajezduAllList)
    print(cenaZajezduAllListSorted)

def SRL_sort_most_expensive(desired_cap):      ##the same only difference 1)click on nejdrazsi 2) sort list reverse=true
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    driver.get(URL_SRL)
    wait = WebDriverWait(driver, 150000)
    time.sleep(2)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)

    cenaZajezduAllList = []                     ##one list that takes prices from the srl
    cenaZajezduAllListSorted = []               ##second list takes the values too, then sorts it low to high

    sortByMostExpensive = driver.find_element_by_xpath("//*[contains(text(), 'od nejdra??????ho')]")
    sortByMostExpensive.click()

    hotelyKarty = driver.find_element_by_xpath("//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_searchResult-content-item']")
    wait.until(EC.visibility_of(hotelyKarty))
    time.sleep(10)
    x=0
    cenaZajezduAll = driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")

    for WebElement in cenaZajezduAll:
        cenaZajezduAllString = cenaZajezduAll[x].text
        cenaZajezduAllString = cenaZajezduAllString[:-3]
        cenaZajezduAllString = ''.join(cenaZajezduAllString.split())
        cenaZajezduAllString = int(cenaZajezduAllString)
        ##print(type(cenaZajezduAllString))
        x=x+1
        cenaZajezduAllList.append(cenaZajezduAllString)
        cenaZajezduAllListSorted.append(cenaZajezduAllString)


    cenaZajezduAllListSorted.sort(reverse=True)


    if cenaZajezduAllListSorted == cenaZajezduAllList:
        print("Razeni od nejdrazshio je OK")

    else:
        print("Razeni od nejdrazshio je spatne")



    print(cenaZajezduAllList)
    print(cenaZajezduAllListSorted)
    driver.quit()

def SRL_map(desired_cap):
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    driver.get(URL_SRL)
    time.sleep(5)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)
    zobrazitNaMape = driver.find_element_by_xpath("//*[@class='f_bar-item f_bar-map']")
    zobrazitNaMape.click()

    time.sleep(5)##try except na kolecko, pokud ok tak click, nenajde tak pokracovat dal
    koleckoCislo = driver.find_element_by_xpath("//*[@class='leaflet-marker-icon marker-cluster marker-cluster-medium leaflet-zoom-animated leaflet-interactive']")
    koleckoCislo.click()
    time.sleep(5)

    actualHotelPin = driver.find_element_by_xpath("//*[@class='leaflet-marker-icon leaflet-zoom-animated leaflet-interactive']")
    ##actualHotelPin.click()
    driver.execute_script("arguments[0].click();", actualHotelPin)          ##at this point im at detail hotelu na map??

    try:
        imgMissing = driver.find_element_by_xpath("//*[@class='f_image f_image--missing']")         ##when theres no photo on the detail on map theres actually class that says it is missing
        if imgMissing.is_displayed():                                                               ##so if I dont find this class = good
            hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
            msg = "V mape v bublibn?? hotelu se nezobrazuje fotka hotelu " + hotelBubble.text
            sendEmail(msg)

    except NoSuchElementException:
        print("actually OK")

    time.sleep(2)

    hotelBubble = driver.find_element_by_xpath("//*[@class='leaflet-popup-content'] //*[@class='f_bubble']")
    hotelBubble.click()
    driver.quit()

def SRL_filtr_strava(desired_cap):     ##jen na allinclusive, muzu si pohrat pozdeji for now enough
    driver = webdriver.Remote(
        command_executor=comandExecutor,
        desired_capabilities=desired_cap)
    driver.get(URL_SRL)
    time.sleep(2)
    acceptConsent(driver)
    time.sleep(2)
    closeExponeaBanner(driver)
    time.sleep(2)

    stravaMenu = driver.find_element_by_xpath("//*[@class='f_menu-item']//*[contains(text(), 'Strava')]")
    stravaMenu.click()
    time.sleep(2)

    allinclusiveMenu = driver.find_element_by_xpath("//*[@class='f_menu-item-content f_menu-item-content--sub'] //*[@class='f_input-label'] //*[contains(text(), 'All inclusive')]")          ##papani v menu ma vzdy vlastni value, 5=all inclusive
    allinclusiveMenu.click()

    potvrditMenu = driver.find_element_by_xpath("//*[@class='f_menu-item']//*[@class='f_button f_button--common f_button_set--smallest']")
    potvrditMenu.click()
    time.sleep(2)       ##potvrzeno chvilak casu na relload


    stravaZajezdu = driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
    x=0
    stravaZajezduList = []
    for WebElement in stravaZajezdu:
        stravaZajezduString = stravaZajezdu[x].text
        stravaZajezduList.append(stravaZajezduString)
        x=x+1

    y=0
    stringInclusve = "All inclusive"
    for _ in stravaZajezduList:
        ##if stravaZajezduList[y] == "All inclusive":
        if "All inclusive" in stravaZajezduList[y]:
            print("ok")
            y=y+1

        else:
            print("stravy nesedi k filtru")
            y = y + 1
    print(stravaZajezduList)
    driver.quit()


def spoustec():

    for cap in caps:
            #Thread(target=SRLtestV2, args=(cap,)).start()
            #Thread(target=SRL_sort_cheapest, args=(cap,)).start()
            #Thread(target=SRL_sort_most_expensive, args=(cap,)).start()
            #Thread(target=SRL_map, args=(cap,)).start()
            Thread(target=SRL_filtr_strava, args=(cap,)).start()

spoustec()