from django.shortcuts import render
from version.utils import version

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def manual(request):
    return render(request, 'manual.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def privacy_policy(request):
    return render(request, 'Policy/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'Policy/terms_of_service.html')

def our_pet(request):
    return render(request, 'our_pet.html')

# Version changing
def homepage(request):
    current_version = version()
    if current_version["weekday"]:
        return render(request, "main/index1.html", version)
    else:
        return render(request, "main/index2.html", version)