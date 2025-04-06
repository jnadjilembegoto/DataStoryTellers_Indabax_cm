import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import streamlit as st
import pydeck as pdk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import plotly.graph_objects as go
from kmodes.kmodes import KModes
from streamlit_echarts import st_echarts
from Datas.data_link import data_dir


def page_profil_load():
    path = data_dir('base_streamlit_storytellers.xlsx')
    data = pd.read_excel(path, sheet_name='year')
    data2 = pd.read_excel(path, sheet_name='donneur')


    # Charger les données
    df=data.copy()
    with st.sidebar:
        st.title('🔬 Profilage')
        st.markdown("---")
        # --- CONTENU PRINCIPAL DE L'APPLICATION ---
    st.markdown("""
            <style>
            .block-container {
                background-color: #f5f5f5;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .stMetric {
                background-color: white;
                padding: 15px;
                border-radius: 8px;
            }
            </style>
            """, unsafe_allow_html=True)

    # --- STYLE CSS ---
    st.markdown("""
        <style>
            body {
                background-color: #F9F9F9;
            }
            .title {
                color: #D12720;
                font-size: 36px;
                font-weight: bold;
            }
            .section-header {
                color: #D12720;
                font-size: 20px;
                font-weight: bold;
            }
            .next-drive {
                background-color: #fff5f5;
                padding: 20px;
                border-radius: 10px;
                border-left: 5px solid #D12720;
            }
        </style>
    """, unsafe_allow_html=True)



    # --- Style CSS personnalisé pour les conteneurs d'indicateurs ---
    st.markdown(
        """
        <style>
        .indicator-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
            margin-bottom: 20px;
            border: 1px solid #eee;
            position: relative; /* Pour le pseudo-élément */
            overflow: hidden; /* Empêche le pseudo-élément de dépasser */
        }
        .indicator-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background-color: #D12720; /* Couleur accent */
        }
        .indicator-title {
            color: #333;
            font-size: 16px;
            margin-bottom: 5px;
        }
        .indicator-value {
            font-size: 28px;
            font-weight: bold;
            color: #D12720;
        }
        .indicator-unit {
            font-size: 14px;
            color: #777;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    ## Donnons une couleur au



    st.markdown(
        """
        <style>
            /* Couleur principale (rouge sang) */
            :root {
                --primary-color: #D12720;
                --secondary-color: #e9ecef; /* Gris clair subtil pour le fond */
                --text-color: #333; /* Gris foncé pour le texte principal */
                --accent-color: #007bff; /* Bleu pour les actions / liens */
            }

            body {
                background-color: var(--secondary-color);
                color: var(--text-color);
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
            }

            /* ... le reste de votre CSS ... */
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Personnalisons la couleur du sidebar 
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                background-color: #ADD8E6 !important; /* Bleu clair */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def generate_distinct_colors(n_colors):
        """
        Génère une palette automatique de couleurs distinctes
        - Le choix des couleurs varie la teinte (H) sur le cercle chromatique,
        la saturation (S) et la luminosité (V) sont ajustées pour rendre les couleurs bien visibles.
        """
        palette = []
        
        for i in range(n_colors):
            # Ajuster la teinte pour garantir des couleurs distinctes
            h = (i / n_colors) % 1.0  # Étaler les couleurs sur le cercle chromatique
            s = 0.9 # Saturation élevée pour des couleurs vives
            v = 0.9  # Luminosité un peu élevée pour ne pas avoir de couleurs trop sombres
            
            # Convertir HSV en RGB
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            hex_color = '#{:02x}{:02x}{:02x}'.format(int(r*255), int(g*255), int(b*255))
            palette.append(hex_color)
        
        return palette

    ## Créer une clonne classe d'âge
    def creer_classe_age_amplitude_egale(df, nom_colonne_age, nom_nouvelle_colonne='Classe_Age', n_classes=5):
        """
        Crée une nouvelle colonne 'Classe_Age' avec un nombre spécifié de classes
        ayant une amplitude égale (entière), basées sur le minimum et le maximum
        entiers de la colonne d'âge.

        :param df: DataFrame contenant la colonne d'âge.
        :param nom_colonne_age: Nom de la colonne contenant l'âge des individus.
        :param nom_nouvelle_colonne: Nom de la nouvelle colonne à créer (par défaut 'Classe_Age').
        :param n_classes: Le nombre de classes d'âge à créer (par défaut 5).
        :return: DataFrame avec la nouvelle colonne 'Classe_Age'.
        """
        if nom_colonne_age not in df.columns:
            print(f"Erreur: La colonne '{nom_colonne_age}' n'existe pas dans le DataFrame.")
            return df

        min_age = int(df[nom_colonne_age].min())
        max_age = int(df[nom_colonne_age].max())

        if min_age == max_age:
            df[nom_nouvelle_colonne] = f"Classe unique ({min_age} ans)"
            return df

        plage_age = max_age - min_age
        if plage_age < n_classes:
            print(f"Avertissement: La plage d'âge ({plage_age}) est inférieure au nombre de classes souhaité ({n_classes}). Les classes pourraient ne pas avoir une amplitude strictement égale.")
            amplitude_flottante = plage_age / n_classes
            bins = [min_age + round(i * amplitude_flottante) for i in range(n_classes + 1)]
            # S'assurer que la dernière borne est au moins max_age
            bins[-1] = max(bins[-1], max_age + 1)
            # Supprimer les bornes dupliquées qui pourraient résulter de l'arrondi
            bins = sorted(list(set(bins)))
            if len(bins) < n_classes + 1:
                n_classes = len(bins) - 1
            labels = [f'[{bins[i]}-{bins[i+1]-1}]' for i in range(n_classes)]

        else:
            amplitude = int(np.ceil(plage_age / n_classes))  # Amplitude entière (arrondi supérieur)
            bins = [min_age + i * amplitude for i in range(n_classes + 1)]
            # Ajuster la dernière borne pour inclure max_age
            if bins[-1] <= max_age:
                bins[-1] = max_age + 1
            labels = [f'[{bins[i]}-{bins[i+1]-1}]' for i in range(n_classes)]

        df[nom_nouvelle_colonne] = pd.cut(df[nom_colonne_age], bins=bins, labels=labels, right=False, include_lowest=True)

        return df
    # Fonction pour créer un graphique en anneau avec style amélioré
    def create_donut_chart(labels, values):
        # Générer une palette de couleurs automatiquement selon le nombre de modalités
        n = len(labels)
        colors = generate_distinct_colors(n_colors=n)

        fig = go.Figure(data=[go.Pie(
            labels=labels, values=values, hole=0.4,
            marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2)),
            textinfo='percent',
            insidetextorientation='horizontal'
        )])
        
        fig.update_layout(
            #title=dict(text=title, font=dict(size=16, family="Arial", color="black"), x=0.1),
            showlegend=True, legend=dict(orientation="h", y=-0.2),
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)"
        )
        return fig


    ## Calcul de l'âge au moment du fon de sang
    def calculer_age_au_don(df, colonne_date_remplissage, colonne_date_naissance, colonne_age_resultat='Age au Don'):
        """
        Calcule l'âge des individus au moment du don de sang et ajoute une nouvelle colonne 'Age au Don'.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données des donneurs.
            colonne_date_remplissage (str): Le nom de la colonne contenant la date de remplissage de la fiche.
            colonne_date_naissance (str): Le nom de la colonne contenant la date de naissance.
            colonne_age_resultat (str, optional): Le nom de la nouvelle colonne pour l'âge calculé.
                                                Par défaut, elle est nommée 'Age au Don'.

        Returns:
            pd.DataFrame: Le DataFrame avec une nouvelle colonne contenant l'âge au moment du don.
        """
        # Convertir les colonnes de dates au format datetime si ce n'est pas déjà le cas
        df[colonne_date_remplissage] = pd.to_datetime(df[colonne_date_remplissage])
        df[colonne_date_naissance] = pd.to_datetime(df[colonne_date_naissance])

        # Calculer la différence entre les dates en jours
        df['Difference_Jours'] = (df[colonne_date_remplissage] - df[colonne_date_naissance]).dt.days

        # Calculer l'âge en années (approximation simple)
        df[colonne_age_resultat] = (df['Difference_Jours'] / 365.25).round().astype(int)

        # Supprimer la colonne temporaire de différence en jours
        df = df.drop(columns=['Difference_Jours'])

        return df


    def clustering_categoriel(df, colonne_clustering, n_clusters):
        """
        Effectue un clustering K-Modes et ajoute une colonne "Classe" avec des noms
        basés sur les centroïdes des clusters. Retourne uniquement le DataFrame.

        :param df: DataFrame contenant les données
        :param colonne_clustering: Liste des colonnes catégorielles à utiliser
        :param n_clusters: Nombre de classes
        :return: DataFrame avec une nouvelle colonne "Classe"
        """
        if not colonne_clustering:
            print("Erreur: Aucune colonne catégorielle spécifiée.")
            return df

        for col in colonne_clustering:
            if col not in df.columns:
                print(f"Erreur: La colonne {col} n'existe pas dans le DataFrame.")
                return df

        km = KModes(n_clusters=n_clusters, init="Huang", n_init=5, verbose=0)
        clusters = km.fit_predict(df[colonne_clustering])
        centroids = km.cluster_centroids_

        classe_mapping = {}
        for i in range(n_clusters):
            centroid_tuple = tuple(centroids[i])
            classe_name = f"Classe_{'_'.join(centroid_tuple)}"
            classe_mapping[i] = classe_name

        df["Classe"] = [classe_mapping[c] for c in clusters]
        return df


    # Graphique polaires
    def afficher_graphique_barres_polaire(base, colonne):
        """
        Affiche un graphique à barres polaire interactif représentant la distribution des professions.
        Au survol, affiche le nom de la modalité et le nombre.
        Les barres sont tracées en fonction du pourcentage.
        """
        if base.empty:
            st.write("Aucune donnée disponible.")
            return

        # Calculer le nombre d'individus par profession
        profession_counts = base[colonne].value_counts().reset_index()
        profession_counts.columns = [colonne, 'Nombre']
        total_individus = profession_counts['Nombre'].sum()
        profession_counts['Pourcentage'] = (profession_counts['Nombre'] / total_individus) * 100
        profession_counts = profession_counts.sort_values(by='Pourcentage', ascending=False).reset_index(drop=True)
        professions = profession_counts[colonne].tolist()
        pourcentages = profession_counts['Pourcentage'].tolist()
        nombres = profession_counts['Nombre'].tolist()

        fig = go.Figure(go.Barpolar(
            r=pourcentages,
            theta=np.linspace(0, 360, len(professions), endpoint=False).tolist(),
            thetaunit='degrees',
            name='Profession',
            marker_color=px.colors.qualitative.Plotly * (len(professions) // len(px.colors.qualitative.Plotly) + 1),
            hovertemplate='<b>%{theta}</b><br>Nombre: %{customdata}<br>Pourcentage: %{r:.2f}%<extra></extra>',
            customdata=nombres,
            text=professions, # Les noms des professions pour les labels
            # textposition='outside' # Cette propriété n'est pas valide pour go.Barpolar
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(showline=False,
                    visible=False,
                    range=[0, max(pourcentages) * 1.2],
                    tickformat='%', # Afficher les pourcentages sur l'axe radial
                    #ticksuffix='%'
                ),
                angularaxis=dict(
                    tickvals=np.linspace(0, 360, len(professions), endpoint=False).tolist(),
                    ticktext=professions,
                direction='clockwise'
                )
            ),
            #title=f"Distribution des individus par profession",
            showlegend=False,
            width=  400,
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)



    def afficher_countplot_par_cluster(df, variable):
        if variable not in df.columns:
            st.error(f"La variable '{variable}' n'existe pas dans le DataFrame.")
            return

        df['Classe'] = df['Classe'].astype(str)

        # Choisir une palette de couleurs sur le thème du don de sang
        blood_palette = sns.color_palette("Reds", n_colors=df['Classe'].nunique())
        sns.set_palette(blood_palette)
        sns.set_style("whitegrid")
        sns.set_context("notebook", font_scale=1.1) # Ajuster le contexte pour la présentation

        plt.figure(figsize=(14, 9)) # Augmenter la taille pour une meilleure visibilité
        ax = sns.countplot(x=variable, data=df, order=df[variable].value_counts().index, hue='Classe')
        plt.title(f'Caractéristiques des clusters suivant {variable}', fontsize=16, fontweight='bold')
        plt.xlabel(variable, fontsize=12)
        plt.ylabel('Nombre de donneurs', fontsize=12) # Rendre l'axe Y plus spécifique
        plt.legend(title='Classe', fontsize=10)

        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}',
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='bottom', fontsize=10, color='black') # Améliorer la lisibilité des annotations

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
            labels={var2: var2, 'Pourcentage': 'Pourcentage (%)'},
        # showlegend=False,
            width=400,
            height=400
        )

            fig.update_traces(textinfo='percent', hoverinfo='percent')

                # Afficher le diagramme circulaire
            fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
            st.plotly_chart(fig)
            


    def afficher_diagramme_en_anneau(base, var2):
        if base.empty:
            st.write("Aucune donnée disponible.")
            return

        # Préparer les données de répartition
        count_data = base[var2].value_counts(normalize=True) * 100
        data_chart = [
            {"value": round(pct, 2), "name": str(cat)}
            for cat, pct in count_data.items()
        ]

        option = {
            "tooltip": {
                "trigger": "item",
                "formatter": "{b} : {d}%"
            },
            "legend": {
                "orient": "vertical",
                "left": "right",
                "top": "center",
                "textStyle": {
                    "fontSize": 14
                }
            },
            "series": [
                {
                    "name": var2,
                    "type": "pie",
                    "radius": ["25%", "50%"],  # donut
                    "avoidLabelOverlap": False,
                    "itemStyle": {
                        "borderRadius": 10,
                        "borderColor": "#fff",
                        "borderWidth": 2
                    },
                    "label": {
                        "show":False,
                        "position": "outside",
                        "formatter": "{b} : {d}%",
                        "fontSize": 14
                    },
                    "labelLine": {
                        "show":False
                    },
                    "emphasis": {
                        "label": {
                            "show":False,
                            "fontSize": 16,
                            "fontWeight": "bold"
                        }
                    },
                    "data": data_chart
                }
            ]
        }

        st_echarts(options=option, height="400px",width="400px")



    def afficher_histogramme_personnalise(base_name, colonne):
        """
        Affiche un graphique de barres horizontales représentant la distribution des professions.

        Args:
            base_name (pd.DataFrame): La base de données contenant les informations.
            colonne_profession (str): Le nom de la colonne contenant les professions.
            titre_graphique (str): Le titre du graphique.
        """
        if base_name.empty:
            st.write("Aucune donnée disponible.")
            return

        # Calculer le nombre d'individus par profession
        profession_counts = base_name[colonne].value_counts().reset_index()
        profession_counts.columns = [colonne, 'Nombre']

        # Calculer les pourcentages
        total_individus = len(base_name)
        if total_individus > 0:
            profession_counts['Pourcentage'] = (profession_counts['Nombre'] / total_individus) * 100
        else:
            profession_counts['Pourcentage'] = 0

        # Trier par pourcentage décroissant
        profession_counts = profession_counts.sort_values(by='Pourcentage', ascending=False).reset_index(drop=True)

        professions = profession_counts[colonne].tolist()
        pourcentages = profession_counts['Pourcentage'].tolist()

        fig = go.Figure()

        for i in range(len(professions)):
            profession = professions[i]
            pourcentage = pourcentages[i]

            fig.add_trace(go.Bar(
                x=[pourcentage],
                y=[profession],
                orientation='h',
                text=[f"{pourcentage:.2f}%"],
                textposition='outside',
                hovertemplate=f"<b>Profession</b>: {profession}<br>" +
                            f"<b>Pourcentage</b>: {pourcentage:.2f}%<extra></extra>"
            ))

        fig.update_layout(
            #title=titre_graphique,
            xaxis=dict(range=[0, 100], ticksuffix='%', title=None),
            yaxis=dict(showticklabels=True, title=None),
            barmode='group',
            showlegend=False,
            margin=dict(l=200, r=20, t=40, b=20), # Marge gauche pour les professions potentiellement longues
            plot_bgcolor='white',
            paper_bgcolor='white',
            width=400,
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)


    def prepare_chart_data(df, column):
            count_data = df[column].value_counts(normalize=True) * 100
            return count_data.index.tolist(), count_data.values.tolist()

    variables_to_plot = [
        "Niveau d'etude", "Genre", "Situation Matrimoniale (SM)", "ÉLIGIBILITÉ AU DON.","Nationalité","Religion"
    ]

    chart_data = {}
    for col in variables_to_plot:
        if col in df.columns:
            chart_data[col] = prepare_chart_data(df, col)


    st.sidebar.write("## Navigation")
    st.sidebar.write("Aller ")
    titres_onglets = ["Caractéristiques Démographiques des donneurs", "Caractéristiques Biologiques des donneurs","Par cluster"]
    onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
    if onglets_selectionnee=="Caractéristiques Démographiques des donneurs":
        st.header('Profil selon les caractéristiques socio-démographique')
        with st.sidebar:
                Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
                Eligi=Eligi.tolist()+["Tout le monde"]
                Eligi_selectionne=st.sidebar.selectbox(
                "Choississez l'état de l'individu:",
                Eligi
                )
        if Eligi_selectionne=="Tout le monde":
            nombre_individus = len(df)
        # age_moyen = base_age["Age_Don"].mean().round(1) if 'Age_Don' in base_age.columns else None
            hemoglobine_moyenne = df['Taux d’hémoglobine'].mean().round(1) if "Taux d’hémoglobine" in df.columns else None

            # --- Affichage des indicateurs dans des colonnes avec le style personnalisé ---
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                    <div class='indicator-container'>
                        <div class='indicator-title'>Nombre donneurs </div>
                        <div class='indicator-value'>{nombre_individus}</div>
                        <div class='indicator-unit'>Personnes</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class='indicator-container'>
                        <div class='indicator-title'>Taux d'Hémoglobine Moyen</div>
                        <div class='indicator-value'>{hemoglobine_moyenne if hemoglobine_moyenne is not None else 'N/A'}</div>
                        <div class='indicator-unit'>g/dL</div>
                    </div>
                """, unsafe_allow_html=True)

                if hemoglobine_moyenne is None:
                    st.warning(f"Colonne 'Taux d’hémoglobine' non trouvée pour calculer le taux d'hémoglobine moyen.")
        
            st.write("Selon l'arrondissement de résidence ")
            colonne1,colonne2 = st.columns(2)
            with colonne1:
                    afficher_histogramme_personnalise(df,"Arrondissement de résidence")
            with colonne2:
                st.write("Selon le Genre")
                st.plotly_chart(create_donut_chart(*chart_data["Genre"]), use_container_width=True)
            colonne_clustering1=["Niveau d'etude","Genre","Situation Matrimoniale (SM)"]
            

            st.markdown("<h3 style='text-align: center;'>Selon la Nationalité</h3>", unsafe_allow_html=True)
            colonne1,colonne2 = st.columns(2)
            with colonne1:
                    #afficher_histogramme_personnalise(df,"Arrondissement de résidence")
                    afficher_histogramme_personnalise(df, "Nationalité")
            with colonne2:
                #st.write("Selon le Genre")
                #st.plotly_chart(create_donut_chart(*chart_data["Genre"]), use_container_width=True)
                with st.container():
                    # Détails par groupe sanguin

                    Nationali_type_counts = df['Nationalité'].value_counts()
                    
                    # Affichage en 2 colonnes
                    b_col1, b_col2 = st.columns(2)
                    
                    for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                        if i % 2 == 0:
                            with b_col1:
                                st.metric(blood_type, count)
                        else:
                            with b_col2:
                                st.metric(blood_type, count)
            #with colonne2:
            

            Genre=df["Genre"].unique()
            Genre_list=Genre.tolist()+ ["Tout le monde"]
            Genre_selectionne=st.selectbox(
            "Choississez le sexe de l'individu:",
            Genre_list)   
            if Genre_selectionne=='Tout le monde':
                
                col = st.columns(2)
                #base_genre=base[base['Genre']==Genre_selectionne]
            
                with col[0]:
                        st.write("Selon le Statut Matrimoniale")
                        afficher_diagramme_en_anneau(df,"Situation Matrimoniale (SM)")
                with col[1]:
                        st.write("Selon la réligion")
                        afficher_diagramme_en_anneau(df, "Religion")
                st.markdown("<h3 style='text-align: center;'>Selon le niveau d'étude</h3>", unsafe_allow_html=True)
                colonne1,colonne2 = st.columns(2)
                with colonne1:
                        afficher_diagramme_en_anneau(df, "Niveau d'etude")
                with colonne2:
                    with st.container():
                    

                        Nationali_type_counts = df["Niveau d'etude"].value_counts()
                        
                        # Affichage en 2 colonnes
                        b_col1, b_col2 = st.columns(2)
                        
                        for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                            if i % 2 == 0:
                                with b_col1:
                                    st.metric(blood_type, count)
                            else:
                                with b_col2:
                                    st.metric(blood_type, count)

            else:
                col = st.columns(2)
                base_genre=df[df['Genre']==Genre_selectionne]
            
            
                #base_genre=base[base['Genre']==Genre_selectionne]
            
                with col[0]:
                        st.write("Selon le Statut Matrimoniale")
                        afficher_diagramme_en_anneau(base_genre,"Situation Matrimoniale (SM)")
                with col[1]:
                        st.write("Selon la réligion")
                        afficher_diagramme_en_anneau(base_genre, "Religion")
                st.markdown("<h3 style='text-align: center;'>Selon le niveau d'étude</h3>", unsafe_allow_html=True)
                colonne1,colonne2 = st.columns(2)
                with colonne1:
                        afficher_diagramme_en_anneau(base_genre, "Niveau d'etude")
                with colonne2:
                    with st.container():
                    

                        Nationali_type_counts = base_genre["Niveau d'etude"].value_counts()
                        
                        # Affichage en 2 colonnes
                        b_col1, b_col2 = st.columns(2)
                        
                        for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                            if i % 2 == 0:
                                with b_col1:
                                    st.metric(blood_type, count)
                            else:
                                with b_col2:
                                    st.metric(blood_type, count)
        else:
            base=df[df['ÉLIGIBILITÉ AU DON.']==Eligi_selectionne]
            # Calculer les indicateurs
        #base_age=calculer_age_au_don(base_Quartier, 'Date de remplissage de la fiche', 'Date de naissance', 'Age_Don')
            nombre_individus = len(base)
        # age_moyen = base_age["Age_Don"].mean().round(1) if 'Age_Don' in base_age.columns else None
            hemoglobine_moyenne = base['Taux d’hémoglobine'].mean().round(1) if "Taux d’hémoglobine" in base.columns else None

            # --- Affichage des indicateurs dans des colonnes avec le style personnalisé ---
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                    <div class='indicator-container'>
                        <div class='indicator-title'>Nombre de donneurs </div>
                        <div class='indicator-value'>{nombre_individus}</div>
                        <div class='indicator-unit'>Personnes</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class='indicator-container'>
                        <div class='indicator-title'>Taux d'Hémoglobine Moyen</div>
                        <div class='indicator-value'>{hemoglobine_moyenne if hemoglobine_moyenne is not None else 'N/A'}</div>
                        <div class='indicator-unit'>g/dL</div>
                    </div>
                """, unsafe_allow_html=True)
            if hemoglobine_moyenne is None:
                    st.warning(f"Colonne 'Taux d’hémoglobine' non trouvée pour calculer le taux d'hémoglobine moyen.")
            st.write("Selon l'arrondissement de résidence ")
            afficher_histogramme_personnalise(base,"Arrondissement de résidence")
            colonne_clustering1=["Niveau d'etude","Genre","Situation Matrimoniale (SM)"]
            st.markdown("<h3 style='text-align: center;'>Selon la Nationalité</h3>", unsafe_allow_html=True)
            colonne1,colonne2 = st.columns(2)
            with colonne1:
                    #afficher_histogramme_personnalise(df,"Arrondissement de résidence")
                    afficher_histogramme_personnalise(base, "Nationalité")
            with colonne2:
                #st.write("Selon le Genre")
                #st.plotly_chart(create_donut_chart(*chart_data["Genre"]), use_container_width=True)
                with st.container():
                    # Détails par groupe sanguin

                    Nationali_type_counts = base['Nationalité'].value_counts()
                    
                    # Affichage en 2 colonnes
                    b_col1, b_col2 = st.columns(2)
                    
                    for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                        if i % 2 == 0:
                            with b_col1:
                                st.metric(blood_type, count)
                        else:
                            with b_col2:
                                st.metric(blood_type, count)
            #with colonne2:
            

            Genre=df["Genre"].unique()
            Genre_list=Genre.tolist()+ ["Tout le monde"]
            Genre_selectionne=st.selectbox(
            "Choississez le sexe de l'individu:",
            Genre_list)   
            if Genre_selectionne=='Tout le monde':
                
                col = st.columns(2)
                base_genre=base[base['Genre']==Genre_selectionne]
            
                with col[0]:
                        st.write("Selon le Statut Matrimoniale")
                        afficher_diagramme_en_anneau(base_genre,"Situation Matrimoniale (SM)")
                with col[1]:
                        st.write("Selon la réligion")
                        afficher_diagramme_en_anneau(base_genre, "Religion")
                st.markdown("<h3 style='text-align: center;'>Selon le niveau d'étude</h3>", unsafe_allow_html=True)
                colonne1,colonne2 = st.columns(2)
                with colonne1:
                        afficher_diagramme_en_anneau(base_genre, "Niveau d'etude")
                with colonne2:
                    with st.container():
                    

                        Nationali_type_counts = base_genre["Niveau d'etude"].value_counts()
                        
                        # Affichage en 2 colonnes
                        b_col1, b_col2 = st.columns(2)
                        
                        for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                            if i % 2 == 0:
                                with b_col1:
                                    st.metric(blood_type, count)
                            else:
                                with b_col2:
                                    st.metric(blood_type, count)

            else:
                col = st.columns(2)
                base_genre=base[base['Genre']==Genre_selectionne]
            
            
                #base_genre=base[base['Genre']==Genre_selectionne]
            
                with col[0]:
                        st.write("Selon le Statut Matrimoniale")
                        afficher_diagramme_en_anneau(base_genre,"Situation Matrimoniale (SM)")
                with col[1]:
                        st.write("Selon la réligion")
                        afficher_diagramme_en_anneau(base_genre, "Religion")
                st.markdown("<h3 style='text-align: center;'>Selon le niveau d'étude</h3>", unsafe_allow_html=True)
                colonne1,colonne2 = st.columns(2)
                with colonne1:
                        afficher_diagramme_en_anneau(base_genre, "Niveau d'etude")
                with colonne2:
                    with st.container():
                    

                        Nationali_type_counts =base_genre["Niveau d'etude"].value_counts()
                        
                        # Affichage en 2 colonnes
                        b_col1, b_col2 = st.columns(2)
                        
                        for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                            if i % 2 == 0:
                                with b_col1:
                                    st.metric(blood_type, count)
                            else:
                                with b_col2:
                                    st.metric(blood_type, count)

    if onglets_selectionnee=="Caractéristiques Biologiques des donneurs":
        st.write('# Profil des donneurs suivant les caractéristiques Biologiques')
        data2=creer_classe_age_amplitude_egale(data2, "Age", 'Classe_Age',5)
        
        #base_cluster =data2[data2["Classe"]==classe_selectionnee]

        nombre_individus = len(data2)
        Age_moyenne = data2['Age'].mean().round(1) if "Age" in data2.columns else None

        # --- Affichage des indicateurs dans des colonnes avec le style personnalisé ---
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>Nombre de personnes </div>
                    <div class='indicator-value'>{nombre_individus}</div>
                    <div class='indicator-unit'>donneurs</div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>Age Moyen</div>
                    <div class='indicator-value'>{Age_moyenne if Age_moyenne is not None else 'N/A'}</div>
                    <div class='indicator-unit'>ans</div>
                </div>
            """, unsafe_allow_html=True)
            if Age_moyenne is None:
                st.warning(f"Colonne 'Taux d’hémoglobine' non trouvée pour calculer le taux d'hémoglobine moyen.")
        col = st.columns(2)
        #with st.sidebar:
        Genre= data2["Sexe"].unique()
        Genre_list=Genre.tolist()+ ['Tout le monde']
        Genre_selectionne=st.selectbox("Choississez le sexe de l'individu:",
        Genre_list
        )
        if Genre_selectionne=="Tout le monde":
            base=data2
            col = st.columns(2)
            #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
            with col[0]:
                    st.write("Classe d'âge")
                    afficher_diagramme_en_anneau(base,"Classe_Age")
                    st.write("Phenotype")
                    afficher_histogramme_personnalise(base,'Phenotype')
            with col[1]:
                    st.write("type de Donation")
                    afficher_diagramme_en_anneau(base,"Type de donation")
                    st.write("Groupe Sanguin ABO / Rhesus")
                    afficher_histogramme(base,'Groupe Sanguin ABO / Rhesus')
                    
            #with st.container():
                
        
        else:

            col = st.columns(2)
            #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
            base=data2[data2['Sexe']==Genre_selectionne]
            with col[0]:
                    st.write("Classe d'âge")
                    afficher_diagramme_en_anneau(base,"Classe_Age")
                    st.write("Phenotype")
                    afficher_histogramme_personnalise(base,'Phenotype')
            with col[1]:
                    st.write("type de Donation")
                    afficher_diagramme_en_anneau(base,"Type de donation")
                    st.write("Groupe Sanguin ABO / Rhesus")
                    afficher_histogramme(base,'Groupe Sanguin ABO / Rhesus')
                    
            #with st.container():
                
                    
        
    if onglets_selectionnee=="Par cluster":
        #base_clustering=base[colonne_clustering1]
        #st.write(clustering_categoriel(base_clustering, colonne_clustering1,5))
        st.write("Analyse par clustering")
                #afficher_histogramme(base, 'Arrondissement de résidence')
        titres_onglets = ["Clustering suivant Caractéristiques Démographiques des donneurs", "Clustering suivant Caractéristiques Biologiques des donneurs"]
        onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
        if onglets_selectionnee=="Clustering suivant Caractéristiques Démographiques des donneurs":
            
            base=df[df["ÉLIGIBILITÉ AU DON."]=="Eligible"]
            colonne_clustering1=["Niveau d'etude","Genre","Situation Matrimoniale (SM)",'Religion']
            base_clustering=pd.DataFrame(clustering_categoriel(base, colonne_clustering1,4))
            #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
            classe=base_clustering["Classe"].unique()
            classe_selectionnee=st.selectbox("choisir une classe:",options=classe)
            
            base_cluster =base_clustering[base_clustering["Classe"]==classe_selectionnee]

            
            # Créer deux colonnes pour afficher les graphi
            
            if len(classe_selectionnee)==0:
                st.write('veuillez selectionné au moins une classe')
            else:
            
                #st.write(f"{classe_selectionnee}")
                col = st.columns(2)
                with col[0]:
                    
                    st.write("Selon le Niveau d'étude")
                    afficher_diagramme_en_anneau(base_cluster, "Niveau d'etude")
                    st.write("Selon le Statut Matrimonial")
                    afficher_histogramme_personnalise(base_cluster, "Situation Matrimoniale (SM)")
                with col[1]:
                    st.write("Selon la Rligion")
                    afficher_diagramme_en_anneau(base_cluster, "Religion")
                    st.write("Selon le Genre")
                    afficher_histogramme_personnalise(base_cluster, "Genre")
                    
                

        if onglets_selectionnee=="Clustering suivant Caractéristiques Biologiques des donneurs":
            
            data2=creer_classe_age_amplitude_egale(data2, "Age", 'Classe_Age',5)
            colonne_clustering1=["Sexe","Groupe Sanguin ABO / Rhesus","Type de donation",'Phenotype']
            base_clustering=pd.DataFrame(clustering_categoriel(data2, colonne_clustering1,4))
            #base1=df[df['Quartier de Résidence'].isin(quartier_selectionne)]
            
            classe=base_clustering["Classe"].unique()
            classe_selectionnee=st.selectbox("choisir une classe:",options=classe)
            
            
            
            base_cluster =base_clustering[base_clustering["Classe"]==classe_selectionnee]

            nombre_individus = len(base_cluster)
        # age_moyen = base_age["Age_Don"].mean().round(1) if 'Age_Don' in base_age.columns else None
            Age_moyenne = base_cluster['Age'].mean().round(1) if "Age" in base_cluster.columns else None

            # --- Affichage des indicateurs dans des colonnes avec le style personnalisé ---
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                    <div class='indicator-container'>
                        <div class='indicator-title'>Nombre de personnes </div>
                        <div class='indicator-value'>{nombre_individus}</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class='indicator-container'>
                        <div class='indicator-title'>Age Moyen</div>
                        <div class='indicator-value'>{Age_moyenne if Age_moyenne is not None else 'N/A'}</div>
                        <div class='indicator-unit'>ans</div>
                    </div>
                """, unsafe_allow_html=True)
                if Age_moyenne is None:
                    st.warning(f"Colonne 'Taux d’hémoglobine' non trouvée pour calculer le taux d'hémoglobine moyen.")
            col = st.columns(2)
        
                    # Créer deux colonnes pour afficher les graphi
            with col[0]:
                        st.write('Profil suivant le sexe')
                        afficher_diagramme_en_anneau(base_cluster, "Sexe")
                        st.write("Profil suivant le Groupe Sanguin ABO / Rhesus ")
                        afficher_histogramme_personnalise(base_cluster, "Groupe Sanguin ABO / Rhesus")

            with col[1]:
                        st.write("Profils suivant  la classe d'âge")
                        afficher_diagramme_en_anneau(base_cluster, "Type de donation")
                        st.write('Profils suivant le type de Phénotype')
                        afficher_histogramme_personnalise(base_cluster, "Phenotype")
            st.write(f"Profil  suivant la classe d'âge")
            afficher_histogramme_personnalise(base_cluster,"Classe_Age")


    st.markdown("""
            <style>
                .css-1v3fvcr { text-align: center !important; }
                .stPlotlyChart { box-shadow: 7px 7px 10px rgba(0, 0, 0, 0.2); border-radius: 10px; }
                h4 { font-weight: bold; }
            </style>
        """, unsafe_allow_html=True)
