from django.contrib import admin
from apps.subscription.models import Subscriber, Subscription


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
