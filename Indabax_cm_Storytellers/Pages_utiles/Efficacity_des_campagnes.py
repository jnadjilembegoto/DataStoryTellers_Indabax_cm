import pandas as pd
from dateutil.relativedelta import relativedelta
import plotly.express as px
import streamlit as st
import pydeck as pdk
import plotly.graph_objects as go
import numpy as np
import colorsys
from streamlit_plotly_events import plotly_events
import graphviz
import locale
from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
    


## Design d'affichage 
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



#st.title(" Competition INDA Hackaton")

st.header('Efficacité de la campagne')

## Visualisation avec un arbre 


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



def darbre(df, key_suffix="1"):
    st.subheader(f"🩸 arbres de donneurs  ")

    colonnes_qualitatives = [col for col in df.select_dtypes(include=['object', 'category']).columns.tolist()+ ['Mois_Annee'] if col != 'Date de naissance']

    colonnes_choisies = st.multiselect(
        "🧩 Sélectionnez les variables dans l'ordre :",
        colonnes_qualitatives,
        default=["A-t-il (elle) déjà donné le sang","ÉLIGIBILITÉ AU DON."] +colonnes_qualitatives[1:2],
        key=f"colonnes_{key_suffix}"
    )



    if len(colonnes_choisies) >= 2 and st.button("Afficher l'arbre",key=key_suffix):
        afficher_arbre_simplifie(df, colonnes_choisies)
    elif len(colonnes_choisies) < 2:
        st.info("Veuillez sélectionner au moins deux variables.")

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
    # Paramétrage de la locale  
    #locale.setlocale(locale.LC_TIME, 'fr_FR')
    if periode == 'jour':
        # Extraire le jour de la semaine
        df['Periode'] = df[colonne_date].dt.strftime('%A') #day_name(locale='fr_FR')
        periode_ordre = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']#['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']#
        titre_nombre = 'Nombre de dons de sang par jour de la semaine'
        titre_proportion = 'Proportion des dons de sang par jour de la semaine'
        label_axe = 'Jour de la semaine'
        df['Periode'] = pd.Categorical(df['Periode'], categories=periode_ordre, ordered=True)
    elif periode == 'mois':
        # Extraire le mois
        df['Periode'] = df[colonne_date].dt.strftime('%B')#month_name(locale='fr_FR')
        periode_ordre = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']#['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']#
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
        st.plotly_chart(fig,use_container_width=True)


def afficher_evolution_dons(df, Var1):
    """
    Fonction pour afficher l'évolution  du nombre de dons de sang.

    Paramètres :
    - df (pd.DataFrame) : Le dataframe contenant les données.
    - Var1 (str) : La colonne de date/temps pour l'axe des x.

    Retour :
    - Affiche un graphique interactif dans Streamlit.
    """

    fig = px.line(
        df,
        x=Var1,
        y='Nombre de Dons',
        #title=f'Évolution du Nombre de Dons de Sang par {Var1}',
        labels={Var1: Var1.replace('_', ' ').title(), 'Nombre de Dons': 'Nombre de Dons'},
        markers=True
    )

    # Personnalisation du graphique
    fig.update_layout(
        xaxis_title=Var1.replace('_', ' ').title(),
        yaxis_title="Nombre de Dons",
        xaxis_tickangle=-45,
        plot_bgcolor="white", # Un fond blanc est souvent plus propre
        hovermode="x unified", # Afficher les infos au survol alignées sur l'axe x
        legend_title_text='Séries' # Si vous avez plusieurs séries
    )

    # Améliorations esthétiques supplémentaires
    fig.update_traces(
        line=dict(width=2), # Épaisseur de la ligne
        marker=dict(size=20, symbol='circle'),
        # Style des marqueurs
    )

    st.plotly_chart(fig, width=100, height=100, use_container_width=False)

def afficher_evolution_comparative_modalites(df, date_col, modalite_col1, modalite_col2):
    """
    Affiche l'évolution comparative du nombre d'individus ayant des combinaisons de modalités
    au fil du temps (années).

    Paramètres :
    - df (pd.DataFrame) : Le dataframe contenant les données.
    - date_col (str) : La colonne contenant l'année.
    - modalite_col1 (str) : La première colonne de modalités.
    - modalite_col2 (str) : La deuxième colonne de modalités.

    Retour :
    - Affiche un graphique interactif dans Streamlit.
    """

    # Grouper par année et les deux colonnes de modalités et compter les individus
    df_grouped = df.groupby([date_col, modalite_col1, modalite_col2]).size().reset_index(name='Nombre d\'Individus')

    # Créer une colonne combinée pour les modalités pour la couleur
    df_grouped['Modalités Combinées'] = df_grouped[modalite_col1].astype(str) + ' - ' + df_grouped[modalite_col2].astype(str)

    fig = px.line(
        df_grouped,
        x=date_col,
        y='Nombre d\'Individus',
        color='Modalités Combinées',
        title=f'Évolution du Nombre d\'Individus par Combinaison de {modalite_col1.replace("_", " ").title()} et {modalite_col2.replace("_", " ").title()} au fil des Années',
        labels={
            date_col: date_col.replace('_', ' ').title(),
            'Nombre d\'Individus': 'Nombre d\'Individus',
            'Modalités Combinées': f'{modalite_col1.replace("_", " ").title()} - {modalite_col2.replace("_", " ").title()}'
        },
        markers=True
    )

    # Personnalisation du graphique
    fig.update_layout(
        xaxis_title=date_col.replace('_', ' ').title(),
        yaxis_title="Nombre d'Individus",
        xaxis_tickangle=-45,
        plot_bgcolor="white",
        hovermode="x unified",
        legend_title_text=f'{modalite_col1.replace("_", " ").title()} - {modalite_col2.replace("_", " ").title()}'
    )

    # Améliorations esthétiques supplémentaires
    fig.update_traces(
        line=dict(width=2),
        marker=dict(size=8, symbol='circle')
    )

    st.plotly_chart(fig, use_container_width=True)



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


def prepare_chart_data(df, column):
        count_data = df[column].value_counts(normalize=True) * 100
        return count_data.index.tolist(), count_data.values.tolist()
        



def afficher_histogramme(base_name, colonne):
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
    data = pd.read_excel(path, sheet_name='year')
    ## Importation de la deuxième base
    data2 = pd.read_excel(path, sheet_name='age')
    
    # Charger les données
    df=data.copy()

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



    st.sidebar.write("## Navigation")
    st.sidebar.write("Aller ")
    titres_onglets = ["Analyse Globale", "Analyse par sexe"]
    onglets_selectionnee=st.sidebar.radio("Forme d'analyse",titres_onglets)
    if onglets_selectionnee=="Analyse Globale":
        #with st.sidebar:
        ## Visualisons l'efficacité du don en s"interessant aux nouveaux donneurs et anciens donneurs
        
        nombre_individus = len(df)
        base_anciens_donneurs=df[df["A-t-il (elle) déjà donné le sang"]=='Oui']
        n_anciens_donneurs=len(base_anciens_donneurs)
        base_nouveaux_donneurs=df[df["A-t-il (elle) déjà donné le sang"]=='Non']
        n_nouveax_donneurs=len(base_nouveaux_donneurs)
        
        #age_moyen = base_age["Age_Don"].mean().round(1) if 'Age_Don' in base_age.columns else None
        #hemoglobine_moyenne = base_age['Taux d’hémoglobine'].mean().round(1) if "Taux d’hémoglobine" in base_age.columns else None

        # --- Affichage des indicateurs dans des colonnes avec le style personnalisé ---

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>Total des donneurs potentiel</div>
                    <div class='indicator-value'>{nombre_individus}</div>
                    
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>anciens donneurs optentiels</div>
                    <div class='indicator-value'>{n_anciens_donneurs}</div>
                
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>nouveaux donneurs potentiels</div>
                    <div class='indicator-value'>{n_nouveax_donneurs}</div>
                
                </div>
        """, unsafe_allow_html=True)
        
        ## Résumons l'éfficacité du dons
        darbre(df, key_suffix="PPP")
        Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
        col1, col2= st.columns(2)  # Ratio des largeurs des colonnes (ajuster selon vos besoins)
        with col1:
            deja_don=df['A-t-il (elle) déjà donné le sang'].unique()
            don_selectionne = st.multiselect(
                "Voulez vous voir les anciens donneurs de sang ?:",
                options=deja_don,
                default=deja_don
            )
        if not don_selectionne:
                st.write("Veuillez choisir si l individu à deja doner sang")
        else:
            with col2:
                Eligi_selectionne = st.multiselect(
                    "Choississez l'état de l'individu:",
                    options=Eligi,
                    default=Eligi
                )
                    
        
        #afficher_evolution_comparative_modalites(base, "Date de remplissage de la fiche",'ÉLIGIBILITÉ AU DON.', 'A-t-il (elle) déjà donné le sang')
        df1=df[df['A-t-il (elle) déjà donné le sang'].isin(don_selectionne)]
        base=df1[df1['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
        
        col = st.columns(2)
        with col[0]:
                #afficher_diagramme_circulaire(base,'ÉLIGIBILITÉ AU DON.')
                st.write("Evolution mensuelle de dons de sang")
                afficher_evolution_dons(group(base,'Mois_Annee'), 'Mois_Annee')
        

        with col[1]:
                st.write("Evolution de dons de sang en fonction de l'âge")
                df1=data2[data2['A-t-il_(elle)_déjà_donné_le_sang_'].isin(don_selectionne)]
            # base=df1[df1['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
        
                base2=df1[df1['ÉLIGIBILITÉ_AU_DON.'].isin(Eligi_selectionne)]

                afficher_evolution_dons(group(base2,"Age"),'Age')  
                
        ## Visualisation par jour ou mois
        periode=["jour", "mois"]
        periode_select=st.selectbox("Choisir la période ", periode)
        visualiser_dons_par_periode(base,"Date de remplissage de la fiche",periode_select)

        Mois=df['Mois_Annee'].unique()

        Mois_selectionne=st.multiselect(
        "Choississez le mois:",
        options = Mois,
        default = Mois[0])
        base1=base[base["Mois_Annee"].isin(Mois_selectionne)]
        

        variables_to_plot = [col for col in df.select_dtypes(include=['object', 'category']).columns.tolist() if col != 'Date de naissance' or col!='Horodateur']
        chart_data = {}
        for col in variables_to_plot:
            if col in base.columns:
                chart_data[col] = prepare_chart_data(base1, col)
        col = st.columns(4)
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
        
        with col[3]:
                if "Situation Matrimoniale (SM)" in chart_data:
                    #st.markdown("<h4 style='color: green; text-align: center;'>Genre</h4>", unsafe_allow_html=True)
                    st.plotly_chart(create_donut_chart(*chart_data["Situation Matrimoniale (SM)"], "Selon la Situation Matrimoniale"), use_container_width=True)
        col=st.columns(2)
        with col[0]:
                #st.header("Proffession")
                afficher_lollipop_modalites(base1,'Profession',10)
        with col[1]:
                Douala=["Douala 1","Douala 2","Douala 3","Douala 4","Douala 5", "Douala 6"]
                base2=base1[base1["Arrondissement de résidence"].isin(Douala)]
                afficher_lollipop_modalites(base2,"Arrondissement de résidence",6)
                #afficher_histogramme(base, 'Arrondissement de résidence')
                
    if onglets_selectionnee=="Analyse par sexe":
        
        with st.sidebar:
                df1=df.copy()
                Genre=df1["Genre"].unique()
                Eligi= df1["ÉLIGIBILITÉ AU DON."].unique()
                Genre_selectionne=st.sidebar.selectbox(
                "Choississez le sexe:",
                Genre)
                
            
        df=df[df['Genre']==Genre_selectionne]

            
        nombre_individus = len(df)
        base_anciens_donneurs=df[df["A-t-il (elle) déjà donné le sang"]=='Oui']
        n_anciens_donneurs=len(base_anciens_donneurs)
        base_nouveaux_donneurs=df[df["A-t-il (elle) déjà donné le sang"]=='Non']
        n_nouveax_donneurs=len(base_nouveaux_donneurs)
        
        #age_moyen = base_age["Age_Don"].mean().round(1) if 'Age_Don' in base_age.columns else None
        #hemoglobine_moyenne = base_age['Taux d’hémoglobine'].mean().round(1) if "Taux d’hémoglobine" in base_age.columns else None

        # --- Affichage des indicateurs dans des colonnes avec le style personnalisé ---

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>Total des donneurs potentiel</div>
                    <div class='indicator-value'>{nombre_individus}</div>
                    
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>anciens donneurs optentiels</div>
                    <div class='indicator-value'>{n_anciens_donneurs}</div>
                
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div class='indicator-container'>
                    <div class='indicator-title'>nouveaux donneurs potentiels</div>
                    <div class='indicator-value'>{n_nouveax_donneurs}</div>
                
                </div>
        """, unsafe_allow_html=True)
        
        ## Résumons l'éfficacité du dons
        darbre(df, key_suffix="PPP")
        Eligi= df["ÉLIGIBILITÉ AU DON."].unique()
        col1, col2= st.columns(2)  # Ratio des largeurs des colonnes (ajuster selon vos besoins)
        with col1:
            deja_don=df['A-t-il (elle) déjà donné le sang'].unique()
            don_selectionne = st.multiselect(
                "Voulez vous voir les anciens donneurs de sang ?:",
                options=deja_don,
                default=deja_don
            )
        if not don_selectionne:
                st.write("Veuillez choisir si l individu à deja doner sang")
        else:
            with col2:
                Eligi_selectionne = st.multiselect(
                    "Choississez l'état de l'individu:",
                    options=Eligi,
                    default=Eligi
                )
                    
        
        #afficher_evolution_comparative_modalites(base, "Date de remplissage de la fiche",'ÉLIGIBILITÉ AU DON.', 'A-t-il (elle) déjà donné le sang')
        df1=df[df['A-t-il (elle) déjà donné le sang'].isin(don_selectionne)]
        base=df1[df1['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
        
        col = st.columns(2)
        with col[0]:
                #afficher_diagramme_circulaire(base,'ÉLIGIBILITÉ AU DON.')
                st.write("Evolution mensuelle de dons de sang")
                afficher_evolution_dons(group(base,'Mois_Annee'), 'Mois_Annee')
        

        with col[1]:
                st.write("Evolution de dons de sang en fonction de l'âge")
                df1=data2[data2['A-t-il_(elle)_déjà_donné_le_sang_'].isin(don_selectionne)]
            # base=df1[df1['ÉLIGIBILITÉ AU DON.'].isin(Eligi_selectionne)]
        
                base2=df1[df1['ÉLIGIBILITÉ_AU_DON.'].isin(Eligi_selectionne)]

                afficher_evolution_dons(group(base2,"Age"),'Age')  
                
        ## Visualisation par jour ou mois
        periode=["jour", "mois"]
        periode_select=st.selectbox("Choisir la période ", periode)
        visualiser_dons_par_periode(base,"Date de remplissage de la fiche",periode_select)

        Mois=df['Mois_Annee'].unique()

        Mois_selectionne=st.multiselect(
        "Choississez le mois:",
        options = Mois,
        default = Mois[0])
        base1=base[base["Mois_Annee"].isin(Mois_selectionne)]
        

        variables_to_plot = [col for col in df.select_dtypes(include=['object', 'category']).columns.tolist() if col != 'Date de naissance' or col!='Horodateur']
        chart_data = {}
        for col in variables_to_plot:
            if col in base.columns:
                chart_data[col] = prepare_chart_data(base1, col)
        col = st.columns(4)
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
        
        with col[3]:
                if "Situation Matrimoniale (SM)" in chart_data:
                    #st.markdown("<h4 style='color: green; text-align: center;'>Genre</h4>", unsafe_allow_html=True)
                    st.plotly_chart(create_donut_chart(*chart_data["Situation Matrimoniale (SM)"], "Selon la Situation Matrimoniale"), use_container_width=True)
        col=st.columns(2)
        with col[0]:
                #st.header("Proffession")
                afficher_lollipop_modalites(base1,'Profession',10)
        with col[1]:
                Douala=["Douala 1","Douala 2","Douala 3","Douala 4","Douala 5", "Douala 6"]
                base2=base1[base1["Arrondissement de résidence"].isin(Douala)]
                afficher_lollipop_modalites(base2,"Arrondissement de résidence",6)

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
