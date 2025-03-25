

import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import streamlit as st
import pydeck as pdk
import numpy as np

from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
data = pd.read_excel(path, sheet_name='year')
## Importation de la deuxième base
data2 = pd.read_excel(path, sheet_name='age')

# Charger les données
df=data.copy()




def afficher_evolution_dons(df,Var1):
    """
    Fonction pour afficher l'évolution  du nombre de dons de sang.

    Paramètres :
    - df (pd.DataFrame) : Le dataframe contenant les données.
    .

    Retour :
    - Affiche un graphique interactif dans Streamlit.
    """
    
    fig = px.line(
        df,
        x=Var1,
        y='Nombre de Dons',
        #title='Évolution Mensuelle du Nombre de Dons de Sang',
        #labels={'Mois_Annee': 'Mois et Année', 'Nombre de Dons': 'Nombre de Dons'},
        markers=True
    )

    # Personnalisation du graphique
    fig.update_layout(
        #xaxis_title="Mois et Année",
        yaxis_title="Nombre de Dons",
        xaxis_tickangle=-45,
        plot_bgcolor="rgba(240,240,240,0.9)"
    )

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)



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

        fig.update_traces(textinfo='percent', hoverinfo='percent+value')

            # Afficher le diagramme circulaire
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig)

## Camenbert
def afficher_diagramme_en_anneau(base, var2):
    if base.empty:
        st.write("Aucune donnée disponible pour ce quartier.")
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

def page_efficacity():
    # Création de colonne mois 

    colonne_date="Date de remplissage de la fiche"


    # Conversion en datetime
    df[colonne_date] = pd.to_datetime(df[colonne_date], errors='coerce')


    # Créer une colonne pour le mois et l'année
    df['Mois_Annee'] = df[colonne_date].dt.to_period('M')

        # Tableau de contingence
    def group(df,Mois_Annee):
        don_evolution = df.groupby(Mois_Annee).size().reset_index(name='Nombre de Dons')

            # Convertir en string pour la visualisation
        don_evolution[Mois_Annee] = don_evolution[Mois_Annee].astype(str)
        return don_evolution


    
    #st.sidebar.write("## Navigation")
    with st.sidebar:
        st.title('📊')
        st.markdown("---")
    titres_onglets = ["Analyse Globale", "Analyse par sexe"]
    onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
    st.sidebar.markdown("---")
    st.sidebar.write("Paramètres d'analyse")
    if onglets_selectionnee=="Analyse Globale":
        with st.sidebar:
                Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
                Eligi_selectionne=st.sidebar.multiselect(
                "Choississez l'état de l'individu:",
                options = Eligi,
                default = Eligi[0])
                Mois=df['Mois_Annee'].unique()

                Mois_selectionne=st.sidebar.multiselect(
                "Choississez l'état de l'individu:",
                options = Mois,
                default = Mois[0])


        base=df[df['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
        base1=base[base["Mois_Annee"].isin(Mois_selectionne)]
        
        col = st.columns(2)
        with col[0]:
                #afficher_diagramme_circulaire(base,'ÉLIGIBILITÉ AU DON.')
                st.header("Evolution mensuelle")
                afficher_evolution_dons(group(base,'Mois_Annee'), 'Mois_Annee')
                st.header("Matrimoniale")
                afficher_diagramme_en_anneau(base1,'Situation Matrimoniale (SM)')
                st.header("Nationalité")
                afficher_histogramme(base1,'Nationalité')


        with col[1]:
                st.header("age")
                base2=data2[data2['ÉLIGIBILITÉ_AU_DON.'].isin(Eligi_selectionne)]

                afficher_evolution_dons(group(base2,"Age"),'Age')
                st.header("Genre")
                afficher_diagramme_en_anneau(base1,"Genre")
                st.header("Réligion")
                afficher_histogramme(base1,"Religion")
            
        
        with st.container():
                st.header("Profession")
                afficher_histogramme(base1,'Profession')
                #afficher_histogramme(base, 'Arrondissement de résidence')

    if onglets_selectionnee=="Analyse par sexe":
        
        with st.sidebar:
                df1=df.copy()
                Genre=df1["Genre"].unique()
                Eligi= df1["ÉLIGIBILITÉ AU DON."].unique()
                Genre_selectionne=st.sidebar.multiselect(
                "Choississez le sexe:",
                options = Genre,
                default = Genre[0])
                df1=df1[df1['Genre'].isin(Genre_selectionne)]

                Eligi_selectionne=st.sidebar.multiselect(
                "Choississez l'état de l'individu:",
                options = Eligi,
                default = Eligi[0])
                Mois=df['Mois_Annee'].unique()

                Mois_selectionne=st.sidebar.multiselect(
                "Choississez l'état de l'individu:",
                options = Mois,
                default = Mois[0])


        base=df1[df1['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
        base1=base[base["Mois_Annee"].isin(Mois_selectionne)]
        afficher_evolution_dons(group(base,'Mois_Annee'), 'Mois_Annee')
        col = st.columns(2)
        with col[0]:
                #afficher_diagramme_circulaire(base,'ÉLIGIBILITÉ AU DON.')
                st.header("Matrimoniale")
                afficher_diagramme_en_anneau(base1,'Situation Matrimoniale (SM)')
                st.header("Nationalité")
                afficher_histogramme(base1,'Nationalité')


        with col[1]:
                #st.header("Genre")
                #afficher_diagramme_en_anneau(base1,'Genre')
                base2=data2[data2['ÉLIGIBILITÉ_AU_DON.'].isin(Eligi_selectionne)]
                base3=base2[base2["Genre_"].isin(Genre_selectionne)]
                afficher_evolution_dons(group(base2,"Age"),'Age')
                st.header("Réligion")
                afficher_histogramme(base1,"Religion")
            
        
        with st.container():
                st.header("Proffession")
                afficher_histogramme(base1,'Profession')
                #afficher_histogramme(base, 'Arrondissement de résidence')

