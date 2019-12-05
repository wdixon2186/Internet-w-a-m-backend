# Generated by Django 2.2.7 on 2019-11-13 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('logline', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='iwam.Script')),
            ],
        ),
    ]