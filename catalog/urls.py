from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index, name='index'),
    path('', views.FoodListView.as_view(), name='catalog'),
    path('food/<int:pk>', views.FoodDetailView.as_view(), name='food-detail'),
    path('about', views.about, name='about'),
]
