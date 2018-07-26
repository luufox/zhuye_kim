# Generated by Django 2.0.6 on 2018-07-17 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20180716_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackGround',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='背景名')),
                ('desc', models.CharField(blank=True, max_length=100, verbose_name='描述')),
                ('image_url', models.ImageField(upload_to='images/BackGround/%Y/%m/%d', verbose_name='图片')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '背景',
                'verbose_name_plural': '背景',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BackGroundCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='背景分类')),
                ('desc', models.CharField(blank=True, max_length=100, verbose_name='描述')),
            ],
            options={
                'verbose_name': '背景分类',
                'verbose_name_plural': '背景分类',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': '大分类', 'verbose_name_plural': '大分类'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['id'], 'verbose_name': '站点', 'verbose_name_plural': '站点'},
        ),
        migrations.AlterModelOptions(
            name='smallcategory',
            options={'ordering': ['id'], 'verbose_name': '小分类', 'verbose_name_plural': '小分类'},
        ),
        migrations.AddField(
            model_name='background',
            name='backgroundcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.BackGroundCategory', verbose_name='小分类'),
        ),
    ]