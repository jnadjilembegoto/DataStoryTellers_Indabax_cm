import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import streamlit as st
import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from kmodes.kmodes import KModes

from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
data = pd.read_excel(path, sheet_name='year')
data2 = pd.read_excel(path, sheet_name='donneur')


# Charger les données
df=data.copy()



def clustering_categoriel(df, colonne_clustering, n_clusters):
    """
    Effectue un clustering K-Modes sur un DataFrame contenant des variables catégorielles,
    et affiche un graphique des clusters en réduisant la dimension avec PCA sur Streamlit.

    :param df: DataFrame contenant les données
    :param colonne_clustering: Liste des colonnes catégorielles à utiliser
    :param n_clusters: Nombre de clusters (par défaut 3)
    :return: DataFrame avec une nouvelle colonne "Cluster"
    """
    if not colonne_clustering:
        st.error("Aucune colonne catégorielle spécifiée.")
        return None

    # Vérification que les colonnes existent
    for col in colonne_clustering:
        if col not in df.columns:
            st.error(f"La colonne {col} n'existe pas dans le DataFrame.")
            return None

    # Création du modèle K-Modes
    km = KModes(n_clusters=n_clusters, init="Huang", n_init=5, verbose=0)

    # Exécution du clustering
    clusters = km.fit_predict(df[colonne_clustering])

    # Ajout des clusters au DataFrame
    df["Cluster"] = clusters
    df['Cluster'] = df['Cluster'].astype(str)

    return df 
 
## Analyse pour determiner les caractéristiques des cluster
def afficher_countplot_par_cluster(df, variable):
    """
    Affiche un countplot de la variable spécifiée, coloré par cluster.

    :param df: DataFrame contenant les données
    :param variable: Nom de la variable à tracer
    """
    # Vérifier que la variable est dans le DataFrame
    if variable not in df.columns:
        st.error(f"La variable '{variable}' n'existe pas dans le DataFrame.")
        return

    # Vérifier que la colonne 'cluster_predicted_5' existe dans le DataFrame
    
    df['Cluster'] = df['Cluster'].astype(str)
    # Créer le graphique
    plt.figure(figsize=(12,8))
    
    ax=sns.countplot(x=variable, data=df, order=df[variable].value_counts().index, hue='Cluster')
    plt.title(f'caratéristiques des clusters suivant {variable}')
    plt.xlabel(variable)
    plt.ylabel('Nombre d\'observations')
    plt.legend(title='Cluster')
    # Ajouter les effectifs sur chaque barre
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10)
    # Afficher le graphique dans Streamlit
    st.pyplot(plt)
    
   

   

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
    with st.sidebar:
        st.title('🔬')
        st.markdown("---")
    titres_onglets = ["Caractéristiques Démographiques des donneurs", "Caractéristiques Biologiques des donneurs","Par cluster"]
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
        colonne_clustering1=["Niveau d'etude","Genre","Situation Matrimoniale (SM)"]
        #
        # clustering_categoriel(df, colonne_clustering1,2)
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
                st.header("Proffession")
                afficher_histogramme(base,'Profession')
                base_clustering=base[colonne_clustering1]
                
                
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

    if onglets_selectionnee=="Par cluster":
        #base_clustering=base[colonne_clustering1]
        #st.write(clustering_categoriel(base_clustering, colonne_clustering1,5))
        st.write("Analyse par clustering")
                #afficher_histogramme(base, 'Arrondissement de résidence')
        titres_onglets = ["Clustering suivant Caractéristiques Démographiques des donneurs", "Clustering suivant Caractéristiques Biologiques des donneurs"]
        onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
        if onglets_selectionnee=="Clustering suivant Caractéristiques Démographiques des donneurs":
            col = st.columns(2)
            base=df[df["ÉLIGIBILITÉ AU DON."]=="Eligible"]
            colonne_clustering1=["Niveau d'etude","Genre","Situation Matrimoniale (SM)",'Religion']
            base_clustering=pd.DataFrame(clustering_categoriel(base, colonne_clustering1,4))
            #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
            
        
            titres_onglets = ["visualisations cluster par cluster", "Comparaisons des clusters"]
            onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
            if onglets_selectionnee=="visualisations cluster par cluster":
                #with st.sidebar:
                    # Obtenir les clusters uniques
                    
                clusters = base_clustering["Cluster"].unique()
                u=clusters
                    # Sélecteur multiselect pour choisir plusieurs clusters
                Cluster_selectionne = st.sidebar.radio(
                        "Choisissez les clusters pour voir les caractéristiques :",options=u
                        #options=clusters.tolist(),
                        #"default=clusters.tolist()  # Par défaut, tous les clusters sont sélectionnés
                    )

                    # Filtrer le DataFrame pour inclure uniquement les clusters sélectionnés
                # Vérifie si des clusters ont été sélectionnés
                base_cluster = base_clustering[base_clustering['Cluster']==Cluster_selectionne]
                        #base_clustering[base_clustering['Cluster']==Cluster_selectionne]
                        
                        # Créer deux colonnes pour afficher les graphiques
                col = st.columns(2)

                with col[0]:
                            afficher_countplot_par_cluster(base_cluster, "Situation Matrimoniale (SM)")
                            afficher_countplot_par_cluster(base_cluster, "Niveau d'etude")

                with col[1]:
                            afficher_countplot_par_cluster(base_cluster, "Genre")
                            afficher_countplot_par_cluster(base_cluster, "Religion")
            else:
                        base_cluster =base_clustering
                        
                        # Créer deux colonnes pour afficher les graphi
                        with col[0]:
                            afficher_countplot_par_cluster(base_cluster, "Situation Matrimoniale (SM)")
                            afficher_countplot_par_cluster(base_cluster, "Niveau d'etude")

                        with col[1]:
                            afficher_countplot_par_cluster(base_cluster, "Genre")
                            afficher_countplot_par_cluster(base_cluster, "Religion")

    
        if onglets_selectionnee=="Clustering suivant Caractéristiques Biologiques des donneurs":
            col = st.columns(2)
            
            colonne_clustering1=["Sexe","Groupe Sanguin ABO / Rhesus","Type de donation",'Phenotype']
            base_clustering=pd.DataFrame(clustering_categoriel(data2, colonne_clustering1,4))
            #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
            
        
            titres_onglets = ["visualisations cluster par cluster", "Comparaisons des clusters"]
            onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
            if onglets_selectionnee=="visualisations cluster par cluster":
                #with st.sidebar:
                    # Obtenir les clusters uniques
                    
                clusters = base_clustering["Cluster"].unique()
                u=clusters
                    # Sélecteur multiselect pour choisir plusieurs clusters
                Cluster_selectionne = st.sidebar.radio(
                        "Choisissez les clusters pour voir les caractéristiques :",options=u
                        #options=clusters.tolist(),
                        #"default=clusters.tolist()  # Par défaut, tous les clusters sont sélectionnés
                    )

                    # Filtrer le DataFrame pour inclure uniquement les clusters sélectionnés
                # Vérifie si des clusters ont été sélectionnés
                base_cluster = base_clustering[base_clustering['Cluster']==Cluster_selectionne]
                        #base_clustering[base_clustering['Cluster']==Cluster_selectionne]
                        
                        # Créer deux colonnes pour afficher les graphiques
                col = st.columns(2)

                with col[0]:
                            afficher_countplot_par_cluster(base_cluster, "Sexe")
                            afficher_countplot_par_cluster(base_cluster, "Groupe Sanguin ABO / Rhesus")

                with col[1]:
                            afficher_countplot_par_cluster(base_cluster, "Type de donation")
                            afficher_countplot_par_cluster(base_cluster, "Phenotype")
            else:
                base_cluster =base_clustering
                        
                        # Créer deux colonnes pour afficher les graphi
                with col[0]:
                            afficher_countplot_par_cluster(base_cluster, "Sexe")
                            afficher_countplot_par_cluster(base_cluster, "Groupe Sanguin ABO / Rhesus")

                with col[1]:
                            afficher_countplot_par_cluster(base_cluster, "Type de donation")
                            afficher_countplot_par_cluster(base_cluster, "Phenotype")