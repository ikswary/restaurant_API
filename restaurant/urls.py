from django.urls import path

from .views import RestaurantView, RestaurantListView, MenuView

urlpatterns = [
    path('/list/<int:page>', RestaurantListView.as_view()),
    path('/list', RestaurantListView.as_view()),
    path('/<int:restaurant_id>', RestaurantView.as_view()),
    path('', RestaurantView.as_view()),
    path('/menu', MenuView.as_view())
]
