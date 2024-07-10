# Análise de complexidade e corretude do algoritmo

## Análise de complexidade

### Estrutura e Funcionalidade do Algoritmo:
&emsp;&emsp;Para o algoritmo utilizado, foi criada uma combinação dos algoritmos heurísticos de Nearest Neighbors para realizar uma pré-otimização das rotas e o algoritmo de two-opt para melhorar essa otimização e reduzir cruzamentos, buscando uma solução mais rápida de percorrimento dos pontos em um problema de caixeiro viajante.


**Algoritmo *Nearest Neighbors***: O algoritmo de *Nearest Neighbors* (ou vizinho mais próximo) é um algoritmo heurístico que começa a partir de um ponto aleatório e busca o ponto vizinho mais próximo a ele, para que assim ele possa avançar para esse ponto. É utilizada a distância de haversine para calcular essa distância, e sua lógica se repete até que todos os pontos sejam percorridos.
Sua complexidade é de $O(n^2)$, pois ele deve verificar a distância até todos os pontos restantes e ver qual o mais próximo e, ainda assim, é considerado um algoritmo leve. Sua estratégia é considerada "gulosa", pois apenas busca uma otimização de mínimo local e não explora outras opções de combinação de percorrimento de pontos.

**Algoritmo *Two-Opt***: O algoritmo de *Two-Opt* é outro algoritmo heurístico, que pega uma rota já definida e muda os arranjos de suas arestas de forma a otimizar a função objetivo (no caso, minimizar distância) e remover cruzamentos que possam ter ocorrido. Ele é utilizado após a otimização do *Nearest Neighbors*, assim tendo seu trabalho já facilitado pela pré-otimização, porém ainda assim ajudando a melhorar como as rotas são construídas. Sua complexidade é de $O(n^2 \cdot k)$, onde *n* é a quantidade de pontos e *k* a quantidade de iterações realizadas até otimizar totalmente uma rota.

&emsp;&emsp;Como citado anteriormente, esses algoritmos se complementam, de forma que o *Nearest Neighbors* realiza uma otimização mais rápida e pior para que o *Two-Opt* consiga realizar uma melhor otimização e remova os cruzamentos.


&emsp;&emsp;A fim de melhorar ainda mais a velocidade do código, foram utilizadas estratégias de clusterização para dividir um problema inviável de ser percorrido em subproblemas menores, dividindo o conjunto em rotas e cada rota em diversos dias, assim reduzindo a complexidade do problema. Para isso foram criadas as variáveis:


- $r$: Quantidade de rotas;
- $d$: Quantidade de dias;
- $n$: Quantidade média de pontos por rota;
- $k$: Quantidade de iterações realizadas pelo *Two-Opt*;

&emsp;&emsp;Anteriormente, a complexidade combinada do *Nearest Neighbors* com o *Two-Opt* era de $O(n^2 \cdot k)$, porém com a clusterização ela se torna $O(r \cdot d \cdot n^2 \cdot k)$. Com essa nova complexidade, a quantidade de pontos que anteriormente estava presente na função exponencial de 2 é reduzida, onde esses valores são diluídos nas variáveis $r$ e $d$, reduzindo assim a complexidade. Por exemplo, se tivéssemos 30 mil pontos na complexidade antiga e utilizássemos 20 iterações de Two-Opt por ponto, teríamos uma complexidade de mais de 18 bilhões. Com a estratégia de clusterização, diluímos esses 30 mil pontos em 60 rotas e 22 dias, mantendo 50 iterações. Dessa forma, temos aproximadamente 23 pontos. Realizando os cálculos, isso resulta em uma complexidade de aproximadamente 14 milhões. Isso mostra uma melhoria significativa, reduzindo enormemente o tempo de processamento.

### Análise de pior e melhor caso

&emsp;&emsp;Para analisar os casos, é necessário entendermos o comportamento das variáveis que complementam *n*, que são *r*, *d*, *k*. As variáveis de *r* e *d* influenciam diretamente em como a complexidade do algoritmo funciona, pois com seu aumento a variável *n* tem seu valor diminuído. A variação de *n* é o que mais influencia a complexidade do algoritmo, por ser uma função exponencial, e quanto maior o seu valor maior a complexidade. Por fim, temos a variável *k* onde, quanto maior a quantidade de cruzamentos e mudanças que o *Two-Opt* tem de fazer, maior a complexidade do algoritmo.

&emsp;&emsp; Assim, temos:

  - Complexidade &Theta; (Pior caso): A complexidade Theta do algoritmo é expressa como &Theta;( r . d . n² . k ), Este valor reflete o comportamento típico ou o caso médio do algoritmo, assumindo que as condições normais são mantidas, como uma distribuição de distâncias razoavelmente uniforme entre os pontos e uma quantidade moderada de iterações. Sua eficiência varia muito de acordo com os valores de *r* e *d* onde, se ambos forem baixos, o valor de n² é mais elevado e, dessa forma, aumenta demais a complexidade do problema. Também temos k, que, caso o algoritmo do *Two-Opt* tenha de fazer muitas mudanças, tem seu valor elevado e afeta a complexidade do algoritmo.
  
- Complexidade &Omega; (Melhor caso): A complexidade Ômega do algoritmo é expressa como &Omega;(r . d . n²). Esse valor descreve o melhor caso garantido do algoritmo, onde a quantidade de iterações 𝑘  do Two-Opt é mínima, possivelmente igual a um, indicando que quase nenhuma melhoria é necessária após a aplicação do Nearest Neighbors. Além disso, valores maiores de *r* e *d* reduzem o valor de *n²*, dessa forma reduzindo o valor dessa variável exponencial e reduzindo drasticamente a complexidade do problema.

# Complexidade e Corretude do Sistema de Roteamento

## Análise de Corretude

### Introdução à Corretude

A corretude de um algoritmo é essencial para garantir resultados confiáveis para todas as entradas válidas. Nos algoritmos `nearest_neighbor` e `walker`, essa corretude se traduz na capacidade de calcular rotas precisas e eficientes com base na proximidade geográfica.

### Corretude do `nearest_neighbor`

**Invariantes de Laço:**
- A lista `visited` contém um caminho que é o mais curto possível a partir do ponto inicial, percorrendo apenas os pontos já visitados.

**Demonstração Formal por Indução:**
- **Base da Indução:** Com um ponto em `visited`, o caminho é o mais curto.
- **Hipótese de Indução:** Após `k` iterações, `visited` contém um caminho ótimo.
- **Passo de Indução:** Adicionar o próximo ponto mais próximo mantém o caminho ótimo para `k+1` pontos.
- **Conclusão:** `visited` contém um caminho que é o mais curto possível.

### Corretude do `walker`

- **Condições de Funcionamento:** Requer todas as colunas necessárias presentes e manipula os dados corretamente.
- **Garantia de Terminação:** Processa todos os grupos de dados finitos dentro de um número limitado de dias e rotas.
- **Resultados Esperados:** Produz rotas diárias com distâncias e tempos calculados consistentemente.

### Corretude das Funções de _Clusterização_ e Simulação

**Integração de _Clusterização_:**
- Utiliza `MiniBatchKMeans` para agrupar pontos com base em sua localização geográfica, garantindo que os pontos dentro de um mesmo _cluster_ estão próximos entre si.
- A divisão em _ sub-clusters_ para rotas diárias assegura a distribuição equitativa dos pontos por dia, facilitando o planejamento logístico.

**Simulação e Análise de Rotas:**
- A função `simulate` integra a _clusterização_ e a formação de rotas, medindo o tempo de processamento e garantindo que os resultados refletem uma simulação realista das condições operacionais.
- As rotas construídas consideram distâncias calculadas pela função `haversine` e são otimizadas para minimizar o tempo de viagem e maximizar a eficiência logística.

### Conclusão da Análise de Corretude

A corretude dos algoritmos `nearest_neighbor`, `walker`, e das funções de _clusterização_ e simulação, é confirmada pela precisão dos cálculos de distância e pela eficácia na formação de rotas que respeitam limites temporais e geográficos. A integração desses componentes forma um sistema robusto que garante a confiabilidade e eficiência necessária para aplicações práticas em logística e planejamento de rotas.