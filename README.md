# Trabalho XML-RPC - Previsão do Tempo

Este projeto é um sistema de previsão do tempo que utiliza o protocolo XML-RPC para comunicação entre cliente e servidor. Ele permite consultar uma previsão do tempo para uma cidade específica e exibe informações como temperatura, condição climática, umidade e velocidade do vento, além de uma previsão para os próximos dias geradas de forma aleatória.

## Como funciona

1. **Servidor XML-RPC**:
   - O servidor é responsável por gerar os dados climáticos de forma aleatória e coerente, incluindo temperatura, condição climática e outros detalhes.
   - Ele utiliza o protocolo XML-RPC para responder às solicitações do cliente.

2. **Cliente Flask**:
   - O cliente é uma aplicação web desenvolvida com Flask.
   - Ele envia solicitações ao servidor XML-RPC para obter os dados climáticos.
   - Os dados são processados e exibidos em uma interface amigável, com ícones representando as condições climáticas.

3. **Interface do Usuário**:
   - A interface permite que o usuário insira o nome de uma cidade para consultar a previsão do tempo.
   - Exibe a previsão atual e os próximos dias, com os dias da semana organizados dinamicamente.

## Instalação

Siga os passos abaixo para configurar e executar o projeto:

### 1. Clone o repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd trabalho-xmlrpc
```

### 2. Crie e ative um ambiente virtual
No Linux/MacOS:
```bash
python3 -m venv weather_rpc
source weather_rpc/bin/activate
```
No Windows:
```bash
python -m venv weather_rpc
weather_rpc\Scripts\activate
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Execute o servidor XML-RPC
```bash
python server.py
```
### 5. Execute o cliente Flask
```bash
python client.py
```
### 6. Acesse a aplicação
Abra o navegador e acesse `http://localhost:5000` para ver a interface do cliente Flask.