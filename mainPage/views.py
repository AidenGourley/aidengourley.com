from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def index(request):
    context = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "PERSONAL WEBSITE: " + request.POST["subject"]
            header = "Sent By: " + request.POST["name"] + "\n" + "Email Address: " + request.POST["emailAddress"] + "\n"
            message = header + request.POST["message"]
            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      ["aiden@aidengourley.com"],
                      fail_silently=False
                      )
            context = {"emailSentMessage": "Success! I'll get back to you soon!", "goToContactForm":True}
        else:
            context = {"emailErrorMessage": "Oh no! One or more of the contact fields were invalid. Please try again!", "goToContactForm":True}
    return render(request, 'mainPage/index.html', context)


def robots(request):
    data = {}
    return render(request, 'mainPage/robots.txt', data, content_type='text/plain')


def sitemap(request):
    data = {}
    return render(request, 'mainPage/sitemap.xml', data, content_type='text/xml')

#def resume(request):
#    data = {}
#    return render(request, 'mainPage/other/AidenGourleyResume.pdf', data, content_type='application/pdf')
