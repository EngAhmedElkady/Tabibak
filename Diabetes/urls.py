from django.urls import path
from . import views
urlpatterns = [
        path('api/Diabetes_data',views.Diabetes_data),

]