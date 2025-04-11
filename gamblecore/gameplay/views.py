from django.shortcuts import render
# ================================================================================
# Slot Machines
# ================================================================================
from gameplay.logic.SlotMachines.classic_slot_machine import ClassicSlotMachine
from gameplay.logic.SlotMachines.bucks_slot_machine import BucksSlotMachine
from gameplay.logic.SlotMachines.tryhard_slot_machine import TryhardSlotMachine
# ================================================================================
# Roulette Wheels
# ================================================================================
from gameplay.logic.RouletteWheels.french_roulette_wheel import FrenchRouletteWheel
from gameplay.logic.RouletteWheels.american_roulette_wheel import AmericanRouletteWheel
from gameplay.logic.RouletteWheels.european_roulette_wheel import EuropeanRouletteWheel
# ================================================================================
# Poker Variants
# ================================================================================
from gameplay.logic.PokerVariants.texas_holdem import TexasHoldem
from gameplay.logic.PokerVariants.omaha_hi import OmahaHi
from gameplay.logic.PokerVariants.seven_card_stud import SevenCardStud
from gameplay.logic.PokerVariants.cantredraw import Cantredraw

# Create your views here.
def play_classic_slot_machine(request):
    if request.method == "POST":
        slot = ClassicSlotMachine()
        result = slot.main()
        return render(request, "gameplay/classic_slot_machine.html", {"result": result})
    return render(request, "gameplay/classic_slot_machine.html")

def play_bucks_slot_machine(request):
    if request.method == "POST":
        slot = BucksSlotMachine()
        result = slot.main()
        return render(request, "gameplay/bucks_slot_machine.html", {"result": result})
    return render(request, "gameplay/bucks_slot_machine.html")

def play_tryhard_slot_machine(request):
    if request.method == "POST":
        slot = ClassicSlotMachine()
        result = slot.main()
        return render(request, "gameplay/tryhard_slot_machine.html", {"result": result})
    return render(request, "gameplay/tryhard_slot_machine.html")

def play_french_roulette_wheel(request):
    if request.method == "POST":
        slot = FrenchRouletteWheel()
        result = slot.main()
        return render(request, "gameplay/french_roulette_wheel.html", {"result": result})
    return render(request, "gameplay/french_roulette_wheel.html")

def play_american_roulette_wheel(request):
    if request.method == "POST":
        slot = AmericanRouletteWheel()
        result = slot.main()
        return render(request, "gameplay/american_roulette_wheel.html", {"result": result})
    return render(request, "gameplay/american_roulette_wheel.html")

def play_european_roulette_wheel(request):
    if request.method == "POST":
        slot = FrenchRouletteWheel()
        result = slot.main()
        return render(request, "gameplay/european_roulette_wheel.html", {"result": result})
    return render(request, "gameplay/european_roulette_wheel.html")

def play_texas_holdem(request):
    if request.method == "POST":
        slot = TexasHoldem()
        result = slot.main()
        return render(request, "gameplay/texas_holdem.html", {"result": result})
    return render(request, "gameplay/texas_holdem.html")

def play_omaha_hi(request):
    if request.method == "POST":
        slot = OmahaHi()
        result = slot.main()
        return render(request, "gameplay/omaha_hi.html", {"result": result})
    return render(request, "gameplay/omaha_hi.html")

def play_seven_card_stud(request):
    if request.method == "POST":
        slot = SevenCardStud()
        result = slot.main()
        return render(request, "gameplay/seven_card_stud.html", {"result": result})
    return render(request, "gameplay/seven_card_stud.html")

def play_cantredraw(request):
    if request.method == "POST":
        slot = Cantredraw()
        result = slot.main()
        return render(request, "gameplay/cantredraw.html", {"result": result})
    return render(request, "gameplay/cantredraw.html")