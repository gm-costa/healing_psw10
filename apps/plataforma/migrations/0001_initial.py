# Generated by Django 5.0.4 on 2024-04-29 16:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=100)),
                ('cnh_rg', models.FileField(upload_to='pessoa/cnh_rg')),
                ('data_nascimento', models.DateField()),
                ('foto', models.ImageField(upload_to='pessoa/foto_perfil')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('is_medico', models.BooleanField(default=False)),
                ('crm', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('data_crm', models.DateField(blank=True, null=True)),
                ('cedula_identidade_medica', models.FileField(blank=True, null=True, upload_to='medico/cim')),
                ('valor_consulta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('especialidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medicos.especialidade')),
            ],
        ),
    ]
