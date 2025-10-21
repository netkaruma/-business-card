



from django.urls import path
from main import views as main_views
from users import views as users_views


app_name = "users"

urlpatterns = [
    path('register/',users_views.register, name = 'register'),
    path('login/', users_views.user_login, name = 'login'),
    path('logout/',users_views.user_logout, name = "logout"),
    path('save-color/',users_views.save_color, name = "save-color"),
]
