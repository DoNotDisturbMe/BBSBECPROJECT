# Generated by Django 4.1.6 on 2023-03-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annoucements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='media/accoucements')),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
