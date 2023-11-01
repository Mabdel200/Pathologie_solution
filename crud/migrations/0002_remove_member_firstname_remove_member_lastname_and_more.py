# Generated by Django 4.1.3 on 2023-11-01 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lastname',
        ),
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='attrite',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='member',
            name='avgOpenToBuy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='avgUtilizationRatio',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='children',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='member',
            name='contactsCount12mon',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='creditLimit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='edu',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='member',
            name='income',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='member',
            name='marital',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='member',
            name='monthOnBooks',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='monthsInactive12mon',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(default='toto', max_length=30),
        ),
        migrations.AddField(
            model_name='member',
            name='totalAmtChngQ4Q1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='totalCtChngQ4Q1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='totalRelationshipCount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='totalRevolvingBal',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='totalTransAmt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='totalTransCt',
            field=models.FloatField(default=0),
        ),
    ]