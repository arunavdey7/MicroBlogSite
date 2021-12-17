from django.urls import include, path
from micro_blog_site_api.views import register_author, get_author_info, login, get_all_posts
from rest_framework import routers


urlpatterns = [

    path('api/addauthor/',register_author),
    path('api/authorinfo',get_author_info),
    path('api/login/',login),
    path('api/getallposts', get_all_posts),
]