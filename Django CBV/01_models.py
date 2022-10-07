from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from main.models import BaseModel


class Unit(BaseModel):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("products:view_unit", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("products:update_unit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("products:delete_unit", kwargs={"pk": self.pk})

    def __str__(self):
        return str(f"{self.code} - {self.name}")


class Product(BaseModel):
    code = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    type = models.CharField(
        max_length=128,
        choices=(("product", "Product"), ("service", "Service")),
        default="product",
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="unit",
        limit_choices_to={"is_deleted": False, "is_active": True},
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = (
            "-date_added",
            "name",
        )

    @property
    def current_stock(self):
        return opening_stock + stock

    def get_absolute_url(self):
        return reverse("products:view_product", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("products:update_product", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("products:delete_product", kwargs={"pk": self.pk})

    def get_unit_url(self):
        return reverse("products:view_unit", kwargs={"pk": self.unit.pk})

    def __str__(self):
        return str(self.name)
