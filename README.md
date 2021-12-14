# Gini



Calculadora do Índice de Gini.

## Descrição



Calculadora de Índice de Gini que permite a decomposição do mesmo em grupos ou estratos presentes no conjunto de dados. O método de cálculo utilizado foi visto na disciplina optativa Análise de Dados Socioeconômicos, oferecida pelo Departamento de Economia da Unesp Araraquara.

Para o conjunto inteiro, a fórmula utilizada é:

<p align = "center">
<img src="https://render.githubusercontent.com/render/math?math=\large G=1-\frac{1}{n}\cdot\sum_{i=1}^{n}(\phi_{i}%2B\phi_{i-1})">
</p>
onde:

<img src="https://render.githubusercontent.com/render/math?math=\large n">: número de indivíduos no conjunto de dados;

<img src="https://render.githubusercontent.com/render/math?math=\large \phi_{i}">: proporção de renda acumulada pelo i-ésimo indivíduo da população

Para dados agrupados, a fórmula é:
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\large G=G_{e}%2B\sum_{h=1}^{k}{\pi_{h} Y_{h} G_{h}}\cdot+G_s">
</p>
onde:

<img src="https://render.githubusercontent.com/render/math?math=\large G_e=1-\sum_{h=1}^{k}\pi_h\cdot(\phi_h%2B+\phi_{h-1})">: Gini intergrupos;

<img src="https://render.githubusercontent.com/render/math?math=\large \phi_{h}">: proporção da população apropriada pelo h-ésimo grupo;

<img src="https://render.githubusercontent.com/render/math?math=\large Y_{h}">: proporção da renda acumulada pelo h-ésimo grupo;

<img src="https://render.githubusercontent.com/render/math?math=\large G_h=1-\frac{1}{n_h}\cdot\sum_{i=1}^{n_h}(\phi_{h,i}%2B\phi_{h,i-1})">: Gini intragrupos (índice de gini de cada grupo);

<img src="https://render.githubusercontent.com/render/math?math=\large G_{s}">: Índice de Gini de sobreposição.

Além de calcular e decompor o índice, o script dá também a possibilidade de plotar a Curva de Lorenz do conjunto de dados passado como argumento para a função.

## Funções


### →`n(dados)`

Retorna o tamanho do conjunto de dados passado como argumento.

### →`renda(dados)`

Retorna uma série ordenada da renda dos indivíduos do conjunto de dados;

### →`renda_total(dados)`

Retorna a soma das rendas de todos os indivíduos;

### →`renda_acumulada(dados)`

Retorna uma série ordenada da proporção de renda acumulada pelos indivíduos do conjunto;

### →`gini(dados)`

Calcula o índice de gini do conjunto de dados passado como argumento;

### →`decomp(grupos, dados)`

Realiza a decomposição do índice de gini para cada subconjunto passado como argumento (`grupos`)

Retorna uma tupla cujos elementos são, **respectivamente**:

1. Lista ordenada contendo o índice de gini de cada grupo;
2. Gini intergrupos (<img src="https://render.githubusercontent.com/render/math?math=\large G_{e}">);
3. Ponderação Gini intragrupos <img src="https://render.githubusercontent.com/render/math?math=\large (\sum_{h=1}^{k}{\pi_{h}\cdot Y_{h}\cdot G_{h}})">;
4. Gini de sobreposição.

### →`lorenz(dados)`

Plota a Curva de Lorenz do conjunto passado como argumento.

## Entradas



As funções recebem um `pd.DataFrame` ou uma lista de DataFrames (função `decomp()`).

## Exemplos



### Função `gini()`

### Amostra desigual e amostra com igualdade perfeita

Considerando uma população muito desigual onde uma pessoa concentra toda a renda, espera-se um índice de gini próximo à um. Já em uma amostra com igualdade perfeita (todos indivíduos com a mesma renda), espera-se um índice de gini de zero

![ex_gini.png](https://github.com/feegioppato/gini/blob/main/ex_gini.png?raw=true)

### Função `decomp()`

Para exemplificar a função `decomp()` utilizei o conjunto de dados *wage1*, presente no pacote `wooldridge`. Este pacote contém todos os conjuntos de dados utilizados no livro **Introdução à Econometria - Jeffrey M. Wooldridge.**

Realizei a decomposição do índice de gini para homens e mulheres.

![ex_decomp.png](https://github.com/feegioppato/gini/blob/main/ex_decomp.png?raw=true)

### Função `lorenz()`

Para exemplificar a função `lorenz()` plotei a Curva de Lorenz para a amostra das mulheres.

![ex_lorenz.png](https://github.com/feegioppato/gini/blob/main/ex_lorenz.png?raw=true)
