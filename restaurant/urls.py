from django.urls import path

from .views import RestaurantView, MenuView

urlpatterns = [
    path('', RestaurantView.as_view()),
    path('/menu', MenuView.as_view())
]
