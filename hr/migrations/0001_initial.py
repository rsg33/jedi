# Generated by Django 3.0.2 on 2020-01-30 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet', models.CharField(max_length=25, verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Планета',
                'verbose_name_plural': 'Планеты',
                'ordering': ('planet',),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=50, verbose_name='Вопрос')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Jedi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_j', models.CharField(max_length=20, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Planet', verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Джедай',
                'verbose_name_plural': 'Джедаи',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_c', models.CharField(max_length=25, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('status_padavan', models.BooleanField(default=False, verbose_name='Падаван')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Planet', verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
                'ordering': ('-created',),
            },
        ),
    ]
