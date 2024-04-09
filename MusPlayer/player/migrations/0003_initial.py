# Generated by Django 5.0.3 on 2024-04-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0002_delete_album_delete_music_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImageAlbum', models.ImageField(upload_to='')),
                ('DateReleased', models.DateField()),
                ('MusicID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url', models.URLField()),
                ('Autor', models.CharField(max_length=250)),
                ('Album', models.CharField(max_length=250)),
                ('Duration', models.IntegerField()),
                ('DateReleased', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=150)),
                ('LastName', models.CharField(max_length=150)),
                ('Login', models.CharField(max_length=250)),
                ('Password', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('DateBirth', models.DateField()),
            ],
        ),
    ]