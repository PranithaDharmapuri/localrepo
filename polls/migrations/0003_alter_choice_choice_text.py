# Generated by Django 5.0.6 on 2024-11-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_vote_choice_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
