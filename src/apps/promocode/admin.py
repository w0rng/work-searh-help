from django.contrib import admin
from apps.promocode.models import Promocode, Activation


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'max_activations', 'count_activations')


@admin.register(Activation)
class ActivationAdmin(admin.ModelAdmin):
    pass
