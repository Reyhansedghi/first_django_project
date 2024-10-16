# Generated by Django 5.0.7 on 2024-09-24 17:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('slug', models.SlugField(null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.IntegerField(null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='products.productscategory')),
            ],
            options={
                'verbose_name': 'دسته بندی کالا',
                'verbose_name_plural': 'دسته بندی های کالا ',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userstatus', models.CharField(choices=[('demander', 'تقاضا کننده'), ('supplier', 'رضه کننده')], default='demander', max_length=50)),
                ('title', models.CharField(max_length=30, null=True, verbose_name='نام کالا')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='تصویر')),
                ('slug', models.SlugField(allow_unicode=True, null=True)),
                ('consumed', models.CharField(max_length=8000, null=True, verbose_name='مورد مصرف')),
                ('description', models.TextField(null=True, verbose_name='معرفی کالا')),
                ('constituents', models.CharField(max_length=8000, null=True, verbose_name='اهم اجزای تشکیل دهنده')),
                ('analytical_material', models.CharField(max_length=8000, null=True, verbose_name='مواد آنالیز')),
                ('color', models.CharField(blank=True, choices=[('white', 'سفید'), ('yellow', 'زرد'), ('orange', 'نارنجی'), ('red', 'قرمز'), ('pink', 'صورتی'), ('purple', 'بنفش'), ('blue', 'آبی'), ('green', 'سبز'), ('brown', 'قهوه ای'), ('black', 'مشکی'), ('gray', 'طوسی'), ('golden', 'طلایی'), ('silver', 'نقره ای')], max_length=50, null=True, verbose_name='رنگ')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='تعداد')),
                ('capacity', models.CharField(blank=True, max_length=50, null=True, verbose_name='ظرفیت')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='قیمت')),
                ('manufacturers', models.CharField(max_length=5000, null=True, verbose_name='تولیدکنندگان')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_products', to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری')),
                ('category', models.ManyToManyField(blank=True, to='products.productscategory', verbose_name='دسته بندی کالا')),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالا ها',
            },
        ),
    ]
