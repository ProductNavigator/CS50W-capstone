# Generated by Django 4.1.4 on 2023-03-19 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PQ', '0020_proposedquestion_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposedquestion',
            name='ptype',
        ),
        migrations.RemoveField(
            model_name='proposedquestion',
            name='pwhen',
        ),
        migrations.RemoveField(
            model_name='proposedquestion',
            name='pwho',
        ),
        migrations.RemoveField(
            model_name='proposedquestion',
            name='pwhy',
        ),
        migrations.AddField(
            model_name='proposedquestion',
            name='ptype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposedtypeq', to='PQ.type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposedquestion',
            name='pwhen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposedwhenq', to='PQ.when'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposedquestion',
            name='pwho',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposedwhoq', to='PQ.who'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposedquestion',
            name='pwhy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposedwhyq', to='PQ.why'),
            preserve_default=False,
        ),
    ]
