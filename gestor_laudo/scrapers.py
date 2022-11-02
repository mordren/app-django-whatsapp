import base64
from imghdr import what
from multiprocessing.util import is_exiting
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import urllib3
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def start():                   
    chrome_options = Options()
    #mantem o chrome aberto mais tempo.
    #chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--profile-directory=Default')
    #salve tudo dentro dessa pasta, para servidor preciso que isso aqui seja modificado.    
    chrome_options.add_argument('--user-data-dir=E:\\Programação\\Python\\App Agil\\app-django-whatsapp\\.wdm\\drivers\\chromedriver\\win32\\107.0.5304') #TODO alterar isso para o servidor.    
    os.environ['WDM_LOCAL'] = '1'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                chrome_options=chrome_options)                        
    print('start service')     
    return driver
    
def scrape(url): 
    driver = start()
    driver.get(url)
    #retono o driver para ser maipulado em outro lugar    
    return driver
    
def importWhatsappQrCode():            
    #pega um script e roda no servidor para pegar o canvas  que é o qrCode
    time.sleep(10)
    try:
        script = "return document.querySelector('canvas[aria-label=\"Scan me!\"]').toDataURL('image/png', 1.0).substring(21);"
        url = driver.execute_script(script)            
        canvas_png = base64.b64decode(url)            
        img_file = open('static/image.png', 'wb')
        img_file.write(canvas_png)
        img_file.close()            
        print('qrcode baixado na pasta media')                            
    except:
        print('Erro na importação do whatsapp')

def WhatsStatus():        
    driver = scrape('https://web.whatsapp.com/')
    time.sleep(20)
    try:
        if (driver.find_element(By.ID, 'pane-side').is_displayed):        
            print("O whatsapp está conectado")            
            driver.close()
    except: 
        importWhatsappQrCode()
        time.sleep(3)
        driver.close()
        return True    
    
def test():     
    chrome_options = Options()
    #mantem o chrome aberto mais tempo.
    #chrome_options.add_experimental_option("detach", True)
    #chrome_options.add_argument('--user-data-dir=./User_Data')    
    chrome_options.add_argument('--profile-directory=Default')
    #salve tudo dentro dessa pasta, para servidor preciso que isso aqui seja modificado.
    chrome_options.add_argument('--user-data-dir=E:\\Programação\\Python\\App Agil\\app-django-whatsapp\\.wdm\\drivers\\chromedriver\\win32\\107.0.5304')
    
    os.environ['WDM_LOCAL'] = '1'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                chrome_options=chrome_options)                            
    print('start service')         
    driver.get('https://web.whatsapp.com/')           
    time.sleep(20)    
    
WhatsStatus()