from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Projet, DevisProjet

@receiver(post_save, sender=Projet)
def create_devis(sender, instance, created, **kwargs):
    if created:
        DevisProjet.objects.create(projet=instance)
