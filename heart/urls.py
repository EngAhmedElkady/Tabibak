from django.urls import path
from . import views
urlpatterns = [
        path('api/heart_data',views.heart_data),

]