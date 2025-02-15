# Generated by Django 3.2.15 on 2022-11-25 09:26

import django.db.models.deletion
import djangocms_text_ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms_forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailNotificationFormPlugin',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('cms_forms.formplugin',),
        ),
        migrations.CreateModel(
            name='EmailNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('default', 'default')],
                                           help_text='Provides the base theme for the email.',
                                           max_length=200,
                                           verbose_name='theme')),
                ('to_name', models.CharField(blank=True, max_length=200,
                                             verbose_name='to name')),
                ('to_email', models.CharField(blank=True, max_length=200,
                                              verbose_name='to email')),
                ('from_name', models.CharField(blank=True, max_length=200,
                                               verbose_name='from name')),
                ('from_email', models.CharField(blank=True, max_length=200,
                                                verbose_name='from email')),
                ('subject', models.CharField(blank=True, max_length=200,
                                             verbose_name='subject')),
                ('body_text', models.TextField(blank=True,
                                               help_text='used when rendering the email in text only mode.',
                                               verbose_name='email body (txt)')),
                ('body_html',
                 djangocms_text_ckeditor.fields.HTMLField(blank=True,
                                                          help_text='used when rendering the email in html.',
                                                          verbose_name='email body (html)')),
                ('form',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='email_notifications',
                                   to='email_notifications.emailnotificationformplugin')),
                ('to_user', models.ForeignKey(blank=True, limit_choices_to={
                    'is_staff': True}, null=True,
                                              on_delete=django.db.models.deletion.CASCADE,
                                              to=settings.AUTH_USER_MODEL,
                                              verbose_name='to user')),
            ],
            options={
                'verbose_name': 'Email notification',
                'verbose_name_plural': 'Email notifications',
            },
        ),
    ]
