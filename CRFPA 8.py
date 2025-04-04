import streamlit as st
import datetime
import random

# 🎯 Date de l'épreuve
date_epreuve = datetime.date(2025, 9, 1)
aujourd_hui = datetime.date.today()
jours_restants = (date_epreuve - aujourd_hui).days
total_jours = (date_epreuve - datetime.date(2025, 1, 1)).days
progression = (total_jours - jours_restants) / total_jours

# 💬 Messages d'encouragement (stock enrichi)
encouragements = [
    "Chaque jour compte. Garde le cap 🚀",
    "Tu es plus proche que tu ne le crois ✨",
    "Rappelle-toi pourquoi tu as commencé 🔥",
    "Un pas après l'autre, tu avances 🧭",
    "Ta rigueur d’aujourd’hui, c’est ta réussite de demain 🏁",
    "Ta discipline t’ouvre des portes que tu n’imagines pas encore.",
    "La confiance se construit en agissant, continue.",
    "Tu n’as pas besoin d’être parfait, juste régulier.",
    "Ce que tu fais aujourd’hui pose les fondations de demain.",
    "Courage. Tu es en train d’écrire une belle histoire.",
    "Tu es en chemin. Et ce chemin te transforme.",
    "Ne doute jamais de ton potentiel.",
    "Continue. Même lentement. Tu avances.",
    "Ce n’est pas la vitesse, mais la direction qui compte.",
    "Fier·e de toi d’avoir tenu jusqu’ici. Continue.",
    "Un jour, ce stress d’aujourd’hui te fera sourire.",
    "Ce que tu apprends aujourd’hui t’appartiendra pour toujours.",
    "Tu construis ta liberté, ta force, ton avenir.",
    "Même dans le doute, tu peux avancer.",
    "Tu es capable. Tu es prêt·e. Tu vas réussir."
]

# 🧘 Visualisations inspirantes
visualisations = [
    "Imagine-toi le 1er septembre au matin, calme, concentré·e. Le silence dans la salle est celui de l'engagement. Tu es à ta place.",
    "Visualise-toi entrant sereinement dans la salle, porté·e par des mois de travail. Tu inspires, tu sais. C’est ton moment.",
    "Le soleil se lève sur le 1er septembre. Tu es là, prêt·e, confiant·e. Tu transformes la pression en puissance.",
    "Tu entres dans la salle avec calme, les épaules basses, la tête haute. Tu es prêt·e.",
    "Tu regardes ta copie, tu sais que tu as les outils. Tu es là pour les utiliser.",
    "Tu inspires profondément, puis tu écris la première ligne. Tu y es. Vraiment.",
    "Tu n’es pas seul·e. Des centaines comme toi ont confiance. Tu fais partie de cette énergie.",
    "Tes mains posées sur la table, tu sens que ton corps sait quoi faire.",
    "Tu souris en entrant : tu as travaillé pour ça. C’est ton moment.",
    "Tu es concentré·e, ton regard est clair, ta posture solide. Tout est en place.",
    "Ce que tu as semé, tu le récoltes aujourd’hui. Tu peux y croire.",
    "La salle est calme, ton esprit aussi. Tu es dans ton axe.",
    "Tu entends les stylos qui grattent. Le tien va marquer des points.",
    "Chaque mot que tu écris construit ton avenir.",
    "Tu t’assois. Tu respires. Tu es prêt·e.",
    "Ton esprit est limpide. Tu sais où tu vas.",
    "Tu regardes autour de toi et tu sais que tu es prêt·e à faire la différence.",
    "Tu sens l’énergie circuler : tu es dans ton pouvoir.",
    "C’est ton moment. C’est ta scène. Tu es à ta place.",
    "Tu n’as plus à prouver, juste à exprimer."
]

# ❓ Questions puissantes pour le jour
questions = [
    "Qu’est-ce qu’une réussite signifierait vraiment pour toi ?",
    "Si tu ne devais retenir qu’une chose de ton parcours, ce serait quoi ?",
    "Quel est le plus petit pas possible aujourd’hui vers ton objectif ?",
    "Qu’est-ce qui te rend fier·e de toi cette semaine ?",
    "Si tu te parlais avec bienveillance, que te dirais-tu aujourd’hui ?",
    "Qu’est-ce qui t’a motivé à commencer ce chemin ?",
    "Quelle pensée t’aiderait à passer cette journée ?",
    "Si tu réussissais demain, que ressentirais-tu ?",
    "Qu’est-ce qui t’apaise dans le chaos ?",
    "De quoi as-tu besoin pour avancer aujourd’hui ?",
    "Quelle est la phrase que tu veux te répéter cette semaine ?",
    "Quelle est la victoire invisible que tu as déjà remportée ?",
    "Si tu regardais ton parcours avec douceur, que verrais-tu ?",
    "Que veux-tu te prouver aujourd’hui ?",
    "Que peux-tu lâcher pour avancer plus léger ?",
    "Qu’est-ce qui mérite ton énergie aujourd’hui ?",
    "Et si tu étais déjà assez ?",
    "Quelle action ferait la différence ce soir ?",
    "Qu’est-ce que tu veux célébrer à la fin de cette journée ?",
    "Qu’est-ce que tu veux dire à ton futur toi aujourd’hui ?"
]

# 🔀 Sélections aléatoires
message = random.choice(encouragements)
visualisation = random.choice(visualisations)
question = random.choice(questions)

# 🖥️ Interface Streamlit
st.set_page_config(page_title="CRFPA Countdown", page_icon="📚")
st.title("🗓️ Compte à rebours CRFPA")

# 👀 Sous-titre avec ajout rassurant
st.markdown(
    f"<h3>👉 Il reste {jours_restants} jour(s) avant l’épreuve du <strong>1er septembre 2025</strong> "
    f"<br><span style='font-size:0.8em; color:gray;'>(ça va aller : je vais réussir !)</span></h3>",
    unsafe_allow_html=True
)

# 🔄 Barre de progression sans pourcentage
st.progress(progression)

st.markdown("---")

st.markdown(f"💪 **Encouragement du jour :**\n> {message}")
st.markdown(f"🧘 **Visualisation mentale :**\n> *{visualisation}*")
st.markdown(f"🧠 **Question du jour :**\n> _{question}_")

st.markdown("---")

# 💥 Message final en très grand
st.markdown(
    """
    <div style='text-align:center; padding: 40px 0;'>
        <h1 style='font-size: 4em; color: #ff4b4b;'>RAPPELLE-TOI :</h1>
        <h1 style='font-size: 6em; font-weight: bold; color: #4BFF4B;'>JE VAIS RÉUSSIR !</h1>
    </div>
    """,
    unsafe_allow_html=True
)
