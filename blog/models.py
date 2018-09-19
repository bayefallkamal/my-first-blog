from django.db import models
from django.utils import timezone

from django.urls import reverse
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   

class Parent(models.Model):

    # Fields
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Numero_Telephone_1 = models.CharField(max_length=18)
    Numero_Telephone_2 = models.CharField(max_length=18)
    Numero_Telephone_3 = models.CharField(max_length=18)
    Adresse = models.CharField(max_length=200)
    Ville = models.CharField(max_length=100)
    Email = models.EmailField()
    Type_Parent = models.CharField(max_length=100)
    Fonction = models.CharField(max_length=100)
    Nationnalite = models.CharField(max_length=100)


    def __unicode__(self):
        return '%s %s' % (self.Prenom, self.Nom)

    def get_absolute_url(self):
        return reverse('daara_khidma_parent_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_parent_update', args=(self.pk,))


class Materiel(models.Model):

    # Fields
    Libelle = models.CharField(max_length=100)
    Type_Materiel = models.CharField(max_length=100)
    Quantite = models.IntegerField()
    Date_entree = models.DateTimeField()


    def __str__(self):
        return self.Libelle  


class Classe(models.Model):

    # Fields
    Nom_Classe = models.CharField(max_length=100)
    Niveau_Classe = models.CharField(max_length=100)


    def __str__(self):
        return self.Nom_Classe  

    def get_absolute_url(self):
        return reverse('daara_khidma_classe_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_classe_update', args=(self.pk,))


class Inscription(models.Model):

    # Fields
    Date_Inscription = models.DateField()
    Type_Inscription = models.CharField(max_length=100)
    Montant = models.FloatField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('daara_khidma_inscription_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_inscription_update', args=(self.pk,))


class Maitre_Coranique(models.Model):

    # Fields
    Prenom = models.CharField(max_length=100)
    Nom = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=100)


    def __unicode__(self):
        return '%s %s' % (self.Prenom, self.Nom)

    def get_absolute_url(self):
        return reverse('daara_khidma_maitre_coranique_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_maitre_coranique_update', args=(self.pk,))


class Matiere(models.Model):

    # Fields
    Nom_Matiere = models.CharField(max_length=255)
    Type_Matiere = models.CharField(max_length=100)



    def __unicode__(self):
        return self.Nom_Matiere

    def get_absolute_url(self):
        return reverse('daara_khidma_matiere_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_matiere_update', args=(self.pk,))





class Eleve(models.Model):

    # Fields
    Photo = models.ImageField()
    Identifiant = models.CharField(max_length=100)
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Date_Naissance = models.DateField()
    Lieu_Naissance = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=100)
    Nationalite = models.CharField(max_length=100)
    Date_Entree = models.DateField()
    Niveau = models.CharField(max_length=100)

    # Relationship Fields
    parents = models.ManyToManyField(Parent)
    maitres = models.ManyToManyField(Maitre_Coranique)
    materiels = models.ManyToManyField(Materiel)
    inscription = models.ForeignKey(Inscription, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('daara_khidma_eleve_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_eleve_update', args=(self.pk,))


class Bulletin(models.Model):

    # Fields
    Anne = models.DateField()
    Commentaires = models.CharField(max_length=100)

    # Relationship Fields
    matieres = models.ManyToManyField(Matiere)
    classe = models.OneToOneField(Classe,on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve,on_delete=models.CASCADE)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('daara_khidma_bulletin_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_bulletin_update', args=(self.pk,))

class Paiement(models.Model):

    # Fields
    Type_Paiement = models.CharField(max_length=100)
    Date_Paiement = models.DateTimeField()
    Mois_Payer = models.DateField()
    Montant = models.FloatField()
    Mode_Reglement = models.CharField(max_length=40)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('daara_khidma_paiement_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('daara_khidma_paiement_update', args=(self.pk,))

