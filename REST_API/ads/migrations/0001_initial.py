# Generated by Django 4.0 on 2021-12-09 21:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(db_index=True, max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid format (should be: LL-NNN-LL/NN)', regex='^[a-zA-Z]{2}-[0-9]{3}-[a-zA-Z]{2}/[0-9]{2}$')], verbose_name='Transaction_Number')),
                ('website_url', models.URLField(verbose_name='Website_URL')),
                ('photo_url', models.URLField(verbose_name='Photo_URL')),
                ('start_date', models.DateField(verbose_name='Start_Date')),
                ('end_date', models.DateField(verbose_name='End_Date')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Only letters are allowed in title', regex='^[a-zA-Z]{2,}$')], verbose_name='Title')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0)], verbose_name='Price')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='User')),
            ],
        ),
    ]
