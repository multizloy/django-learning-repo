# Generated by Django 4.2.5 on 2023-10-16 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0002_category_lead_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="organisation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="leads.userprofile",
            ),
        ),
    ]
