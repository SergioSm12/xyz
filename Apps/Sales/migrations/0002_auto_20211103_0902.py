# Generated by Django 3.2.9 on 2021-11-03 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='fk_id_person_cashier',
        ),
        migrations.AddField(
            model_name='ticket',
            name='fk_id_person_customer',
            field=models.ForeignKey(db_column='fk_id_person_customer', null=True, on_delete=django.db.models.deletion.CASCADE, to='Sales.person'),
        ),
    ]
