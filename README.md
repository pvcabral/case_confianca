# Projeto de Automação de Coleta de Dados de Ações

Este projeto tem como objetivo automatizar a coleta de dados de ações financeiras e armazená-los em um banco de dados SQL Server. O script realiza a coleta dos dados utilizando o Selenium, configurações específicas de acesso ao banco de dados e opções personalizadas definidas em arquivos de configuração.

## Requisitos

Antes de utilizar o script, você precisa garantir que o seu ambiente está configurado corretamente. Siga os passos abaixo:

### 1. Instalar o Google Chrome e Google Drive

1. **Verifique a versão do seu Google Chrome**.
2. **Baixe a versão correspondente do Google Drive**:  
   Acesse o link abaixo para baixar a versão do Google Drive compatível com a versão do seu Chrome:  
   [Baixar ChromeDrive](https://googlechromelabs.github.io/chrome-for-testing/)
3. **Instale o ChromeDrive** na pasta do seu Windows.
4. Utilize o comando ```python pip install -r requirements.txt``` para baixar os requirements.


### 2. Instalar e Configurar o SQL Server

Para armazenar os dados coletados, você precisa ter o SQL Server instalado e configurado corretamente. Siga os passos abaixo para configurar o SQL Server:

#### 2.1 Baixar e Instalar o SQL Server

1. **Baixar o SQL Server**:
   - Acesse o site oficial da Microsoft para baixar o SQL Server:  
     [Baixar SQL Server](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads)
   - Escolha a edição desejada (a edição Developer é gratuita e possui todos os recursos).

2. **Instalar o SQL Server**:
   - Execute o instalador e siga as instruções para instalar o SQL Server.
   - Durante a instalação, selecione a opção "Instalação padrão" para configurar um servidor SQL básico.

#### 2.2 Criar o Servidor e o Banco de Dados

Após a instalação do SQL Server:

1. **Abrir o SQL Server Management Studio (SSMS)**:
   - Se o SSMS não estiver instalado, você pode baixá-lo [aqui](https://docs.microsoft.com/pt-br/sql/ssms/download-sql-server-management-studio-ssms).

2. **Conectar ao SQL Server**:
   - Abra o SSMS e conecte-se ao servidor SQL utilizando a autenticação configurada durante a instalação (pode ser Autenticação do Windows ou do SQL Server).

3. **Criar um Banco de Dados**:
   - No SSMS, clique com o botão direito em "Databases" e selecione "New Database...".
   - Nomeie o banco de dados como `dados_acoes` (ou o nome especificado no arquivo `settings.json`).

**Importante**: O script cria automaticamente as tabelas necessárias no banco de dados `dados_acoes` quando é executado pela primeira vez. Não é necessário criar as tabelas manualmente.

### 3. Configurar o Ambiente

#### 3.1 Criar a Pasta de Downloads

Crie uma pasta chamada `downloads` no diretório onde o script será executado. Essa pasta será utilizada para armazenar os arquivos baixados.

#### 3.2 Configurar Credenciais de Acesso ao Banco de Dados

Crie um arquivo chamado `settings.json` no mesmo diretório do script com a seguinte estrutura:

```json
{
    "server": "server_banco",
    "database": "nome_do_banco",
    "username": "user_banco",
    "password": "password_banco"
}
```
