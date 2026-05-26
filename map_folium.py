import pandas as pd
import folium
import matplotlib.colors as mcolors

# =========================
# FUNÇÃO DE GERAÇÃO
# =========================

def gerar_mapa(csv_entrada, html_saida):

    # =========================
    # CARREGAMENTO
    # =========================

    df = pd.read_csv(csv_entrada)

    # Remove linhas sem coordenadas
    df = df.dropna(subset=["latitude", "longitude", "cluster"])

    # Corrige decimal
    df["latitude"] = (
        df["latitude"]
        .astype(str)
        .str.replace(",", ".")
        .astype(float)
    )

    df["longitude"] = (
        df["longitude"]
        .astype(str)
        .str.replace(",", ".")
        .astype(float)
    )

    # =========================
    # GERAÇÃO DINÂMICA DE CORES
    # =========================

    clusters_unicos = sorted(df["cluster"].unique())

    cores_base = list(mcolors.TABLEAU_COLORS.values())

    cores_clusters = {
        cluster: cores_base[i % len(cores_base)]
        for i, cluster in enumerate(clusters_unicos)
    }

    # =========================
    # MAPA BASE
    # =========================

    mapa = folium.Map(
        location=[
            df["latitude"].mean(),
            df["longitude"].mean()
        ],
        zoom_start=4,
        tiles="CartoDB dark_matter"
    )

    # =========================
    # PLOT DOS MUNICÍPIOS
    # =========================

    for _, row in df.iterrows():

        cluster = row["cluster"]

        popup = f"""
        <b>Município:</b> {row.get('municipio', 'N/A')}<br>
        <b>UF:</b> {row.get('sigla_uf', 'N/A')}<br>
        <b>Cluster:</b> {cluster}<br>
        <b>CO2e:</b> {row.get('emissao_co2e', 'N/A')}<br>
        <b>Energia Renovável:</b> {row.get('energia_renovavel', 'N/A')}<br>
        """

        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=5,
            color=cores_clusters[cluster],
            fill=True,
            fill_color=cores_clusters[cluster],
            fill_opacity=0.7,
            popup=folium.Popup(popup, max_width=300),
            tooltip=f"Cluster {cluster}"
        ).add_to(mapa)

    # =========================
    # SALVAR MAPA
    # =========================

    mapa.save(html_saida)

    print(f"Mapa salvo: {html_saida}")


# =========================
# KMEANS
# =========================

gerar_mapa(
    "output/input_kmeans.csv",
    "output/mapa_kmeans.html"
)

# =========================
# KMEDOIDS
# =========================

gerar_mapa(
    "output/input_kmedoids.csv",
    "output/mapa_kmedoids.html"
)
