# Generated by Django 4.2.1 on 2023-05-25 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('name', models.CharField(max_length=150, verbose_name='어메니티 이름')),
                ('description', models.TextField(verbose_name='소개')),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('name', models.CharField(max_length=150, verbose_name='방 이름')),
                ('country', models.CharField(max_length=50, verbose_name='국가')),
                ('city', models.CharField(max_length=100, verbose_name='도시')),
                ('price', models.PositiveIntegerField(verbose_name='가격')),
                ('rooms', models.PositiveIntegerField(verbose_name='방 개수')),
                ('toilets', models.PositiveIntegerField(verbose_name='화장실')),
                ('description', models.TextField(verbose_name='소개')),
                ('address', models.CharField(max_length=200, verbose_name='주소')),
                ('pet_friendly', models.BooleanField(default=True, verbose_name='애견동반')),
                ('kind', models.CharField(choices=[('entire_place', 'Entire Place'), ('private_room', 'Private Room'), ('shared_room', 'Shared Room')], max_length=20, verbose_name='방 종류')),
                ('amenities', models.ManyToManyField(related_name='rooms', to='rooms.amenity', verbose_name='어메니티')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='categories.category', verbose_name='카테고리')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL, verbose_name='주인')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]