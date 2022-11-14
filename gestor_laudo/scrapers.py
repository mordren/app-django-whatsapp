import base64
from pathlib import Path
import os 
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import urllib
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

BASE_DIR = Path(__file__).resolve().parent.parent

driver = webdriver

#aqui fiz algumas mudanças para rodar no servidor online
def startHeroku():
    chrome_options = Options()
    #mantem o chrome aberto mais tempo.
    #chrome_options.add_experimental_option("detach", True)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get('/usr/bin/google-chrome')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")    
    #chrome_options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Safari/537.36")
    chrome_options.add_argument('--user-data-dir=/usr/bin/google-chrome') #TODO alterar isso para o servidor.    
    os.environ['WDM_LOCAL'] = '1'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                chrome_options=chrome_options)                        
    print('start service')     
    return driver

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
    global driver                
    try:
        driver.get(url)
    except:
        print(os.name)
        if(os.name == 'nt'):
            driver = start()
        else:
            driver = startHeroku()       
        driver.get(url)    

    
    
def importWhatsappQrCode():            
    #pega um script e roda no servidor para pegar o canvas  que é o qrCode
    global driver    
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

def whats_login():        
    global driver
    scrape('https://web.whatsapp.com/')    
    #TODO fazer uma barra de progresso na view que irá chamar ele.            
    while len(driver.find_elements(By.ID, 'pane-side')) < 1:        
        time.sleep(1)
        print('esperando para conectar')                 
        #faz uma verificação se o whatsapp está conectado na conta.
        if (len(driver.find_elements(By.ID, 'pane-side')) >= 1):            
            return True
        if (len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div/canvas')) >= 1):
            return False
    
def send_messege(msg,telefone):    
    global driver 
    texto = urllib.parse.quote(msg)
    url = f"http://web.whatsapp.com/send?phone={telefone}&text={texto}"
    scrape(url)                
    while len(driver.find_elements(By.ID, 'pane-side')) < 1:            
        time.sleep(1)
        print('whats carregando')    
    time.sleep(3)
    
    if (len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]'))  > 0):
        print('numero invalido')
        time.sleep(3)
        driver.close()
        return 'Numero Inválido:'
    else:        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        time.sleep(4)
        driver.close()
        return 'msg ok'
    
print(os.name)