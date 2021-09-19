# Generated by Django 3.2.6 on 2021-09-19 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='post_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram_App.posts'),
        ),
        migrations.AlterField(
            model_name='instauser',
            name='user_detail',
            field=models.CharField(max_length=100),
        ),
    ]