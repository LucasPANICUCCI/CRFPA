import datetime
import random
import webbrowser

# Date de l'épreuve (1er septembre 2025)
date_epreuve = datetime.date(2025, 9, 1)
aujourd_hui = datetime.date.today()
jours_restants = (date_epreuve - aujourd_hui).days

# Liste des messages d'encouragement
encouragements = [
    "Chaque jour compte. Garde le cap !",
    "Tu es plus proche que tu ne le crois.",
    "Rappelle-toi pourquoi tu as commencé.",
    "Tu vas y arriver, un pas à la fois.",
    "Ta rigueur d’aujourd’hui, c’est ta réussite de demain."
]

# Liste des situations inspirantes
situations = [
    "Imagine-toi le 1er septembre au matin, installé·e calmement à ta table, concentré·e, prêt·e. Le silence dans la salle est celui de l'engagement. Tu es à ta place.",
    "Visualise-toi entrant sereinement dans la salle, chaque pas porté par des mois de travail. Tu inspires, tu sais. C’est ton moment.",
    "Le soleil se lève sur le 1er septembre. Tu es là, prêt·e, confiant·e. Tu es celui ou celle qui transforme la pression en puissance."
]

# Liste d'images apaisantes (via Unsplash)
images = [
    "https://source.unsplash.com/featured/?calm,nature",
    "https://source.unsplash.com/featured/?zen,forest",
    "https://source.unsplash.com/featured/?sunrise,peace",
    "https://source.unsplash.com/featured/?mountains,relax",
    "https://source.unsplash.com/featured/?ocean,serenity"
]

# Sélection aléatoire
message = random.choice(encouragements)
situation = random.choice(situations)
image_url = random.choice(images)

# Affichage
print(f"📅 Il reste {jours_restants} jour(s) avant la première épreuve du CRFPA (1er septembre 2025).")
print(f"\n💬 Encouragement : {message}")
print(f"\n🧘 Visualisation : {situation}")
print(f"\n🖼️ Image apaisante : {image_url}")

# Ouvrir automatiquement l'image dans le navigateur
ouvrir = input("\nSouhaites-tu ouvrir l'image apaisante dans ton navigateur ? (o/n) : ")
if ouvrir.lower() == 'o':
    webbrowser.open(image_url)
