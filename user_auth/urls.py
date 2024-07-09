from django.urls import path
from user_auth import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("verify_otp/<int:user_id>/", views.verify_otp, name="verify_otp"),
]
