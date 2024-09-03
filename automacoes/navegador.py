import time 
from automacoes.chrome import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


class Navegador:
    def __init__(self):
        self.chrome = Chrome().driver()
        self.short_wait = WebDriverWait(self.chrome, 5)
        self.long_wait = WebDriverWait(self.chrome, 10)
        
    def print_log(self,texto):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print(f'[{current_time}] [navegador]: {texto}')

    def abrir_pagina(self,url):
        self.print_log(f'Abrindo página {url}')
        self.chrome.get(url)
        self.print_log(f'Página {url} aberta')

    def pegar_dados(self, xpath):
        self.print_log(f'Pegando os dados')
        element = self.short_wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element
    
    def criar_tabela(self, xpath):
        self.print_log(f'Criando tabela')
        table = self.pegar_dados(xpath)
        table_columns = table.find_elements(By.TAG_NAME, 'thead')
        column_names = [column.text for column in table_columns[0].find_elements(By.TAG_NAME, 'th')]
        df = pd.DataFrame(columns=column_names)
        table_rows = table.find_elements(By.TAG_NAME, 'tbody')
        linha = 0
        self.print_log('Preenchendo tabela')
        for row in table_rows:
            for data in row.text.split('\n'):
                if "Dividend" in data or "Stock Split" in data:
                    continue
                data_list = data.split(' ')
                datetime_str = ' '.join(data_list[:3])
                datetime_obj = pd.to_datetime(datetime_str)
                data_list[:3] = [datetime_obj]
                data_list = [str(item) for item in data_list] 
                df.loc[linha] = data_list
                linha += 1
        self.print_log('Tabela preenchida')
        return df


