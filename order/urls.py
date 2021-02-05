from django.urls import path

from order.views import CartView, EditCartView, CleanCartView

urlpatterns = [
    path('<int:pk>', CartView.as_view()),
    path('edit/<int:pk>', EditCartView.as_view()),
    path('clean/<int:pk>', CleanCartView.as_view()),
]
