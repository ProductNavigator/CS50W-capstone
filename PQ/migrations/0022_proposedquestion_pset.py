# Generated by Django 4.1.4 on 2023-03-19 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PQ', '0021_remove_proposedquestion_ptype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposedquestion',
            name='pset',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposedsetq', to='PQ.set'),
            preserve_default=False,
        ),
    ]
