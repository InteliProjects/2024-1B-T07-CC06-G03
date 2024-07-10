# Guia para Executar o _Backend_ em Flask e Rodar Testes da API E6eu

## 1. Clonar o Repositório

&emsp;&emsp;Clone o repositório do _backend_ Flask para sua máquina local usando o Git:

```bash
git clone https://github.com/Inteli-College/2024-1B-T07-CC06-G03.git
```

## 2. Instalar Dependências

&emsp;&emsp;Certifique-se de ter o Python e o pip instalados. Em seguida, navegue até o diretório do projeto e instale as dependências necessárias usando o arquivo `requirements.txt`:

```bash
cd .\codigo\backend\
pip install -r requirements.txt
```

&emsp;&emsp;Isso instalará todas as bibliotecas Python necessárias para o projeto.

## 3. Configurar Ambiente Virtual (Essencial para a execução dos testes unitários)

&emsp;&emsp;É uma boa prática configurar um ambiente virtual para isolar as dependências do seu projeto. Use o seguinte comando para criar e ativar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

&emsp;&emsp;Isso criará um ambiente virtual chamado `venv` e o ativará.

## 4. Iniciar o Servidor Flask

&emsp;&emsp;Para iniciar o servidor Flask, é necessário executar o arquivo principal do seu aplicativo. Geralmente, o arquivo principal é chamado `app.py` ou `run.py`. Use o seguinte comando para iniciar o servidor:

```bash
python run.py
```

## 5. Executar Testes

### 5.1 Testes Unitários

&emsp;&emsp;Certifique-se de que está no diretório raiz do seu projeto. Em seguida, execute os testes usando pytest:

```bash
pytest
```

&emsp;&emsp;Isso executará todos os testes encontrados no projeto.

### 5.2 Testes no Postman

&emsp;&emsp;É possível realizar testes da API Flask usando o Postman, uma ferramenta popular para testar APIs. Para facilitar a configuração dos testes no Postman, fornecemos uma coleção pronta que contém uma série de requisições pré-configuradas para interagir com sua API.

* Para acessar a coleção no Postman, siga o link abaixo:

    [_Collection_ de Testes no Postman](https://speeding-meteor-26896.postman.co/workspace/New-Team-Workspace~dbc2dfef-7156-4920-97f0[…]4e70-85d0-fe344defdcad?action=share&creator=33784019)

&emsp;&emsp;Certifique-se de importar esta coleção no seu ambiente do Postman para começar a executar os testes na sua API Flask.

&emsp;&emsp;Esta coleção inclui uma variedade de solicitações `HTTP`, como `GET`, `POST`, `PUT` e `DELETE`, para testar diferentes endpoints da sua API. Além disso, cada solicitação inclui exemplos de dados de entrada e saída, para ajudá-lo a entender como formatar suas solicitações corretamente.

&emsp;&emsp;Na rota `upload`, é crucial a inserção do arquivo `csv` contendo os dados fornecidos pela Aegea. Quanto aos demais arquivos de entrada (_body_ -> _raw_) das rotas `start_simulation` e `start_automation`, eles já estão pré-definidos na coleção, portanto, não será necessário ajustá-los.

# 6. Conlcusões

&emsp;&emsp;Ao usar o Postman para testar a API da equipe **E6eu**, é possível verificar se todas as rotas estão respondendo corretamente e se os dados são processados e retornados conforme o esperado. Isso é fundamental para garantir o bom funcionamento da aplicação e para identificar e corrigir possíveis problemas ou _bugs_.