import streamlit as st
from PIL import Image
from Photos.photo_link import main_dir

logo_path = main_dir("campagne_cameroun_dst.webp")
logo = Image.open(logo_path)

def accueil_load():
    
    with st.sidebar:
        st.title('🏠 Accueil')
    st.sidebar.markdown('---')
    st.sidebar.markdown("## Base de données utilisée")
    st.sidebar.markdown("""[*Données appurées*](https://www.google.com/search?q=Afriland&oq=afr&gs_lcrp=EgZjaHJvbWUqDggAEEUYOxhDGIAEGIoFMg4IABBFGDsYQxiABBiKBTIGCAEQRRhAMgYIAhBFGD0yBggDEEUYPTIGCAQQRRg8MgYIBRBFGEEyBggGEEUYPDIGCAcQRRg80gEINDU5M2owajmoAgCwAgA&sourceid=chrome&ie=UTF-8)
                        """)
    st.sidebar.markdown('---')
    st.sidebar.markdown("## Scripts de l'application")
    st.sidebar.markdown("""[*Code de l'application*](https://www.google.com/search?q=Afriland&oq=afr&gs_lcrp=EgZjaHJvbWUqDggAEEUYOxhDGIAEGIoFMg4IABBFGDsYQxiABBiKBTIGCAEQRRhAMgYIAhBFGD0yBggDEEUYPTIGCAQQRRg8MgYIBRBFGEEyBggGEEUYPDIGCAcQRRg80gEINDU5M2owajmoAgCwAgA&sourceid=chrome&ie=UTF-8)
                        """)
    # En-tête de la page
    #st.title("🩸Save a Life, Donate Blood")
    # Centrer le titre en utilisant Markdown et HTML  
    st.markdown(  
    """
    <div style="border: 4px solid black; padding: 10px; width: fit-content; margin: auto;">
        <h1 style='text-align: center;'>🩸 Save a Life, Donate Blood</h1>
    </div>
    """,  
    unsafe_allow_html=True  
)
    st.image(logo, use_column_width=True)

    st.markdown("""
    Bienvenue sur l'application interactive de suivi des campagnes de don de sang. 
    Ce tableau de bord vous permet d'explorer et d'analyser les données des donneurs afin d'améliorer les futures campagnes.
    """)
    st.markdown('---')
    # Présentation des fonctionnalités clés
    st.subheader("🔍 Fonctionnalités du tableau de bord :")
    st.markdown("""
    - 📍 **Cartographie des donneurs** : Répartition géographique interactive
    - 🏥 **Analyse des conditions de santé** : Visualisation des critères d'éligibilité
    - 🔬 **Profilage des donneurs** : Clustering basé sur des données démographiques
    - 📊 **Efficacité des campagnes** : Analyse des tendances et facteurs influents
    - 🔄 **Fidélisation des donneurs** : Étude de la récurrence des dons
    - 🧠 **Analyse de sentiment** : Classification des retours des donneurs
    - 🤖 **Modèle de prédiction** : Évaluation de l’éligibilité au don
    - 🧑‍💻 **Chat Blood Assistant analyst** : Pour une compréhension approfondie des notions et termes d'usage
    - ℹ️ **About us** : Une présentation de tous les membres de la Data Storytellers Team
    """)
    st.markdown('---')

    # Bouton pour accéder au tableau de bord
    st.markdown("### 🌍 Explorez les fonctionnalités dès maintenant !")

    # Créer des colonnes pour l'affichage
    col1, col2, col3 = st.columns([1, 2, 1])  # 1 colonne petite, 2 colonnes grandes, 1 petite à droite

    # Placer le bouton dans la colonne du milieu (col2)
    with col2:
        if st.button("Accéder aux Fonctionnalités"):
            st.markdown("""
        <style>
            .red-arrow {
                font-size: 50px;
                color: red;  /* La couleur de la flèche */
            }
        </style>
        <div class="red-arrow">⬅️</div> Veuillez cliquer sur la barre latérale de la page
    """, unsafe_allow_html=True)
            #fonctionnality_load()
            #st.switch_page("dashboard")  # Rediriger vers la page "dashboard.py"
    # Footer

    st.markdown("---")
    st.markdown("📌 **Projet réalisé Par la DATA STORY TELLER TEAM dans le cadre du Challenge de Visualisation des Données** | 🚀 Développé avec **Python & Streamlit**")

