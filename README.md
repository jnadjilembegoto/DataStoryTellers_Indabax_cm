# README - Tableau de Bord de la Campagne de Don de Sang

## 📌 Introduction
Ce tableau de bord a été conçu pour analyser et optimiser les campagnes de don de sang en exploitant des données réelles. Il permet aux utilisateurs de visualiser et d'interpréter des tendances clés, d'améliorer les stratégies de collecte et d'identifier les facteurs influençant l'éligibilité et la fidélisation des donneurs.

## 🔑 Fonctionnalités du Tableau de Bord
- 📍 **Cartographie des donneurs** : Répartition géographique interactive des donneurs.
- 🏥 **Analyse des conditions de santé** : Visualisation des critères d'éligibilité.
- 🔬 **Profilage des donneurs** : Clustering basé sur des données démographiques.
- 📊 **Efficacité des campagnes** : Analyse des tendances et des facteurs influents.
- 🔄 **Fidélisation des donneurs** : Étude de la récurrence des dons.
- 💬 **Analyse de sentiment** : Classification des retours des donneurs.
- 🤖 **Modèle de prédiction** : Évaluation de l’éligibilité au don.
- ℹ️ **About us** : Présentation des membres de la Data Storytellers Team.

## 🛠️ Outils Utilisés
- **Langage** : Python
- **Framework Web** : Streamlit
- **Bibliothèques de Data Science et de Visualisation** :
  - Pandas (Manipulation des données)
  - NumPy (Calculs numériques)
  - Seaborn & Matplotlib (Visualisation statique)
  - Plotly (Graphiques interactifs)
  - Folium & streamlit-folium (Cartographie interactive)
  - Pydeck (Visualisation avancée sur cartes)
  - WordCloud (Analyse textuelle)
- **Gestion des dates** : Dateutil
- **Lecture des fichiers** : OpenPyXL

## 📊 Hypothèses de Développement

### 🔹 Base avec Année de Naissance
1. **Date de remplissage de la fiche** :
   - Toutes les campagnes ont eu lieu en **2019**, toute observation hors 2019 a été supprimée.
   - Correction des dates mal formatées (`jj/mm/0019` → `jj/mm/2019`).
   - Suppression des observations avec date de remplissage manquante.
2. **Date de naissance** : Non utilisée car une autre base fournit directement l'âge.
3. **Nationalité** :
   - Catégorisation : "Non précisé" pour les non-nationaux.
   - Correction des fautes d'orthographe.
4. **Religion** : Correction et standardisation des modalités.
5. **Taux d’hémoglobine** : Suppression des unités pour homogénéisation.
6. **Date des dernières règles (DDR)** : Supprimée car redondante.
7. **Sélectionner "OK" pour envoyer** : Supprimée car non pertinente.
8. **Raisons d’indisponibilité et de non-éligibilité** :
   - Normalisation des variables liées.
   - Agrégation des modalités similaires et remplacement des `NaN` par `"sans_raison"`.
9. **Profession** : Correction des variations orthographiques pour uniformisation.

### 🔹 Base avec Âge
1. Suppression des individus avec **0 et 1 an**.
2. Application des mêmes transformations que pour la base précédente.

### 🔹 Base Donneur
1. Suppression des valeurs non numériques dans l'âge.
2. Élimination des valeurs aberrantes.

## 🚀 Conclusion
Ce tableau de bord fournit une vision détaillée et interactive des campagnes de don de sang, permettant d’optimiser les stratégies de collecte et d’améliorer l’expérience des donneurs. Il allie **visualisation avancée, analyse de données et modélisation prédictive**, offrant ainsi un outil puissant pour la prise de décision.

📌 **Data Storytellers Team** remercie tous les contributeurs et espère que cet outil facilitera la gestion des futures campagnes de don de sang ! 🙌

