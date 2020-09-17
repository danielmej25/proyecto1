# Generated by Django 2.2.3 on 2020-09-15 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actividad',
            fields=[
                ('idActividad', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('idEstudiante', models.PositiveIntegerField()),
                ('descripcion', models.CharField(max_length=50)),
                ('justificante', models.FileField(blank=True, null=True, upload_to='b_activities_app/archivos')),
                ('estado', models.CharField(max_length=20)),
                ('fechaInicio', models.DateTimeField()),
                ('fechaFin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='curso',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.actividad')),
                ('programa', models.CharField(max_length=50)),
                ('horasAsignadas', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
            bases=('b_activities_app.actividad',),
        ),
        migrations.CreateModel(
            name='estanciaInvestigacion',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.actividad')),
                ('proposito', models.CharField(max_length=50)),
                ('institucion', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Estancia  de  investigación',
                'verbose_name_plural': 'Estancias  de  investigación',
            },
            bases=('b_activities_app.actividad',),
        ),
        migrations.CreateModel(
            name='exposicionResultados',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.actividad')),
                ('modalidad', models.CharField(max_length=50)),
                ('duracion', models.PositiveIntegerField()),
                ('lugar', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Exposición de resultados',
                'verbose_name_plural': 'Exposición de resultados',
            },
            bases=('b_activities_app.actividad',),
        ),
        migrations.CreateModel(
            name='parcipacionProyecto',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.actividad')),
                ('nombreInvestigador', models.CharField(max_length=50)),
                ('informacionVRI', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Participación  en  proyecto',
                'verbose_name_plural': 'Participación  en  proyectos',
            },
            bases=('b_activities_app.actividad',),
        ),
        migrations.CreateModel(
            name='ponenciaCongreso',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.actividad')),
                ('entidadOrganizadora', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'ponencia en congreso',
                'verbose_name_plural': 'ponencias en congresos',
            },
            bases=('b_activities_app.actividad',),
        ),
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('actividad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='b_activities_app.actividad')),
                ('tipo', models.CharField(max_length=50)),
                ('autores', models.CharField(max_length=50)),
                ('datosGenerales', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
            bases=('b_activities_app.actividad',),
        ),
    ]
