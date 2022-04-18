from django import forms
from apps.subscription.models import Subscription



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ['name', 'price']
