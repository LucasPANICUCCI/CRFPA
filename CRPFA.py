import { useState, useEffect } from "react";

const encouragements = [
  "Chaque jour compte. Garde le cap !",
  "Tu es plus proche que tu ne le crois.",
  "Rappelle-toi pourquoi tu as commencé.",
  "Tu vas y arriver, un pas à la fois.",
  "Ta rigueur d’aujourd’hui, c’est ta réussite de demain."
];

const images = [
  "https://source.unsplash.com/featured/?calm,nature",
  "https://source.unsplash.com/featured/?zen,forest",
  "https://source.unsplash.com/featured/?sunrise,peace",
  "https://source.unsplash.com/featured/?mountains,relax",
  "https://source.unsplash.com/featured/?ocean,serenity"
];

const situations = [
  "Imagine-toi le 1er septembre au matin, installé·e calmement à ta table, concentré·e, prêt·e. Le silence dans la salle est celui de l'engagement. Tu es à ta place.",
  "Visualise-toi entrant sereinement dans la salle, chaque pas porté par des mois de travail. Tu inspires, tu sais. C’est ton moment.",
  "Le soleil se lève sur le 1er septembre. Tu es là, prêt·e, confiant·e. Tu es celui ou celle qui transforme la pression en puissance."
];

export default function CRFPAApp() {
  const [joursRestants, setJoursRestants] = useState(0);
  const [message, setMessage] = useState("");
  const [image, setImage] = useState("");
  const [situation, setSituation] = useState("");

  useEffect(() => {
    const dateEpreuve = new Date("2025-09-01");
    const aujourdHui = new Date();
    const diff = Math.ceil((dateEpreuve - aujourdHui) / (1000 * 60 * 60 * 24));
    setJoursRestants(diff);

    // Sélections aléatoires
    setMessage(encouragements[Math.floor(Math.random() * encouragements.length)]);
    setImage(images[Math.floor(Math.random() * images.length)]);
    setSituation(situations[Math.floor(Math.random() * situations.length)]);
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white p-6">
      <h1 className="text-3xl font-bold mb-4 text-center">CRFPA - Compte à rebours</h1>
      <p className="text-xl text-gray-700 mb-2">
        Il reste <span className="font-semibold text-indigo-600">{joursRestants}</span> jours avant la première épreuve (Métropole - 1er septembre 2025).
      </p>
      <p className="italic text-lg text-green-700 mb-4">{message}</p>
      <p className="text-center text-md text-gray-600 mb-6">{situation}</p>
      <img src={image} alt="Inspiration" className="w-full max-w-md rounded-xl shadow-xl" />
    </div>
  );
}