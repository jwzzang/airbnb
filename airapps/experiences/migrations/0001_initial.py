# Generated by Django 4.2.1 on 2023-05-25 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_alter_category_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('name', models.CharField(max_length=100, verbose_name='특전')),
                ('detail', models.CharField(blank=True, default='', max_length=250, verbose_name='특전종류')),
                ('explanation', models.TextField(blank=True, default='', verbose_name='설명')),
            ],
            options={
                'verbose_name': '체험',
                'verbose_name_plural': '체험 관리',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('name', models.CharField(max_length=200, verbose_name='경험명')),
                ('country', models.CharField(max_length=50, verbose_name='국가')),
                ('city', models.CharField(max_length=100, verbose_name='도시')),
                ('price', models.PositiveIntegerField(verbose_name='가격')),
                ('address', models.CharField(max_length=200, verbose_name='주소')),
                ('start_time', models.TimeField(verbose_name='시작시간')),
                ('end_time', models.TimeField(verbose_name='종료시간')),
                ('description', models.TextField(verbose_name='소개')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiences', to='categories.category', verbose_name='카테고리')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL, verbose_name='호스트')),
                ('perks', models.ManyToManyField(related_name='experiences', to='experiences.perk', verbose_name='특전')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
