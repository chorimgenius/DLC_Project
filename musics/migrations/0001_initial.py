# Generated by Django 4.1.3 on 2022-11-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review', '0002_remove_review_name_review_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('artists', models.CharField(max_length=50)),
                ('music_image', models.ImageField(default='', max_length=255, null=True, upload_to='')),
                ('likes', models.ManyToManyField(related_name='like_music', to='review.review')),
            ],
        ),
    ]
