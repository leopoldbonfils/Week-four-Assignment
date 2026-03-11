# inventory/models.py

from django.db import models


# ── MODEL 1: Category ────────────────────────────────────
class Category(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"   # fixes "Categorys" in Admin
        ordering = ['name']


# ── MODEL 2: InventoryItem ───────────────────────────────
class InventoryItem(models.Model):

    # ── Core Fields ──
    name        = models.CharField(max_length=200)
    sku         = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit
    category    = models.ForeignKey(
                    Category,
                    on_delete=models.SET_NULL,  # keep item even if category deleted
                    null=True,
                    blank=True
                  )
    quantity    = models.PositiveIntegerField(default=0)
    unit_price  = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    # ── Status ──
    is_active   = models.BooleanField(default=True)

    # ── Timestamps ──
    created_at  = models.DateTimeField(auto_now_add=True)  # set ONCE on creation
    updated_at  = models.DateTimeField(auto_now=True)      # updated on EVERY save

    # ── String Representation ──
    def __str__(self):
        return f"{self.name} (SKU: {self.sku})"

    # ── Computed Properties (not stored in DB) ──
    @property
    def total_value(self):
        """Total stock value = quantity × unit_price"""
        return self.quantity * self.unit_price

    @property
    def is_low_stock(self):
        """Warn when fewer than 10 units remain"""
        return self.quantity < 10

    @property
    def stock_status(self):
        """Human-readable stock status"""
        if self.quantity == 0:
            return "Out of Stock"
        elif self.quantity < 10:
            return "Low Stock"
        else:
            return "In Stock"

    class Meta:
        ordering     = ['-created_at']   # newest first
        verbose_name = "Inventory Item"