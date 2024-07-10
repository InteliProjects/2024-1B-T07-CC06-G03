# Documentação dos Resultados alcançados com a execução do algoritmo Nearest Neighbors

## Introdução

&emsp;&emsp;O algoritmo Nearest Neighbors é uma heurística de construção de rotas que busca encontrar a solução ótima para o Problema do Caixeiro Viajante (TSP) de forma mais rápida e eficiente. A ideia principal é iniciar a rota em um ponto qualquer e, a partir dele, visitar o ponto mais próximo que ainda não foi visitado. Esse processo é repetido até que todos os pontos tenham sido visitados, retornando ao ponto de origem ao final.

&emsp;&emsp;Neste contexto, o algoritmo Nearest Neighbors foi aplicado ao problema de otimização das rotas de leitura de hidrômetros da Aegea, com o objetivo de minimizar a distância total percorrida por rota para cada um dos leituristas. A seguir, apresentamos os resultados obtidos com a execução do algoritmo e as principais conclusões derivadas da análise dos resultados.

## Resultados

&emsp;&emsp; Após a execução do algoritmo Nearest Neighbors, o programa exibirá informações no console sobre o tempo total de viagem, a distância percorrida e o tempo total de execução. Além disso, se o tempo total de viagem for menor ou igual a 6 horas, a rota calculada será salva em um arquivo CSV na pasta "database". Caso contrário, uma mensagem informando que o tempo de viagem excedeu o limite será exibida, e a rota não será salva, isso foi feito para garantir que as rotas geradas sejam viáveis e atendam às restrições de tempo estabelecidas.


### Arquivo CSV de Saída

&emsp;&emsp;O arquivo CSV gerado pelo algoritmo Nearest Neighbors contém as informações da rota otimizada calculada, incluindo:

- Número de identificação do cliente: identificador único de cada cliente na rota.
- Latitude e longitude do cliente: coordenadas geográficas do cliente, utilizadas para calcular a distância entre os pontos de leitura.
- Logradouro do cliente: endereço do cliente, utilizado para identificar o local de leitura do hidrômetro.
- Número do cliente: número do endereço do cliente, utilizado para identificar o local de leitura do hidrômetro.


&emsp;&emsp;O arquivo CSV gerado pode ser utilizado para visualizar a rota otimizada no mapa e analisar a sequência de visitas aos clientes ao longo da rota. Além disso, as informações contidas no arquivo CSV podem ser utilizadas para calcular a distância total percorrida, o tempo total de viagem e outras métricas relevantes para avaliar a eficiência da rota otimizada, que são disponibilizadas no console após a execução do algoritmo.


### Saída do Console

&emsp;&emsp;As informações exibidas no console após a execução do algoritmo Nearest Neighbors incluem:

- Tempo total de viagem: tempo total necessário para percorrer a rota calculada, considerando a distância entre os pontos de leitura e a velocidade média de deslocamento.
- Distância total percorrida: distância total percorrida ao longo da rota calculada, considerando a distância entre os pontos de leitura.
- Tempo total de execução: tempo total necessário para executar o algoritmo Nearest Neighbors e calcular a rota otimizada.
- Mensagem de sucesso ou falha: indica se a rota foi calculada com sucesso e salva no arquivo CSV ou se o tempo de viagem excedeu o limite de 6 horas e a rota não foi salva.



### Resultados obtidos pelo algoritmo Nearest Neighbors

&emsp;&emsp; O algoritmo Nearest Neighbors foi executado diversas vezes com diferentes configurações de entrada, que variaram o número de clientes/pontos que seriam visitados pelo leiturista. Os resultados obtidos estão localizados na pasta "database" e o nome do arquivo muda conforme o número de clientes que foram visitados, por exemplo, "output_10.csv" indica que a rota otimizada possui 10 clientes e "output_20.csv" indica que a rota otimizada possui 20 clientes. Aqui está um exemplo de saída gerado pelo algoritmo Nearest Neighbors para diferentes configurações de entrada, com 10 e 500 clientes, respectivamente. No entanto, os resultados obtidos para outras configurações de entrada podem ser encontrados na pasta "database".

#### 10 Clientes

```csv
Id,Latitude,Longitude,Logradouro,Numero
1,-22.819022,-43.318819,PRES DUTRA,132.0
2,-22.818946,-43.318989,PRES DUTRA,142.0
3,-22.818946,-43.318989,PRES DUTRA,142.0
4,-22.818787,-43.319347,PRES DUTRA,192.0
5,-22.818847,-43.318282,PROF FRANCA AMARAL,15.0
6,-22.818825,-43.318116,PROF FRANCA AMARAL,42.0
7,-22.819011,-43.317944,PROF FRANCA AMARAL,12.0
8,-22.818902,-43.317523,DO VIGARIO GERAL,51.0
9,-22.818763,-43.317178,DO VIGARIO GERAL,123.0
10,-22.818599,-43.318277,PROF FRANCA AMARAL,84.0

```
 * mensagem no console: 

```console
Tempo total de viagem: 0 horas e 24 minutos. Dentro do limite de 6 horas.
Distância total percorrida: 0.41 Km.
Tempo total de execução: 0.22 segundos.
Arquivo 'output_10.csv' foi salvo com sucesso na pasta database.
```

&emsp;&emsp;Nesse caso o algoritmo salvou a rota otimizada no arquivo "output_10.csv" pois o tempo total de viagem foi menor que 6 horas, que está dentro do limite estabelecido. 

#### 500 Clientes

* mensagem no console: 

```console
Tempo total de viagem: 17 horas e 59 minutos. Fora do limite de 6 horas.
Distância total percorrida: 6.61 Km.
Tempo total de execução: 2.85 segundos.
Tempo de viagem excedeu o limite de 6 horas. Rota não foi salva.
```

&emsp;&emsp;Nesse caso o algoritmo não salvou a rota otimizada no arquivo "output_500.csv" pois o tempo total de viagem foi maior que 6 horas, que está fora do limite estabelecido.

## Conclusões

&emsp;&emsp;Os resultados obtidos com a execução do algoritmo Nearest Neighbors demonstram a eficácia dessa heurística na otimização das rotas de leitura de hidrômetros da Aegea. A abordagem de construção de rotas baseada na escolha do ponto mais próximo a ser visitado em cada etapa do percurso permitiu encontrar soluções viáveis e eficientes para o problema, minimizando a distância total percorrida por rota. Com isso, foi possível calcular a força de trabalho necessária para atender a demanda de leitura de hidrômetros no mês, que ao executar o algoritmo com 160 pontos de leitura, obteve-se um tempo total de viagem de 5 horas e 50 minutos, dentro do limite de 6 horas estabelecido. Dessa forma, foi feito um cálculo em que foi multiplicado 160 ( número de pontos de leitura) por 22 (dias de trabalho mensal), obtendo o número de pontos de leitura que um leiturista consegue atender em um mês. Baseado nisso, foi possível executar um algoritmo de clusterização para determinar o número de leituristas necessários para atender a demanda de leitura de hidrômetros no mês.

