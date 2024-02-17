# urls.py in timenow app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_time_page, name='show_time_page'),  # To serve the HTML page
    path('update/', views.current_time, name='update_time'),  # For the Ajax call
]
