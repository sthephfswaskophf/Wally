#williammarques
#https://github.com/swaskophf

#bibliotecas necessarias, caso nao tenha instalada em sua maquina basta executar os comandos (pip instal....)
from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import time

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(15) #da um sleep de 15 segundos, tempo para scannear o QRCODE

