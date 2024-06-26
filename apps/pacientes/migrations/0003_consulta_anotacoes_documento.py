# Generated by Django 5.0.4 on 2024-05-04 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_alter_consulta_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='anotacoes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('documento', models.FileField(upload_to='consulta/documentos')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pacientes.consulta')),
            ],
        ),
    ]
