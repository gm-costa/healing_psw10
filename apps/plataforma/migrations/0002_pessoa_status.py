# Generated by Django 5.0.4 on 2024-05-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='status',
            field=models.CharField(choices=[('A', 'Aprovado'), ('R', 'Reprovado'), ('S', 'Solicitado')], default='S', max_length=1),
        ),
    ]
