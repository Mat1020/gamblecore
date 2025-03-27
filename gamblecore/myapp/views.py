from django.shortcuts import render

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