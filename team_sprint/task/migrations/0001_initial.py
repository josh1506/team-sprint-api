# Generated by Django 4.0.10 on 2023-03-18 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
        ('project', '0001_initial'),
        ('sprint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.CharField(blank=True, max_length=255, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('sprint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sprint.sprint')),
            ],
        ),
    ]
