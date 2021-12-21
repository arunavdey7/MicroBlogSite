from django.urls import include, path
from micro_blog_site_api.views import dislike, new_post, register_author, get_author_info, login, get_all_posts,new_post, like, dislike
from rest_framework import routers


urlpatterns = [

    path('api/addauthor/',register_author),
    path('api/authorinfo',get_author_info),
    path('api/login/',login),
    path('api/getallposts', get_all_posts),
    path('api/newpost/', new_post),
    path('api/like', like),
    path('api/dislike', dislike),
]