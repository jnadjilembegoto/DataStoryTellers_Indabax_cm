from openai import OpenAI
import streamlit as st
import difflib

def chat_load():
    st.title("Chat Blood - Assistant Analyst")

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Message d'accueil de l'assistant
    with st.chat_message("assistant"):
        st.write("Bonjour, je suis Chat Blood, votre assistant")

    # Définir le modèle par défaut si ce n'est pas déjà fait
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"#"gpt-4o-mini"

    # Conserver les messages de chat dans l'état de session
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Base de connaissances
    knowledge_base = {
        "Qu'est-ce que cette application?": "Cette application vous permet de faire des simulations de loi des extrêmes et d'avoir une idée globale sur la théorie des valeurs extrêmes.",
        "Qui es tu? ":"je m'appelle Chat Blood et je suis votre assistant analyste pour la campagne de don de sang.",
        "Parle moi de toi?": "Je suis un modèle d'intelligence artificielle développé par la Data Story Tellers Team. Mon rôle est d'aider à répondre à des questions, fournir des informations, et assister dans divers types de tâches de manière conversationnelle. Je n'ai pas de pensées ou d'expériences personnelles, mais je suis ici pour vous aider avec vos demandes. Vous pouvez me posez des questions en rapport avec la campagne de don de sang",
        "Comment utiliser cette application ?": "Pour utiliser cette fonctionnalité, vous devez accéder à l'accueil comme présenté dans la barre latérale de navigation et lire l'utilisation présentée en bas de ladite page",
    }

    # Afficher les messages précédents
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    def get_response(user_input):
        """Retourne la réponse de la base de connaissances si disponible."""
        for question, answer in knowledge_base.items():
            if question.lower() in user_input.lower():
                return answer
        return None

    def find_best_match(user_input):
        """Retourne la meilleure correspondance pour une question approximative."""
        questions = list(knowledge_base.keys())
        best_match = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.5)
        if best_match:
            return knowledge_base[best_match[0]]
        return None

    if prompt := st.chat_input("Posez votre question ou dites quelque chose :"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = get_response(prompt) or find_best_match(prompt)

        with st.chat_message("assistant"):
            if response:
                st.markdown(response)
            else:
                # Si aucune réponse n'est trouvée, interrogez l'API OpenAI
                try:
                    stream = client.chat.completions.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    )

                    response = st.write_stream(stream)
                except Exception as e: 
                    response = st.write(f"Erreur : {str(e)}")

        # Stockez la réponse de l'assistant
        st.session_state.messages.append({"role": "assistant", "content": response})

    






