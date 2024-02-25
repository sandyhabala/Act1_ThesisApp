from django.urls import path
from . import views

app_name = "searcher"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:id>", views.detail, name="detail"),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]
