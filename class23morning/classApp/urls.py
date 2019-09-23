from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('music/',views.music),
    path('music/lukas/',views.lukas),
    path('music/script/',views.script),
    path('music/mack/',views.mack),
]