from django.shortcuts import render
import datetime

# This file is in charge of the Version changing.
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