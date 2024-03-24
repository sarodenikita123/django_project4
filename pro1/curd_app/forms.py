from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "from-control"}),
            "phone_number": forms.NumberInput(),
            "booking_date_time": forms.DateInput(),
            "ticket_type": forms.RadioSelect()
        }

