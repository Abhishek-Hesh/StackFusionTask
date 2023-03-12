from django.urls import path
from .views import *
app_name = 'registeration'

urlpatterns = [
    path('', registerForm, name='form'),
    path('save/', save, name='save'),
    path('home/', home, name='home'),
    path('jsonresponse/vals', vals, name='vals')
]