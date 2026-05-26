import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn_extra.cluster import KMedoids
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
    "emissao_nox",
    "emissao_covnm",
    "emissao_mp25_total",
    "emissao_mpcomb",
    "emissao_co2e",
    "energia_renovavel"
]

X = df[features]

# =========================
# NORMALIZAÇÃO
# =========================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =========================
# KMEDOIDS
# =========================

n_clusters = int(input("Insira a quantidade de clusters: "))
n_seed = int(input("Insira a seed: "))

kmedoids = KMedoids(
    n_clusters=n_clusters,
    random_state=n_seed
)

clusters = kmedoids.fit_predict(X_scaled)

df["cluster"] = clusters

# =========================
# COEFICIENTE DE SILHUETA
# =========================

silhouette = silhouette_score(X_scaled, clusters)

print(f"\nCoeficiente de Silhueta (KMedoids): {silhouette:.4f}")

# =========================
# EXPORTAÇÃO PARA FOLIUM
# =========================

df.to_csv(
    "output/input_kmedoids.csv",
    index=False,
    encoding="utf-8"
)

print("\nCSV clusterizado gerado com sucesso.")

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

plt.title(
    f"KMedoids | Silhouette: {silhouette:.4f}"
)

plt.xlabel("PCA 1")
plt.ylabel("PCA 2")

plt.show()
