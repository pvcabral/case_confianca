# Projeto de Automação de Coleta de Dados de Ações

Este projeto tem como objetivo automatizar a coleta de dados de ações financeiras e armazená-los em um banco de dados SQL Server. O script realiza a coleta dos dados utilizando o selenium, configurações específicas de acesso ao banco de dados e opções personalizadas definidas em arquivos de configuração.

## Requisitos

Antes de utilizar o script, você precisa garantir que o seu ambiente está configurado corretamente. Siga os passos abaixo:

### 1. Instalar o Google Chrome e Google Drive

1. **Verifique a versão do seu Google Chrome**.
2. **Baixe a versão correspondente do Google Drive**:  
   Acesse o link abaixo para baixar a versão do Google Drive compatível com a versão do seu Chrome:  
   [Baixar Google Drive](https://googlechromelabs.github.io/chrome-for-testing/)
3. **Instale o Google Drive** na pasta do seu Windows.

### 2. Configurar o Ambiente

#### 2.1 Criar a Pasta de Downloads

Crie uma pasta chamada `downloads` no diretório onde o script será executado. Essa pasta será utilizada para armazenar os arquivos baixados.

#### 2.2 Configurar Credenciais de Acesso ao Banco de Dados

Crie um arquivo chamado `settings.json` no mesmo diretório do script com a seguinte estrutura:

```json
{
    "server": "servidor_do_banco_de_dados",
    "database": "nome_do_banco_de_dados",
    "username": "username_banco",
    "password": "password_banco"
}
