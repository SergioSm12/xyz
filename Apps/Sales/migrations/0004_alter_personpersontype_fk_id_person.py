# Generated by Django 3.2.8 on 2021-11-19 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0003_auto_20211103_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpersontype',
            name='fk_id_person',
            field=models.ForeignKey(db_column='fk_id_person', on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='Sales.person'),
        ),
    ]
