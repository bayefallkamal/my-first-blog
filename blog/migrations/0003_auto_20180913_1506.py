# Generated by Django 2.1 on 2018-09-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180913_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='Commentaires',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='classe',
            name='Niveau_Classe',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Adresse',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Date_Entree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Identifiant',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Lieu_Naissance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Nationalite',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Niveau',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='Prenom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='Type_Inscription',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='maitre_coranique',
            name='Adresse',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='maitre_coranique',
            name='Nom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='maitre_coranique',
            name='Telephone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='materiel',
            name='Type_Materiel',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='Type_Matiere',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paiement',
            name='Mode_Reglement',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='paiement',
            name='Type_Paiement',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Adresse',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Fonction',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Nationnalite',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Numero_Telephone_1',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Numero_Telephone_2',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Numero_Telephone_3',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Prenom',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Type_Parent',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parent',
            name='Ville',
            field=models.CharField(max_length=100),
        ),
    ]