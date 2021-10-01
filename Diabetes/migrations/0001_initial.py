# Generated by Django 3.2.7 on 2021-10-01 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diabets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.DecimalField(decimal_places=2, max_digits=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Pregnancies', models.IntegerField()),
                ('Glucose', models.IntegerField()),
                ('SkinThickness', models.IntegerField()),
                ('Insulin', models.IntegerField()),
                ('result', models.IntegerField(blank=True, default=0, null=True)),
                ('result2', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
