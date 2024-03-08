from django.urls import path

from .views import SignUpView

# from "../../../src/vue/login.vue" import login


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]