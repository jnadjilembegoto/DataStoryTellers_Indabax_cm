import streamlit as st




def ml_analyse():

    # Interface Streamlit pour entrer les paramètres utilisateur
    st.title("Prédiction de l'éligibilité au don de sang")

    # Créer des champs de saisie pour les paramètres
    age = st.slider("Âge", 18, 100, 30)

    # Saisie du niveau d'étude (utilisation d'un selectbox)
    niveau_etude = st.selectbox("Niveau d'étude", ["Bac", "Licence", "Master", "Doctorat"])

    # Saisie du genre (utilisation d'un selectbox)
    genre = st.selectbox("Genre", ["Homme", "Femme"])

    # Saisie de la situation matrimoniale (utilisation d'un selectbox)
    situation_matrimoniale = st.selectbox("Situation matrimoniale", ["Célibataire", "Marié", "Divorcé"])

    # Saisie de la religion (utilisation d'un selectbox)
    religion = st.selectbox("Religion", ["Christianisme", "Islam"])

    # Lorsque l'utilisateur clique sur "Prédire", on fait la prédiction
    st.button("Prédire l'éligibilité au don de sang")
        # Encoder les valeurs des entrées utilisateur avec l'encoder global
    
    
