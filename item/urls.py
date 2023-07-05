from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    # Add a slash at the end of the path
    path('<int:pk>/', views.detail, name='detail'),
]
