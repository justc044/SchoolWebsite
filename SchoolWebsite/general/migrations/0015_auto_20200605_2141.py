# Generated by Django 3.0.6 on 2020-06-05 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_course_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membergrade',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.Grade'),
        ),
    ]
