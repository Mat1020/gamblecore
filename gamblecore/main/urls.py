from django.urls import path
from . import views

urlpatterns = [
    path('', views.version, name='version'),
    path('about/', views.about, name='about'),
    path('manual/', views.manual, name='manual'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('policy/privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('policy/terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('our_pet/', views.our_pet, name='our_pet'),
]
