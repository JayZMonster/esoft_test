from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('hand/', views.HandInput.as_view(), name='hand'),
    path('import/', views.ImportInput.as_view(), name='import'),
]
