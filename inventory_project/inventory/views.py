# inventory/views.py

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import InventoryItem
from .forms import InventoryItemForm


# ── READ: List all items ─────────────────────────────────
class ItemListView(LoginRequiredMixin, ListView):
    model               = InventoryItem
    template_name       = 'inventory/item_list.html'
    context_object_name = 'items'
    paginate_by         = 5

    def get_queryset(self):
        qs    = super().get_queryset().filter(is_active=True)
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        context          = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


# ── READ: Single item detail ─────────────────────────────
class ItemDetailView(LoginRequiredMixin, DetailView):
    model               = InventoryItem
    template_name       = 'inventory/item_detail.html'
    context_object_name = 'item'


# ── CREATE: Add new item ─────────────────────────────────
class ItemCreateView(LoginRequiredMixin, CreateView):
    model         = InventoryItem
    form_class    = InventoryItemForm
    template_name = 'inventory/item_form.html'
    success_url   = reverse_lazy('inventory:list')

    def form_valid(self, form):
        messages.success(
            self.request, '✅ Item created successfully!'
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context          = super().get_context_data(**kwargs)
        context['title'] = 'Add New Item'
        return context


# ── UPDATE: Edit existing item ───────────────────────────
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model         = InventoryItem
    form_class    = InventoryItemForm
    template_name = 'inventory/item_form.html'
    success_url   = reverse_lazy('inventory:list')

    def form_valid(self, form):
        messages.success(
            self.request, '✏️ Item updated successfully!'
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context          = super().get_context_data(**kwargs)
        context['title'] = f'Edit: {self.object.name}'
        return context


# ── DELETE: Remove item ──────────────────────────────────
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model               = InventoryItem
    template_name       = 'inventory/item_confirm_delete.html'
    context_object_name = 'item'
    success_url         = reverse_lazy('inventory:list')

    def post(self, request, *args, **kwargs):
        messages.warning(
            request, '🗑️ Item deleted successfully.'
        )
        return super().post(request, *args, **kwargs)