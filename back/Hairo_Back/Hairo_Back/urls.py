from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import landing_page, login_view, signup_view, ressources_pages, course_details_by_name
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import QCMViewSet, ResultatViewSet, QCMListView # Assure-toi de modifier 'my_app' avec le nom de ton application Django
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('qcms/names/', views.get_all_qcms , name='qcm-names'),
    path('', landing_page, name='landing'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('api/events/', views.agenda, name='events'),
    path('api/cours/', ressources_pages, name='cours-list'),
    path('api/course-details-by-name/', course_details_by_name, name='course-details-by-name'),
    # Intégration des routes du router pour les API QCM et résultats
]