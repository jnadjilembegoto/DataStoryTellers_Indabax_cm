import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import streamlit as st
import pydeck as pdk
import plotly.graph_objects as go
import numpy as np
import colorsys

import graphviz


from streamlit_echarts import st_echarts
from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
data = pd.read_excel(path, sheet_name='year')
df_donn=data[data["A-t-il (elle) déjà donné le sang"]=='Oui']

df=df_donn.copy()

def page_fidelisation():
    # --- CONTENU PRINCIPAL DE L'APPLICATION ---
    #st.markdown("<h1 class='title'>Tableau de Bord Don de Sang</h1>", unsafe_allow_html=True)


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

    st.markdown("<h2 style='text-align: center; font-weight: bold;'>Statistiques des donneurs réguliers</h2>", unsafe_allow_html=True)
    st.write("cette partie se consacre sur les individus ayant déja donné le sang au moins une fois avant la nouvelle seance de don de sang")


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


    st.markdown("""
        <style>
            .indicator-container {
                background-color: #007BFF; /* 🔵 bleu Bootstrap */
                border-radius: 10px;
                padding: 20px;
                color: white;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 10px;
            }
            .indicator-title {
                font-size: 18px;
                font-weight: bold;
            }
            .indicator-value {
                font-size: 32px;
                font-weight: bold;
                margin-top: 10px;
            }
            .indicator-unit {
                font-size: 14px;
                margin-top: 4px;
            }
        </style>
    """, unsafe_allow_html=True)


    st.markdown("""
        <style>
            /* 🩸 Fond général clair */
            body, .main, .block-container {
                background-color: #F9F9F9 !important;
                color: #2C3E50;
            }

            /* 🩺 En-têtes Streamlit */
            h1, h2, h3, h4, h5 {
                color: #C0392B;
            }

            /* 🔵 Boutons Streamlit */
            .stButton > button {
                background-color: #C0392B;
                color: white;
                border-radius: 8px;
                border: none;
                font-weight: bold;
            }
            .stButton > button:hover {
                background-color: #A93226;
                color: white;
            }

            /* 🔳 Boîtes de sélection (selectbox, slider, etc.) */
            .stSelectbox, .stSlider {
                background-color: #FFFFFF;
                border-radius: 5px;
            }

            /* 🎯 Titres centrés */
            .css-1v3fvcr {
                text-align: center !important;
            }

            /* 🔲 Encadré des graphiques Plotly */
            .stPlotlyChart {
                background-color: #F9F9F9;
                border: 2px solid #C0392B;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 4px 4px 10px rgba(192, 57, 43, 0.2);
            }

            /* 📦 Cartes statistiques (indicateurs) */
            .indicator-container {
                background-color: #2980B9;
                color: white;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            }

            .indicator-title {
                font-size: 18px;
                font-weight: bold;
            }

            .indicator-value {
                font-size: 32px;
                font-weight: bold;
                margin-top: 10px;
            }

            .indicator-unit {
                font-size: 14px;
                margin-top: 4px;
            }
        </style>
    """, unsafe_allow_html=True)


    ##  Recuperons la base des personnes ayant données le sang à plusieurs réprises

    


    st.markdown("""
    <style>
    /* === Fond principal de l'app === */
    [data-testid="stAppViewContainer"] {
        background-color: #E6A2A2;
        color: #31333F;
        font-family: 'Segoe UI', sans-serif;
    }

    /* === En-tête transparent === */
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }

    /* === Titres et textes === */
    h1, h2, h3, h4, h5, h6 {
        color: #FF4B4B;
    }

    p, li, span, div {
        color: #31333F;
    }

    /* === Boutons === */
    button[kind="primary"] {
        background-color: #FF4B4B;
        color: white;
        border: none;
        border-radius: 6px;
    }

    button[kind="primary"]:hover {
        background-color: #d93636;
    }

    /* === Widgets (inputs, sliders, selects, etc.) === */
    .stSelectbox, .stSlider, .stTextInput, .stTextArea {
        background-color: #93B8EF;
        color: #31333F;
        border-radius: 6px;
        border: 1px solid #FF4B4B;
    }

    /* === Code blocks, markdown, etc. === */
    .stMarkdown, .stCodeBlock {
        background-color: #f7dede;
        color: #31333F;
        border-radius: 6px;
    }

    /* === Graphviz charts === */
    svg {
        background-color: transparent !important;
    }

    .node text {
        fill: #31333F !important;
        font-size: 12px;
        font-family: 'Arial', sans-serif;
    }

    .node rect {
        fill: #93B8EF !important;
        stroke: #FF4B4B !important;
        rx: 8;
        ry: 8;
    }
    </style>
    """, unsafe_allow_html=True)


    # Définir les couleurs pour le thème des dons de sang
    primary_color = "#FF4B4B"  # Rouge vif (évoque le sang)
    secondary_color = "#93B8EF" # Jaune/Or (pour l'importance)
    background_color = "#E6A2A2" # Gris clair pour le fond
    text_color = "#31333F"      # Gris foncé pour le texte

    # Style CSS personnalisé
    st.markdown(f"""
        <style>
            .indicator-container {{
                background-color: {background_color};
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                border-left: 5px solid {primary_color}; /* Bordure colorée à gauche */
            }}
            .indicator-title {{
                font-size: 16px;
                color: {text_color};
                margin-bottom: 5px;
            }}
            .indicator-value {{
                font-size: 24px;
                font-weight: bold;
                color: {primary_color}; /* Couleur principale pour la valeur */
            }}
        </style>
    """, unsafe_allow_html=True)


    ## Ecrivons une fonction pour voir l'évolution de don de sang journaliser ou mensuelle
    ## Constructions d'arbre de donneurs reguliers


    def afficher_arbre_simplifie(df: pd.DataFrame, colonnes: list):
        """
        Affiche un arbre simplifié et narratif basé sur les variables sélectionnées.
        Args:
            df: DataFrame des données
            colonnes: liste ordonnée des colonnes à utiliser comme niveaux de l’arbre
        """

        def generer_id(niveau, modalite, parent=""):
            modalite = str(modalite).replace(" ", "_").replace("'", "").replace('"', "")
            return f"{niveau}_{modalite}_{parent}"

        def construire_arbre(df_filtre, parent_id, niveau):
            if niveau >= len(colonnes) or df_filtre.empty:
                return
            
            col = colonnes[niveau]
            total = len(df_filtre)
            
            n_modalites = 2 if niveau < 2 else 2  # Top 2 au début, puis top 1
            top_modalites = df_filtre[col].value_counts(normalize=True).nlargest(n_modalites)

            for modalite, prop in top_modalites.items():
                label = label = f"{col}\n{modalite} ({prop:.1%})"

                node_id = generer_id(niveau, modalite, parent_id)

                # Ajouter le nœud et la liaison
                dot.node(node_id, label)
                dot.edge(parent_id, node_id)

                # Filtrer pour l'étape suivante
                sous_df = df_filtre[df_filtre[col] == modalite]
                construire_arbre(sous_df, node_id, niveau + 1)

        

        try:
            dot = graphviz.Digraph(format="svg")
            dot.attr(rankdir="LR")  # Gauche → Droite
            #dot.attr("node", shape="box", style="filled", fillcolor="#FFEEEE", color="#BB0A21")
            dot.attr('node', shape='box', style='filled', fillcolor='#FFEEEE', color='#BB0A21', fontname='Arial', fontsize='10')


            # Racine = 1ère variable
            racine = "racine"
            dot.node(racine, colonnes[0], fillcolor="#DCDCDC")

            construire_arbre(df, racine, 0)

            st.graphviz_chart(dot)

        except Exception as e:
            st.error(f"Erreur lors de la génération de l’arbre : {str(e)}")
            st.code(str(e))



    def app_streamlit(df, key_suffix="1"):
        st.subheader(f"🩸 Répartitions des donneurs réguliers ")

        colonnes_qualitatives = [col for col in df.select_dtypes(include=['object', 'category']).columns.tolist() if col != 'Date de naissance' or col!='Horodateur']

        colonnes_choisies = st.multiselect(
            "🧩 Sélectionnez les variables dans l'ordre :",
            colonnes_qualitatives,
            default=colonnes_qualitatives[0:2],
            key=f"colonnes_{key_suffix}"
        )

    
    
        if len(colonnes_choisies) >= 2 and st.button("Afficher caractéristiques des donneurs reguliers") :
            afficher_arbre_simplifie(df, colonnes_choisies)
        elif len(colonnes_choisies) < 2:
            st.info("Veuillez sélectionner au moins deux variables.")



    ## Visualisation journalier ou mensuel
    def visualiser_dons_par_periode(df, colonne_date, periode):
        """
        Visualise le nombre ou la proportion de dons de sang par jour ou par mois.

        Args:
            df (pd.DataFrame): La base de données contenant les informations sur les dons.
            colonne_date (str): Le nom de la colonne contenant la date du don.
            periode (str, optional): La période d'agrégation ('jour' ou 'mois'). Par défaut 'jour'.
        """
        if colonne_date not in df.columns:
            st.error(f"La colonne '{colonne_date}' n'existe pas dans le DataFrame.")
            return

        try:
            df[colonne_date] = pd.to_datetime(df[colonne_date])
        except ValueError:
            st.error(f"Impossible de convertir la colonne '{colonne_date}' en format datetime. Veuillez vérifier le format des dates.")
            return

        if periode == 'jour':
            # Extraire le jour de la semaine
            df['Periode'] = df[colonne_date].dt.strftime('%A')#dt.day_name(locale='fr_FR')
            periode_ordre = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  #['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
            titre_nombre = 'Nombre de dons de sang par jour de la semaine'
            titre_proportion = 'Proportion des dons de sang par jour de la semaine'
            label_axe = 'Jour de la semaine'
            df['Periode'] = pd.Categorical(df['Periode'], categories=periode_ordre, ordered=True)
        elif periode == 'mois':
            # Extraire le mois
            df['Periode'] = df[colonne_date].dt.strftime('%B')#dt.month_name(locale='fr_FR')
            periode_ordre = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']  #['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
            titre_nombre = 'Nombre de dons de sang par mois'
            titre_proportion = 'Proportion des dons de sang par mois'
            label_axe = 'Mois'
            df['Periode'] = pd.Categorical(df['Periode'], categories=periode_ordre, ordered=True)
        else:
            st.error(f"La valeur '{periode}' n'est pas valide pour la période. Veuillez choisir 'jour' ou 'mois'.")
            return

        # Calculer le nombre par période
        dons_par_periode = df['Periode'].value_counts().sort_index()

        # Calculer la proportion par période
        proportions_par_periode = df['Periode'].value_counts(normalize=True).sort_index() * 100

        # Choisir le type de visualisation
        type_visualisation = st.radio(
            "Type de visualisation :",
            ("Nombre", "Proportion (%)")
        )

        if type_visualisation == "Nombre":
            fig = px.bar(dons_par_periode, x=dons_par_periode.index, y=dons_par_periode.values,
                        title=titre_nombre,
                        labels={'index': label_axe, 'y': 'Nombre de dons'})
            st.plotly_chart(fig, use_container_width=True)
        elif type_visualisation == "Proportion (%)":
            fig = px.bar(proportions_par_periode, x=proportions_par_periode.index, y=proportions_par_periode.values,
                        title=titre_proportion,
                        labels={'index': label_axe, 'y': 'Proportion (%)'})
            st.plotly_chart(fig, use_container_width=True)

    ## Créer une clonne classe d'âge
    def creer_classe_age_amplitude_egale(df, nom_colonne_age, nom_nouvelle_colonne='Classe_Age', n_classes=5):#
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



    # Fonction pour créer un graphique en anneau avec style amélioré
    def create_donut_chart(labels, values, title):
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
            title=dict(text=title, font=dict(size=16, family="Arial", color="black"), x=0.1),
            showlegend=True, legend=dict(orientation="h", y=-0.2),
            margin=dict(l=20, r=20, t=40, b=20),
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)",
            **dict(width=350, height=400) # Ajoutez ou modifiez width et height ici
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
            paper_bgcolor='white'
        )

        st.plotly_chart(fig, use_container_width=True)


    def afficher_graphique_barres_polaire(base, colonne_profession):
        """
        Affiche un graphique à barres polaire interactif représentant la distribution des professions.
        Au survol, affiche le nom de la modalité et le nombre.
        Les barres sont tracées en fonction du pourcentage.
        """
        if base.empty:
            st.write("Aucune donnée disponible.")
            return

        # Calculer le nombre d'individus par profession
        profession_counts = base[colonne_profession].value_counts().reset_index()
        profession_counts.columns = [colonne_profession, 'Nombre']
        total_individus = profession_counts['Nombre'].sum()
        profession_counts['Pourcentage'] = (profession_counts['Nombre'] / total_individus) * 100
        profession_counts = profession_counts.sort_values(by='Pourcentage', ascending=False).reset_index(drop=True)
        professions = profession_counts[colonne_profession].tolist()
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
                radialaxis=dict(
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
            title=f"Distribution des individus par profession",
            showlegend=False,
            width=750,
            height=750
        )

        st.plotly_chart(fig, use_container_width=True)
    ## Recuperons la liste des donneurs eligibles au don
    def afficher_pyramide_des_ages(df, colonne_age, colonne_genre):
        """
        Affiche une pyramide des âges des donneurs de sang par genre.
        Les modalités de genre sont détectées automatiquement.

        Args:
            df (pd.DataFrame): La base de données des donneurs de sang.
            colonne_age (str): Le nom de la colonne contenant l'âge des donneurs.
            colonne_genre (str): Le nom de la colonne contenant le genre des donneurs.
        """
        if colonne_age not in df.columns:
            st.error(f"La colonne '{colonne_age}' n'existe pas dans le DataFrame.")
            return
        if colonne_genre not in df.columns:
            st.error(f"La colonne '{colonne_genre}' n'existe pas dans le DataFrame.")
            return

        # Obtenir les modalités uniques de la colonne Genre
        modalites_genre = df[colonne_genre].unique()

        # Identifier potentiellement le genre féminin et masculin (adapter si nécessaire)
        genre_feminin = None
        genre_masculin = None

        for modalite in modalites_genre:
            modalite_lower = str(modalite).lower()
            if 'femme' in modalite_lower or 'female' in modalite_lower or 'f' == modalite_lower:
                if genre_feminin is None:  # Prend la première occurrence comme référence
                    genre_feminin = modalite
            elif 'homme' in modalite_lower or 'male' in modalite_lower or 'm' == modalite_lower:
                if genre_masculin is None:  # Prend la première occurrence comme référence
                    genre_masculin = modalite

        if genre_feminin is None or genre_masculin is None:
            st.warning(
                f"Impossible d'identifier automatiquement les genres féminin et masculin "
                f"dans la colonne '{colonne_genre}'. Veuillez vérifier les données. "
                f"Modalités trouvées : {', '.join(map(str, modalites_genre))}"
            )
            return

        # Créer des groupes d'âge
        bins = list(range(0, df[colonne_age].max() + 6, 5))
        labels = [f'{i}-{i+4}' for i in bins[:-1]]
        df['Groupe_Age'] = pd.cut(df[colonne_age], bins=bins, labels=labels, right=False)

        # Calculer la distribution des âges par genre
        age_distribution = df.groupby(['Groupe_Age', colonne_genre]).size().unstack(fill_value=0)

        # Créer la figure Plotly
        fig = go.Figure()

        # Ajouter la distribution masculine
        if genre_masculin in age_distribution.columns:
            fig.add_trace(go.Bar(
                y=age_distribution.index,
                x=age_distribution[genre_masculin],
                orientation='h',
                name=str(genre_masculin).capitalize(),
                marker_color='skyblue'
            ))

        # Ajouter la distribution féminine
        if genre_feminin in age_distribution.columns:
            fig.add_trace(go.Bar(
                y=age_distribution.index,
                x=-age_distribution[genre_feminin],
                orientation='h',
                name=str(genre_feminin).capitalize(),
                marker_color='salmon'
            ))

        # Mettre à jour le layout
        fig.update_layout(
            title='Pyramide des Âges des Donneurs de Sang par Genre',
            yaxis_title='Groupe d\'Âge',
            xaxis_title='Nombre de Donneurs',
            barmode='relative',
            xaxis=dict(tickformat='|f', title_standoff=25),
            height=600,  
            bargap=0.2
        )

        # Afficher la figure dans Streamlit
        st.plotly_chart(fig, use_container_width=True)

    base=df[df["ÉLIGIBILITÉ AU DON."]=="Eligible"]

    #st.sidebar.write("## Navigation")
    #st.sidebar.write("Aller ")
    with st.sidebar:
        Arron = base["Arrondissement de résidence"].unique()
        Arron_selectionne = st.sidebar.multiselect(
            "Choisissez l'Arrondissement:", options=Arron, default=Arron[0] if len(Arron) > 0 else None
        )

        base_arron = base[base['Arrondissement de résidence'].isin(Arron_selectionne)]
        Quartier_selectionne = []  # Initialisation pour éviter les erreurs si aucun arrondissement n'est sélectionné
        base_Quartier = base_arron # Initialisation pour éviter les erreurs si aucun arrondissement n'est sélectionné

        if not Arron_selectionne:
            st.sidebar.warning("Veuillez choisir au moins un arrondissement.")
        #else:
        
    # Quartier = base_arron["Quartier de Résidence"].unique()
        #Quartier_selectionne = st.multiselect(
        #  "Choisissez le Quartier:", options=Quartier, default=Quartier if len(Quartier) > 0 else None
        #)
        #if not Quartier_selectionne:
        # st.sidebar.warning("Veuillez choisir au moins un quartier après avoir sélectionné un arrondissement.")
        #else:
        # base_Quartier = base_arron[base_arron["Quartier de Résidence"].isin(Quartier_selectionne)]

    # Préparer les données pour les graphiques
    # Utilisez 'base_Quartier' pour vos analyses et graphiques car il contient les données filtrées
    if not Arron_selectionne:
        st.warning("Veuillez choisir au moins un arrondissement dans la barre latérale pour afficher les données.")
    #elif not Quartier_selectionne:
        #st.warning("Veuillez choisir au moins un quartier dans la barre latérale pour afficher les données.")

    # Préparer les données pour les graphiques
    # Fonction pour préparer les données

    else:

        # Calculer les indicateurs
        base_age=calculer_age_au_don(base_Quartier, 'Date de remplissage de la fiche', 'Date de naissance', 'Age_Don')
        nombre_individus = len(base_Quartier)
        
        age_moyen = base_age["Age_Don"].mean().round(1) if 'Age_Don' in base_age.columns else None
        hemoglobine_moyenne = base_age['Taux d’hémoglobine'].mean().round(1) if "Taux d’hémoglobine" in base_age.columns else None

        # --- Affichage des indicateurs dans des colonnes avec le style personnalisé ---
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>Nombre d'Individus réguliers</div>
                    <div class='indicator-value'>{nombre_individus}</div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>Âge Moyen</div>
                    <div class='indicator-value'>{age_moyen if age_moyen is not None else 'N/A'}</div>
                    <div class='indicator-unit'>ans</div>
                </div>
            """, unsafe_allow_html=True)
            if age_moyen is None:
                st.warning(f"Colonne 'Age_Don' non trouvée pour calculer l'âge moyen.")

        with col3:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>Taux d'Hémoglobine Moyen</div>
                    <div class='indicator-value'>{hemoglobine_moyenne if hemoglobine_moyenne is not None else 'N/A'}</div>
                    <div class='indicator-unit'>g/dL</div>
                </div>
            """, unsafe_allow_html=True)
            if hemoglobine_moyenne is None:
                st.warning(f"Colonne 'Taux d’hémoglobine' non trouvée pour calculer le taux d'hémoglobine moyen.")
        ## Définissons une colonne classe d"âge :
        base_class_age=creer_classe_age_amplitude_egale(base_age, 'Age_Don','Classe_Age', n_classes=5)
        app_streamlit(base_class_age,key_suffix="Selon les arronidssents choisis")
        ## Pyramide des âge des donneurs reguliers
        afficher_pyramide_des_ages(base_age, "Age_Don", "Genre")

        def prepare_chart_data(df, column):
            count_data = df[column].value_counts(normalize=True) * 100
            return count_data.index.tolist(), count_data.values.tolist()
        variables_to_plot = [
            "Niveau d'etude", "Genre", "Situation Matrimoniale (SM)", "ÉLIGIBILITÉ AU DON.","Nationalité","Religion"
        ]
        chart_data = {}
        for col in variables_to_plot:
            if col in base.columns:
                chart_data[col] = prepare_chart_data(base, col)


        

        class_age=base_class_age["Classe_Age"].unique()
        age_selectionne=st.multiselect("choisissez une tranche d'age", options=class_age,default=class_age[0])#
        if age_selectionne:
            base_age_filtre=base_class_age[base_class_age["Classe_Age"].isin(age_selectionne)]
            chart_data = {}
            for col in variables_to_plot:
                if col in base.columns:
                    chart_data[col] = prepare_chart_data(base_age_filtre, col)

            ## Divisons la page en deux colonne
            st.markdown("<h3 style='text-align: center;'>Situation Matrimoniale (SM)</h3>", unsafe_allow_html=True)
            colonne1,colonne2 = st.columns(2)
            with colonne1:
                    if "Situation Matrimoniale (SM)" in chart_data:
                        #st.markdown("<h4 style='color: green; text-align: center;'>Situation Matrimoniale</h4>", unsafe_allow_html=True)
                        st.plotly_chart(create_donut_chart(*chart_data["Situation Matrimoniale (SM)"], "Situation Matrimoniale"), use_container_width=True)

            with colonne2:
                with st.container():                   
                    Nationali_type_counts =base_age_filtre["Situation Matrimoniale (SM)"].value_counts()
                    
                    # Affichage en 2 colonnes
                    #b_col1, b_col2 = st.columns(2)
                    
                    for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                        #if i % 2 == 0:
                            #with b_col1:
                                st.metric(blood_type, count)
                        #else:
                            #with b_col2:
                                #st.metric(blood_type, count)

            col = st.columns(3)
            with col[0]:

                    if "Nationalité" in chart_data:
                        st.plotly_chart(create_donut_chart(*chart_data["Nationalité"], "Selon la Nationalité"), use_container_width=True)
                    
            with col[1]:
                    if "Genre" in chart_data:
                        #st.markdown("<h4 style='color: green; text-align: center;'>Genre</h4>", unsafe_allow_html=True)
                        st.plotly_chart(create_donut_chart(*chart_data["Genre"], "Selon le Genre"), use_container_width=True)
            with col[2]:
                    if "Religion" in chart_data:
                        #st.markdown("<h4 style='color: green; text-align: center;'>Genre</h4>", unsafe_allow_html=True)
                        st.plotly_chart(create_donut_chart(*chart_data["Religion"], "Selon la Religion"), use_container_width=True)
            ##  Création de la colonne classe d'âge
            

            with st.container():
                    #st.header("Proffession")
                    #afficher_histogramme(base,'Profession')
                    Genre_selectionne = [] 
                    Genre=base_Quartier["Genre"].unique()
                    Genre_selectionne = st.multiselect(
            "Choisissez le Sexe:", options=Genre, default=Genre if len(Genre) > 0 else None
        )
                    base_Genre = base_age_filtre[base_age_filtre['Genre'].isin(Genre_selectionne)]
                    # Initialisation pour éviter les erreurs si aucun Genre n'est sélectionné
                    st.markdown(
                        """
                        <style>
                            /* Cibler la zone d'affichage des éléments sélectionnés (l'intérieur) */
                            .stMultiSelect > div:first-child {
                                background-color: #FF0000 !important; /* Remplacez par le rouge de Stata ou une couleur similaire */
                                border: 1px solid #ccc;
                                border-radius: 3px;
                                padding: 5px;
                                cursor: pointer;
                                color: white !important; /* Assurez-vous que le texte est lisible sur le fond rouge */
                            }

                            /* Cibler les badges des options sélectionnées (facultatif) */
                            .stMultiSelect > div:first-child div[data-baseweb="tag"] {
                                background-color: white; /* Couleur claire pour les badges sur fond rouge */
                                color: black;
                                border-radius: 3px;
                                padding: 2px 5px;
                                margin-right: 2px;
                            }

                        </style>
                        """,
                        unsafe_allow_html=True,
                    )

                    if not Genre_selectionne:
                        st.sidebar.warning("Veuillez choisir le Genre.")
                    else:
                            #afficher_histogramme_personnalise(base_Genre, "Niveau d'etude","selon Niveau d'étude")
                        st.markdown("<h3 style='text-align: center;'>Selon le niveau d'étude</h3>", unsafe_allow_html=True)
                        colonne1,colonne2 = st.columns(2)
                        with colonne1:
                                afficher_diagramme_en_anneau(base_Genre, "Niveau d'etude")
                        with colonne2:
                            with st.container():                   
                                Nationali_type_counts =base_Genre["Niveau d'etude"].value_counts()
                                
                                # Affichage en 2 colonnes
                                b_col1, b_col2 = st.columns(2)
                                
                                for i, (blood_type, count) in enumerate( Nationali_type_counts.items()):
                                    if i % 2 == 0:
                                        with b_col1:
                                            st.metric(blood_type, count)
                                    else:
                                        with b_col2:
                                            st.metric(blood_type, count)

                        ##Visualisons les proffessions des donneurs réguliers

                        afficher_graphique_barres_polaire(base_Genre, 'Profession')
                        #"#visualisons les périodes de don de sang

                        periode=["jour", "mois"]
                        periode_select=st.selectbox("Choisir la période ", periode)
                        visualiser_dons_par_periode(base_age_filtre,"Date de remplissage de la fiche",periode_select)

                        

                        

                    
                        #app_streamlit(base_age_filtre,key_suffix="")


                        #afficher_arbre_donneur_ideal_top2(base_age_filtre, ["Genre","Profession","Classe_Age"])
        else:
            st.write("Veuillez choisir au moins une tranche d'age ")
            # Ajout de styles CSS pour améliorer l'apparence
    st.markdown("""
        <style>
            /* Centrage du texte */
            .css-1v3fvcr { text-align: center !important; }

            /* Style des graphiques Plotly */
            .stPlotlyChart {
                background-color: #D6EAF8; /* Couleur douce de fond */
                border: 3px solid #C0392B; /* 🔴 contour rouge sang */
                box-shadow: 5px 5px 15px rgba(192, 57, 43, 0.4); /* ombre rouge */
                border-radius: 10px;
                padding: 10px;
            }

            h4 {
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)








