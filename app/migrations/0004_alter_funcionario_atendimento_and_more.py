# Generated by Django 4.2 on 2023-04-18 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_funcionario_atendimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='atendimento',
            field=models.IntegerField(choices=[(-2, '😡'), (-1, '🙁'), (0, '😐'), (1, '🙂'), (2, '😀')]),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='pontualidade',
            field=models.IntegerField(choices=[(-2, '😡'), (-1, '🙁'), (0, '😐'), (1, '🙂'), (2, '😀')]),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='qualidade',
            field=models.IntegerField(choices=[(-2, '😡'), (-1, '🙁'), (0, '😐'), (1, '🙂'), (2, '😀')]),
        ),
    ]
