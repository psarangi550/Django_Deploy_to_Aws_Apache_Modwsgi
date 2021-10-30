from django.urls import path
from .import views
app_name="apache2"
urlpatterns = [
    path('', views.index_view)
]
