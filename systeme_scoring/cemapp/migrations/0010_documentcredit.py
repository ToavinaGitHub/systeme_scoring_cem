# Generated by Django 5.1.3 on 2024-11-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cemapp', '0009_remove_client_matricule'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_document', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('client_status', models.CharField(choices=[('Nouveau', 'Nouveau Client'), ('Ancien', 'Ancien Client')], max_length=50)),
            ],
        ),
    ]