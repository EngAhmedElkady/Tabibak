# Generated by Django 3.2.7 on 2021-10-01 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kidney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('age', models.DecimalField(decimal_places=2, max_digits=4)),
                ('al', models.IntegerField()),
                ('su', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bgr', models.IntegerField(verbose_name='blood glucose random')),
                ('bu', models.IntegerField(verbose_name='blood urea')),
                ('sc', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='serum creatinine')),
                ('hemo', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='haemoglobin')),
                ('pcv', models.IntegerField(verbose_name='packed cell volume')),
                ('wc', models.IntegerField(verbose_name='white blood cell count')),
                ('htn', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=100, verbose_name='ypertension')),
                ('result', models.IntegerField(blank=True, default=0, null=True)),
                ('result2', models.CharField(blank=True, default=0, max_length=50, null=True)),
            ],
        ),
    ]
