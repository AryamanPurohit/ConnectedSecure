# Generated by Django 5.1.4 on 2025-01-07 12:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_tag_project_vote_ratio_project_vote_total_reviews_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reviews",
            new_name="Review",
        ),
    ]
