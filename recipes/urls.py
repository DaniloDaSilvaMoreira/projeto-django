from django.urls import path
from recipes.views import home1, home2, contato, sobre

urlpatterns = [
    path('', home1),
    path('home/', home2),
    path('contato/', contato),
    path('sobre/', sobre)
]