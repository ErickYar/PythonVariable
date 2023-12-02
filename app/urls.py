from django.urls import path
from app import views
urlpatterns = [
 path('home/',views.home,name='home'),
 path('inicio/',views.inicio,name='inicio'),
 path('index/<str:nombre>',views.index,name='index'),
 path('hincha/<int:num>',views.equipo,name='hincha')
]
