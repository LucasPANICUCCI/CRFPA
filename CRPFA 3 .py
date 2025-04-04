import datetime
import random
import webbrowser

# 🎯 Date de l'épreuve
date_epreuve = datetime.date(2025, 9, 1)
aujourd_hui = datetime.date.today()
jours_restants = (date_epreuve - aujourd_hui).days

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

# 🎲 Sélection aléatoire
message = random.choice(encouragements)
visualisation = random.choice(visualisations)
image_url = random.choice(images)

# 📣 Affichage stylisé
print("\n🗓️  Compte à rebours CRFPA")
print(f"👉 Il reste {jours_restants} jour(s) avant l’épreuve du 1er septembre 2025.\n")
print(f"💪 Encouragement :\n→ {message}\n")
print(f"🧘 Visualisation :\n→ {visualisation}\n")
print(f"🌅 Image apaisante :\n→ {image_url}")

# 🔗 Option d’ouverture de l’image
ouvrir = input("\n🔍 Ouvrir l’image dans ton navigateur ? (o/n) : ")
if ouvrir.lower() == 'o':
    webbrowser.open(image_url)
