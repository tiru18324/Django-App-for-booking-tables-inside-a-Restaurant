# Generated by Django 3.1.5 on 2021-02-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinmond', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fooditemsss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pic')),
                ('price', models.IntegerField()),
                ('discount', models.BooleanField(default=False)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='fooditems',
        ),
    ]
