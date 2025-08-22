from django import forms

class ServiceRequestForm(forms.Form):
    full_name = forms.CharField(max_length=150, required=True)
    company_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=30, required=False)

    SERVICE_CHOICES = [
        ("insurance_medicals", "Insurance Medicals"),
        ("occupational_medicals", "Occupational Health Medicals"),
        ("travel_nurses", "Travel Nurses"),
        ("mobile_clinics", "Health & Safety Mobile Clinics"),
    ]
    
    service = forms.ChoiceField(choices=SERVICE_CHOICES, required=True)
