# Generated by Django 4.2.1 on 2023-05-25 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('name', models.CharField(max_length=50, verbose_name='카테고리')),
                ('kind', models.CharField(choices=[('rooms', 'Rooms'), ('experiences', 'Experiences')], max_length=20, verbose_name='카테고리 종류')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]