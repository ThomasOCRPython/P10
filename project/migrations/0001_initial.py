# Generated by Django 4.0.1 on 2022-02-21 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('NO', 'NO'), ('YES', 'YES')], max_length=3)),
                ('role', models.CharField(choices=[('AUTHOR', 'AUTHOR'), ('CONTRIBUTOR', 'CONTRIBUTOR')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('BACKEND', 'Back-end'), ('FRONTEND', 'Front-end'), ('IOS', 'iOS'), ('ANDROID', 'Android')], max_length=9)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('tag', models.CharField(choices=[('BUG', 'BUG'), ('AMELIORATION', 'AMELIORATION'), ('TÂCHE', 'TÂCHE')], max_length=120)),
                ('priority', models.CharField(choices=[('FAIBLE', 'FAIBLE'), ('MOYENNE', 'MOYENNE'), ('ELEVEE', 'ELEVEE')], max_length=120)),
                ('project_id', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('A FAIRE', 'A FAIRE'), ('EN COURS', 'EN COURS'), ('TERMINE', 'TERMINE')], max_length=120)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.contributor')),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.issue')),
            ],
        ),
    ]
