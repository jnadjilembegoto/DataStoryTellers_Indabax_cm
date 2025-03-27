import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import streamlit as st
import pydeck as pdk
import numpy as np
import folium
import streamlit as st
from streamlit_folium import folium_static
#st.title(" Competition INDA Hackaton")
from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
data = pd.read_excel(path, sheet_name='year')

# copions les données
df=data.copy()



# Dictionnaire avec les coordonnées pour chaque quartier de Douala
quartier_coords = {
    "Logbaba": (4.05, 9.7),
    "NDOGPASSI 2": (4.06, 9.71),
    "Dakar": (4.07, 9.72),
    "NGANGUE": (4.08, 9.73),
    "Douala": (4.05, 9.7),
    "BEPENDA": (4.05, 9.75),
    "Bepanda": (4.06, 9.74),
    "Pk14": (4.06, 9.76),
    "Ari": (4.05, 9.78),
    "Makepe": (4.06, 9.78),
    "NYALLA": (4.05, 9.71),
    "Deido": (4.05, 9.73),
    "Bastos": (4.05, 9.75),
    "New bell": (4.05, 9.76),
    "Sic cacao": (4.05, 9.77),
    "Boko": (4.05, 9.78),
    # Ajoutez d'autres quartiers de Douala ici
}

# Fonction pour obtenir les coordonnées
def get_coordinates(quartier):
    return quartier_coords.get(quartier, (None, None))

def generate_donor_map(df, quartier_col):
    # Vérifier si la colonne existe
    if quartier_col not in df.columns:
        st.error(f"La colonne '{quartier_col}' n'existe pas dans les données.")
        return

    # Compter le nombre de donneurs par quartier
    quartiers_donneurs = df[quartier_col].value_counts().reset_index()
    quartiers_donneurs.columns = ['Quartier', 'Nombre_Donneurs']

    # Initialisation de la carte
    m = folium.Map(location=[4.05, 9.7], zoom_start=12)

    # Ajouter des cercles sur la carte pour chaque quartier
    for _, row in quartiers_donneurs.iterrows():
        quartier = row['Quartier']
        lat, lon = get_coordinates(quartier)

        if lat is not None and lon is not None:
            # Ajuster la taille en fonction du nombre de donneurs
            radius = row['Nombre_Donneurs'] * 0.005  # Vous pouvez ajuster ce facteur selon vos besoins
            folium.CircleMarker(
                location=[lat, lon],
                radius=radius,  # Taille proportionnelle au nombre de donneurs
                popup=f"{quartier}: {row['Nombre_Donneurs']} donneurs ({lat}, {lon})",
                color="blue" if radius > 2 else "red",  # Couleur selon la participation
                fill=True,
                fill_color="blue" if radius > 2 else "red",
                fill_opacity=0.5
            ).add_to(m)

    # Afficher la carte dans Streamlit
    folium_static(m)




# Dictionnaire avec les coordonnées pour chaque quartier de Douala
quartier_coords = {
    "Logbaba": (4.05, 9.7),
    "NDOGPASSI 2": (4.06, 9.71),
    "Dakar": (4.07, 9.72),
    "NGANGUE": (4.08, 9.73),
    "Douala": (4.05, 9.7),
    "BEPENDA": (4.05, 9.75),
    "Bepanda": (4.06, 9.74),
    "Pk14": (4.06, 9.76),
    "Ari": (4.05, 9.78),
    "Douala douala": (4.05, 9.7),
    "Logbessou": (4.05, 9.7),
    "Makepe": (4.06, 9.78),
    "Pk12": (4.06, 9.75),
    "NYALLA": (4.05, 9.71),
    "Nyalla": (4.05, 9.72),
    "Nkolbong": (4.05, 9.73),
    "Yassa": (4.05, 9.74),
    "Ngodi bakoko": (4.05, 9.71),
    "Ndokoti": (4.05, 9.71),
    "Deido": (4.05, 9.73),
    "Bastos": (4.05, 9.75),
    "New bell": (4.05, 9.76),
    "Sic cacao": (4.05, 9.77),
    "Boko": (4.05, 9.78),
    "Ndogpassi 3": (4.06, 9.74),
    "Ndogpassi": (4.06, 9.75),
    "PK13": (4.06, 9.73),
    "PK9": (4.05, 9.72),
    "BESSENGUE": (4.05, 9.76),
    "Newbell": (4.05, 9.75),
    "Yansoki": (4.05, 9.75),
    "Ndobo": (4.05, 9.74),
    "Mbanga": (4.05, 9.73),
    "Pk8": (4.05, 9.72),
    "Village": (4.05, 9.74),
    "Japoma": (4.05, 9.75),
    "Terminus saint Michel": (4.05, 9.76),
    "Bonanjo": (4.05, 9.77),
    "Bonaberi": (4.05, 9.78),
    # Ajoutez d'autres quartiers de Douala si nécessaire
}

# Fonction pour obtenir les coordonnées
def get_coordinates(quartier):
    return quartier_coords.get(quartier, (None, None))

def generate_donor_map_quartier(df, quartier_col):
    # Vérifier si la colonne existe
    if quartier_col not in df.columns:
        st.error(f"La colonne '{quartier_col}' n'existe pas dans les données.")
        return

    # Compter le nombre de donneurs par quartier
    quartiers_donneurs = df[quartier_col].value_counts().reset_index()
    quartiers_donneurs.columns = ['Quartier', 'Nombre_Donneurs']

    # Initialisation de la carte
    m = folium.Map(location=[4.05, 9.7], zoom_start=12)

    # Ajouter des cercles sur la carte pour chaque quartier
    for _, row in quartiers_donneurs.iterrows():
        quartier = row['Quartier']
        lat, lon = get_coordinates(quartier)

        if lat is not None and lon is not None:
            # Ajuster la taille en fonction du nombre de donneurs
            radius = row['Nombre_Donneurs'] * 0.005  # Vous pouvez ajuster ce facteur selon vos besoins
            folium.CircleMarker(
                location=[lat, lon],
                radius=radius,  # Taille proportionnelle au nombre de donneurs
                popup=f"{quartier}: {row['Nombre_Donneurs']} donneurs ({lat}, {lon})",
                color="blue" if radius > 2 else "red",  # Couleur selon la participation
                fill=True,
                fill_color="blue" if radius > 2 else "red",
                fill_opacity=0.5
            ).add_to(m)

    # Afficher la carte dans Streamlit
    folium_static(m)


     



def afficher_diagramme_en_anneau(base, var2):
    if base.empty:
        st.header("Aucune donnée disponible pour ce quartier.")
    else:
        # Calculer les pourcentages
        count_data = base[var2].value_counts(normalize=True) * 100
        count_data = count_data.reset_index()
        count_data.columns = [var2, 'Pourcentage']

        # Créer le diagramme en anneau
        fig = px.pie(
            count_data,
            names=var2,
            values='Pourcentage',
            hover_data=['Pourcentage'],
            labels={var2: var2, 'Pourcentage': 'Pourcentage (%)'},
            color_discrete_sequence=['#D95F0E'],  # Palette de couleurs
            hole=0.4  # Définir le trou pour faire un anneau
        )

        # Personnalisation du diagramme en anneau
        fig.update_traces(
            textinfo='percent+label',  # Affiche les étiquettes et les pourcentages
            hoverinfo='label+percent+value',  # Affiche plus d'infos en hover
            textfont_size=14
        )

        # Ajustement de la mise en page
        fig.update_layout(
            margin=dict(l=20, r=20, t=40, b=40),
            showlegend=True
        )

        # Afficher le diagramme
        st.plotly_chart(fig)





def afficher_histogramme(base, var2):
    if base.empty:
        st.header("Aucune donnée disponible pour ce quartier.")
    else:
        # Calculer les pourcentages
        count_data = base[var2].value_counts(normalize=True) * 100  # Calculer le pourcentage
        count_data = count_data.reset_index()
        count_data.columns = [var2, 'Pourcentage']  # Renommer les colonnes

        # Créer un histogramme des pourcentages
        fig = px.bar(
            count_data,
            x=var2,
            y='Pourcentage',
            text='Pourcentage'  # Affichage automatique des pourcentages
        )
# Formater les pourcentages avec deux décimales et le symbole '%'
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='auto')
        # Masquer la légende
        fig.update_traces(showlegend=False)
        fig.update_layout(xaxis_title='')  # Titre de l'axe X vide

        # Afficher l'histogramme
        st.plotly_chart(fig)



## Diagramme circulaire
def afficher_diagramme_circulaire(base, var2):
    if base.empty:
        st.header("Aucune donnée disponible pour ce quartier.")
    else:
        # Calculer les pourcentages
        count_data = base[var2].value_counts(normalize=True) * 100  # Calculer le pourcentage
        count_data = count_data.reset_index()
        count_data.columns = [var2, 'Pourcentage']  # Renommer les colonnes

        # Créer un diagramme circulaire des pourcentages
        fig = px.pie(
        count_data,
        names=var2,
        values='Pourcentage',
        hover_data=['Pourcentage'],  # Pour afficher les pourcentages en hover
        labels={var2: var2, 'Pourcentage': 'Pourcentage (%)'}
    )

        fig.update_traces(textinfo='percent', hoverinfo='percent+value')

            # Afficher le diagramme circulaire
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig)
def carto_page_load():
    st.sidebar.write("## Navigation")
    st.sidebar.write("Aller ")
    titres_onglets = ["Analyse par Arrondissement","Analyse par Quartier de résidence 🌍"]
    # Exemple d'utilisation :
    onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)

    if onglets_selectionnee=="Analyse par Arrondissement":
            Arrondi = df['Arrondissement de résidence'].unique()
            quartier_selectionne = st.sidebar.multiselect(
            "Choississez l'arrondissement de résidence:",
            options = Arrondi,
            default = Arrondi[0]
        )
            #quartier_selectionne = st.selectbox("Sélectionnez un quartier :", quartiers)
            Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
            Eligi_selectionne=st.sidebar.multiselect(
            "Choississez l'état de l'individu:",
            options = Eligi,
            default = Eligi[0])
    
            col = st.columns(2)
            with col[0]:
                #st.header('Pour Arrondissement selectionné:')
                base=df[df['Arrondissement de résidence'].isin(quartier_selectionne)]
                st.header("Eligibilité au Don")
                afficher_diagramme_en_anneau(base,'ÉLIGIBILITÉ AU DON.')
                base=base[base['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
                st.header("Matrimoniale")
                afficher_diagramme_circulaire(base,'Situation Matrimoniale (SM)')
                
            ## Impact des variables santé

            with col[1]:
                st.header("Toute la population:")
                afficher_diagramme_en_anneau(df,'ÉLIGIBILITÉ AU DON.' )
                base=base[base['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
                st.header('Genre')
                afficher_diagramme_circulaire(base,'Genre')

            with st.container():
        ## Arrondissement de résidence
                base=df[df['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
                st.header("Arrondissement de résidence")
                generate_donor_map(base,"Arrondissement de résidence")
                st.header("Arrondissements")
                afficher_histogramme(base, 'Arrondissement de résidence')
            
                
    if onglets_selectionnee=="Analyse par Quartier de résidence 🌍":
            with st.sidebar:
                quartiers = df['Quartier de Résidence'].unique()
                quartier_selectionne = st.sidebar.multiselect(
                "Choississez le quartier de résidence:",
                options = quartiers,
                default = quartiers[0]
            )
                
                Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
                Eligi_selectionne=st.sidebar.multiselect(
                "Choississez l'état de l'individu:",
                options = Eligi,
                default = Eligi[0]
            )#quartier_selectionne = st.selectbox("Sélectionnez un quartier :", quartiers)
                


                
            col = st.columns(2)
            base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
            base=base1[base1['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
            with col[0]:
                st.header('Pour quartier selectionné:')

                afficher_diagramme_circulaire(base1,'ÉLIGIBILITÉ AU DON.')
                st.header('Matrimoniale')
                afficher_diagramme_en_anneau(base1,'Situation Matrimoniale (SM)')
                st.header('Proffession')
                afficher_histogramme(base1,'Profession')


            with col[1]:
                st.header("Toute la population:")
                afficher_diagramme_en_anneau(df,'ÉLIGIBILITÉ AU DON.' )
                st.header("Genre")
                afficher_diagramme_circulaire(base1,'Genre')
                st.header('Religion')
                afficher_histogramme(base1,"Religion")
            
            #col1=st.columns(2)
            #with col1[0]:

            with st.container():
        ## Arrondissement de résidence
                base=df[df['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
                st.header('Quartier de résidence')
                afficher_histogramme(base, 'Quartier de Résidence')
                st.header('Quartier de Résidence')
                generate_donor_map_quartier(base, 'Quartier de Résidence')

