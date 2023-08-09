# Generated by Django 4.1.7 on 2023-08-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ScName', models.CharField(max_length=50)),
                ('ScPrincipal', models.CharField(max_length=50)),
                ('ScLocation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=50)),
                ('Sage', models.IntegerField()),
                ('ScName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nvn', to='app.school')),
            ],
        ),
    ]
