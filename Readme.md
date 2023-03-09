# ProjectManager

```
ProjectManager est une plateforme de gestion et de suivi de projtes 
immobilier appliquée dans le cas de l'entreprise SIEFTP.
```

- Configuration :

    - Framework : Django (BackEnd)
    - HTML / CSS/ JAVASCRIPT (FrontEnd)
    - PostgreSql (Base de Données)

- Applications :
    - Users ( Pour gerer toutes les données liées aux utilisateur)
    - Materiel ( Pour gerer les stock et inventaires de l'entreprise)
    - Projet ( Pour la gestion des projets)

- Dictionnaire de données

## Application User

    - User
        - nom
        - prenoms
        - email
        - password
        - active
        - created
        - updated
        - is_client
        - is_ouvrier
        - is_responsable
        - is_admin

    - Domaine
        - nom
        - active
        - created
        - updated

    - Profile
        - user_id (Table User)
        - telephone
        - lieu_de_residence
        - sexe
        - photo
        - cout_journalier
        - domaine_id (Table Domaine)
        - active
        - created
        - updated

## Application Projet

    - Categorie
        - nom
        - active
        - created
        - updated

    - Projet
        - nom
        - categorie_id (Table Categorie)
        - proprietaire_id (Table Profile)
        - localite
        - cout_estimatif
        - active
        - created
        - updated
    - DevisProjet
        - projet_id (Table Projet)
        - active
        - created
        - updated

    - ElementDevis
        - titre
        - cout
        - active
        - created
        - updated

    - Equipe
        -  projet (Table Projet)
        -  activite (Table ElementDevis)
        -  reponsable (Table profile)
        -  duree
        -  active
        -  created
        -  updated

    - EquipeOuvrier
        - equipe_id
        - ouvrier_id
        -   active
        -  created
        -  updated

## Application Materiel

    - Categorie
        - nom
        - active
        - created
        - updated

    - Materiel
        - nom
        - categorie_id (Table Categorie)
        - prix
        - quantite
        - active
        - created
        - updated

    -  Mouvement
        - materiel_id  (Table Materiel)
        - effectue_par (Table Profil)
        - projet (Table Projet)
        - quantite
        - active
        - created
        - updated


####################################################################
