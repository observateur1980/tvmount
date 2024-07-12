from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='homepage'),
    path('send-email/', views.send_get_quote_email, name='send-email'),
    path('send-get-phone-number/', views.send_phone_number_email, name='send-contact-email'),
]