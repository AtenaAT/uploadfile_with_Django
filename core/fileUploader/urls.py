
from django.urls import path, include



urlpatterns = [

    path('api/', include('fileUploader.api.urls')),

] 