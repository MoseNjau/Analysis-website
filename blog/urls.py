from django.urls import path
from . import views
from .views import PostView


app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:post_slug>/<int:year>/<int:month>/<int:day>/', views.post_detail, name='post_details'),
    path('posts/<slug:status>', views.MyPosts.as_view(),name="my_posts"),
    path('post_view/', PostView.as_view(), name='post_view'),
]