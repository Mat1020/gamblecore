from django.shortcuts import render

from gameplay.logic.SlotMachines import classic_slot_machine, bucks_slot_machine, tryhard_slot_machine
from gameplay.logic.RouletteWheels import french_roulette_wheel, american_roulette_wheel, european_roulette_wheel
from gameplay.logic.PokerVariants import texas_holdem, omaha_hi, seven_card_stud, cantredraw

# Create your views here.

# ================================================================================
# Slot Machines
# ================================================================================
def play_classic_slot_machine(request):
    if request.method == "POST":
        slot = classic_slot_machine()
        result = slot.main()
        return render(request, "gameplay/classic_slot_machine.html", {"result": result})
    return render(request, "gameplay/classic_slot_machine.html")

def play_bucks_slot_machine(request):
    if request.method == "POST":
        slot = bucks_slot_machine()
        result = slot.main()
        return render(request, "gameplay/bucks_slot_machine.html", {"result": result})
    return render(request, "gameplay/bucks_slot_machine.html")

def play_tryhard_slot_machine(request):
    if request.method == "POST":
        slot = tryhard_slot_machine()
        result = slot.main()
        return render(request, "gameplay/tryhard_slot_machine.html", {"result": result})
    return render(request, "gameplay/tryhard_slot_machine.html")
# ================================================================================
# Roulette Wheels
# ================================================================================
def play_french_roulette_wheel(request):
    if request.method == "POST":
        slot = french_roulette_wheel()
        result = slot.main()
        return render(request, "gameplay/french_roulette_wheel.html", {"result": result})
    return render(request, "gameplay/french_roulette_wheel.html")

def play_american_roulette_wheel(request):
    if request.method == "POST":
        slot = american_roulette_wheel()
        result = slot.main()
        return render(request, "gameplay/american_roulette_wheel.html", {"result": result})
    return render(request, "gameplay/american_roulette_wheel.html")

def play_european_roulette_wheel(request):
    if request.method == "POST":
        slot = european_roulette_wheel()
        result = slot.main()
        return render(request, "gameplay/european_roulette_wheel.html", {"result": result})
    return render(request, "gameplay/european_roulette_wheel.html")
# ================================================================================
# Poker Variants
# ================================================================================
def play_texas_holdem(request):
    if request.method == "POST":
        slot = texas_holdem()
        result = slot.main()
        return render(request, "gameplay/texas_holdem.html", {"result": result})
    return render(request, "gameplay/texas_holdem.html")

def play_omaha_hi(request):
    if request.method == "POST":
        slot = omaha_hi()
        result = slot.main()
        return render(request, "gameplay/omaha_hi.html", {"result": result})
    return render(request, "gameplay/omaha_hi.html")

def play_seven_card_stud(request):
    if request.method == "POST":
        slot = seven_card_stud()
        result = slot.main()
        return render(request, "gameplay/seven_card_stud.html", {"result": result})
    return render(request, "gameplay/seven_card_stud.html")

def play_cantredraw(request):
    if request.method == "POST":
        slot = cantredraw()
        result = slot.main()
        return render(request, "gameplay/cantredraw.html", {"result": result})
    return render(request, "gameplay/cantredraw.html")