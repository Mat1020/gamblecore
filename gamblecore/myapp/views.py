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
    today = datetime.datetime.today() # 0 = Monday, 6 = Sunday
    weekday = today.weekday() 
    
    if weekday < 5:
        return render(request, "Version/index1.html")
    else:
        saturday = today - datetime.timedelta(days=(weekday - 5))
        sunday = today - datetime.timedelta(days=(weekday - 6))

        saturday_date = saturday.strftime("%B %d") # Month + Day
        sunday_date = sunday.strftime("%d") # Day

        return render(request, "Version/index2.html", {
            "saturday_date": saturday_date,
            "sunday_date": sunday_date
        })
    
    # if today < 5:
    #     template_name = "Version/index1.html"  # Weekday
    # else:
    #     template_name = "Version/index2.html"  # Weekend

    # return render(request, "Version/index2.html")
