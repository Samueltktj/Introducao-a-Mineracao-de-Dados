import pandas as pd

# Carregar o dataset
df = pd.read_csv("dataset/cidades.csv")

# Visualizar os nomes atuais das colunas
print(df.columns.tolist())

# Drop nas colunas com dados nao significativos
df = df.drop(columns=[
    "Código IBGE",
    "mun_MUNNOME",
    "mun_MUNNOMEX",
    "uf_CODIGO_UF",
    "mun_codigo_adotado",
    "mun_coordenadas"
])

# Renomear colunas restantes
df = df.rename(columns={
    "Populacao": "populacao",
    "ano": "ano",
    "mun_AMAZONIA": "amazonia",
    "mun_FRONTEIRA": "fronteira",
    "mun_CAPITAL": "capital",
    "mun_LATITUDE": "latitude",
    "mun_LONGITUDE": "longitude",
    "mun_ALTITUDE": "altitude",
    "mun_AREA": "area",
    "uf_SIGLA_UF": "sigla_uf",
    "uf_NOME_UF": "nome_uf",
    "venda_gasolina(l)": "venda_gasolina",
    "venda_etanol(l)": "venda_etanol",
    "venda_diesel(l)": "venda_diesel",
    "emissao_CO": "emissao_co",
    "emissao_NOx": "emissao_nox",
    "emissao_COVNM": "emissao_covnm",
    "emissao_MP2.5_total": "emissao_mp25_total",
    "emissao_MPcomb": "emissao_mpcomb",
    "emissao_CO2e": "emissao_co2e",
    "prc_energia_renovavel": "energia_renovavel",
    "Município": "municipio",
    "Região": "regiao",
    "uf_REGIAO": "uf_regiao"
})

# Verificacao inicial
print(df.head())
print(df.info())

# Quantidade de cidades por ano
'''
cidades_por_ano = (
    df.groupby("ano")
      .size()
      .reset_index(name="quantidade_cidades")
      .sort_values(by="quantidade_cidades", ascending=False)
)
print(cidades_por_ano)
'''
# Verificar resultado
print(df.head())

# Retirando cidades sem dados de energia renovavel
df = df.dropna(subset=["energia_renovavel"])

# Removendo Fortaleza do Tabocão
df = df[df["municipio"] != "Fortaleza do Tabocão"]
df = df[df["municipio"] != "São Paulo"]
# Filtrar apenas registros de 2020
input_2020 = df[df["ano"] == 2020].copy()

# Salvar dataset tratado
input_2020.to_csv(
    "dataset/input_2020.csv",
    index=False,
    encoding="utf-8"
)
