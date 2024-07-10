# Instruções para Executar a Aplicação React com Back-End em Flask

## Pré-requisitos

Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas em seu sistema:

- [Node.js e npm](https://nodejs.org/en/download/)
- [Python 3.x](https://www.python.org/downloads/)
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/)

## Passos para Baixar e Executar as Dependências da Aplicação React

1. **Clone o Repositório:**
   
   Abra o terminal e clone o repositório da aplicação. Use o seguinte comando:
   ```bash
   git clone https://github.com/Inteli-College/2024-1B-T07-CC06-G03.git
   ```

2. **Navegue até a Pasta do Projeto React:**

   No terminal, navegue até a pasta do projeto React:
   ```bash
   cd .\codigo\frontend\
   ```

3. **Instale as Dependências:**

   No terminal, instale as dependências do projeto usando npm:
   ```bash
   npm install
   ```

4. **Execute a Aplicação React:**

   No terminal, execute a aplicação React com o comando:
   ```bash
   npm run dev
   ```

5. **Acesse a Aplicação no Navegador:**

   Abra seu navegador e acesse:
   ```
   http://localhost:5173/
   ```

## Passos para Executar o Back-End em Flask

1. **Navegue até a Pasta do Projeto Flask:**

   Abra um novo terminal ou um novo painel no terminal dividido do VS Code e navegue até a pasta do projeto Flask:
   ```bash
   cd .\codigo\backend\
   ```

2. **Crie um Ambiente Virtual:**

   Crie um ambiente virtual para o projeto:
   ```bash
   python -m venv venv
   ```

3. **Ative o Ambiente Virtual:**

   Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as Dependências:**

   Com o ambiente virtual ativado, instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o Back-End Flask:**

   No terminal, execute a aplicação Flask:
   ```bash
   python run.py
   ```

## Executando com o Terminal Dividido no VS Code

1. **Abrir o VS Code:**

   Abra o Visual Studio Code e abra a pasta do repositório clonado.

2. **Abrir o Terminal Dividido:**

   - Pressione `Ctrl + Shift + ` para abrir um novo terminal.
   - Clique no ícone de dividir terminal (um ícone de tela dividida) para criar um terminal dividido.
   
3. **Configurar o Terminal para o Front-End:**

   - No primeiro terminal, navegue até a pasta do projeto React e execute a aplicação:
     ```bash
     cd .\codigo\frontend\
     npm run dev
     ```

4. **Configurar o Terminal para o Back-End:**

   - No segundo terminal, navegue até a pasta do projeto Flask e execute a aplicação:
     ```bash
     cd .\codigo\backend\
     source venv/bin/activate  # (ou venv\Scripts\activate no Windows)
     python run.py
     ```

5. **Acesse a Aplicação no Navegador:**

   Abra seu navegador e acesse:
   ```
   http://localhost:5173/
   ```

&emsp;&emsp;Com esses passos, você terá tanto o _front-end_ em React quanto o _back-end_ em Flask rodando simultaneamente em um terminal dividido no VS Code.

## Resumo

- Clone o repositório.
- Navegue até a pasta `cd .\codigo\frontend` e instale as dependências com `npm install`.
- Execute a aplicação React com `npm run dev`.
- Navegue até a pasta `cd .\codigo\backend\`, crie e ative um ambiente virtual, instale as dependências com `pip install -r requirements.txt`, e execute o back-end Flask com `python run.py`.
- Use o terminal dividido no VS Code para gerenciar ambos os serviços simultaneamente.

Siga essas instruções para garantir que sua aplicação React com back-end em Flask esteja configurada e executando corretamente.