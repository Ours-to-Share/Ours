# Generated by Django 3.2.5 on 2021-09-03 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_rename_cat_skill_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')], default='B', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.skill')),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessonDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1024)),
                ('banner_img', models.ImageField(upload_to='lessons')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.lesson')),
            ],
        ),
    ]
