# Generated by Django 4.1.1 on 2022-09-29 19:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='ogólne', max_length=50, verbose_name='Kategoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name=' '),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Dodaj zdjęcie'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Kliknij powyżej by przeczytać post.', max_length=50, verbose_name='Opisz temat jednym krótkim zdaniem'),
        ),
    ]