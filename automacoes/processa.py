import pandas as pd 
import time

class Processa:
    def __init__(self):
        pass

    def print_log(self,texto):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print(f'[{current_time}] [Processa dados]: {texto}')

    def processa_dados(self, df):
        self.print_log('Processando dados')
        df['Date'] = pd.to_datetime(df['Date'])
        df['Open'] = df['Open'].apply(lambda x: x.replace(',', '') if isinstance(x, str) else x).replace('-', None).astype(float)
        df['High'] = df['High'].apply(lambda x: x.replace(',', '') if isinstance(x, str) else x).replace('-', None).astype(float)
        df['Low'] = df['Low'].apply(lambda x: x.replace(',', '') if isinstance(x, str) else x).replace('-', None).astype(float)
        df['Close'] = df['Close'].apply(lambda x: x.replace(',', '') if isinstance(x, str) else x).replace('-', None).astype(float)
        df['Adj Close'] = df['Adj Close'].apply(lambda x: x.replace(',', '') if isinstance(x, str) else x).replace('-', None).astype(float)
        df['Volume'] = df['Volume'].apply(lambda x: x.replace(',', '') if isinstance(x, str) else x).replace('-', None).astype(float)
        self.print_log('Dados processados')
        return df
    
    def trata_dados(self, df):
        self.print_log('Tratando dados')
        new_df = pd.DataFrame()
        new_df['Month'] = df['Date'].dt.strftime('%B %Y')
        new_df['max_open'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Open'].transform('max')
        new_df['min_open'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Open'].transform('min')
        new_df['max_close'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Close'].transform('max')
        new_df['min_close'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Close'].transform('min')
        new_df['close'] = round(df.groupby(df['Date'].dt.strftime('%B %Y'))['Close'].transform('mean'),2)
        new_df['max_high_month'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['High'].transform('max')
        new_df['min_high_month'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['High'].transform('min')
        new_df['max_low_month'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Low'].transform('max')
        new_df['min_low_month'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Low'].transform('min')
        new_df['max_volume'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Volume'].transform('max')
        new_df['min_volume'] = df.groupby(df['Date'].dt.strftime('%B %Y'))['Volume'].transform('min')
        new_df = new_df.drop_duplicates(subset=['Month'])
        self.print_log('Dados tratados')
        return new_df
    
    def salva_dados(self, df, banco):
        self.print_log('Salvando dados')
        df.to_csv(f'./downloads/{banco}_tratado.csv', index=False)
        self.print_log(f'Arquivo {banco}_tratado.csv criado e salvo na pasta downloads')
        return df
    
    def calcular_variacao(self,df,banco):
        self.print_log('Calculando variação')
        linhas = [banco,df.close.std(),df.close.mean(),round((df.close.std()/df.close.mean())*100,2)]
        self.print_log(f'Variação da acao {banco} calculada')
        return linhas
    


