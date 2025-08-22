from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ServiceRequestForm

def index(request):
    # Just serve the form (empty instance)
    form = ServiceRequestForm()
    context = {
        "page_title": "Ubiquitous Med",
        "form": form,
    }
    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            company_name = form.cleaned_data.get("company_name", "")
            email = form.cleaned_data["email"]
            phone = form.cleaned_data.get("phone_number", "")
            service = form.cleaned_data["service"]

            # Compose email
            subject = f"New Service Inquiry from {full_name}"
            message = (
                f"Full Name: {full_name}\n"
                f"Company: {company_name or 'N/A'}\n"
                f"Email: {email}\n"
                f"Phone: {phone or 'N/A'}\n"
                f"Service: {service}\n"
            )

            # Send email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,     # from
                [settings.EMAIL_HOST_USER],        # to (configure in settings)
                fail_silently=False,
            )

            # Redirect back to index (homepage)
            return redirect("home")

    # If GET or invalid form → redirect to index
    return redirect("home")


def booking(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            company_name = form.cleaned_data.get("company_name", "")
            email = form.cleaned_data["email"]
            phone = form.cleaned_data.get("phone_number", "")
            service = form.cleaned_data["service"]

            # Compose email
            subject = f"New Booking from {full_name}"
            message = (
                f"Full Name: {full_name}\n"
                f"Company: {company_name or 'N/A'}\n"
                f"Email: {email}\n"
                f"Phone: {phone or 'N/A'}\n"
                f"Service: {service}\n"
            )

            # Send email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,     # from
                [settings.EMAIL_BOOKING],        # to (configure in settings)
                fail_silently=False,
            )

            # Redirect back to index (homepage)
            return redirect("home")

    # If GET or invalid form → redirect to index
    return redirect("home")