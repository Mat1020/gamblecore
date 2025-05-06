from django.shortcuts import render
from django.http import JsonResponse

from gameplay.logic.SlotMachines import classic_slot_machine, bucks_slot_machine, tryhard_slot_machine
from gameplay.logic.RouletteWheels import french_roulette_wheel, american_roulette_wheel, european_roulette_wheel
from gameplay.logic.PokerVariants import texas_holdem, omaha_hi, seven_card_stud, cantredraw

# Create your views here.
# ================================================================================
# Slot Machines
# ================================================================================

def play_classic_slot_machine(request):
    if request.method == "POST" and request.is_ajax():
        stats = classic_slot_machine.main()
        return JsonResponse(stats) 
    return render(request, "gameplay/classic_slot_machine.html")

# def play_classic_slot_machine(request):
#     if request.method == "POST":
#         stats = classic_slot_machine.main()
#         return render(request, "gameplay/classic_slot_machine.html", {"stats": stats})
#     return render(request, "gameplay/classic_slot_machine.html")

def play_bucks_slot_machine(request):
    if request.method == "POST":
        stats = bucks_slot_machine.main()
        return render(request, "gameplay/bucks_slot_machine.html", {"stats": stats})
    return render(request, "gameplay/bucks_slot_machine.html")

def play_tryhard_slot_machine(request):
    if request.method == "POST":
        stats = tryhard_slot_machine.main()
        return render(request, "gameplay/tryhard_slot_machine.html", {"stats": stats})
    return render(request, "gameplay/tryhard_slot_machine.html")

# ================================================================================
# Roulette Wheels
# ================================================================================
def play_french_roulette_wheel(request):
    if request.method == "POST":
        stats = french_roulette_wheel.main()
        return render(request, "gameplay/french_roulette_wheel.html", {"stats": stats})
    return render(request, "gameplay/french_roulette_wheel.html")

def play_american_roulette_wheel(request):
    if request.method == "POST":
        stats = american_roulette_wheel.main()
        return render(request, "gameplay/american_roulette_wheel.html", {"stats": stats})
    return render(request, "gameplay/american_roulette_wheel.html")

def play_european_roulette_wheel(request):
    if request.method == "POST":
        stats = european_roulette_wheel.main()
        return render(request, "gameplay/european_roulette_wheel.html", {"stats": stats})
    return render(request, "gameplay/european_roulette_wheel.html")

# ================================================================================
# Poker Variants
# ================================================================================
def play_texas_holdem(request):
    if request.method == "POST":
        stats = texas_holdem.main()
        return render(request, "gameplay/texas_holdem.html", {"stats": stats})
    return render(request, "gameplay/texas_holdem.html")

def play_omaha_hi(request):
    if request.method == "POST":
        stats = omaha_hi.main()
        return render(request, "gameplay/omaha_hi.html", {"stats": stats})
    return render(request, "gameplay/omaha_hi.html")

def play_seven_card_stud(request):
    if request.method == "POST":
        stats = seven_card_stud.main()
        return render(request, "gameplay/seven_card_stud.html", {"stats": stats})
    return render(request, "gameplay/seven_card_stud.html")

def play_cantredraw(request):
    if request.method == "POST":
        stats = cantredraw.main()
        return render(request, "gameplay/cantredraw.html", {"stats": stats})
    return render(request, "gameplay/cantredraw.html")