import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud

#st.title(" Competition INDA Hackaton")

from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
data = pd.read_excel(path, sheet_name='year')

# Charger les données
df=data.copy()

def page_santeElig():
    #st.sidebar.write("## Navigation")
    #st.sidebar.markdown("---")
    # Liste des conditions de santé
    conditions = [
        "antibiotherapie", "hemoglobine_basse", "ist_recente", "drepanocytaire",
        "diabetique", "hypertendu", "asthmatique", "cardiaque"
    ]

    
    
    with st.sidebar:
        st.title("🏥")
        st.markdown("---")
    titres_onglets = ["Impact global des maladies sur l'éligibilité", "Impact spéficique"]
    onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
    
    if onglets_selectionnee== "Impact global des maladies sur l'éligibilité":
        # Filtrer le DataFrame pour ne garder que les donneurs "non éligibles"
        # Remplacer "Oui" par True et "Non" par False, et gérer NaN
        # Filtrer les donneurs non éligibles
        df_non_eligible = df[df["ÉLIGIBILITÉ AU DON."] == "non éligible"]
        df_non_eligible = df_non_eligible[conditions].applymap(lambda x: True if x == "Oui" else (False if x == "Non" else x))


        # Liste des conditions de santé
        conditions = [
            "antibiotherapie", "hemoglobine_basse", "ist_recente", "drepanocytaire",
            "diabetique", "hypertendu", "asthmatique", "cardiaque"
        ]

        

        # Liste des conditions "Oui" parmi les donneurs non éligibles
        conditions_oui = []

        # Vérification de chaque condition et ajout à la liste si "Oui"
        for condition in conditions:
            # Compter uniquement les "Oui" et ignorer NaN
            conditions_oui.extend([condition] * df_non_eligible[condition].sum())

        # Générer le WordCloud avec les conditions ayant la valeur "Oui"
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(conditions_oui))

        # Affichage du WordCloud dans Streamlit
        st.subheader("Maladies récurrentes chez les donneurs non éligibles")
        st.image(wordcloud.to_array(), use_column_width=True)


    if onglets_selectionnee=="Impact spéficique":
        # Créer un selectbox pour choisir une condition parmi celles-ci
        condition_choisie = st.sidebar.selectbox("Choisissez une condition de santé", conditions)

       

        # Création du graphique pour la condition choisie
        st.subheader(f"Impact de la condition '{condition_choisie}' sur l'éligibilité au don de sang")

        # Groupement des données par la condition choisie et l'éligibilité
        condition_df = df.groupby([condition_choisie, 'ÉLIGIBILITÉ AU DON.']).size().unstack().fillna(0)

        # Affichage des statistiques
        st.write(f"Nombre de donneurs pour la condition '{condition_choisie}' :")
        st.dataframe(condition_df)

        # Création du graphique
        plt.figure(figsize=(8, 5))
        sns.barplot(x=condition_df.index, y=condition_df["non éligible"])#, label="Eligible")
        #sns.barplot(x=condition_df.index, y=condition_df["non éligible"], color="red", label="non éligible")

        # Ajouter des titres et des labels
        plt.title(f"Comparaison de l'éligibilité pour la condition '{condition_choisie}'", fontsize=14)
        plt.xlabel(condition_choisie, fontsize=12)
        plt.ylabel("Nombre de donneurs non éligible", fontsize=12)
        #plt.legend(title="Éligibilité")

        # Affichage du graphique dans Streamlit
        st.pyplot(plt)

    






