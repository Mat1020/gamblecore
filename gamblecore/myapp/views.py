from django.shortcuts import render
import datetime

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

# Version changing
def version(request):
    today = datetime.datetime.today().weekday()  # 0 = Monday, 6 = Sunday
    
    if today < 5:
        template_name = "Version/index1.html"  # Weekday
    else:
        template_name = "Version/index2.html"  # Weekend

    return render(request, template_name)
