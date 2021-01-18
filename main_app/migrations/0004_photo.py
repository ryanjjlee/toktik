# Generated by Django 3.1 on 2021-01-16 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210116_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.member')),
            ],
        ),
    ]