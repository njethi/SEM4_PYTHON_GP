from django.urls import path
from . import views
urlpatterns = [ 
 path('<int:weather_id>', views.detail, 
 name='detail'),
]