# Gini

---

Calculadora do Índice de Gini.

## Descrição

---

Calculadora de Índice de Gini que permite a decomposição do mesmo em grupos ou estratos presentes no conjunto de dados. O método de cálculo utilizado foi visto na disciplina optativa Análise de Dados Socioeconômicos, oferecida pelo Departamento de Economia da Unesp Araraquara.

Para o conjunto inteiro, a fórmula utilizada é a seguinte:

$$G=1-\frac{1}{n}\cdot\sum_{i=1}^{n}(\phi_{i} + \phi_{i-1})$$

onde:

$n$: número de indivíduos no conjunto de dados;

$\phi_{i}$: proporção de renda acumulada pelo i-ésimo indivíduo da população

Para dados agrupados, a fórmula é:

$$G=G_{e}+\sum_{h=1}^{k}{\pi_{h}\cdot Y_{h}\cdot G_{h}}\space+G_s$$

onde:

$G_e=1-\sum_{h=1}^{k}\pi_h\cdot(\phi_h+\phi_{h-1})$: Gini intergrupos;

$\pi_{h}$: proporção da população apropriada pelo h-ésimo grupo;

$Y_{h}$: proporção da renda acumulada pelo h-ésimo grupo;

$G_h=1-\frac{1}{n_h}\cdot\sum_{i=1}^{n_h}(\phi_{h,i} + \phi_{h,i-1})$: Gini intragrupos (índice de gini de cada grupo);

$G_{s}$: Índice de Gini de sobreposição.

Além de calcular e decompor o índice, o script dá também a possibilidade de plotar a Curva de Lorenz do conjunto de dados passado como argumento para a função.

## Funções

---

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

Retorna uma tupla cujos elementos são, respectivamente:

1. Lista ordenada contendo o índice de gini de cada grupo;
2. Gini intergrupos ($G_{e}$);
3. Ponderação Gini intragrupos ($\sum_{h=1}^{k}{\pi_{h}\cdot Y_{h}\cdot G_{h}}$);
4. Gini de sobreposição.

### →`lorenz(dados)`

Plota a Curva de Lorenz do conjunto passado como argumento.

## Entradas

---

As funções recebem um `pd.Series` (`dados`) ou uma lista de séries (`decomp()`).

## Exemplos

---

### Função `gini()`

### Amostra desigual e amostra com igualdade perfeita

Considerando uma população muito desigual onde uma pessoa concentra toda a renda, espera-se um índice de gini próximo à um. Já em uma amostra com igualdade perfeita (todos indivíduos com a mesma renda), espera-se um índice de gini de zero

![ex_gini.png](Gini%20936cc3145439425891819fa97f962c46/ex_gini.png)

### Função `decomp()`

Para exemplificar a função `decomp()`, utilizei o conjunto de dados *wage1*, presente no pacote `wooldridge`. Este pacote contém todos os conjuntos de dados utilizados no livro **Introdução à Econometria - Jeffrey M. Wooldridge.**

Realizei a decomposição do índice de gini para homens e mulheres.

![ex_decomp.png](Gini%20936cc3145439425891819fa97f962c46/ex_decomp.png)

### Função `lorenz()`

Para exemplificar a função `lorenz()` plotei a Curva de Lorenz para a amostra das mulheres.

![ex_lorenz.png](Gini%20936cc3145439425891819fa97f962c46/ex_lorenz.png)