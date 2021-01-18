=======
# OC_V2_P2 - Projet de scraping du site  "Books to Scrape"

Pré requis,
=======
utilition du fichier requirements.txt en vue de créer l'environnement des librairies du projet
pour le créer, lancer la commande :
python -m -venv env
Pour l'alimenter, lancer la commande :
pip install -r requirements.txt

Le projet est composé de 3 principaux fichiers :
=======
- un_livre.py : comporte 3 fonctions "collecter_infos_livre", "imprimer_infos_livre" et "telecharger_image"
- livres_une_categorie.py : comporte 2 fonctions "collecter_pages_categorie",  "collecter_livres_categorie"
- livres_site_entier.py : implemente le scraping du site en entier avec le téléchargement des images des livres
Pour tester, lancer python livres_site_entier.py et laissez vous guider !

