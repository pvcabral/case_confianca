import pandas as pd
from sqlalchemy import create_engine
import time
import json


with open('settings.json') as f:
    config = json.load(f)

SERVER = config['server']
DATABASE = config['database']
USERNAME = config['username']
PASSWORD = config['password']
class Exportacao_banco: 
    def __init__(self):
        pass

    def print_log(self,texto):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print(f'[{current_time}] [Exportacao banco]: {texto}')

    def exporta_banco(self, df, banco):
        self.print_log('Exportando dados para o banco')
        engine = create_engine(f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server')
        df.to_sql(banco, con=engine, if_exists='replace', index=False)
        self.print_log(f'Dados da tabela {banco} exportados')
        return df
