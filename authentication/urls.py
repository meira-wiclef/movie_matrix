from django.urls import path
from .views import login


urlpatterns = [
    path('', login, name="login"),
    path('/reset-passoword', reset_password, name="reset_password"),
]