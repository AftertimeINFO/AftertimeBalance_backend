# Generated by Django 4.2.4 on 2023-10-26 17:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
                ('moment_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('moment_update', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelShips',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id_mt', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('type', models.IntegerField()),
                ('flag', models.CharField(max_length=2)),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('course', models.IntegerField(null=True)),
                ('heading', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('moment_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('moment_update', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Substances',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('moment_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('moment_update', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelShipLocation',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('moment', models.DateTimeField()),
                ('type_location', models.IntegerField()),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
                ('course', models.IntegerField(null=True)),
                ('heading', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('ship', models.ForeignKey(db_column='uuid_ships', on_delete=django.db.models.deletion.CASCADE, to='core.modelships', verbose_name='uuid_ships')),
            ],
        ),
        migrations.CreateModel(
            name='BalanceSubstances',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('moment', models.DateField(null=True)),
                ('count', models.BigIntegerField()),
                ('moment_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('moment_update', models.DateTimeField(auto_now=True, null=True)),
                ('location', models.ForeignKey(db_column='uuid_locations', on_delete=django.db.models.deletion.CASCADE, to='core.locations', verbose_name='uuid_locations')),
                ('substance', models.ForeignKey(db_column='uuid_substances', on_delete=django.db.models.deletion.CASCADE, to='core.substances', verbose_name='uuid_substances')),
            ],
        ),
    ]
