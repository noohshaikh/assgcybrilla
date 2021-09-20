from django.urls import path
from . import views

urlpatterns = [
    path('encoder', views.get_encoder_page),
    path('encode', views.get_encoded_url),
    path('decode/<int:userId>/<str:encodedUrl>', views.decode_url_and_redirect)
]