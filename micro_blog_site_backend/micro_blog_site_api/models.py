from django.db import models

# Create your models here.


class Authors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    likes_count = models.IntegerField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)



class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
