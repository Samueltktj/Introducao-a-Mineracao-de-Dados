# Introducao-a-Mineracao-de-Dados

Projeto da disciplina de Mineração de Dados com foco em clusterização de municípios brasileiros utilizando K-Means e visualização geográfica com Folium.

---

# Fluxo de Execução

A execução deve seguir esta ordem:

1. preprocessamento.py
2. kmeans.py
3. map_folium.py

---

# Diretrizes para Iterações do Modelo

Ao realizar modificações ou novas iterações no algoritmo (ajuste de hiperparâmetros, alteração do número de clusters, remoção de outliers/variáveis, etc.), é obrigatório salvar os resultados gerados na pasta `iteraçoes/`. 

Para cada experimento, adicione:
* O gráfico de dispersão resultado do K-Means;
* O mapa interativo gerado em formato HTML (`.html`);
* A base de dados clusterizada em formato CSV (`.csv`).
* As anotações dos resultados

---

# Instalação das Bibliotecas

Linux / Fedora:

```bash
python -m venv .venv
source .venv/bin/activate
pip install pandas scikit-learn matplotlib folium
