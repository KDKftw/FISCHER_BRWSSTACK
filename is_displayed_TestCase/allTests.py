from SRL import SRL_isDisplayed
from DetailHotelu import Detail_isDisplayed
from FM import FM_isDisplayed
from LM import LM_isDisplayed
from SDO import SDO_isDisplayed
from HP import HomePage_isDisplayed
from threading import Thread
from to_import import caps


for cap in caps:
        Thread(target=SRL_isDisplayed, args=(cap,)).start()
        Thread(target=Detail_isDisplayed, args=(cap,)).start()
        Thread(target=FM_isDisplayed, args=(cap,)).start()
        Thread(target=LM_isDisplayed, args=(cap,)).start()
        Thread(target=SDO_isDisplayed, args=(cap,)).start()
        Thread(target=HomePage_isDisplayed, args=(cap,)).start()
