
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from loginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('loginapp.urls')),
    path('', views.login_view, name='root_login'),
]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])