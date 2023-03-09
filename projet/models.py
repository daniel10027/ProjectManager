from django.db import models
from users.models import Profile
from django.utils.translation import gettext_lazy as _
# Create your models here.


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


class Projet(models.Model):
    """Model definition for Projet."""
    nom = models.CharField(max_length=50)
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, related_name="categorie_projet")
    proprietaire = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projet_proprietaire")
    localite = models.CharField(max_length=50)
    cout_estimatif = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Projet."""

        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        """Unicode representation of Projet."""
        return f"{self.nom,  self.proprietaire.user.nom , self.localite}"


class DevisProjet(models.Model):
    """Model definition for DevisProjet."""
    projet = models.OneToOneField(
        Projet, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for DevisProjet."""

        verbose_name = 'Devis Projet'
        verbose_name_plural = 'Devis Projets'

    def __str__(self):
        """Unicode representation of DevisProjet."""
        return f"{self.projet}"


class ElementDevis(models.Model):
    """Model definition for ElementDevis."""
    devis = models.ForeignKey(
        DevisProjet, on_delete=models.CASCADE, related_name="elements_devis")
    titre = models.CharField(max_length=150)
    cout = models.FloatField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for ElementDevis."""

        verbose_name = 'Element Devis'
        verbose_name_plural = 'Element Devis'

    def __str__(self):
        """Unicode representation of ElementDevis."""
        return f"{self.titre, self.cout}"


class Equipe(models.Model):
    """Model definition for Equipe."""
    projet = models.ForeignKey(
        Projet, on_delete=models.CASCADE, related_name="equipe_projet")
    activite = models.OneToOneField(
        ElementDevis, on_delete=models.CASCADE)
    responsable = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="equipe_responsable")
    ouvrier = models.ManyToManyField(
        Profile, verbose_name=_("Ouvrier de l'équipe"))
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Equipe."""

        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        """Unicode representation of Equipe."""
        return f"{self.projet , self.active, self.responsable}"
