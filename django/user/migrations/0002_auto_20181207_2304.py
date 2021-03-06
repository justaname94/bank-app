# Generated by Django 2.1.4 on 2018-12-08 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=30)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
            ],
        ),
        migrations.RenameField(
            model_name='securityquestion',
            old_name='user',
            new_name='profile',
        ),
        migrations.AlterUniqueTogether(
            name='securityquestion',
            unique_together={('question', 'profile')},
        ),
    ]
