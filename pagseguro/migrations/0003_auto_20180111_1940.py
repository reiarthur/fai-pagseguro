# Generated by Django 2.0.1 on 2018-01-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagseguro', '0002_auto_20150506_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='date',
            field=models.DateTimeField(help_text='Data em que o checkout foi realizado.', verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='message',
            field=models.TextField(blank=True, help_text='Mensagem apresentada no caso de erro no checkout.', verbose_name='Mensagem de erro'),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='date',
            field=models.DateTimeField(verbose_name='Data'),
        ),
    ]