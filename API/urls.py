from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
<<<<<<< Updated upstream
<<<<<<< Updated upstream
 
 #path('match/<int:pk>', views.matchList),
 path('match/<HomeTeam>/<AwayTeam>/', views.searchMatch),
 
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

 path('match/<HomeTeam>/<AwayTeam>/', views.searchMatch),
 

]





