from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import landing_page, login_view, signup_view, ressources_pages, microsoft_login, course_details_by_name
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import QCMViewSet, ResultatViewSet, QCMListView
from django.urls import path, include


router = DefaultRouter()
router.register(r'qcms', QCMViewSet)
router.register(r'resultats', ResultatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', landing_page, name='landing'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('api/cours/', ressources_pages, name='cours-list'),
    path('api/course-details-by-name/', views.course_details_by_name, name='course-details-by-name'),
    path('microsoft-login/', microsoft_login, name='microsft-login'),
    path('microsoft-callback', views.microsoft_callback, name='microsoft-callback'),
    path('api/course-details-by-name/', course_details_by_name, name='course-details-by-name'),
    path('api/qcms/names/', QCMListView.as_view(), name='qcm-names'),
    path('api/', include(router.urls)),
]
