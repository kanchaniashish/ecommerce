# Generated by Django 3.2.23 on 2023-12-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('phoneNum', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
