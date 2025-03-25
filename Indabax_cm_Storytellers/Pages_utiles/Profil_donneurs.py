import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import streamlit as st
import pydeck as pdk
import numpy as np
#st.title(" Competition INDA Hackaton")


from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
data = pd.read_excel(path, sheet_name='year')
data2 = pd.read_excel(path, sheet_name='donneur')

# Charger les données
df=data.copy()


def afficher_histogramme(base, var2):
    if base.empty:
        st.write("Aucune donnée disponible pour ce quartier.")
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
        st.write("Aucune donnée disponible pour ce quartier.")
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

        fig.update_traces(textinfo='percent', hoverinfo='percent')

            # Afficher le diagramme circulaire
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig)

## diagramme en anneau
def afficher_diagramme_en_anneau(base, var2):
    if base.empty:
        st.write("Aucune donnée disponible .")
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
            textinfo='percent',  # Affiche les étiquettes et les pourcentages
            hoverinfo='percent+value',  # Affiche plus d'infos en hover
            textfont_size=14
        )

        # Ajustement de la mise en page
        fig.update_layout(
            margin=dict(l=20, r=20, t=40, b=40),
            showlegend=True
        )

        # Afficher le diagramme
        st.plotly_chart(fig)

def page_profil_load():
    #st.sidebar.write("## Navigation")
    #st.sidebar.write("Aller ")
    with st.sidebar:
        st.title('🔬')
        st.markdown("---")
    titres_onglets = ["Caractéristiques Démographiques des donneurs", "Caractéristiques Biologiques des donneurs"]
    onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
    if onglets_selectionnee=="Caractéristiques Démographiques des donneurs":
            
        with st.sidebar:
                Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
                Eligi_selectionne=st.sidebar.multiselect(
                "Choississez l'état de l'individu:",
                options = Eligi,
                default = Eligi[0])

        col = st.columns(2)
        #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
        base=df[df['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
        with col[0]:
                #st.write('Pour quartier selectionné:')

                #afficher_diagramme_circulaire(base,'ÉLIGIBILITÉ AU DON.')
                st.header("Matrimoniale")
                afficher_diagramme_en_anneau(base,"Situation Matrimoniale (SM)")

                st.header("Nationalité")
                afficher_histogramme(base,'Nationalité')


        with col[1]:
                st.header("Genre")
                afficher_diagramme_en_anneau(base,'Genre')
                st.header("Réligion")
                afficher_histogramme(base,"Religion")
            
        
        with st.container():
                st.header("Profession")
                afficher_histogramme(base,'Profession')
                #afficher_histogramme(base, 'Arrondissement de résidence')
    if onglets_selectionnee=="Caractéristiques Biologiques des donneurs":
            
        with st.sidebar:
            Genre= data2["Sexe"].unique()
            Genre_selectionne=st.sidebar.multiselect("Choississez le sexe de l'individu:",
            options = Genre,
            default = Genre[0])

        col = st.columns(2)
        #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
        base=data2[data2['Sexe'].isin(Genre_selectionne)]
        with col[0]:
                st.write("Sanguin/Rhesus")
                afficher_diagramme_circulaire(base,'Groupe Sanguin ABO / Rhesus')

        with col[1]:
                st.write("type de Donation")
                afficher_diagramme_circulaire(base,"Type de donation")
                
        with st.container():
                st.header("Phenotype")
                afficher_histogramme(base,'Phenotype')
