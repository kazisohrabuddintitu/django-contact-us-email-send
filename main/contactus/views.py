from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Form Submission'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\n\n{form.cleaned_data["message"]}'
            from_email = form.cleaned_data["email"]
            to_email = ['kazisohrab73@gmail.com']
            send_mail(subject, message, from_email, to_email, fail_silently=False)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
