import streamlit as st
from PIL import Image
from Photos.photo_link import main_dir
from Pages_utiles.About_us  import about_us_page

from Pages_utiles.Efficacity_des_campagnes import page_efficacity 
from Pages_utiles.Fidelisation_donneurs import page_fidelisation 
from Pages_utiles.Sante_aligibility import page_santeElig
from Pages_utiles.ACP import acp_analyse
from Pages_utiles.ML import ml_analyse
#from Pages_utiles.Profil_donneurs2 import page_profil_load
from Pages_utiles.Profil_des_donneurs import page_profil_load
from Pages_utiles.carto2 import carto_page_load
from Pages_utiles.ChatBlood import chat_load
from Pages_utiles.Fonctionnalities import fonctionnalities_load


logo_path = main_dir("campagne_cameroun_dst.webp")
logo = Image.open(logo_path)
coeur_path=main_dir("sang_coeur.webp")
coeur= Image.open(coeur_path)
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
    st.sidebar.image(coeur, use_column_width=True)
    st.sidebar.markdown('---')
    
    # En-tête de la page
    #st.title("🩸Save a Life, Donate Blood")
    # Centrer le titre en utilisant Markdown et HTML  
       # Appliquer le style CSS amélioré
    st.markdown("""
        <style>
            .custom-box {
                border: 3px solid #8B0000;  /* Rouge foncé */
                padding: 5px;
                width: 100%;
                margin: auto;
                border-radius: 12px;
                box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.2);
                background-color: #fff5f5; /* Blanc rosé */
            }
            .title-text {
                text-align: center;
                font-size: 26px;
                font-weight: bold;
                color: #B22222; /* Rouge bordeaux */
                font-family: 'Arial', sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)

    # Création du bloc stylisé
    
    st.markdown("""
        <div class="custom-box">
            <h1 class="title-text">🩸Save a Life, Donate Blood</h1>
        </div>
    """, unsafe_allow_html=True)
     
    
    st.image(logo, use_column_width=True)

    st.markdown("""
    Bienvenue sur l'application interactive de suivi des campagnes de don de sang. 
    Ce tableau de bord permet d'explorer et d'analyser les données des donneurs de sang afin d'améliorer les futures campagnes.
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
        #st.rerun()
    
# Interface d'authentification
if "auth_page" in st.session_state and st.session_state.auth_page:

    
    with st.container():
        colg,colc,cold=st.columns([1, 2, 1])  # 1:1:2 signifie que la colonne du milieu est deux fois plus large  

        with colc:
            
            # Utilisation d'un formulaire pour valider avec "Enter"
            with st.form(key="login_form"):
                st.subheader("Connexion 🔒")
                username = st.text_input("Nom d'utilisateur 👤")
                password = st.text_input("Mot de passe 🔑", type="password")

                # Bouton de validation du formulaire (Enter fonctionne aussi)
                submit_button = st.form_submit_button("✅ Valider")

                if submit_button:  # Vérifie si le formulaire est soumis
                    if username == "admin" and password == "password123":  
                        st.session_state.auth_status = True
                        st.session_state.username = username
                        st.session_state.auth_page = False
                        st.rerun()  # Rafraîchir pour charger la nouvelle interface
                    else:
                        st.error("❌ Identifiants incorrects. Veuillez réessayer.")
                
    st.markdown("---")
    st.markdown("📌 **Projet réalisé Par la Data Storytellers Team dans le cadre du Challenge de Visualisation des Données** | 🚀 Développé avec **Python & Streamlit**")

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

