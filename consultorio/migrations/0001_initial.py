# Generated by Django 3.1.3 on 2020-12-17 02:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=180)),
                ('dosis', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('fechanacimiento', models.DateTimeField(blank=True)),
                ('direccion', models.CharField(max_length=180)),
                ('telefono', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creado')),
                ('sintomas', models.TextField()),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicamentos', to='consultorio.medicamento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='consultorio.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True)),
                ('estado', models.CharField(blank=True, max_length=10, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='consultorio.paciente')),
            ],
        ),
    ]