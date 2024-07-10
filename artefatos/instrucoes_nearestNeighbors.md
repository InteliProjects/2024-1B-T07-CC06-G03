# Guia para Executar o Algoritmo Nearest Neighbors para Roteamento de Leituristas

&emsp;&emsp;Este guia destina-se a explicar como executar o algoritmo `nearestNeighbors.py`, bem como entender sua saída. O algoritmo é projetado para calcular uma rota ótima para leitura de hidrômetros com base em dados geográficos de entrada. A saída inclui informações sobre o tempo total de viagem, a distância percorrida e a rota calculada.

## Requisitos de Instalação

&emsp;&emsp;Para executar o algoritmo, você precisa ter o Python instalado em seu sistema. Além disso, as seguintes bibliotecas Python devem ser instaladas:

- pandas
- haversine

&emsp;&emsp;Você pode instalar essas bibliotecas usando o pip, através do seguinte comando no terminal:

```bash
pip install pandas haversine
```

## Como Executar o Algoritmo

1. **Baixe o Código**: Faça o download do código fonte do algoritmo em Python ou clone o repositório do projeto em sua máquina local, caso clone o repositório. 

    ```bash
    git clone https://github.com/Inteli-College/2024-1B-T07-CC06-G03.git
    ```
2. **Navegue até o diretório do código fonte**: Navegue até o diretório onde o código fonte do algoritmo está localizado.
    ```bash
    cd .\codigo\backend\algoritmo\
    ``` 
3. **Prepare os Dados de Entrada**: O algoritmo requer um arquivo CSV contendo dados de latitude, longitude e outros detalhes sobre os pontos de leitura. Certifique-se de que o arquivo CSV esteja corretamente formatado e acessível pelo algoritmo.

4. **Execute o Algoritmo**: No terminal, navegue até o diretório onde o código fonte do algoritmo está localizado. Em seguida, execute o seguinte comando:

    ```bash
    python nearestNeighbors.py <number_of_rows>
    ```

&emsp;&emsp;Substitua `<number_of_rows>` pelo número de linhas de dados que você deseja processar. Este argumento é necessário para indicar ao algoritmo quantas linhas de dados do arquivo CSV devem ser consideradas.

&emsp;&emsp;Por exemplo:

```bash
python nearestNeighbors.py 100
```

&emsp;&emsp;Isso irá executar o algoritmo utilizando as primeiras 100 linhas do arquivo de dados.

1. **Analise a Saída**: O algoritmo exibirá informações no console sobre o tempo total de viagem, a distância percorrida e o tempo total de execução. Além disso, se o tempo total de viagem for menor ou igual a 6 horas, a rota calculada será salva em um arquivo CSV na pasta "database". Caso contrário, uma mensagem informando que o tempo de viagem excedeu o limite será exibida, e a rota não será salva.

## Sobre a Saída

- **Tempo Total de Viagem**: Indica o tempo total necessário para percorrer a rota calculada, considerando a velocidade média do leiturista e o tempo de leitura de cada ponto.

- **Distância Total Percorrida**: Representa a distância total percorrida ao longo da rota, medida em quilômetros.
- **Tempo Total de Execução**: Mostra o tempo total que o algoritmo levou para processar os dados e calcular a rota.
- **Status da Execução**: Informa se o tempo total de viagem está dentro do limite de 6 horas. Se estiver dentro do limite, a rota calculada será salva em um arquivo CSV; caso contrário, a rota não será salva.

&emsp;&emsp;Além disso, o arquivo de saída, denominado "output<number_of_rows>.csv", contém informações sobre a rota calculada pelo algoritmo de roteamento de leituristas. Este arquivo CSV possui as seguintes colunas:

1. **Id**: Um identificador único para cada ponto na rota.
2. **Latitude**: A latitude do ponto geográfico.
3. **Longitude**: A longitude do ponto geográfico.
4. **Logradouro**: O nome do logradouro associado ao ponto.
5. **Numero**: O número do endereço associado ao ponto.

&emsp;&emsp;Cada linha no arquivo representa um ponto na rota calculada, com sua respectiva latitude, longitude, logradouro e número do endereço.

&emsp;&emsp;Ademais, cada linha representa um ponto na rota, com suas respectivas informações de latitude, longitude, logradouro e número. Este arquivo pode ser utilizado para visualizar a rota em um mapa ou para qualquer outra análise que seja necessária.

## Conclusão

&emsp;&emsp;Este guia fornece instruções claras sobre como executar o algoritmo `nearestNeighbors.py`, bem como interpretar sua saída. Certifique-se de fornecer os dados de entrada corretos e acompanhar as informações apresentadas no console para entender melhor o desempenho do algoritmo e os resultados obtidos.