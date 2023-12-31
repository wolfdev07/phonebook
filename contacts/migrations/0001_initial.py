# Generated by Django 4.2.7 on 2023-11-15 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=120)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='contact_photos/')),
                ('birthday', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_type_options', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=255)),
                ('code_country', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=60)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contactmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('exterior_number', models.CharField(max_length=10)),
                ('internal_number', models.CharField(max_length=10)),
                ('neighborhood', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('references', models.TextField()),
                ('contatc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contactmodel')),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contacts.states')),
            ],
        ),
    ]
