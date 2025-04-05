import streamlit as st
from PIL import Image
from Photos.photo_link import main_dir
from Pages_utiles.About_us  import about_us_page

from Pages_utiles.Efficacity_des_campagnes import page_efficacity 
from Pages_utiles.Fidelisation_donneurs import page_fidelisation 
from Pages_utiles.Sante_aligibility import page_santeElig
from Pages_utiles.ACP import acp_analyse
from Pages_utiles.ML import ml_analyse
from Pages_utiles.Profil_donneurs2 import page_profil_load
from Pages_utiles.carto2 import carto_page_load
from Pages_utiles.ChatBlood import chat_load
from Pages_utiles.Fonctionnalities import fonctionnalities_load


logo_path = main_dir("campagne_cameroun_dst.webp")
logo = Image.open(logo_path)
# Configuration de la page
st.set_page_config(
        page_title="Tableau de Bord - Don de Sang",
        page_icon="🩸",
        layout="wide",
        initial_sidebar_state="expanded"
    )


# Initialisation de l'état de session
if "auth_status" not in st.session_state:
    st.session_state.auth_status = False  # False = non connecté
if "username" not in st.session_state:
    st.session_state.username = ""

# Page d'accueil
if not st.session_state.auth_status:
    with st.sidebar:
        st.title('🏠 Accueil')
    st.sidebar.markdown('---')
    st.sidebar.markdown("## Base de données utilisée")
    st.sidebar.markdown("""[*Données appurées*](https://www.google.com/)
                        """)
    st.sidebar.markdown('---')
    st.sidebar.markdown("## Scripts de l'application")
    st.sidebar.markdown("""[*Code de l'application*](https://www.google.com/)
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
    if st.button("Accéder aux Fonctionnalités"):
        st.session_state.auth_page = True
        st.rerun()
    st.markdown("---")
    st.markdown("📌 **Projet réalisé Par la Data Storytellers Team dans le cadre du Challenge de Visualisation des Données** | 🚀 Développé avec **Python & Streamlit**")

# Interface d'authentification
if "auth_page" in st.session_state and st.session_state.auth_page:
    st.title("Authentification")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Valider"):
        if username == "admin" and password == "password123":  # 🔹 Remplace par ta logique d'authentification
            st.session_state.auth_status = True
            st.session_state.username = username
            st.session_state.auth_page = False
            st.rerun()  # Rafraîchir pour charger la nouvelle interface
        else:
            st.error("Identifiants incorrects. Veuillez réessayer.")

    if st.button("Retour à l'accueil"):
        del st.session_state["auth_page"]
        st.rerun()

# Interface après connexion (avec Sidebar)
if st.session_state.auth_status:
    st.sidebar.title(f"Bienvenue, {st.session_state.username} 👋")
    # Barre latérale pour la navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Aller à :", ["Fonctionnalités","Cartographie de la Répartition des Donneurs","Profil des donneurs","Fidélisation des donneurs","Condition de santé et éligibilité","Efficacité des campagnes","Analyse de sentiments","Modèle de prédiction","Chat Blood","About Us"])

    #st.title(f"Page {page}")
    if page == "About Us":
        about_us_page()
    elif page=="Chat Blood":
        chat_load()
    elif page=="Analyse de sentiments":
        acp_analyse()
    elif page=="Efficacité des campagnes":
        page_efficacity()
    elif page=="Fidélisation des donneurs":
        page_fidelisation()
    elif page=="Condition de santé et éligibilité":
        page_santeElig()
    elif page=="Profil des donneurs":
        page_profil_load()
    elif page=="Modèle de prédiction":
        ml_analyse()
    elif page=="Cartographie de la Répartition des Donneurs":
        carto_page_load()
    else :
        fonctionnalities_load()
        #st.write("⚙️ Paramètres de votre compte.")


    if st.sidebar.button("Se déconnecter"):
        del st.session_state["auth_status"]
        del st.session_state["username"]
        st.rerun()

