from django.urls import path
from .views import UserView, SingUpView, GetUserDataView

urlpatterns = [
    path('', UserView.as_view()),
    path('signup', SingUpView.as_view()),
    path('user', GetUserDataView.as_view()),
]
