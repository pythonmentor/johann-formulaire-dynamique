from django.db import models
from django_extensions.db.fields import AutoSlugField

class CountryManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class Country(models.Model):
    name = models.CharField("nom du pays", max_length=150)
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name="slug du pays")

    objects = CountryManager()

    def natural_key(self):
        return (self.slug,)

    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"

    def __str__(self):
        return self.name


class SupplierManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class Supplier(models.Model):
    name = models.CharField("nom du fournisseur", max_length=150)
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name="slug du fournisseur")
    country = models.ForeignKey("exemple.Country", on_delete=models.SET_NULL, null=True, verbose_name="pays")

    objects = SupplierManager()

    def natural_key(self):
        return (self.slug,)

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"

    def __str__(self):
        return self.name


class BrandManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)

class Brand(models.Model):
    name = models.CharField("nom de la marque", max_length=150)
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name="slug de la marque")
    supplier = models.ForeignKey("exemple.Supplier", on_delete=models.SET_NULL, null=True, verbose_name="fournisseur")

    objects = BrandManager()

    def natural_key(self):
        return (self.slug,)

    class Meta:
        verbose_name = "Marque"
        verbose_name_plural = "Marques"

    def __str__(self):
        return self.name