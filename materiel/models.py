from users.models import Profile
from django.db import models
from projet.models import Projet

type_mouvement = (
        ('ENTREE', 'ENTREE',),
        ('SORTIE', 'SORTIE',),
)# Create your models here.
class Categorie(models.Model):
    """Model definition for Categorie."""
    nom = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return f"{self.nom}"

class Materiel(models.Model):
    """Model definition for Materiel."""
    nom = models.CharField(max_length=150)
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name="categorie_materiel")
    prix_unitaire = models.FloatField(default=0)
    quantite = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Materiel."""

        verbose_name = 'Materiel'
        verbose_name_plural = 'Materiels'

    def __str__(self):
        """Unicode representation of Materiel."""
        return f"{self.nom} - Quantité : {self.quantite} Prix Unitaire : {self.prix_unitaire}"


class Mouvement(models.Model):
    """Model definition for Mouvement."""
    materiel  = models.ForeignKey(
        Materiel, on_delete=models.CASCADE, related_name="materiel_mouvement")
    effectue_par  = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile_mouvement")
    projet  = models.ForeignKey(
        Projet, on_delete=models.CASCADE, related_name="projet_mouvement", null=True, blank=True)
    type_mouvement = models.CharField(max_length=6, choices=type_mouvement,)
    quantite = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for Mouvement."""

        verbose_name = 'Mouvement'
        verbose_name_plural = 'Mouvements'

    def __str__(self):
        """Unicode representation of Mouvement."""
        return f"{self.materiel} {self.effectue_par}"

 