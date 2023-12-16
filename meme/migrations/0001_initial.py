# Generated by Django 4.2.7 on 2023-12-16 08:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemeDetail',
            fields=[
                ('meme_detail_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.content')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('meme_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meme_content_1', to='content.content')),
                ('content_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meme_content_2', to='content.content')),
                ('primary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary', to='meme.memedetail')),
                ('secondary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondary', to='meme.memedetail')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]