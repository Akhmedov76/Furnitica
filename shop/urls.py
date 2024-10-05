from django.urls import path

from shop import views
from shop.views import home_page_view

app_name = 'users'
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify-email'),
    path('', home_page_view),

]
