
from django.urls import path
from comments import views

app_name = "comments"

urlpatterns = [
    path('reg/',views.comment_register, name = "register_comment"),
    path('update-like/',views.update_like, name = "likes"),
    path('delete/',views.delete_comment, name = "delete_comment"),
]
