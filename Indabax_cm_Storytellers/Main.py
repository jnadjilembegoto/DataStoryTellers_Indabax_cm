import streamlit as st

from Pages_utiles.Accueil import accueil_load

from Pages_utiles.About_us  import about_us_page

from Pages_utiles.ACP import acp_analyse

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
page = st.sidebar.selectbox("Aller à :", ["Accueil","ACP","About Us"])

if page == "About Us":
    about_us_page()
elif page=="ACP":
    acp_analyse()
else:
    accueil_load()

