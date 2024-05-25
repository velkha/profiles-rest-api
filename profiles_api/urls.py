from django.urls import path

from profiles_api.endpoints import custom_view

urlpatterns = [
    path('custom-view/', custom_view.CustomView.as_view())
]
