# Generated by Django 4.0.4 on 2022-04-24 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('price', models.IntegerField(verbose_name='金額')),
                ('description', models.TextField(blank=True, null=True, verbose_name='概要')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.paymentcategory', verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('price', models.IntegerField(verbose_name='金額')),
                ('description', models.TextField(blank=True, null=True, verbose_name='概要')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.incomecategory', verbose_name='カテゴリ')),
            ],
        ),
    ]