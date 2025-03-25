import streamlit as st

from Pages_utiles.Accueil import accueil_load

from Pages_utiles.About_us  import about_us_page

from Pages_utiles.Efficacity_des_campagnes import page_efficacity 
from Pages_utiles.Fidelisation_donneurs import page_fidelisation 
from Pages_utiles.Sante_aligibility import page_santeElig
from Pages_utiles.ACP import acp_analyse
from Pages_utiles.Profil_donneurs import page_profil_load


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
        initial_sidebar_state="collapsed"
    )



# Barre latérale pour la navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Aller à :", ["Accueil","Profil des donneurs","Fidélisation des donneurs","Condition de santé et éligibilité","Efficacité des campagnes","ACP","About Us"])

if page == "About Us":
    about_us_page()
elif page=="ACP":
    acp_analyse()
elif page=="Efficacité des campagnes":
    page_efficacity()
elif page=="Fidélisation des donneurs":
    page_fidelisation()
elif page=="Condition de santé et éligibilité":
    page_santeElig()
elif page=="Profil des donneurs":
    page_profil_load()
else:
    accueil_load()

