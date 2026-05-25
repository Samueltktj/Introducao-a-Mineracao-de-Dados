import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# =========================
# CARREGAMENTO
# =========================

df = pd.read_csv("dataset/input_2020.csv")

# =========================
# FEATURES
# =========================

features = [
    #"populacao",
    "venda_gasolina",
    "venda_etanol",
    "venda_diesel",
    "emissao_co",
    "energia_renovavel"
]

X = df[features]

# =========================
# NORMALIZAÇÃO
# =========================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =========================
# KMEANS
# =========================

kmeans = KMeans(
    n_clusters=int(input("Insira a quantidade de clusters: ")),
    random_state=42
)

df["cluster"] = kmeans.fit_predict(X_scaled)

# =========================
# EXPORTAÇÃO PARA FOLIUM
# =========================

df.to_csv(
    "output/input_clusterizado.csv",
    index=False,
    encoding="utf-8"
)

print("CSV clusterizado gerado com sucesso.")

# =========================
# PCA PARA VISUALIZAÇÃO
# =========================

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

# =========================
# VISUALIZAÇÃO DOS CLUSTERS
# =========================

plt.figure(figsize=(10, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=df["cluster"]
)

plt.title("Clusters de Municípios")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")

plt.show()


