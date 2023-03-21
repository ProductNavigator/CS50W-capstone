# Generated by Django 4.1.4 on 2023-03-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PQ', '0018_set_firsttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptext', models.CharField(max_length=10000)),
                ('pdateadded', models.DateTimeField()),
                ('ptype', models.ManyToManyField(blank=True, related_name='proposedtypeq', to='PQ.type')),
                ('pwhen', models.ManyToManyField(blank=True, related_name='proposedwhenq', to='PQ.when')),
                ('pwho', models.ManyToManyField(blank=True, related_name='proposedwhoq', to='PQ.who')),
                ('pwhy', models.ManyToManyField(blank=True, related_name='proposedwhyq', to='PQ.why')),
            ],
        ),
    ]