# Generated by Django 4.0.4 on 2022-04-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('accNo', models.IntegerField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('regTime', models.DateTimeField(auto_now_add=True)),
                ('issued', models.BooleanField(default=False)),
                ('borrower', models.CharField(blank=True, default='', max_length=200)),
                ('last_issue_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
