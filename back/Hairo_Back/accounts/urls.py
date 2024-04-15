from django.urls import path

from .views import SignUpView, dashboard_view

# from "../../../src/vue/login.vue" import login


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('dashboard/', dashboard_view, name='dashboard'),
]