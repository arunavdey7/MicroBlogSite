from rest_framework import serializers

from micro_blog_site_api.models import Authors, Categories, Likes, Comments, Posts

class PostsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Posts
       fields = ('heading', 'created_at', 'updated_at', 'description','content','likes_count','category_id','author_id')


class AuthorsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Authors
       fields = ('first_name', 'last_name', 'email', 'password','bio','profile_pic')

class CommentsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Comments
       fields = ('author_id', 'comment', 'post_id','date_time')

class LikesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Likes
       fields = ('author_id', 'post_id')

class CategoriesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Categories
       fields = ('category')