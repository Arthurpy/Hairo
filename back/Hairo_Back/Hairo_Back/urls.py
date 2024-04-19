from django.contrib import admin
from django.urls import path, include
from .views import landing_page, login_view, signup_view, ressources_pages, microsoft_login, course_details_by_name
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import QCMListView
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qcms/names/', views.get_all_qcms , name='qcm-names'),
    path('', landing_page, name='landing'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('api/cours/', ressources_pages, name='cours-list'),
    path('api/course-details-by-name/', views.course_details_by_name, name='course-details-by-name'),
    path('microsoft-login/', microsoft_login, name='microsft-login'),
    path('microsoft-callback', views.microsoft_callback, name='microsoft-callback'),
    path('api/course-details-by-name/', course_details_by_name, name='course-details-by-name'),
    path('api/qcms/names/', QCMListView.as_view(), name='qcm-names'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
