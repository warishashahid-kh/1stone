
from django.urls import path
from loginapp import views

urlpatterns = [
    path('login/', views.login_view, name='login'),

    path('', views.login_view, name='root_login'), # This directs the root URL to your login_view
]
# ...