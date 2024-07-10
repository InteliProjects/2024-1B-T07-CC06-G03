# 2024-1B-T07-CC06-G03

<table>
<tr>
<td>
<a href= "https://www.aegea.com.br/"><img src="./artefatos/imagens/logos/logo-aegea.png" alt="Aegea" border="0" width="60%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="./artefatos/imagens/logos/inteli-logo.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="40%"></a>
</td>
</tr>
</table>

# Introdução

&emsp;&emsp;O projeto desenvolvido pelo grupo E6eu visa criar uma solução de otimização para as rotas de leitura de hidrômetros de consumo mensal da Aegea Saneamento. Nosso objetivo é maximizar a eficiência e precisão na prestação desses serviços essenciais, contribuindo para a melhoria dos processos operacionais da empresa.

# Projeto: Solução de otimização para rotas de leitura de hidrômetros de consumo mensal

# Grupo: _E6eu_

# Integrantes:

- <a href="https://www.linkedin.com/in/filipe-calabro-3b3517243/">Filipe Calabro</a>
- <a href="https://www.linkedin.com/in/hugo-noyma/">Hugo Noyma</a>
- <a href="https://www.linkedin.com/in/isabelle-santos-507067204/">Isabelle Santos</a>
- <a href="https://www.linkedin.com/in/lucasbmr/">Lucas Rego</a>
- <a href="https://www.linkedin.com/in/pedro-bannwart/">Pedro Bannwart</a>
- <a href="https://www.linkedin.com/in/tommygoto/">Tommy Goto</a>

##  Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/tmsasaki?originalSubdomain=br">Tomaz Mikio Sasaki</a>
### Instrutores
- <a href="https://www.linkedin.com/in/rafael-will-m-de-araujo-20809b18b/?originalSubdomain=br">Rafael Will M. de Araujo</a>
- <a href="https://www.linkedin.com/in/cristinagramani/?originalSubdomain=br">Cristina Gramani</a>
- <a href="https://www.linkedin.com/in/anacristinadossantos/?originalSubdomain=br">Ana Cristina dos Santos</a>
- <a href="https://www.linkedin.com/in/flavia-santoro-79704820?originalSubdomain=br">Flavia Santoro</a> 
- <a href="https://www.linkedin.com/in/janainamandra/?originalSubdomain=br">Janaína Mandra Garcia</a>
- <a href="https://www.linkedin.com/in/pedroteberga?originalSubdomain=br">Pedro Teberga</a>
- <a href="https://www.linkedin.com/in/sergio-venancio-a509b342/?originalSubdomain=br">Sergio Venancio</a>
- <a href="https://www.linkedin.com/in/rodolfo-goya-6ab187/">Rodolfo Goya</a> 

# Descrição

&emsp;&emsp;Este projeto aborda o desafio de otimizar as rotas de leitura de hidrômetros para a Aegea Saneamento e Participações S.A., uma das líderes no setor de saneamento no Brasil. O foco principal é aumentar a eficiência e a precisão na coleta dos dados de consumo de água, uma operação crítica para a empresa. Um algoritmo otimizador desenvolvido especificamente para esse fim foi utilizado, levando em consideração múltiplas variáveis operacionais, incluindo dias de leitura, horas de trabalho diárias, velocidade dos leituristas e número de leituristas.

&emsp;&emsp;O algoritmo proposto é inspirado no Problema do Caixeiro Viajante (PCV), adaptado para contemplar múltiplos "caixeiros" (leituristas) e otimizar várias rotas simultaneamente. A abordagem foi complementada com estudos de caso e metodologias que foram aplicadas em outros contextos de otimização de rotas, como concessionárias de energia elétrica, para desenvolver uma solução robusta e adaptável.

&emsp;&emsp;Os resultados obtidos demonstram a viabilidade da solução em reduzir significativamente a distância total percorrida e o tempo necessário para completar as rotas, além de equilibrar melhor a carga de trabalho entre os leituristas. Este estudo não apenas melhora a operacionalidade da Aegea, mas também contribui para a satisfação do cliente e sustentabilidade ambiental, ao minimizar o tempo de deslocamento e maximizar a eficiência do processo de leitura de hidrômetros.


# Código

Esta é a pasta para o código dos componentes de software desenvolvidos pelo grupo.

   ```
   - codigo
      - algoritmos
      - analise_dados
      - backend
      - database
      - frontend
   ```

# Configuração de desenvolvimento

Para baixar e executar o código deste projeto, siga os passos abaixo:

Clone o repositório usando:

```
git clone https://github.com/Inteli-College/2024-1B-T07-CC06-G03.git

```

## Rodando o Backend da aplicação

### Requisitos

#### Rodando o backend através das extensões do Python

#### Rodando o backend através do terminal

1. No repositório clonado, vá para a pasta do _backend_ através desse comando no terminal
   ```
   cd .\codigo\backend\
   ```
2. Dentro desse diretório, execute o seguinte comando para instalar as depndências corretas do _backend_ do projeto:
    ```
   pip install -r requirements.txt
   ```
3. Dentro desse diretório, execute o seguinte comando para rodar o _backend_ do projeto:
   ```
   python run.py
   ```
3. O terminal exibirá o processamento e, uma vez que o backend estiver totalmente carregado e em execução, você verá mensagens indicando que o servidor está pronto para aceitar conexões. Certifique-se de observar qualquer mensagem de erro ou aviso que possa surgir durante o processo de inicialização.

## Rodando o Frontend da aplicação

### Requisitos

1. No repositório clonado, vá para a pasta do _frontend_ através desse comando no terminal
   ```
   cd .\codigo\frontend\
   ```

2. Dentro desse diretório, execute o seguinte comando para instalar as depndências corretas do _frontend_ do projeto:
    ```
   npm install
   ```

3. Dentro desse diretório, execute o seguinte comando para rodar o _frontend_ do projeto:
   ```
   npm run dev
   ```
4. O terminal exibirá o processamento e, uma vez que o backend estiver totalmente carregado e em execução, você verá mensagens indicando que o servidor está pronto para aceitar conexões. Certifique-se de observar qualquer mensagem de erro ou aviso que possa surgir durante o processo de inicialização.

# Releases

- SPRINT1: 26/04/2024  
    * Entendimento do problema.
    * Entendimento do negócio.
    * Entendimento da experiência do usuário.
- SPRINT2: 10/05/2024 
    * Versão simplificada do problema.
    * Artigo inicial.
    * Protótipo front-end.
- SPRINT3: 24/05/2024
    * Front-end da aplicação.
    * 2a versão do artigo.
    * Desenvolvimento do back-end da aplicação.
- SPRINT4: 07/06/2024
     * Complexidade e corretude do algoritmo.
     * Atualização do artigo.
     * Integração da aplicação (back-end e front-end).
- SPRINT5: 21/06/2024  
     * Finalização dos ajustes na aplicação.
     * Revisão do Código.
     * Conclusão e revisão do artigo.

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">

<a property="dct:title" rel="cc:attributionURL">Grupo</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName">Inteli, [Filipe Calabro](https://www.linkedin.com/in/filipe-calabro-3b3517243/), [Hugo Noyma](https://www.linkedin.com/in/hugo-noyma/), [Isabelle Santos](https://www.linkedin.com/in/isabelle-santos-507067204/), [Pedro Bennwart](https://www.linkedin.com/in/pedro-bannwart/), [Lucas Rego](https://www.linkedin.com/in/lucasbmr/), [Tommy Goto](https://www.linkedin.com/in/tommygoto/)</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
