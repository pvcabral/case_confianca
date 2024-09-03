from automacoes.navegador import Navegador
from automacoes.processa import Processa
from exportacoes.banco_de_dados import Exportacao_banco
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import pandas as pd

with open('config.json') as f:
    config = json.load(f)


BANCOS = config['BANCOS']

def main():
    navegador = Navegador()
    for banco in BANCOS:
        navegador.abrir_pagina(f'https://finance.yahoo.com/quote/{banco}/history/')
        df = navegador.criar_tabela('//*[@id="nimbus-app"]/section/section/section/article/div[1]/div[3]/table')
        df.to_csv(f'./downloads/{banco}.csv', index=False)
        navegador.print_log(f'Arquivo {banco}.csv criado na pasta downloads')

    processa = Processa()
    exportacao = Exportacao_banco()
    for banco in BANCOS:
        df = pd.read_csv(f'./downloads/{banco}.csv')
        df = processa.processa_dados(df)
        df = processa.trata_dados(df)
        df = processa.salva_dados(df, banco)
        df = exportacao.exporta_banco(df, banco)

    
    df = pd.DataFrame(columns=['banco','std_close','mean_close', 'variation_close'])
    tamanho = 0
    for banco in BANCOS:
        dados_tratatados = pd.read_csv(f'./downloads/{banco}_tratado.csv')
        linha = processa.calcular_variacao(dados_tratatados, banco)
        df.loc[tamanho] = linha
        tamanho += 1
    df = exportacao.exporta_banco(df, 'Variacao_acoes')

    
if __name__ == '__main__':
    main()