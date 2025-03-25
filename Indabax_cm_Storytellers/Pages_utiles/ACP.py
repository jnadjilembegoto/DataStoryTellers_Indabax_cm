import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Charger les données (remplace avec ton propre fichier si nécessaire)
from Datas.data_link import data_dir

path = data_dir('base_streamlit_storytellers.xlsx')
df = pd.read_excel(path, sheet_name='year')

def wordcloud_non_eligibilite():
    st.subheader("🔍 Nuage de mots des raisons de non-éligibilité")

    # Vérifier si la colonne existe dans le DataFrame
    if "Raisons_Non_Eligibilite" not in df.columns:
        st.error("La colonne 'Raisons_Non_Eligibilite' est introuvable dans les données.")
        return

    # Nettoyer les données : supprimer NaN et concaténer les raisons
    text = " ".join(str(reason) for reason in df["Raisons_Non_Eligibilite"].dropna())

    # Générer le WordCloud
    wordcloud = WordCloud(
        width=800, height=400, background_color="white", colormap="Reds",
        max_words=100, contour_color="black"
    ).generate(text)

    # Afficher le WordCloud dans Streamlit
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")  # Cacher les axes
    st.pyplot(fig)



def acp_analyse():
    
    
    st.sidebar.title("💬")
    st.sidebar.markdown("---")
    # Appel de la fonction pour l'affichage
    wordcloud_non_eligibilite()
    
