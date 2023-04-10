# %%
from selenium import webdriver 
from selenium.webdriver.common.by import By
#Biblioteca usada para identificar tags html e buscar na pág
from selenium.webdriver.chrome.options import Options
# Biblioteca usada para escolher se quero ver a aplicação sendo executada ou não
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import json as json
import urllib as urllib
from time import sleep
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
import zipfile
from datetime import date
import pandas as pd
import shutil 
# %%
op = Options()
#Encurtando o nome do import
op.headless = False
#Quando o headless receber True a aplicação não é vista, quando é false vemos a aplicação sendo executada
servico = Service((ChromeDriverManager().install()))
navegador = webdriver.Chrome(service=servico,options=op )
from datetime import date,timedelta


# %%
hj = date.today()
hj = hj - timedelta(1)

# %%

link = 'https://app.sprinklr.com/ui/login?returnTo=%2Fui%2Fservice%2Flogin%3Fservice%3Dspr%26returnTo%3Dhttps%253A%252F%252Fspace.sprinklr.com%252Fsocial%252Finsights%252Freporting%252Fdashboard%252F640b9d4b72b8e67503ebc0ee%252Ftab%252F0&service=spr'
navegador.get(url=link)
action = ActionChains(navegador)
def Extrair_zip():
    os.chdir('C:\\Users\\Enrico\\Downloads')
    for i in os.listdir():
        if i == 'PfizerPro.zip':
            shutil.move('C:\\Users\\Enrico\\Downloads\\'+ i,'E:\\Enrico_Work\\Sprinklr_HHY_Auto\\')
    os.chdir('E:\\Enrico_Work\\Sprinklr_HHY_Auto')
    sleep(5)
    with zipfile.ZipFile('PfizerPro.zip', 'r') as zip_ref:
        zip_ref.extract('PfizerProKPIs_1.csv', 'E:\\Enrico_Work\\Sprinklr_HHY_Auto\\')
        zip_ref.extract('URLs_2.csv', 'E:\\Enrico_Work\\Sprinklr_HHY_Auto\\')
        zip_ref.extract('AdVariants_3.csv', 'E:\\Enrico_Work\\Sprinklr_HHY_Auto\\')

def dados_PfizerProKPIs():
    dados_PfizerProKPIs = pd.read_csv('PfizerProKPIs_1.csv',sep=',')
    dados_PfizerProKPIs.fillna(0.0,inplace=True)
    dados_PfizerProKPIs.to_csv('PfizerProKPIs.csv', sep = ';')
    

def remover():
    os.remove('AdVariants_3.csv')
    os.remove('URLs_2.csv')
    os.remove('PfizerProKPIs_1.csv')
    os.remove('PfizerPro.zip')


# %%
navegador.find_element(By.XPATH, '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/div[1]/input').send_keys('###########')
sleep(2)
navegador.find_element(By.XPATH, '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div/form/div[1]/div[2]/button').click()
sleep(3)
navegador.find_element(By.XPATH, '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/div[1]/input').send_keys('############')
sleep(2)
navegador.find_element(By.XPATH, '//*[@id="root"]/div/div/div/section[2]/section/div[1]/div/div/div/div/div/div[2]/form/div[2]/button').click()

sleep(8)

# %%
navegador.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/section/div[2]/div[1]/div[1]/header/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/button').click()
sleep(5)
navegador.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/div/div/ul/li[9]').click()
sleep(3)                         
navegador.find_element(By.XPATH, '//*[contains(text(), "CSV")]').click()
sleep(3)
navegador.find_element(By.XPATH, '/html/body/div[9]/div/div[2]/div/div/div/div[2]/div/form/div/div/div[2]/div[2]/div[1]').click()
sleep(2)
navegador.find_element(By.XPATH, '/html/body/div[9]/div/div[2]/div/div/div/div[3]/button[2]').click()

# %%
sleep(20)
navegador.find_element(By.ID,'sw-id--21__anchor').click()
sleep(3)
navegador.find_element(By.LINK_TEXT,'this link').click()
sleep(7)


# %%
Extrair_zip()
sleep(10)

# %%
dados_PfizerProKPIs()

# %%
remover()
navegador.close()


