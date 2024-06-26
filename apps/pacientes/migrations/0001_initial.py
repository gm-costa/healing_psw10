# Generated by Django 5.0.4 on 2024-04-30 20:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Agendada'), ('C', 'Cancelada'), ('I', 'Iniciada'), ('F', 'Finalizada'), ('NC', 'Não compareceu')], default='A', max_length=2)),
                ('link', models.URLField(blank=True, null=True)),
                ('data_aberta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medicos.datasabertas')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
