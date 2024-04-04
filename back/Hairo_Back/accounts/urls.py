from django.urls import path

from .views import SignUpView, UserCreate

# from "../../../src/vue/login.vue" import login


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('api/signup/', UserCreate.as_view(), name='api-signup'),
]