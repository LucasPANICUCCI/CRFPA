import streamlit as st
import datetime
import random

# 🎯 Date de l'épreuve
date_epreuve = datetime.date(2025, 9, 1)
aujourd_hui = datetime.date.today()
jours_restants = (date_epreuve - aujourd_hui).days
total_jours = (date_epreuve - datetime.date(2025, 1, 1)).days
progression = (total_jours - jours_restants) / total_jours

# 💬 Messages d'encouragement
encouragements = [
    "Chaque jour compte. Garde le cap 🚀",
    "Tu es plus proche que tu ne le crois ✨",
    "Rappelle-toi pourquoi tu as commencé 🔥",
    "Un pas après l'autre, tu avances 🧭",
    "Ta rigueur d’aujourd’hui, c’est ta réussite de demain 🏁"
]

# 🧘 Visualisations inspirantes
visualisations = [
    "Imagine-toi le 1er septembre au matin, calme, concentré·e. Le silence dans la salle est celui de l'engagement. Tu es à ta place.",
    "Visualise-toi entrant sereinement dans la salle, porté·e par des mois de travail. Tu inspires, tu sais. C’est ton moment.",
    "Le soleil se lève sur le 1er septembre. Tu es là, prêt·e, confiant·e. Tu transformes la pression en puissance."
]

# ❓ Questions puissantes
questions = [
    "Qu’est-ce qu’une réussite signifierait vraiment pour toi ?",
    "Si tu ne devais retenir qu’une chose de ton parcours, ce serait quoi ?",
    "Quel est le plus petit pas possible aujourd’hui vers ton objectif ?",
    "Qu’est-ce qui te rend fier·e de toi cette semaine ?",
    "Si tu te parlais avec bienveillance, que te dirais-tu aujourd’hui ?"
]

# 🔀 Sélections aléatoires
message = random.choice(encouragements)
visualisation = random.choice(visualisations)
question = random.choice(questions)

# 🖥️ Interface Streamlit
st.set_page_config(page_title="CRFPA Countdown", page_icon="📚")
st.title("🗓️ Compte à rebours CRFPA")
st.subheader(f"👉 Il reste **{jours_restants} jour(s)** avant l’épreuve du **1er septembre 2025**.")

# 🔄 Barre de progression sans pourcentage
st.progress(progression)

st.markdown("---")

st.markdown(f"💪 **Encouragement du jour :**\n> {message}")
st.markdown(f"🧘 **Visualisation mentale :**\n> *{visualisation}*")
st.markdown(f"🧠 **Question du jour :**\n> _{question}_")

st.markdown("---")

# 🔥 Message en très gros, centré
st.markdown(
    """
    <div style='text-align:center; padding: 40px 0;'>
        <h1 style='font-size: 4em; color: #ff4b4b;'>RAPPELLE-TOI :</h1>
        <h1 style='font-size: 6em; font-weight: bold; color: #4BFF4B;'>JE VAIS RÉUSSIR !</h1>
    </div>
    """,
    unsafe_allow_html=True
)
