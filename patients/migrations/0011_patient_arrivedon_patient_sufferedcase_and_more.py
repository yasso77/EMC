# Generated by Django 5.0.4 on 2024-05-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_alter_patient_options_patient_age_patient_remarks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='arrivedOn',
            field=models.CharField(blank=True, db_column='ArrivedOn', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='sufferedcase',
            field=models.CharField(blank=True, db_column='SufferedCase', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='createdby',
            field=models.CharField(blank=True, db_column='CreatedBy', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='remarks',
            field=models.CharField(blank=True, db_column='Remarks', max_length=2055, null=True),
        ),
    ]
