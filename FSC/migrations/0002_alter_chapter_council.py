# Generated by Django 5.1.1 on 2024-12-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='council',
            field=models.CharField(choices=[('Interfraternity Council', 'Interfraternity Council'), ('Panhellenic Council', 'Panhellenic Council'), ('Multicultural Sorority and Fraternity Council', 'Multicultural Sorority and Fraternity Council'), ('Professional Fraternities & Sororities', 'Professional Fraternities & Sororities')], max_length=100),
        ),
    ]
