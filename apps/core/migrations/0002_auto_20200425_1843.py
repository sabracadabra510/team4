# Generated by Django 3.0.5 on 2020-04-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='donationrequest',
            name='library',
            field=models.CharField(default='Null', max_length=50),
            preserve_default=False,
        ),
    ]