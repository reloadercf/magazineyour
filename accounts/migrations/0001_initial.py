# Generated by Django 2.1.3 on 2018-11-14 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('correo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
                ('revista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revista.Revista')),
            ],
        ),
    ]
