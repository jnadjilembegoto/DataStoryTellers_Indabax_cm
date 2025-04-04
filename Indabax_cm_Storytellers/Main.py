import streamlit as st

from Pages_utiles.Accueil import accueil_load

from Pages_utiles.About_us  import about_us_page

from Pages_utiles.Efficacity_des_campagnes import page_efficacity 
from Pages_utiles.Fidelisation_donneurs import page_fidelisation 
from Pages_utiles.Sante_aligibility import page_santeElig
from Pages_utiles.ACP import acp_analyse
from Pages_utiles.ML import ml_analyse
from Pages_utiles.Profil_donneurs2 import page_profil_load
from Pages_utiles.carto2 import carto_page_load
from Pages_utiles.ChatBlood import chat_load


import openpyxl


#data_full_path = os.path.join(main_dir, "Datas/africa_employment_data.xlsx")
#@st.cache
#def load_data():
#    return pd.read_excel(data_full_path)

# Configuration de la page
st.set_page_config(
        page_title="Tableau de Bord - Don de Sang",
        page_icon="🩸",
        layout="wide",
        initial_sidebar_state="expanded"
    )
#collapsed


# Barre latérale pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Aller à :", ["Accueil","Cartographie de la Répartition des Donneurs","Profil des donneurs","Fidélisation des donneurs","Condition de santé et éligibilité","Efficacité des campagnes","Analyse de sentiments","Modèle de prédiction","Chat Blood","About Us"])

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
else:
    accueil_load()

