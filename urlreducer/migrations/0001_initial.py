# Generated by Django 3.1.3 on 2021-09-20 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redirect_url', models.TextField()),
                ('encoded_url', models.TextField()),
                ('issued_to', models.TextField()),
                ('added_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'url_registry',
            },
        ),
    ]