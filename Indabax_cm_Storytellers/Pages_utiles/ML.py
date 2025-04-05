import streamlit as st
import joblib
import numpy as np

from Datas.data_link import data_dir
path = data_dir('modele_eligibilite.joblib')

def ml_analyse():
    # Charger le modèle
    model = joblib.load(path)
    
    # Interface utilisateur avec Streamlit
    st.title("🩸 Prédiction d'Éligibilité au Don de Sang")
    
    # Collecte des données utilisateur
    genre = st.radio("Genre", ["Homme", "Femme"])
    age = st.number_input("Âge", min_value=0, max_value=120, value=30)
    taux_hemoglobine = st.number_input("Taux d’hémoglobine", min_value=0.0, max_value=20.0, value=13.5)
    
    donne_sang = st.checkbox("A déjà donné le sang ?")
    antibiotique = st.checkbox("Sous antibiothérapie ?")
    hemoglobine_basse = st.checkbox("Hémoglobine basse ?")
    dernier_don_3mois = st.checkbox("Dernier don dans les 3 mois ?")
    ist_recente = st.checkbox("IST récente ?")
    
    # Variables spécifiques aux femmes
    if genre == "Femme":
        allaitement = st.checkbox("Allaitement en cours ?")
        accouchement_6mois = st.checkbox("Accouchement dans les 6 mois ?")
        ivg_6mois = st.checkbox("IVG dans les 6 mois ?")
        enceinte = st.checkbox("Enceinte ?")
        ddr_mauvais = st.checkbox("Dernières règles < 14 jours ?")
    else:
        allaitement = accouchement_6mois = ivg_6mois = enceinte = ddr_mauvais = False
    
    transfusion_antecedent = st.checkbox("Antécédents de transfusion ?")
    porteur_maladies = st.checkbox("Porteur de maladies ?")
    opere = st.checkbox("Opéré récemment ?")
    drepanocytaire = st.checkbox("Drepanocytaire ?")
    diabetique = st.checkbox("Diabétique ?")
    hypertendu = st.checkbox("Hypertendu ?")
    asthmatique = st.checkbox("Asthmatique ?")
    cardiaque = st.checkbox("Cardiaque ?")
    tatoue = st.checkbox("Tatoué ?")
    scarifie = st.checkbox("Scarifié ?")
    
    # Transformation des valeurs en format numérique
    donnees = np.array([
        age,
        1 if genre == "Homme" else 0,
        int(donne_sang),
        taux_hemoglobine,
        int(antibiotique),
        int(hemoglobine_basse),
        int(dernier_don_3mois),
        int(ist_recente),
        int(ddr_mauvais),
        int(allaitement),
        int(accouchement_6mois),
        int(ivg_6mois),
        int(enceinte),
        int(transfusion_antecedent),
        int(porteur_maladies),
        int(opere),
        int(drepanocytaire),
        int(diabetique),
        int(hypertendu),
        int(asthmatique),
        int(cardiaque),
        int(tatoue),
        int(scarifie)
    ]).reshape(1, -1)
    
    # Bouton de prédiction
    if st.button("Prédire l'éligibilité"):
        prediction = model.predict(donnees)[0]
        
        if prediction == 1:
            st.success("✅ L'individu est Eligible.")
        elif prediction == 2:
            st.error("❌ L'individu est Définitivement non-eligible.")
        elif prediction == 3:
            st.warning("⚠️ L'individu est Temporairement non-eligible.")
        else:
            st.info(f"ℹ️ Modalité inconnue : {prediction}")

