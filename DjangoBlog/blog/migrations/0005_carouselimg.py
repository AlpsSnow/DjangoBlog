# Generated by Django 2.2.7 on 2019-12-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191108_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('image', models.ImageField(upload_to='carousel_pics', verbose_name='图片')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
    ]