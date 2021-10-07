from SRL import test_SRL
from DetailHotelu import test_Detail
from FM import test_FM
from LM import test_LM
from SDO import test_SDO
from HP import test_HomePage
from threading import Thread
from to_import import caps


for cap in caps:
        Thread(target=test_SRL, args=(cap,)).start()
        Thread(target=test_Detail, args=(cap,)).start()
        Thread(target=test_FM, args=(cap,)).start()
        Thread(target=test_LM, args=(cap,)).start()
        Thread(target=test_SDO, args=(cap,)).start()
        Thread(target=test_HomePage, args=(cap,)).start()
