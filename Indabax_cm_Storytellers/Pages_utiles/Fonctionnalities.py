import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objs as go 
from dateutil.relativedelta import relativedelta  # Pour le calcul précis des mois/jours
import time
from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')

df = pd.read_excel(path, sheet_name='year')
df['Date de remplissage de la fiche'] = pd.to_datetime(df['Date de remplissage de la fiche'])


def fonctionnalities_load():
    
   

    # CSS personnalisé pour les conteneurs
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
    st.title("👁️ Vue globale sur la campagne")
    st.markdown("---")
    # ---- 2. STATISTIQUES URGENCES ----  
    with st.container():
        st.subheader("📊 L'urgence en chiffres au Cameroun")
        cols = st.columns(3)
        with cols[0]:
            st.metric("Besoin en sang/an", "> 400 000", help="MINSANTE, Cameroun, 2023")
        with cols[1]:
            st.metric("Dons annuels", "~150 000", "+12% vs 2022",help="MINSANTE, Cameroun, 2023")
        with cols[2]:
            st.metric("Taux de donneurs", "0.8%", "De la population éligible",help="MINSANTE, Cameroun, 2023")
    
    # Section statistiques
    


    # Fonction pour calculer la durée en mois et jours
    def calculate_duration(start, end):
        rd = relativedelta(end, start)
        months = rd.years * 12 + rd.months
        days = rd.days
        return months, days

    # Calcul de la durée si une plage valide est sélectionnée
    duration_str = "N/A"
    
    st.markdown("---")
    # Section statistiques
    with st.container():
        col_tit1,col_ti2=st.columns(2)
        with col_tit1:
            st.subheader("📜 Historique campagne -Douala")
        with col_ti2:
            min_date = df['Date de remplissage de la fiche'].min().to_pydatetime()
            max_date = df['Date de remplissage de la fiche'].max().to_pydatetime()
            
            date_range = st.date_input(
                "🔎 Période d'observation",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date,
                format="DD/MM/YYYY"
            )
            
            # Vérification qu'une plage valide est sélectionnée
            if len(date_range) == 2:
                start_date, end_date = date_range
                filtered_df = df[
                    (df['Date de remplissage de la fiche'].dt.date >= start_date) & 
                    (df['Date de remplissage de la fiche'].dt.date <= end_date)
                ]
            else:
                filtered_df = df
                st.warning("Veuillez sélectionner une plage de dates valide")

        stats_col1, stats_col2, stats_col3 = st.columns(3)
        with stats_col1:
            if len(date_range) == 2:
                start_date, end_date = date_range
                months, days = calculate_duration(start_date, end_date)
                duration_str = f"{months} mois et {days} jrs"
            st.metric("📅 Durée de campagne", duration_str)
        with stats_col2:
            st.metric("👥 Total des participants", len(filtered_df["Date de remplissage de la fiche"]))
        with stats_col3:
            nb_elig = len(filtered_df[filtered_df["ÉLIGIBILITÉ AU DON."]=="Eligible"])
            st.metric("✅ Eligibles au don de sang", f"{nb_elig} Personnes")

    
    with st.container():
        st.subheader("🔵 Evolution du nombre des participants à la campagne")
                    
                    # Compter les occurrences de chaque date  
        occurrences = filtered_df['Date de remplissage de la fiche'].value_counts().sort_index()  

                    #occurrences = df['Date de remplissage de la fiche'].value_counts().sort_index()  
        occurrences = occurrences.reset_index()  
        occurrences.columns = ['Date de remplissage de la fiche', 'Occurrences']  # Renommer les colonnes pour la clarté  

                # Créer un graphique vide
        fig = px.line(occurrences.iloc[:1], x="Date de remplissage de la fiche", y="Occurrences", markers=True, title="Progression")

        # Afficher le graphique dans Streamlit
        chart = st.plotly_chart(fig, use_container_width=True)

        # Animation : Ajouter les points progressivement
        for i in range(2, len(occurrences) + 1):
            fig = px.line(occurrences.iloc[:i], x="Date de remplissage de la fiche", y="Occurrences", markers=True, title="Progression")
            chart.plotly_chart(fig, use_container_width=True)
            time.sleep(0.5)
        
            
            
