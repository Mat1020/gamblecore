from django.urls import path
from . import views

urlpatterns = [
    # Slot Machines
    path("classic_slot_machine/", views.play_classic_slot_machine, name="play_classic_slot_machine"),
    path("bucks_slot_machine/", views.play_bucks_slot_machine, name="play_bucks_slot_machine"),
    path("tryhard_slot_machine/", views.play_tryhard_slot_machine, name="play_tryhard_slot_machine"),

    # Roulette Wheels
    path("french_roulette_wheel/", views.play_french_roulette_wheel, name="play_french_roulette_wheel"),
    path("american_roulette_wheel/", views.play_american_roulette_wheel, name="play_american_roulette_wheel"),
    path("european_roulette_wheel/", views.play_european_roulette_wheel, name="play_european_roulette_wheel"),

    # Poker Variants
    path("texas_holdem/", views.play_texas_holdem, name="play_texas_holdem"),
    path("omaha_hi/", views.play_omaha_hi, name="play_omaha_hi"),
    path("seven_card_stud/", views.play_seven_card_stud, name="play_seven_card_stud"),
    path("cantredraw/", views.play_cantredraw, name="play_cantredraw"),
]