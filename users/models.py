from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from PIL import Image

sexes = (
        ('Masculin', 'Masculin',),
        ('Feminin', 'Feminin',),
)

class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    nom = models.CharField(max_length=150)
    prenoms = models.CharField(max_length=150)
    email = models.EmailField(unique=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_client = models.BooleanField(_("CLIENT"), default=False, help_text=_(
        "Definie si l'utilisateur est un client"),)
    is_ouvrier = models.BooleanField(_("OUVRIER"), default=False, help_text=_(
        "Definie si l'utilisateur est un ouvrier"),)
    is_responsable = models.BooleanField(_("RESPONSABLE"), default=False, help_text=_(
        "Definie si l'utilisateur est un responsable"),)
    is_admin = models.BooleanField(_("ADMINISTRATEUR"), default=False, help_text=_(
        "Definie si l'utilisateur est un administrateur"),)
    is_staff = models.BooleanField(_("MEMBRE DU STAFF"), default=False, help_text=_(
        "Definie si l'utilisateur est un embre du Staff"),)
    is_active = models.BooleanField(_("ACTIVE"), default=False, help_text=_(
        "Definie si l'utilisateur est active"),)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return "{} {}".format(self.nom, self.prenoms)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

class Domaine(models.Model):
    """Model definition for Domaine."""
    nom = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Domaine."""

        verbose_name = 'Domaine'
        verbose_name_plural = 'Domaines'

    def __str__(self):
        """Unicode representation of Domaine."""
        return f"{self.nom}"

class Profile(models.Model):
    """Model definition for Profile."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(blank=True, max_length=10)
    lieu_de_residence = models.CharField(blank=True, max_length=50)
    sexe = models.CharField(max_length=10, choices=sexes,)
    photo = models.ImageField(upload_to='profiles/photo', default='none.png')
    cout_journalier = models.FloatField(default=0)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return f"{self.user.nom, self.user.prenoms }"

    # TODO: Define custom methods here
