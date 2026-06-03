# Introducao-a-Mineracao-de-Dados

Projeto da disciplina de Mineração de Dados com foco em clusterização de municípios brasileiros utilizando algoritmos de aprendizado não supervisionado e visualização geográfica interativa.

Link para os arquivos entregaveis: https://drive.google.com/drive/folders/1iZuhWM8ytXZY-E5mGHuZUw3kg5swCio5?usp=sharing

O projeto realiza:
- pré-processamento dos dados;
- clusterização utilizando K-Means;
- clusterização utilizando K-Medoids;
- avaliação de qualidade utilizando Coeficiente de Silhueta;
- visualização geográfica com Folium;
- visualização bidimensional com PCA.

---

# Autores

 -SAMUEL LIMA MARTINS — 173820
 -PEDRO COELHO TEROSSI — 225883
 -LEONARDO BONFÁ SCHROEDER — 289156
 -GABRIEL FERREIRA DAMASCENO ALTINO — 234791
 - 
 -
 - 
---

# Objetivo do Projeto

Identificar padrões ambientais, energéticos e de consumo entre municípios brasileiros através de técnicas de mineração de dados.

O trabalho utiliza:
- emissões atmosféricas;
- consumo de combustíveis;
- indicadores energéticos;
- dados geográficos dos municípios brasileiros.

---

# Estrutura do Projeto

```text
Introducao-a-Mineracao-de-Dados/
│
├── dataset/
│   ├── cidades.csv
│   ├── input_2020.csv
│
├── output/
│   ├── input_kmeans.csv
│   ├── input_kmedoids.csv
│   ├── mapa_kmeans.html
│   ├── mapa_kmedoids.html
│   └── iteracoes/
│       ├── iteracao_1/
│       ├── iteracao_2/
│       └── ...
│
├── pre_processing.py
├── kmeans.py
├── kmedoids.py
├── map_folium.py
└── README.md
```

---

# Fluxo de Execução

A execução do projeto deve seguir obrigatoriamente esta ordem:

---

## 1 - Pré-Processamento

Executar:

```bash
python pre_processing.py
```

Responsável por:
- carregar o dataset original;
- remover colunas irrelevantes;
- tratar valores ausentes;
- remover cidades inválidas;
- filtrar apenas registros do ano de 2020;
- exportar o dataset tratado.

Arquivo de entrada:

```text
dataset/cidades.csv
```

Arquivo gerado:

```text
dataset/input_2020.csv
```

---

## 2 - Clusterização com K-Means

Executar:

```bash
python kmeans.py
```

Responsável por:
- normalizar os dados;
- aplicar K-Means;
- calcular o Coeficiente de Silhueta;
- gerar visualização PCA;
- exportar CSV clusterizado.

Arquivos gerados:

```text
output/input_kmeans.csv
```

---

## 3 - Clusterização com K-Medoids

Executar:

```bash
python kmedoids.py
```

Responsável por:
- normalizar os dados;
- aplicar K-Medoids;
- calcular o Coeficiente de Silhueta;
- gerar visualização PCA;
- exportar CSV clusterizado.

Arquivos gerados:

```text
output/input_kmedoids.csv
```

---

## 4 - Visualização Geográfica

Executar:

```bash
python map_folium.py
```

Responsável por:
- carregar os CSVs clusterizados;
- gerar mapas interativos;
- visualizar clusters geograficamente.

Arquivos gerados:

```text
output/mapa_kmeans.html
output/mapa_kmedoids.html
```

Os mapas podem ser abertos diretamente no navegador.

---

# Variáveis Utilizadas

O modelo utiliza as seguintes features:

```text
venda_gasolina
venda_etanol
venda_diesel
emissao_co
emissao_nox
emissao_covnm
emissao_mp25_total
emissao_mpcomb
emissao_co2e
energia_renovavel
```

---

# Técnicas Utilizadas

## Pré-Processamento
- remoção de colunas irrelevantes;
- tratamento de valores nulos;
- filtragem temporal;
- limpeza de inconsistências.

---

## Clusterização
- K-Means;
- K-Medoids;
- normalização com StandardScaler.

---

## Métricas de Qualidade

O projeto utiliza:

### Coeficiente de Silhueta

Métrica utilizada para avaliar a qualidade dos agrupamentos.

Interpretação:

| Valor | Qualidade |
|---|---|
| próximo de 1 | excelente separação |
| próximo de 0 | separação moderada |
| negativo | agrupamento ruim |

---

# Visualização

## PCA
Utilizado para reduzir dimensionalidade e permitir visualização dos clusters em duas dimensões.

---

## Folium
Utilizado para:
- visualização geográfica;
- análise espacial dos clusters;
- mapas interativos.

---

# Diretrizes para Iterações do Modelo

Ao realizar modificações ou novas iterações no algoritmo:
- alteração de hiperparâmetros;
- mudança no número de clusters;
- remoção de features;
- remoção de outliers;
- mudanças de normalização;

é obrigatório salvar os resultados gerados na pasta:

```text
output/iteracoes/
```

Cada iteração deve conter:
- CSV clusterizado;
- mapa HTML;
- gráfico PCA;
- anotações dos resultados;
- valor do Coeficiente de Silhueta.

Exemplo:

```text
output/iteracoes/iteracao_1/
│
├── input_kmeans.csv
├── input_kmedoids.csv
├── mapa_kmeans.html
├── mapa_kmedoids.html
├── grafico_kmeans.png
├── grafico_kmedoids.png
└── anotacoes.txt
```

---

# Instalação das Bibliotecas

Linux / Fedora:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instalar dependências:

```bash
pip install pandas scikit-learn matplotlib folium scikit-learn-extra
```

---

# Bibliotecas Utilizadas

- pandas
- scikit-learn
- scikit-learn-extra
- matplotlib
- folium

---

# Algoritmos Comparados

| Algoritmo | Característica |
|---|---|
| K-Means | Mais rápido e amplamente utilizado |
| K-Medoids | Mais robusto contra outliers |

---

# Saídas Geradas

| Arquivo | Descrição |
|---|---|
| input_2020.csv | Dataset tratado |
| input_kmeans.csv | Resultado do K-Means |
| input_kmedoids.csv | Resultado do K-Medoids |
| mapa_kmeans.html | Mapa geográfico do K-Means |
| mapa_kmedoids.html | Mapa geográfico do K-Medoids |

---
