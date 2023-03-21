# Generated by Django 4.1.4 on 2023-03-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PQ', '0008_alter_set_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dateadded',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='set',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='typeset', to='PQ.type', verbose_name='types of questions you look for'),
        ),
        migrations.AlterField(
            model_name='set',
            name='when',
            field=models.ManyToManyField(blank=True, related_name='wheset', to='PQ.when', verbose_name='when you want to use them'),
        ),
        migrations.AlterField(
            model_name='set',
            name='who',
            field=models.ManyToManyField(blank=True, related_name='whoset', to='PQ.who', verbose_name='who you want to ask'),
        ),
        migrations.AlterField(
            model_name='set',
            name='why',
            field=models.ManyToManyField(blank=True, related_name='whyset', to='PQ.why', verbose_name='why you want to ask them'),
        ),
    ]