import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime

from Datas.data_link import data_dir
path = data_dir('base_streamlit_storytellers.xlsx')
#@st.cache_data
df = pd.read_excel(path, sheet_name='donneur')
df['Horodateur'] = pd.to_datetime(df['Horodateur'])

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
    st.title(" Vue globale sur la campagne")
    
    # Section statistiques
    with st.container():
        st.subheader("📊 Statistiques clés")
        stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
        
        with stats_col1:
            st.metric("Donneuses", len(df[df['Sexe'] == 'Feminin']))
            
        with stats_col2:
            st.metric("Donneurs", len(df[df['Sexe'] == 'Masculin']))
            
        with stats_col3:
            most_common_blood = df['Groupe Sanguin ABO / Rhesus'].mode()[0]
            st.metric("Groupe sanguin le plus fréquent", most_common_blood)
        
        with stats_col4:
            avg_age = int(df['Age'].mean())
            st.metric("Âge moyen des donneurs", f"{avg_age} ans")

    # Première ligne avec deux colonnes
    col1, col2 = st.columns([2, 1])

    with col1:
        with st.container():
            st.subheader("🔵 Répartition des groupes sanguins")
            
            # Diagramme circulaire
            blood_counts = df['Groupe Sanguin ABO / Rhesus'].value_counts().reset_index()
            blood_counts.columns = ['Groupe Sanguin', 'Nombre']
            
            fig = px.pie(blood_counts, 
                        values='Nombre', 
                        names='Groupe Sanguin', 
                        hole=0.3,
                        color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        with st.container():
            st.subheader("🩸 Dons")
            
            # Total des dons
            total_donations = len(df)
            st.metric("Total des dons", total_donations)
            
            # Détails par groupe sanguin
            st.markdown("**Dons par groupe sanguin**")
            blood_type_counts = df['Groupe Sanguin ABO / Rhesus'].value_counts()
            
            # Affichage en 2 colonnes
            b_col1, b_col2 = st.columns(2)
            
            for i, (blood_type, count) in enumerate(blood_type_counts.items()):
                if i % 2 == 0:
                    with b_col1:
                        st.metric(blood_type, count)
                else:
                    with b_col2:
                        st.metric(blood_type, count)

    # Deuxième ligne avec deux colonnes
    col3, col4 = st.columns([1, 2])

    with col3:
        with st.container():
            st.subheader("👥 Donneurs")
            
            # Nombre de donneurs uniques (approximation)
            active_donors = df['Horodateur'].nunique()
            st.metric("Donneurs actifs", active_donors)
            
            # Prochaine collecte
            next_drive = "24 Juillet 2024"
            st.metric("Prochaine collecte", next_drive)
            st.caption("Date prévue")

    with col4:
        with st.container():
            st.subheader("📈 Analyses complémentaires")
            
            # Sélecteur d'analyse
            analysis_option = st.selectbox("Analyser par :", 
                                        ['Sexe', 'Age', 'Type de donation', 'Phenotype'])
            
            if analysis_option == 'Age':
                fig = px.histogram(df, x='Age', nbins=20, 
                                title="Répartition par âge des donneurs",
                                labels={'Age': 'Âge', 'count': 'Nombre'},
                                color_discrete_sequence=['#ff4b4b'])
                fig.update_layout(yaxis_title="Nombre de donneurs")
                st.plotly_chart(fig, use_container_width=True)
            else:
                counts = df[analysis_option].value_counts().reset_index()
                counts.columns = [analysis_option, 'Nombre']
                
                fig = px.bar(counts, 
                            x=analysis_option, 
                            y='Nombre', 
                            title=f"Répartition par {analysis_option.lower()}",
                            labels={analysis_option: analysis_option, 'Nombre': 'Nombre'},
                            color=analysis_option,
                            color_discrete_sequence=px.colors.sequential.RdBu)
                st.plotly_chart(fig, use_container_width=True)


    # Pied de page
    st.markdown("---")
    st.caption("Dernière mise à jour : " + datetime.now().strftime("%d/%m/%Y %H:%M"))
