from django.urls import path
from . import views
urlpatterns = [
        path('api/kidney_data',views.kidney_data),

]