import base64
import os 
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import urllib
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver
def startHeroku():
    chrome_options = Options()
    #mantem o chrome aberto mais tempo.
    #chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    #salve tudo dentro dessa pasta, para servidor preciso que isso aqui seja modificado.    
    chrome_options.add_argument('--user-data-dir=E:\\Programação\\Python\\App Agil\\app-django-whatsapp\\.wdm\\drivers\\chromedriver\\win32\\107.0.5304') #TODO alterar isso para o servidor.        
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
        print(driver.current_window_handle)   
        driver.get(url)
    except:
        driver = start()
        driver.get(url)    
    
def importWhatsappQrCode():            
    #pega um script e roda no servidor para pegar o canvas  que é o qrCode
    global driver
#    scrape('https://web.whatsapp.com/')
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

#desatualiado não usaar mais
def whatsAppStatus():
    driver = scrape('https://web.whatsapp.com/')    
    while len(driver.find_elements(By.ID, 'pane-side')) < 1:
        time.sleep(1)
        print('whats deslogado')        
    time.sleep(2)

def whatsLogin():        
    global driver
    scrape('https://web.whatsapp.com/')    
    #TODO fazer uma barra de progresso na view que irá chamar ele.        
    while len(driver.find_elements(By.ID, 'pane-side')) < 1:        
        time.sleep(1)
        print('esperando para conectar')
        try:
            if (driver.find_element(By.TAG_NAME, 'canvas').is_displayed()):
                return False
        except:
            print('sem qr code')
                
    if len(driver.find_elements(By.ID, 'pane-side')) >= 1:
        print("O whatsapp está conectado")    
        return True
    
def test():
    # Setup wait for later
    driver = scrape('http://www.google.com.br')
    driver = scrape('http://www.google.com.br')    
  
def sendMessege(msg,telefone):    
    global driver 
    texto = urllib.parse.quote(msg)
    url = f"http://web.whatsapp.com/send?phone={telefone}&text={texto}"
    #driver = WhatsAppStatus()    
    scrape(url)            
    print(url)
    while len(driver.find_elements(By.ID, 'pane-side')) < 1:            
        time.sleep(1)
        print('whats carregando')    
    time.sleep(3)        
    
    numinvalido = len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]'))    
    
    if (numinvalido > 0):
        print('numero invalido')
        return 'Numero Inválido:'
    else:        
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        time.sleep(5)
        return 'Mensagem enviada com sucesso'
    
#enviarMensagem('test 1',45998364044)
#enviarMensagem('test automático',4598042239)
#WhatsAppStatus()
def encerrar():
    global driver 
    driver.close()    