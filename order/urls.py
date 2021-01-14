from django.urls import path

from order.views import CartView, EditCartView, CleanCartView

urlpatterns = [
    path('', CartView.as_view()),
    path('<int:pk>', EditCartView.as_view()),
    path('clean/<int:pk>', CleanCartView.as_view()),
]
