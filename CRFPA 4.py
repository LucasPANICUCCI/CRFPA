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

# 🌄 Images apaisantes (Unsplash)
images = [
    "https://source.unsplash.com/featured/?calm,nature",
    "https://source.unsplash.com/featured/?zen,forest",
    "https://source.unsplash.com/featured/?sunrise,peace",
    "https://source.unsplash.com/featured/?mountains,relax",
    "https://source.unsplash.com/featured/?ocean,serenity"
]

# 🧠 Sélections aléatoires
message = random.choice(encouragements)
visualisation = random.choice(visualisations)
image_url = random.choice(images)

# 🖥️ Interface Streamlit
st.set_page_config(page_title="CRFPA Countdown", page_icon="📚")
st.title("🗓️ Compte à rebours CRFPA")
st.subheader(f"👉 Il reste **{jours_restants} jour(s)** avant l’épreuve du **1er septembre 2025**.")

# 🔄 Barre de progression
st.progress(progression, text=f"Progression vers le jour J : {int(progression * 100)}%")

st.markdown("---")

st.markdown(f"💪 **Encouragement du jour :**\n> {message}")
st.markdown(f"🧘 **Visualisation mentale :**\n> *{visualisation}*")

st.markdown("---")

st.image(image_url, caption="🌅 Respire. Visualise. Tu es prêt·e.", use_container_width=True)

if st.button("🔗 Ouvrir l’image dans le navigateur"):
    st.markdown(f"[Clique ici pour ouvrir dans un nouvel onglet]({image_url})", unsafe_allow_html=True)
