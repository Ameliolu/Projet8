# Generated by Django 2.2.5 on 2019-12-12 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name_fr', models.CharField(max_length=255)),
                ('nutrition_grade_fr', models.CharField(max_length=1)),
                ('url_product', models.CharField(max_length=255)),
                ('brands', models.CharField(max_length=255)),
                ('image_front_url', models.CharField(max_length=255)),
                ('salt', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_web.Category')),
            ],
        ),
    ]
