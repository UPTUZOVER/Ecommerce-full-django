# Generated by Django 5.0.6 on 2024-06-21 09:35

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_main",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="Asosiy rasmi",
                    ),
                ),
                (
                    "count",
                    models.IntegerField(null=True, verbose_name="Maxulot miqdori"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="Maxulot narxi",
                    ),
                ),
                (
                    "discount",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="chegirmna"
                    ),
                ),
                (
                    "true_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="oxirgi narx",
                    ),
                ),
                (
                    "img1",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="Birinchi rasm",
                    ),
                ),
                (
                    "img2",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="Ikkinchi rasm",
                    ),
                ),
                (
                    "img3",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="Uchinchi rasm",
                    ),
                ),
                (
                    "updated_on",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Yangilangan sana"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Yaratilgan sana"
                    ),
                ),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="categories.category",
                        verbose_name="Turkum",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
                "ordering": ["-created_on"],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="ProductTranslation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200, unique=True, verbose_name="Mahsul nomi"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Mahsul tavsifi"),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Translation",
                "db_table": "products_product_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
