from SRL import SRL
from DetailHotelu import Detail
from FM import FM
from LM import LM
from SDO import SDO
from HP import HomePage
from threading import Thread
from to_import import caps


for cap in caps:
        Thread(target=SRL, args=(cap,)).start()
        Thread(target=Detail, args=(cap,)).start()
        Thread(target=FM, args=(cap,)).start()
        Thread(target=LM, args=(cap,)).start()
        Thread(target=SDO, args=(cap,)).start()
        Thread(target=HomePage, args=(cap,)).start()
