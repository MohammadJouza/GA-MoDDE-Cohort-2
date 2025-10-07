from django import forms
from .models import Feeding


class FeedingForm(forms.ModelForm):
    # control room/class
    class Meta:
        model = Feeding
        fields = ["date", "meal"]
        # Many of the attributes in the Meta class are in common with CBVs because the CBV was using them behind the scenes to create a ModelForm as previously mentioned.
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "SELECT A DATE", "type": "date"},
            ),
        }
