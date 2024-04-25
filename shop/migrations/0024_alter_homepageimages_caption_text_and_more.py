# Generated by Django 4.1.5 on 2023-03-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_alter_homepageimages_caption_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageimages',
            name='caption_text',
            field=models.CharField(blank=True, default='', help_text='Fashion Collections', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homepageimages',
            name='date_text',
            field=models.CharField(blank=True, default='', help_text='Summer 2020', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homepageimages',
            name='description_text',
            field=models.TextField(blank=True, default='', help_text='Lorem ipsum dolor sit amet', null=True),
        ),
    ]
