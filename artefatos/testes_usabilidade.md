# Testes de usabilidade da plataforma

&emsp;&emsp;Os testes de usabilidade são essenciais no desenvolvimento de _software_ e aplicações, pois permitem avaliar como usuários reais interagem com o produto. Através desses testes, é possível identificar e corrigir problemas de interação que podem não ser evidentes para os desenvolvedores mas que afetam negativamente a experiência do usuário. Além disso, os testes de usabilidade ajudam a reduzir os custos de desenvolvimento ao identificar problemas cedo no processo, aumentam a satisfação e a retenção dos usuários ao melhorar a usabilidade e a acessibilidade, e oferecem dados valiosos que apoiam decisões informadas durante o desenvolvimento.

## Testes de usabilidade

&emsp;&emsp;Para os testes de usabilidade, foram selecionadas pessoas que se encaixassem no perfil de gestão representado pela persona do projeto, de forma a entender como esse usuário se comporta ao utilizar a plataforma, se ela atende a todas as necessidades do cliente e é entendível e navegável.

&emsp;&emsp;Foram desenvolvidas algumas tarefas, e o desempenho do usuário em concluir as respectivas tarefas foi anotado em forma de [planilha](https://docs.google.com/spreadsheets/d/1S2-av-HPREhq1ombQiz0CiFgPJB2H9I0su1Xq9KxHIo/edit?usp=sharing), para se ter uma maior noção de como foi a utilização entre usuários da plataforma:

## Conclusões e melhorias

### Análise dos testes realizados
&emsp;&emsp;Com base nos testes realizados com os usuários, é possível perceber alguns padrões de interação dos usuários com a plataforma e elencar-los:
- Em geral, não houveram problemas com o entendimento dos inputs e como executar o algoritmo;
- A interpretação da tabela foi possível, apesar de contar com alguns erros de interpretação dos usuários, principalmente quanto aos dias que eram entendidos não como "subdivisões" das rotas, e sim como uma medida quantitativa;
- Metade dos usuários não reparou / entendeu as métricas geradas pelo algoritmo, algo que curiosamente mudava caso a tabela fosse menor, pois essas informações se tornavam mais visíveis
- Ações extras para manipulação da tabela e algoritmo funcionaram bem, com todos conseguindo usar os filtros, baixar os outputs do algoritmo e reiniciar o algoritmo;
- Mesmo sabendo onde resetar o algoritmo, nenhum dos usuários o fez antes de rodas o próximo algoritmo (necessário para o funcionamento);
- Acessar um dia específico do algoritmo foi, em geral, uma tarefa fácil, porém um dos usuários tentou clicar na linha da tabela ao invés de diretamente no "dia" da linha, fazendo com que ocorresse uma falha no acesso da tela detalhada;
- A interpretação da tabela foi mais fácil do que a de sumário, onde os usuários demoraram a entender as informações, porém, conseguiram eventualmente entendê-las por completo. O mesmo se aplica para as métricas geradas;
- A utilização do mapa foi relativamente fácil, onde os usuários se dividiram bem entre usar o *scroll* do mouse ou os botões de *zoom* para interagir com o mapa;
- A visualização das *labels* e dos índices no mapa mostrou-se desafiadora, com alguns usuários incapazes de entender o que fazer e outros levando mais tempo para se familiarizar. A sugestão predominante foi tornar o botão de índice mais visível e adicionar um botão específico para facilitar sua ativação.
- Após utilizar um algoritmo, o entendimento do outro foi consideravelmente facilitada, mostrando assim uma familiaridade entre a utilização dos algoritmos;

### Melhorias possíveis:
&emsp;&emsp;Após analisarmos as interações dos usuários com a plataforma e compreender suas facilidades e dificuldades com a utilização da mesma, algumas mudanças podem ser feitas para melhorar a experiência dos usuários:
- Melhorar os nomes das colunas, como substituir "dia" por "dia do percorrimento", para evitar interpretações equivocadas como sendo uma medida quantitativa;
- Dar mais destaque às métricas geradas e, possivelmente, criar uma aba com explicações sobre o significado de cada uma das métricas, facilitando assim a utilização da plataforma por usuários com menos conhecimento técnico.
- Especificar a necessidade de reiniciar o algoritmo ao tentar rodar outro enquanto ainda há um registro em execução, adicionando um aviso ao tentar executar o algoritmo sem reinício;
- Permitir o clique na linha inteira da tabela para acessar os detalhes de um dia;
- Mudar a ordem das métricas na tabela detalhada, onde a ordem de aparecimento das métricas não corresponde com a ordem das colunas;
- Dar mais destaque ao botão de _index_, usando uma cor mais forte que se destaque melhor em relação ao fundo do mapa;
- Permitir que o usuário clique na linha da tabela para ver o *label* do endereço associado a essa linha.

## Materiais Complementares

- [Tabela com registros dos testes de usabilidade, ocorrências e ações de melhorias.](https://docs.google.com/spreadsheets/d/1S2-av-HPREhq1ombQiz0CiFgPJB2H9I0su1Xq9KxHIo/edit?usp=sharing)