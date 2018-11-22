# Generated by Django 2.1.3 on 2018-11-22 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_revista', models.CharField(max_length=80)),
                ('logo', models.ImageField(upload_to='logos_revistas')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='categorias',
            name='revista_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revista.Revista'),
        ),
    ]
