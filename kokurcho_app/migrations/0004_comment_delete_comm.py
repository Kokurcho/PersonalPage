# Generated by Django 4.0.4 on 2022-06-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokurcho_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('contents', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='comm',
        ),
    ]