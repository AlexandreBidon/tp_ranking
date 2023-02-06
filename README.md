# TP 3 : Expansion de requête et ranking 

## Présentation
**Auteur** : Alexandre Bidon

**Note** : Ce repo contient le code d'un TP du cours d'indexation web. Le sujet du TP est [disponible ici](https://github.com/AlexandreBidon/tp_ranking/blob/master/docs/TP3.pdf).

Ce repo présente une implémentation basique d'un ranking de page web.

### Comment lancer le ranking

Pour commencer il faut installer les dépendances du projet :

> pip install -r requirements.txt

Il est ensuite possible d'utiliser l'outil avec la commande suivante :

> python3 main.py --request <insérer sa requete>

Il est possible d'ajouter les arguments suivants à la commande :

- '--request_all_tokens' : désactivé par défaut. Si True, cherche uniquement les sites contenant tous les termes de la requete. (Filtre ET/OU)
- '--result_file' : pour modifier le chemin du fichier d'export

## Fonctionnement
