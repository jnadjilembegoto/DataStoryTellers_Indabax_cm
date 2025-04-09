
import streamlit as st
import branca.colormap as cm
import folium
from streamlit_folium import folium_static
from streamlit_folium import folium_static
from streamlit_plotly_events import plotly_events
import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import pandas as pd
import osmnx as ox
import folium
from streamlit_folium import st_folium
import streamlit as st
import json
from thefuzz import process
import os
import pydeck as pdk
import plotly.graph_objects as go

import colorsys

import graphviz


from streamlit_echarts import st_echarts

from Datas.data_link import data_dir

def carto_page_load():
    #st.title(" Competition INDA Hackaton")
    # st.markdown("""
    # <style>
    # /* === Fond principal de l'app === */
    # [data-testid="stAppViewContainer"] {
    #     background-color: #E6A2A2;
    #     color: #31333F;
    #     font-family: 'Segoe UI', sans-serif;
    # }

    # /* === En-tête transparent === */
    # [data-testid="stHeader"] {
    #     background-color: rgba(0,0,0,0);
    # }

    # /* === Titres et textes === */
    # h1, h2, h3, h4, h5, h6 {
    #     color: #FF4B4B;
    # }

    # p, li, span, div {
    #     color: #31333F;
    # }

    # /* === Boutons === */
    # button[kind="primary"] {
    #     background-color: #FF4B4B;
    #     color: white;
    #     border: none;
    #     border-radius: 6px;
    # }

    # button[kind="primary"]:hover {
    #     background-color: #d93636;
    # }

    # /* === Widgets (inputs, sliders, selects, etc.) === */
    # .stSelectbox, .stSlider, .stTextInput, .stTextArea {
    #     background-color: #93B8EF;
    #     color: #31333F;
    #     border-radius: 6px;
    #     border: 1px solid #FF4B4B;
    # }

    # /* === Code blocks, markdown, etc. === */
    # .stMarkdown, .stCodeBlock {
    #     background-color: #f7dede;
    #     color: #31333F;
    #     border-radius: 6px;
    # }

    # /* === Graphviz charts === */
    # svg {
    #     background-color: transparent !important;
    # }

    # .node text {
    #     fill: #31333F !important;
    #     font-size: 12px;
    #     font-family: 'Arial', sans-serif;
    # }

    # .node rect {
    #     fill: #93B8EF !important;
    #     stroke: #FF4B4B !important;
    #     rx: 8;
    #     ry: 8;
    # }
    # </style>
    # """, unsafe_allow_html=True)


    # # Définir les couleurs pour le thème des dons de sang
    # primary_color = "#FF4B4B"  # Rouge vif (évoque le sang)
    # secondary_color = "#93B8EF" # Jaune/Or (pour l'importance)
    # background_color = "#E6A2A2" # Gris clair pour le fond
    # text_color = "#31333F"      # Gris foncé pour le texte

    # # Style CSS personnalisé
    # st.markdown(f"""
    #     <style>
    #         .indicator-container {{
    #             background-color: {background_color};
    #             padding: 15px;
    #             border-radius: 10px;
    #             box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    #             text-align: center;
    #             border-left: 5px solid {primary_color}; /* Bordure colorée à gauche */
    #         }}
    #         .indicator-title {{
    #             font-size: 16px;
    #             color: {text_color};
    #             margin-bottom: 5px;
    #         }}
    #         .indicator-value {{
    #             font-size: 24px;
    #             font-weight: bold;
    #             color: {primary_color}; /* Couleur principale pour la valeur */
    #         }}
    #     </style>
    # """, unsafe_allow_html=True)


    # # --- Style CSS personnalisé pour les conteneurs d'indicateurs ---
    # st.markdown(
    #     """
    #     <style>
    #     .indicator-container {
    #         background-color: #fff;
    #         padding: 20px;
    #         border-radius: 10px;
    #         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    #         margin-bottom: 20px;
    #         border: 1px solid #eee;
    #         position: relative; /* Pour le pseudo-élément */
    #         overflow: hidden; /* Empêche le pseudo-élément de dépasser */
    #     }
    #     .indicator-container::before {
    #         content: '';
    #         position: absolute;
    #         top: 0;
    #         left: 0;
    #         width: 5px;
    #         height: 100%;
    #         background-color: #D12720; /* Couleur accent */
    #     }
    #     .indicator-title {
    #         color: #333;
    #         font-size: 16px;
    #         margin-bottom: 5px;
    #     }
    #     .indicator-value {
    #         font-size: 28px;
    #         font-weight: bold;
    #         color: #D12720;
    #     }
    #     .indicator-unit {
    #         font-size: 14px;
    #         color: #777;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # ## Donnons une couleur au



    # st.markdown(
    #     """
    #     <style>
    #         /* Couleur principale (rouge sang) */
    #         :root {
    #             --primary-color: #D12720;
    #             --secondary-color: #e9ecef; /* Gris clair subtil pour le fond */
    #             --text-color: #333; /* Gris foncé pour le texte principal */
    #             --accent-color: #007bff; /* Bleu pour les actions / liens */
    #         }

    #         body {
    #             background-color: var(--secondary-color);
    #             color: var(--text-color);
    #             font-family: 'Arial', sans-serif;
    #             line-height: 1.6;
    #             margin: 0;
    #             padding: 0;
    #         }

    #         /* ... le reste de votre CSS ... */
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # # Personnalisons la couleur du sidebar 
    # st.markdown(
    #     """
    #     <style>
    #         [data-testid="stSidebar"] {
    #             background-color: #ADD8E6 !important; /* Bleu clair */
    #         }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )


    # st.markdown("""
    #     <style>
    #         .indicator-container {
    #             background-color: #007BFF; /* 🔵 bleu Bootstrap */
    #             border-radius: 10px;
    #             padding: 20px;
    #             color: white;
    #             text-align: center;
    #             box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    #             margin-bottom: 10px;
    #         }
    #         .indicator-title {
    #             font-size: 18px;
    #             font-weight: bold;
    #         }
    #         .indicator-value {
    #             font-size: 32px;
    #             font-weight: bold;
    #             margin-top: 10px;
    #         }
    #         .indicator-unit {
    #             font-size: 14px;
    #             margin-top: 4px;
    #         }
    #     </style>
    # """, unsafe_allow_html=True)


    # st.markdown("""
    #     <style>
    #         /* 🩸 Fond général clair */
    #         body, .main, .block-container {
    #             background-color: #F9F9F9 !important;
    #             color: #2C3E50;
    #         }

    #         /* 🩺 En-têtes Streamlit */
    #         h1, h2, h3, h4, h5 {
    #             color: #C0392B;
    #         }

    #         /* 🔵 Boutons Streamlit */
    #         .stButton > button {
    #             background-color: #C0392B;
    #             color: white;
    #             border-radius: 8px;
    #             border: none;
    #             font-weight: bold;
    #         }
    #         .stButton > button:hover {
    #             background-color: #A93226;
    #             color: white;
    #         }

    #         /* 🔳 Boîtes de sélection (selectbox, slider, etc.) */
    #         .stSelectbox, .stSlider {
    #             background-color: #FFFFFF;
    #             border-radius: 5px;
    #         }

    #         /* 🎯 Titres centrés */
    #         .css-1v3fvcr {
    #             text-align: center !important;
    #         }

    #         /* 🔲 Encadré des graphiques Plotly */
    #         .stPlotlyChart {
    #             background-color: #F9F9F9;
    #             border: 2px solid #C0392B;
    #             border-radius: 10px;
    #             padding: 10px;
    #             box-shadow: 4px 4px 10px rgba(192, 57, 43, 0.2);
    #         }

    #         /* 📦 Cartes statistiques (indicateurs) */
    #         .indicator-container {
    #             background-color: #2980B9;
    #             color: white;
    #             border-radius: 10px;
    #             padding: 20px;
    #             text-align: center;
    #             box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    #         }

    #         .indicator-title {
    #             font-size: 18px;
    #             font-weight: bold;
    #         }

    #         .indicator-value {
    #             font-size: 32px;
    #             font-weight: bold;
    #             margin-top: 10px;
    #         }

    #         .indicator-unit {
    #             font-size: 14px;
    #             margin-top: 4px;
    #         }
    #     </style>
    # """, unsafe_allow_html=True)



    st.header("Cartographie des donneurs")


    #geojson_path=r"C://Users//TIAO ELIASSE//Desktop//Streamlit_Storytellers//Hackaton INDA//TIAO_workèfinal1//arrondissements_de_douala.geojson"

    geojson_path=data_dir("arrondissements_de_douala.geojson")
    path = data_dir('base_streamlit_storytellers.xlsx')
    data = pd.read_excel(path, sheet_name='year')
    # copions les données
    df=data.copy()

    def afficher_lollipop_modalites(df, colonne_modalite, n_top=20,key="1"):
        """
        Affiche un graphique en lollipop interactif pour les N modalités les plus fréquentes,
        avec option d'afficher les valeurs en nombre ou en pourcentage et affichage au clic.
        """
        top_modalites_counts = df[colonne_modalite].value_counts().nlargest(n_top).sort_values()
        modalites = top_modalites_counts.index.tolist()
        frequences_nombre = top_modalites_counts.values.tolist()
        total_count = len(df)
        frequences_pourcentage = [(freq / total_count) * 100 for freq in frequences_nombre]

        # Initialiser l'état pour le point cliqué
        if 'clicked_point_lollipop' not in st.session_state:
            st.session_state['clicked_point_lollipop'] = None

        # Option pour l'utilisateur de choisir l'affichage
        option_affichage = st.radio(
            f"Afficher les fréquences pour '{colonne_modalite.replace('_', ' ').title()}' en :",
            ('Nombre', 'Pourcentage'),
            index=0,
            horizontal=True,key=colonne_modalite
        )

        fig = go.Figure()

        # Ajouter les segments (lignes)
        fig.add_trace(go.Scatter(
            x=[0] * len(modalites),
            y=modalites,
            mode='lines',
            line=dict(color='lightgray', width=2),
            hoverinfo='none'
        ))

        # Ajouter les marqueurs (points) roses et interactifs avec gestion des clics
        if option_affichage == 'Nombre':
            x_values = frequences_nombre
            hover_text = [f'{modalite}: {freq}' for modalite, freq in zip(modalites, frequences_nombre)]
            hovertemplate = '<b>%{y}</b>: %{x}<extra></extra>'
            xaxis_title = 'Nombre de Dons'
        else:
            x_values = frequences_pourcentage
            hover_text = [f'{modalite}: {freq:.2f}%' for modalite, freq in zip(modalites, frequences_pourcentage)]
            hovertemplate = '<b>%{y}</b>: %{x:.2f}%<extra></extra>'
            xaxis_title = 'Pourcentage des Dons'

        fig.add_trace(go.Scatter(
            x=x_values,
            y=modalites,
            mode='markers',
            marker=dict(
                size=30,
                color='palevioletred',
                line=dict(width=1, color='deeppink'),
                opacity=0.8
            ),
            text=hover_text,
            hovertemplate=hovertemplate,
            customdata=list(range(len(modalites))) # Associer un index à chaque point
        ))

        # Ajouter une annotation si un point a été cliqué
        if st.session_state['clicked_point_lollipop'] is not None:
            clicked_index = st.session_state['clicked_point_lollipop']['pointIndex']
            annotation_x = x_values[clicked_index]
            annotation_y = modalites[clicked_index]
            annotation_text = hover_text[clicked_index]

            fig.add_annotation(
                x=annotation_x,
                y=annotation_y,
                text=annotation_text,
                showarrow=True,
                arrowhead=1,
                ax=20,
                ay=-30,
                bgcolor="white",
                opacity=0.8
            )

        fig.update_layout(
        # title=f'Top {n_top} des Modalités de {colonne_modalite.replace("_", " ").title()}',
            xaxis_title=xaxis_title,
            #yaxis_title=colonne_modalite.replace('_', ' ').title(),
            plot_bgcolor="white",
            hovermode='y unified',
            title_font=dict(size=30, color='indianred'),
            yaxis=dict(autorange="reversed"),
        )

        # Gérer les événements de clic avec streamlit_plotly_events
        clicked = plotly_events(fig, key=colonne_modalite+'1')

        if clicked:
            st.session_state['clicked_point_lollipop'] = clicked[0]

        #st.plotly_chart(fig, use_container_width=True)






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



    def app_streamlit(df, cols,key_suffix="1"):
        st.subheader(f"🩸 Répartitions des donneurs réguliers ")

        #colonnes_qualitatives = [col for col in df.select_dtypes(include=['object', 'category']).columns.tolist() if col != 'Date de naissance' or col!='Horodateur']

        colonnes_choisies = st.multiselect(
            "🧩 Sélectionnez les variables dans l'ordre :",
            cols,
            default=cols[0:2],
            key=f"colonnes_{key_suffix}"
        )

    
    
        if len(colonnes_choisies) >= 2 and st.button("Afficher caractéristiques des donneurs reguliers") :
            afficher_arbre_simplifie(df, colonnes_choisies)
        elif len(colonnes_choisies) < 2:
            st.info("Veuillez sélectionner au moins deux variables.")
    def get_centroid(coords):
        """Calcule le centroïde à partir de coordonnées GeoJSON (Polygon ou MultiPolygon)."""
        flat_coords = []
        def flatten(c):
            if isinstance(c, (int, float)):
                return
            elif len(c) > 0 and isinstance(c[0], (int, float)):
                flat_coords.append(c)
            else:
                for sub in c:
                    flatten(sub)
        
        flatten(coords)
        if not flat_coords:
            return [4.0511, 9.7679]  # Coordonnées par défaut si aucune coordonnée valide
        lat = sum(c[1] for c in flat_coords) / len(flat_coords)
        lon = sum(c[0] for c in flat_coords) / len(flat_coords)
        return [lat, lon]

    def afficher_carte_donneurs(df, col_var,
                            #geojson_path=r"C://Users//TIAO ELIASSE//Desktop//Streamlit_Storytellers//Hackaton INDA//TIAO_workèfinal1//arrondissements_de_douala.geojson",
                            ville_centre=[4.0511, 9.7679]):
        try:
            # Vérifier si le fichier existe
            if not os.path.exists(geojson_path):
                st.error(f"Fichier GeoJSON introuvable à l'emplacement: {geojson_path}")
                return

            # Ouvrir et charger le fichier geojson correctement
            with open(geojson_path, 'r', encoding='utf-8') as f:
                geojson_data = json.load(f)
            
            # Création de la carte
            m_arr = folium.Map(location=ville_centre, zoom_start=12, tiles="CartoDB Positron")
            
            # Filtrer les arrondissements
            arr_features = [f for f in geojson_data['features'] if f['properties'].get('admin_level') == "8"]
            geojson_arr = {'type': 'FeatureCollection', 'features': arr_features}
            arr_names_geojson = [f['properties'].get('name', 'Inconnu') for f in arr_features]
            
            # Compter les donneurs par arrondissement
            arrondissement_counts = df[col_var].value_counts().reset_index()
            arrondissement_counts.columns = [col_var, 'Nombre de Donneurs']
            
            # Créer le mapping des noms d'arrondissements
            arr_name_mapping = {}
            non_specified_arr_count = 0
            douala_non_precise_count = 0
            
            for df_name in arrondissement_counts[col_var]:
                if pd.isna(df_name) or str(df_name).lower() in ['non précisé', 'unknown', 'n/a', '']:
                    arr_name_mapping[df_name] = "Non précisé"
                    non_specified_arr_count += arrondissement_counts[arrondissement_counts[col_var] == df_name]['Nombre de Donneurs'].values[0]
                elif isinstance(df_name, str) and "Douala (Non précisé)" in df_name:
                    arr_name_mapping[df_name] = "Non précisé"
                    douala_non_precise_count += arrondissement_counts[arrondissement_counts[col_var] == df_name]['Nombre de Donneurs'].values[0]
                else:
                    match = process.extractOne(str(df_name), arr_names_geojson)
                    if match and match[1] >= 80:
                        arr_name_mapping[df_name] = match[0]
                    else:
                        arr_name_mapping[df_name] = df_name

            # Créer une colonne mappée
            df['arrondissement_de_residence_mapped'] = df[col_var].map(arr_name_mapping)
            arrondissement_counts_mapped = df['arrondissement_de_residence_mapped'].value_counts().reset_index()
            arrondissement_counts_mapped.columns = ['arrondissement_de_residence_mapped', 'Nombre de Donneurs']

            # Filtrer "Non précisé" pour le Choropleth
            arrondissement_counts_valid = arrondissement_counts_mapped[arrondissement_counts_mapped['arrondissement_de_residence_mapped'] != "Non précisé"]

            # Ajouter les compteurs aux features
            for feature in arr_features:
                name = feature['properties'].get('name', 'Inconnu')
                count = arrondissement_counts_valid[arrondissement_counts_valid['arrondissement_de_residence_mapped'] == name]['Nombre de Donneurs'].values
                feature['properties']['donneurs'] = int(count[0]) if len(count) > 0 else 0

            # Définir le style des polygones pour l'interactivité
            def style_function(feature):
                count = feature['properties'].get('donneurs', 0)
                return {
                    'fillColor': get_color(count),
                    'color': 'white',
                    'weight': 2,
                    'dashArray': '3',
                    'fillOpacity': 0.7
                }
            
            def highlight_function(feature):
                return {
                    'weight': 3,
                    'color': '#666',
                    'dashArray': '',
                    'fillOpacity': 0.7
                }
            
            def get_color(d):
                return '#800026' if d > 500 else \
                    '#BD0026' if d > 400 else \
                    '#E31A1C' if d > 300 else \
                    '#FC4E2A' if d > 200 else \
                    '#FD8D3C' if d > 100 else \
                    '#FEB24C'
            
            # Ajouter la couche GeoJSON interactive
            tooltip = folium.GeoJsonTooltip(
                fields=['name', 'donneurs'],
                aliases=['Arrondissement:', 'Nombre de donneurs:'],
                style=("background-color: white; color: #333; font-family: arial; font-size: 12px; padding: 10px;")
            )
            
            geojson_layer = folium.GeoJson(
                geojson_arr,
                name="arrondissements",
                style_function=style_function,
                highlight_function=highlight_function,
                tooltip=tooltip,
                popup=folium.GeoJsonPopup(
                    fields=['name', 'donneurs'],
                    aliases=['Arrondissement:', 'Nombre de donneurs:'],
                    localize=True,
                    style="background-color: white; color: #333; font-family: arial;"
                )
            )
            geojson_layer.add_to(m_arr)
            
            # Ajouter les cercles proportionnels aux centres des arrondissements
            for _, row in arrondissement_counts_valid.iterrows():
                arr_name = row['arrondissement_de_residence_mapped']
                count = row['Nombre de Donneurs']
                for feature in arr_features:
                    if feature['properties'].get('name') == arr_name:
                        coords = feature['geometry']['coordinates']
                        centroid = get_centroid(coords)
                        folium.CircleMarker(
                            location=centroid,
                            radius=max(count / 5, 4),  # Assurez-vous que les petits cercles sont visibles
                            popup=f"<b>{arr_name}</b><br>Nombre de donneurs: {count}",
                            tooltip=f"{arr_name}: {count} donneurs",
                            color="#FF5722",
                            fill=True,
                            fill_color="#FF5722",
                            fill_opacity=0.7
                        ).add_to(m_arr)

            # Ajouter un marqueur séparé pour la somme de "Non précisé" et "Douala (Non précisé)"
            total_non_precise = non_specified_arr_count + douala_non_precise_count
            if total_non_precise > 0:
                popup_text = f"Non localisés: {total_non_precise} donneurs (Non précisé: {non_specified_arr_count}, Douala (Non précisé): {douala_non_precise_count})"
                folium.CircleMarker(
                    location=ville_centre,
                    radius=max(total_non_precise / 5, 6),
                    popup=popup_text,
                    tooltip="Donneurs non localisés",
                    color="red",
                    fill=True,
                    fill_color="red",
                    fill_opacity=0.7
                ).add_to(m_arr)

            # Ajouter une légende pour les couleurs
            
            colormap = cm.LinearColormap(
                ['#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026'],
                vmin=0, vmax=600,
                caption='Nombre de donneurs'
            )
            colormap.add_to(m_arr)
            
            # Ajouter un contrôle de couches
            folium.LayerControl().add_to(m_arr)

            # Créer des conteneurs pour l'interface interactive
        
            from streamlit_folium import st_folium
            
                # Rendre la carte interactive avec st_folium
            map_data = st_folium(m_arr, width=700, height=500, returned_objects=["last_object_clicked", "last_clicked"])
            
        
                
            if map_data and "last_object_clicked" in map_data:
                clicked_obj = map_data["last_object_clicked"]
                2
                # Si l'objet cliqué est un arrondissement
                if clicked_obj and "properties" in clicked_obj:
                    properties = clicked_obj["properties"]
                    arr_name = properties.get("name", "Inconnu")
                    donneurs = properties.get("donneurs", 0)
                    
                    
                        #
                
        except Exception as e:
            st.error(f"Erreur : {str(e)}")
            #st.exception(e)  # Afficher plus de détails sur l'erreur
    

    # Télécharger les géométries des quartiers
    tags = {"place": "suburb"}
    gdf = ox.features_from_place("Douala, Cameroon", tags=tags)

    # Nettoyage et extraction des centroïdes
    quartiers_coords = {
        row["name"]: [row.geometry.centroid.y, row.geometry.centroid.x]
        for idx, row in gdf.iterrows()
        if "name" in row and row.geometry and row.geometry.is_valid
    }



    def afficher_carte_donneurs_par_quartier(df, col_quartier, quartiers_coords=quartiers_coords, ville_centre=[4.0511, 9.7679]):
        """
        Affiche une carte de Douala avec des cercles proportionnels représentant
        le nombre de donneurs par quartier, en se basant sur les coordonnées GPS.

        Args:
            df (pd.DataFrame): La base contenant les donneurs.
            col_quartier (str): Le nom de la colonne contenant les quartiers.
            quartiers_coords (dict): Dictionnaire quartier -> [latitude, longitude].
            ville_centre (list): Coordonnées du centre de la carte (par défaut : Douala).
        """
        

        # Nettoyage des noms de quartiers dans df
        df[col_quartier] = df[col_quartier].astype(str).str.strip().str.title()

        # Comptage des donneurs par quartier
        quartier_counts = df[col_quartier].value_counts().reset_index()
        quartier_counts.columns = ['quartier', 'nombre_donneurs']

        # Création de la carte
        m = folium.Map(location=ville_centre, zoom_start=12, tiles="CartoDB Positron")

        non_located = 0  # Compteur de quartiers sans coordonnées

        for _, row in quartier_counts.iterrows():
            quartier = row['quartier']
            nb = row['nombre_donneurs']
            coords = quartiers_coords.get(quartier)

            if coords:
                folium.CircleMarker(
                    location=coords,
                    radius=max(nb / 5, 4),
                    popup=f"<b>{quartier}</b><br>Nombre de donneurs: {nb}",
                    tooltip=f"{quartier}: {nb} donneurs",
                    color="#E53935",
                    fill=True,
                    fill_color="#E53935",
                    fill_opacity=0.7
                ).add_to(m)
            else:
                non_located += nb

        # Ajout d’un point central pour les quartiers non localisés
        if non_located > 0:
            folium.CircleMarker(
                location=ville_centre,
                radius=max(non_located / 5, 6),
                popup=f"<b>Non localisés</b><br>{non_located} donneurs",
                tooltip="Donneurs non localisés",
                color="red",
                fill=True,
                fill_color="red",
                fill_opacity=0.6
            ).add_to(m)

        # Titre et affichage
    # st.subheader("📍 Répartition des donneurs par quartier à Douala")
        st_folium(m, width=700, height=500)


    def afficher_carte_donneurs_Quartier(df, col_var,
                                #geojson_path=r"C://Users//TIAO ELIASSE//Desktop//Streamlit_Storytellers//Hackaton INDA//TIAO_workèfinal1//arrondissements_de_douala.geojson",
                                ville_centre=[4.0511, 9.7679]):
        try:
            # Vérifier si le fichier existe
            if not os.path.exists(geojson_path):
                st.error(f"Fichier GeoJSON introuvable à l'emplacement: {geojson_path}")
                return

            # Ouvrir et charger le fichier geojson correctement
            with open(geojson_path, 'r', encoding='utf-8') as f:
                geojson_data = json.load(f)
            
            # Création de la carte
            m_quart = folium.Map(location=ville_centre, zoom_start=12, tiles="CartoDB Positron")
            
            # Filtrer les quartiers
            quart_features = [f for f in geojson_data['features'] if f['properties'].get('admin_level') == "9"]  # Changez "9" si nécessaire
            geojson_quart = {'type': 'FeatureCollection', 'features': quart_features}
            quart_names_geojson = [f['properties'].get('name', 'Inconnu') for f in quart_features]
            
            # Compter les donneurs par quartier
            quartier_counts = df[col_var].value_counts().reset_index()
            quartier_counts.columns = [col_var, 'Nombre de Donneurs']
            
            # Créer le mapping des noms de quartiers
            quart_name_mapping = {}
            non_specified_quart_count = 0
            
            for df_name in quartier_counts[col_var]:
                if pd.isna(df_name) or str(df_name).lower() in ['non précisé', 'unknown', 'n/a', '']:
                    quart_name_mapping[df_name] = "Non précisé"
                    non_specified_quart_count += quartier_counts[quartier_counts[col_var] == df_name]['Nombre de Donneurs'].values[0]
                else:
                    match = process.extractOne(str(df_name), quart_names_geojson)
                    if match and match[1] >= 80:
                        quart_name_mapping[df_name] = match[0]
                    else:
                        quart_name_mapping[df_name] = df_name

            # Créer une colonne mappée
            df['quartier_de_residence_mapped'] = df[col_var].map(quart_name_mapping)
            quartier_counts_mapped = df['quartier_de_residence_mapped'].value_counts().reset_index()
            quartier_counts_mapped.columns = ['quartier_de_residence_mapped', 'Nombre de Donneurs']

            # Filtrer "Non précisé" pour le Choropleth
            quartier_counts_valid = quartier_counts_mapped[quartier_counts_mapped['quartier_de_residence_mapped'] != "Non précisé"]

            # Ajouter les compteurs aux features
            for feature in quart_features:
                name = feature['properties'].get('name', 'Inconnu')
                count = quartier_counts_valid[quartier_counts_valid['quartier_de_residence_mapped'] == name]['Nombre de Donneurs'].values
                feature['properties']['donneurs'] = int(count[0]) if len(count) > 0 else 0

            # Définir le style des polygones pour l'interactivité
            def style_function(feature):
                count = feature['properties'].get('donneurs', 0)
                return {
                    'fillColor': get_color(count),
                    'color': 'white',
                    'weight': 2,
                    'dashArray': '3',
                    'fillOpacity': 0.7
                }
            
            def highlight_function(feature):
                return {
                    'weight': 3,
                    'color': '#666',
                    'dashArray': '',
                    'fillOpacity': 0.7
                }
            
            def get_color(d):
                return '#800026' if d > 500 else \
                    '#BD0026' if d > 400 else \
                    '#E31A1C' if d > 300 else \
                    '#FC4E2A' if d > 200 else \
                    '#FD8D3C' if d > 100 else \
                    '#FEB24C'
            
            # Ajouter la couche GeoJSON interactive
            tooltip = folium.GeoJsonTooltip(
                fields=['name', 'donneurs'],
                aliases=['Quartier:', 'Nombre de donneurs:'],
                style=("background-color: white; color: #333; font-family: arial; font-size: 12px; padding: 10px;")
            )
            
            geojson_layer = folium.GeoJson(
                geojson_quart,
                name="quartiers",
                style_function=style_function,
                highlight_function=highlight_function,
                tooltip=tooltip,
                popup=folium.GeoJsonPopup(
                    fields=['name', 'donneurs'],
                    aliases=['Quartier:', 'Nombre de donneurs:'],
                    localize=True,
                    style="background-color: white; color: #333; font-family: arial;"
                )
            )
            geojson_layer.add_to(m_quart)
            
            # Ajouter les cercles proportionnels aux centres des quartiers
            for _, row in quartier_counts_valid.iterrows():
                quart_name = row['quartier_de_residence_mapped']
                count = row['Nombre de Donneurs']
                for feature in quart_features:
                    if feature['properties'].get('name') == quart_name:
                        coords = feature['geometry']['coordinates']
                        centroid = get_centroid(coords)
                        folium.CircleMarker(
                            location=centroid,
                            radius=max(count / 5, 4),  # Assurez-vous que les petits cercles sont visibles
                            popup=f"<b>{quart_name}</b><br>Nombre de donneurs: {count}",
                            tooltip=f"{quart_name}: {count} donneurs",
                            color="#FF5722",
                            fill=True,
                            fill_color="#FF5722",
                            fill_opacity=0.7
                        ).add_to(m_quart)

            # Ajouter un marqueur séparé pour les donneurs non précisés
            if non_specified_quart_count > 0:
                popup_text = f"Non localisés: {non_specified_quart_count} donneurs"
                folium.CircleMarker(
                    location=ville_centre,
                    radius=max(non_specified_quart_count / 5, 6),
                    popup=popup_text,
                    tooltip="Donneurs non localisés",
                    color="red",
                    fill=True,
                    fill_color="red",
                    fill_opacity=0.7
                ).add_to(m_quart)

            # Ajouter une légende pour les couleurs
            import branca.colormap as cm
            colormap = cm.LinearColormap(
                ['#FEB24C', '#FD8D3C', '#FC4E2A', '#E31A1C', '#BD0026', '#800026'],
                vmin=0, vmax=600,
                caption='Nombre de donneurs'
            )
            colormap.add_to(m_quart)
            
            # Ajouter un contrôle de couches
            folium.LayerControl().add_to(m_quart)

            # Rendre la carte interactive avec st_folium
            from streamlit_folium import st_folium
            map_data = st_folium(m_quart, width=700, height=500, returned_objects=["last_object_clicked", "last_clicked"])
            
            if map_data and "last_object_clicked" in map_data:
                clicked_obj = map_data["last_object_clicked"]
                if clicked_obj and "properties" in clicked_obj:
                    properties = clicked_obj["properties"]
                    quart_name = properties.get("name", "Inconnu")
                    donneurs = properties.get("donneurs", 0)
                    st.markdown(f"### {quart_name}")
                    st.metric("Nombre de donneurs", donneurs)
                    
        except Exception as e:
            st.error(f"Erreur : {str(e)}")
            st.exception(e)  # Afficher plus de détails sur l'erreur

    
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

    def afficher_histogramme_groupé(base_name, colonne, colonne_couleur=None, n_top=10, 
                                    mode_affichage='Pourcentage', affichage_interactif=False):
        """
        Affiche un histogramme horizontal groupé représentant la distribution des modalités d'une colonne,
        décomposée par une variable secondaire (optionnelle).

        Args:
            base_name (pd.DataFrame): La base de données.
            colonne (str): La colonne principale à analyser.
            colonne_couleur (str, optional): La colonne secondaire à afficher par couleurs/groupes.
            n_top (int): Nombre de modalités principales à afficher.
            mode_affichage (str): 'Nombre' ou 'Pourcentage'.
            affichage_interactif (bool): Si True, l'utilisateur peut choisir entre nombre et pourcentage.
        """
        if base_name.empty:
            st.write("Aucune donnée disponible.")
            return

    

        # Sélection des modalités principales
        top_modalites = base_name[colonne].value_counts().nlargest(n_top).index.tolist()
        df_top = base_name[base_name[colonne].isin(top_modalites)]

        # Calcul des fréquences
        if colonne_couleur:
            freqs = df_top.groupby([colonne, colonne_couleur]).size().unstack(fill_value=0)
            if mode_affichage == 'Pourcentage':
                freqs = freqs.divide(freqs.sum(axis=1), axis=0) * 100
        else:
            freqs = df_top[colonne].value_counts().to_frame(name='Nombre')
            if mode_affichage == 'Pourcentage':
                total = freqs['Nombre'].sum()
                freqs['Pourcentage'] = (freqs['Nombre'] / total) * 100

        # Création du graphe
        fig = go.Figure()
        couleurs = ['crimson', 'royalblue', 'seagreen', 'orange', 'darkorchid', 'darkcyan']

        if colonne_couleur:
            for i, couleur in enumerate(freqs.columns):
                x_vals = freqs[couleur].tolist()
                y_vals = freqs.index.tolist()
                fig.add_trace(go.Bar(
                    x=x_vals,
                    y=y_vals,
                    name=str(couleur),
                    orientation='h',
                    marker_color=couleurs[i % len(couleurs)],
                    hovertemplate=f"<b>{colonne.title()}</b>: %{{y}}<br><b>{couleur}</b>: %{{x:.2f}}"
                                + ("%" if mode_affichage == 'Pourcentage' else "") + "<extra></extra>"
                ))
        else:
            y_vals = freqs.index.tolist()
            x_vals = freqs[mode_affichage].tolist()
            fig.add_trace(go.Bar(
                x=x_vals,
                y=y_vals,
                orientation='h',
                text=[f"{val:.2f}%" if mode_affichage == 'Pourcentage' else f"{int(val)}" for val in x_vals],
                textposition='outside',
                marker_color='steelblue',
                hovertemplate=f"<b>%{{y}}</b><br><b>{mode_affichage}</b>: %{{x:.2f}}<extra></extra>"
            ))

        fig.update_layout(
            xaxis=dict(title=mode_affichage, ticksuffix='%' if mode_affichage == 'Pourcentage' else ''),
            yaxis=dict(title=None, showticklabels=True),
            barmode='group' if colonne_couleur else 'stack',
            plot_bgcolor='white',
            paper_bgcolor='white',
            margin=dict(l=0, r=0, t=0, b=0),
            legend_title=colonne_couleur.replace('_', ' ').title() if colonne_couleur else None,
            height=200
        )

        st.plotly_chart(fig, use_container_width=True)



    def afficher_lollipop_modalites(df, colonne_modalite, n_top=20,key="1"):
        """
        Affiche un graphique en lollipop interactif pour les N modalités les plus fréquentes,
        avec option d'afficher les valeurs en nombre ou en pourcentage et affichage au clic.
        """
        top_modalites_counts = df[colonne_modalite].value_counts().nlargest(n_top).sort_values()
        modalites = top_modalites_counts.index.tolist()
        frequences_nombre = top_modalites_counts.values.tolist()
        total_count = len(df)
        frequences_pourcentage = [(freq / total_count) * 100 for freq in frequences_nombre]

        # Initialiser l'état pour le point cliqué
        if 'clicked_point_lollipop' not in st.session_state:
            st.session_state['clicked_point_lollipop'] = None

        # Option pour l'utilisateur de choisir l'affichage
        option_affichage = st.radio(
            f"Afficher les fréquences pour '{colonne_modalite.replace('_', ' ').title()}' en :",
            ('Nombre', 'Pourcentage'),
            index=0,
            horizontal=True,key=colonne_modalite
        )

        fig = go.Figure()

        # Ajouter les segments (lignes)
        fig.add_trace(go.Scatter(
            x=[0] * len(modalites),
            y=modalites,
            mode='lines',
            line=dict(color='lightgray', width=2),
            hoverinfo='none'
        ))

        # Ajouter les marqueurs (points) roses et interactifs avec gestion des clics
        if option_affichage == 'Nombre':
            x_values = frequences_nombre
            hover_text = [f'{modalite}: {freq}' for modalite, freq in zip(modalites, frequences_nombre)]
            hovertemplate = '<b>%{y}</b>: %{x}<extra></extra>'
            xaxis_title = 'Nombre de Dons'
        else:
            x_values = frequences_pourcentage
            hover_text = [f'{modalite}: {freq:.2f}%' for modalite, freq in zip(modalites, frequences_pourcentage)]
            hovertemplate = '<b>%{y}</b>: %{x:.2f}%<extra></extra>'
            xaxis_title = 'Pourcentage des Dons'

        fig.add_trace(go.Scatter(
            x=x_values,
            y=modalites,
            mode='markers',
            marker=dict(
                size=30,
                color='palevioletred',
                line=dict(width=1, color='deeppink'),
                opacity=0.8
            ),
            text=hover_text,
            hovertemplate=hovertemplate,
            customdata=list(range(len(modalites))) # Associer un index à chaque point
        ))

        # Ajouter une annotation si un point a été cliqué
        if st.session_state['clicked_point_lollipop'] is not None:
            clicked_index = st.session_state['clicked_point_lollipop']['pointIndex']
            annotation_x = x_values[clicked_index]
            annotation_y = modalites[clicked_index]
            annotation_text = hover_text[clicked_index]

            fig.add_annotation(
                x=annotation_x,
                y=annotation_y,
                text=annotation_text,
                showarrow=True,
                arrowhead=1,
                ax=20,
                ay=-30,
                bgcolor="white",
                opacity=0.8
            )

        fig.update_layout(
        # title=f'Top {n_top} des Modalités de {colonne_modalite.replace("_", " ").title()}',
            xaxis_title=xaxis_title,
            #yaxis_title=colonne_modalite.replace('_', ' ').title(),
            plot_bgcolor="white",
            hovermode='y unified',
            title_font=dict(size=30, color='indianred'),
            yaxis=dict(autorange="reversed"),
        )

        # Gérer les événements de clic avec streamlit_plotly_events
        clicked = plotly_events(fig, key=colonne_modalite+'1')

        if clicked:
            st.session_state['clicked_point_lollipop'] = clicked[0]

        #st.plotly_chart(fig, use_container_width=True)


    def afficher_lollipop_groupé(df, colonne_modalite, colonne_couleur, n_top=10, affichage='Nombre'):
        import plotly.graph_objects as go

        # 1. Top modalités de la colonne principale
        top_modalites = df[colonne_modalite].value_counts().nlargest(n_top).index.tolist()
        df_top = df[df[colonne_modalite].isin(top_modalites)]

        # 2. Fréquences croisées
        freqs = df_top.groupby([colonne_modalite, colonne_couleur]).size().unstack(fill_value=0)

        # 3. Pourcentages si besoin
        if affichage == 'Pourcentage':
            total = freqs.sum(axis=1)
            freqs = freqs.divide(total, axis=0) * 100

        # 4. Couleurs automatiques
        couleurs = ['crimson', 'royalblue', 'seagreen', 'orange', 'mediumvioletred', 'darkcyan']

        # 5. Création du graphe lollipop groupé
        fig = go.Figure()
        y_categories = freqs.index.tolist()

        for i, couleur in enumerate(freqs.columns):
            x_vals = freqs[couleur].tolist()
            fig.add_trace(go.Scatter(
                x=x_vals,
                y=y_categories,
                mode='markers',
                name=couleur,
                marker=dict(
                    size=14,
                    color=couleurs[i % len(couleurs)],
                    line=dict(width=1, color='black')
                ),
                line=dict(color='lightgray', width=2),
                hovertemplate=f"<b>{couleur}</b><br>%{{y}}: %{{x:.2f}}" + ("%" if affichage == "Pourcentage" else "") + "<extra></extra>"
            ))

        fig.update_layout(
            #title=f"Top {n_top} {colonne_modalite.title()}s par {colonne_couleur.replace('_',' ').title()}",
            xaxis_title="Pourcentage" if affichage == "Pourcentage" else "Nombre",
            yaxis=dict(autorange="reversed"),
            plot_bgcolor='white',
            hovermode='closest',
            legend_title=colonne_couleur.title(),
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)




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

    #st.sidebar.write("## Navigation")
    #st.sidebar.write("Aller ")
    #titres_onglets = ["Analyse par Arrondissement","Analyse par Quartier de résidence 🌍"]
    # Exemple d'utilisation :
    #onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
    Douala=["Douala 1","Douala 2","Douala 3","Douala 4","Douala 5", "Douala 6"]

    #



    base11=df[df["Arrondissement de résidence"].isin(Douala)]
    df1=df.copy()

    arrondissement_counts =base11['Arrondissement de résidence'].value_counts().reset_index()
    arrondissement_counts.columns = ['Arrondissement de résidence', 'Nombre de Donneurs']



    Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
    Eligi_list=Eligi.tolist()+['Tout le monde']


    Eligi_selectionne=st.selectbox(
    "Choississez l'état de l'individu:",
    Eligi_list,
    )

    if Eligi_selectionne=='Tout le monde':
        col=st.columns(2)
        
        with col[0]:
            st.write("Selon Arrondissements")
            afficher_carte_donneurs(df, col_var="Arrondissement de résidence")
        with col[1]:
            st.write("Selon Quartier de résidence")
            afficher_carte_donneurs_par_quartier(df[df["Quartier de Résidence"].isin(quartiers_coords)], 'Quartier de Résidence')
        #afficher_carte_donneurs_Quartier(df, col_var="Quartier de Résidence")
    else:
        
        col=st.columns(2)
        
        df1=df[df["ÉLIGIBILITÉ AU DON."]==Eligi_selectionne]
        with col[0]:
            st.write("Selon Arrondissements")
            afficher_carte_donneurs(df1,col_var="Arrondissement de résidence")
        with col[1]:
            st.write("Selon Quartier de résidence")
            afficher_carte_donneurs_par_quartier(df1[df1['Quartier de Résidence'].isin(quartiers_coords)] ,'Quartier de Résidence')

    #with colonne[1]:
    #st.write("Selon le Quartier de résidence")
    #afficher_carte_donneurs(df,'Quartier de Résidence')

    st.write('Top 2 des Arrondissements où il y a eu plus de potentiels donneurs')
    afficher_arbre_simplifie(base11, ["Arrondissement de résidence","Quartier de Résidence","ÉLIGIBILITÉ AU DON."]) 

    Mode_d_affichage=st.selectbox("Veuillez choisir le mode de visualisation", ["Pourcentage","Nombre"],index=0,
                
                )

    col=st.columns(2 )
    with col[0]:
        afficher_histogramme_groupé(base11, "Arrondissement de résidence", colonne_couleur="Genre", n_top=10, 
                                    mode_affichage=Mode_d_affichage, affichage_interactif=True)
        afficher_histogramme_groupé(base11, "Arrondissement de résidence", colonne_couleur="Religion", n_top=10, 
                                    mode_affichage=Mode_d_affichage, affichage_interactif=True)
        
    with col[1]:
        afficher_histogramme_groupé(base11, "Arrondissement de résidence", colonne_couleur="Niveau d'etude", n_top=10, 
                                    mode_affichage=Mode_d_affichage, affichage_interactif=True)
        afficher_histogramme_groupé(base11, "Arrondissement de résidence", colonne_couleur="Situation Matrimoniale (SM)", n_top=10, 
                                    mode_affichage=Mode_d_affichage, affichage_interactif=True)
        


    col=st.columns(2)
    with col[0]:
        Arrondi =base11['Arrondissement de résidence'].unique()

        Arrondi_selectionne = st.multiselect(
        "Choississez l'arrondissement de résidence:",
        options = Arrondi,
        default = Arrondi[0]
        )
    if not Arrondi_selectionne:
        st.write("Veuillez selectionner au moins un arrondissement de résidence svp")
    else:
        with col[1]:
            Eligi=base11['ÉLIGIBILITÉ AU DON.'].unique()

            Eligi_selectionne = st.multiselect(
        "Choississez l'illégibilité de l'individu:",
        options = Eligi,
        default = Eligi
        )
        if not  Eligi_selectionne:
            st.write("veuillez choisir un état svp")
        else:
            afficher_lollipop_modalites(base11,"Quartier de Résidence", n_top=10,key="1")


    #quartier_selectionne = st.selectbox("Sélectionnez un quartier :", quartiers)


    # st.markdown("""
    #     <style>
    #         /* Centrage du texte */
    #         .css-1v3fvcr { text-align: center !important; }

    #         /* Style des graphiques Plotly */
    #         .stPlotlyChart {
    #             background-color: #D6EAF8; /* Couleur douce de fond */
    #             border: 3px solid #C0392B; /* 🔴 contour rouge sang */
    #             box-shadow: 5px 5px 15px rgba(192, 57, 43, 0.4); /* ombre rouge */
    #             border-radius: 10px;
    #             padding: 10px;
    #         }

    #         h4 {
    #             font-weight: bold;
    #         }
    #     </style>
    # """, unsafe_allow_html=True)

