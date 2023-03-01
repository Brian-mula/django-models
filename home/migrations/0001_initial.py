# Generated by Django 4.1.7 on 2023-03-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creater', models.CharField(default='Mulati brian', max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
    ]