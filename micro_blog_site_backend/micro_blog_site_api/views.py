from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from micro_blog_site_backend.settings import SECRET_KEY
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from micro_blog_site_api.serializers import AuthorsSerializer,PostsSerializer, CategoriesSerializer, LikesSerializer, CommentsSerializer
from micro_blog_site_api.models import Authors, Categories, Comments, Likes, Posts
import hashlib, jwt
from datetime import datetime
import logging

# Create your views here.
SECRET = 'JGJDLKZUENIBVE61749456'

#Setting up a logging facility
logging.basicConfig(filename="logs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

@api_view(['POST'])
def register_author(request):
    try:
        _first_name = request.data['first_name']
        _last_name = request.data['last_name']
        _email = request.data['email']
        _password = request.data['password']
        _password = hashlib.md5(_password.encode()).hexdigest()
        _bio = request.data['bio']
        _profile_pic = request.data['profile_pic']
        encoded_jwt = jwt.encode({"email":_email}, SECRET ,algorithm="HS256")
        new_author = Authors(
                        first_name = _first_name,
                        last_name = _last_name,
                        email = _email,
                        password = _password,
                        bio = _bio,
                        profile_pic = _profile_pic
                    )
        try:
            new_author.save()
            return Response({'success': True, 'token': encoded_jwt})
        except Exception as err_msg:
            print('Error: ',err_msg)
            return Response({'success': False,
                             'message': str(err_msg)
            })
    except:
        return Response({'success': False,
                         'message': 'Deformed Body Request'
            })

@api_view(['GET'])
def get_author_info(request):
    try:
        token = request.headers['token']
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        author = Authors.objects.get(email = payload['email'])
        return Response({'success': True,
                        'author_info': {
                            'first_name': author.first_name,
                            'last_name': author.last_name,
                            'email': author.email,
                            'bio': author.bio,
                            'profile_pic': author.profile_pic
                        }
                    })
    except Exception as err_msg:
        return Response({
                'success': False,
                'message': 'Invalid or expired token'
            })

@api_view(['POST'])
def login(request):
    try:
        _email = request.data['email']
        _password = request.data['password']
        _password = hashlib.md5(_password.encode()).hexdigest()
        author = Authors.objects.get(email = _email, password = _password)
        token = jwt.encode({"email":_email}, SECRET ,algorithm="HS256")
        return Response(
            {
                'success': True,
                'token': token
            }
        )
    except Exception as err_msg:
        return Response({
                'success': False,
                'message': str(err_msg)
            })


@api_view(['GET'])
def get_all_posts(request):
    posts = []
    try:
        _posts = Posts.objects.all()
        for post in _posts:
            posts.append(
                {
                    'post_id' : post.id,
                    'heading' : post.heading,
                    'created_at': post.created_at,
                    'updated_at' : post.updated_at,
                    'description' : post.description,
                    'content' : post.content,
                    'likes_count' : post.likes_count,
                    'category_id' : post.category_id.id,
                    'category' : post.category_id.category,
                    'author_id' : post.author_id.id,
                    'author' : post.author_id.first_name + ' ' + post.author_id.last_name
                }
            )
        posts.sort(key = lambda post:int(post['likes_count']), reverse = True)
        return Response({
            'success': True,
            'posts': posts
        })
    except Exception as err_msg:
        return Response({
            'success': False,
            'message': str(err_msg)
        })

@api_view(['GET'])
def posts_of_category(request):
    _category = request.headers['category']
    posts = []
    try:
        _posts = Posts.objects.get(category = _category)
        for post in _posts:
            posts.append(
                {
                    'heading' : post.heading,
                    'created_at': post.created_at,
                    'updated_at' : post.updated_at,
                    'description' : post.description,
                    'content' : post.content,
                    'likes_count' : post.likes_count,
                    'category_id' : post.category_id,
                    'category' : Categories.objects.get(id = post.category_id).category,
                    'author_id' : post.author_id,
                    'author' : Authors.objects.get(id = post.author_id)
                }
            )
        posts.sort(key = lambda post:int(post.likes_count), reverse = True)
        return Response({
            'success': True,
            'posts': posts
        })
    except Exception as err_msg:
        return Response({
            'success': False,
            'posts': [],
            'message': str(err_msg)
        })

@api_view(['GET'])
def author_posts_by_reverse_chrono(request):
    posts = []
    try:
        token = request.headers['token']
        _email = jwt.decode(token, SECRET, algorithms=["HS256"]).email
        _author_id = Authors.objects.get(email = _email).author_id
        _posts = Posts.objects.get(author_id = _author_id)
        for post in _posts:
            posts.append(
                {
                    'heading' : post.heading,
                    'created_at': post.created_at,
                    'updated_at' : post.updated_at,
                    'description' : post.description,
                    'content' : post.content,
                    'likes_count' : post.likes_count,
                    'category_id' : post.category_id,
                    'category' : Categories.objects.get(id = post.category_id).category,
                    'author_id' : post.author_id,
                    'author' : Authors.objects.get(id = post.author_id).first_name
                }
            )
        posts.sort(key = lambda post: post.created_at, reverse = True)
        return Response({
            'success': True,
            'posts': posts
        })
    except Exception as err_msg:
        return Response({
            'success': False,
            'posts': [],
            'message': str(err_msg)
        })

@api_view(['GET'])
def author_posts_by_likes(request):
    posts = []
    try:
        token = request.headers['token']
        _email = jwt.decode(token, SECRET, algorithms=["HS256"]).email
        _author_id = Authors.objects.get(email = _email).author_id
        _posts = Posts.objects.get(author_id = _author_id)
        for post in _posts:
            posts.append(
                {
                    'heading' : post.heading,
                    'created_at': post.created_at,
                    'updated_at' : post.updated_at,
                    'description' : post.description,
                    'content' : post.content,
                    'likes_count' : post.likes_count,
                    'category_id' : post.category_id,
                    'category' : Categories.objects.get(id = post.category_id).category,
                    'author_id' : post.author_id,
                    'author' : Authors.objects.get(id = post.author_id)
                }
            )
        posts.sort(key = lambda post: int(post.likes_count), reverse = True)
        return Response({
            'success': True,
            'posts': posts
        })
    except Exception as err_msg:
        return Response({
            'success': False,
            'posts': [],
            'message': str(err_msg)
        })

@api_view(['GET'])
def get_post(request):
    try:
        _post_id = request.headers['post_id']
        post = Posts.objects.get(post_id = _post_id)
        post = {
                    'heading' : post.heading,
                    'created_at': post.created_at,
                    'updated_at' : post.updated_at,
                    'description' : post.description,
                    'content' : post.content,
                    'likes_count' : post.likes_count,
                    'category_id' : post.category_id,
                    'category' : Categories.objects.get(id = post.category_id).category,
                    'author_id' : post.author_id,
                    'author' : Authors.objects.get(id = post.author_id)
                }
        return Response(
            {
                'success': True,
                'post': post
            }
        )
    except Exception as err_msg :
        return Response(
            {
                'success': False,
                'message': str(err_msg) 
            }
        )
    
@api_view(['GET'])
def about_author(request):
    try:
        author_id = request.headers['author_id']
        author = Authors.objects.get(id = author_id)
        author_info = {
                        'first_name': author.first_name,
                        'last_name': author.last_name,
                        'email': author.email,
                        'bio': author.bio,
                        'profile_pic': author.profile_pic
                    }
        return Response(
            {
                'success': True,
                'author_info': author_info
            }
        )
    except Exception as err_msg:
        return Response(
            {
                'success': False,
                'message': str(err_msg) 
            }
        )

@api_view(['POST'])
def new_post(request):
    flag = False
    try:
        token = request.headers['token']
        _email = jwt.decode(token, SECRET, algorithms=["HS256"])['email']
        _author_id = Authors.objects.get(email = _email)
        _heading = request.data['heading']
        _content = request.data['content']
        _created_at = request.data['created_at']
        _updated_at = request.data['updated_at']
        _description = request.data['description']
        _likes_count = request.data['likes_count']
        _category = request.data['category']
        _categories = Categories.objects.all()
        for category_item in _categories:
            if(_category.upper() == category_item.category.upper()):
                _category_id = category_item
                flag = True
                break
        if(flag == False):
            new_category = Categories(category = _category)
            new_category.save()
            _categories = Categories.objects.all()
            for category_item in _categories:
                if(_category.upper() == category_item.category.upper()):
                    _category_id = category_item
                    flag = False
                    break

        new_post = Posts(
            heading = _heading,
            created_at = _created_at,
            updated_at = _updated_at,
            description = _description,
            content = _content,
            likes_count = _likes_count,
            category_id = _category_id,
            author_id = _author_id
        ) 
        new_post.save()
        return Response(
            {
                'success': True
            }
        )
    except Exception as err_msg:
        return Response(
            {
                'success': False,
                'message': str(err_msg) 
            }
        )

@api_view(['GET'])
def like(request):
    try:
        token = request.headers['token']
        _post_id = request.data['post_id']
        _email = jwt.decode(token, SECRET, algorithms=["HS256"])['email']
        _author_id = Authors.objects.get(email = _email)
        current_likes_count = Posts.objects.get(id = _post_id).likes_count
        Posts.objects.filter(id = _post_id).update(likes_count = current_likes_count + 1)
        likes = Likes(author_id = _author_id, post_id = Posts.objects.get(id = _post_id))
        likes.save()
        return Response(
            {
                'success': True
            }
        )
    except Exception as err_msg:
        return Response(
            {
                'success': False,
                'message': str(err_msg)
            }
        )

@api_view(['GET'])
def dislike(request):
    try:
        token = request.headers['token']
        _post_id = request.data['post_id']
        _email = jwt.decode(token, SECRET, algorithms=["HS256"])['email']
        _author_id = Authors.objects.get(email = _email)
        current_likes_count = Posts.objects.get(id = _post_id).likes_count
        Posts.objects.filter(id = _post_id).update(likes_count = current_likes_count - 1)
        Likes.objects.filter(author_id = _author_id, post_id = Posts.objects.get(id = _post_id)).delete()
        return Response(
            {
                'success': True
            }
        )
    except Exception as err_msg:
        return Response(
            {
                'success': False,
                'message': str(err_msg)
            }
        )
    
@api_view(['POST'])
def comment(request):
    try:
        token = request.headers['token']
        _comment = request.data['comment']
        _post_id = request.data['post_id']
        _email = jwt.decode(token, SECRET, algorithms=["HS256"])['email']
        _author_id = Authors.objects.get(email = _email)
        _date_time = datetime.now()
        new_comment = Comments(comment = _comment, post_id = Posts.objects.get(id = _post_id), date_time = _date_time, author_id = _author_id)
        new_comment.save()
        return Response(
            {
                'success': True
            }
        )
    except Exception as err_msg:
        return Response(
            {
                'success': False,
                'message': str(err_msg)
            }
        )

@api_view(['POST'])
def uncomment(request):
    try:
        token = request.headers['token']
        _post_id = request.data['post_id']
        _email = jwt.decode(token, SECRET, algorithms=["HS256"])['email']
        _author_id = Authors.objects.get(email = _email)
        Comments.objects.filter(author_id = _author_id, post_id = Posts.objects.get(id = _post_id)).delete()
        return Response(
            {
                'success': True
            }
        )
    except Exception as err_msg:
        return Response(
            {
                'success': False,
                'message': str(err_msg)
            }
        )

@api_view(['POST'])
def get_comments_for_post(request):
    try:
        _post_id = request.data['post_id']
        comments = Comments.objects.filter(post_id = Posts.objects.get(id = _post_id))
        comments_list = []
        for cmnt in comments:
            logger.info("Loading Comments")
            comments_list.append(
                {
                    'author_id' : cmnt.author_id.id, 
                    'author' : cmnt.author_id.first_name + ' ' + cmnt.author_id.last_name,
                    'comment' : cmnt.comment,
                    'post_id' : cmnt.post_id.id,
                    'date_time' : cmnt.date_time
                }
            )
        return Response(
            {
                'success': True,
                'comments': comments_list
            }
        )
    except Exception as err_msg:
        return Response(
            {
                'success' : False,
                'message' : str(err_msg)
            }
        )
        


'''
Required End Points:

GET --> DONE
/api/getallposts

GET --> DONE
/api/postsofcategory
headers:
	category

GET --> DONE
/api/authorpostsbyreversechrono
headers:
	jwt
	

GET --> DONE
/api/authorpostsbylikes
headers:
	jwt

GET --> DONE
/api/authorlikedposts
headers:
	jwt

GET --> DONE
/api/getpost
headers:
	post_id

GET --> DONE
/api/aboutauthor
headers:
	author_id

POST --> DONE
/api/newpost
headers:
    jwt
body:
	heading
	created_at
	updated_at
	description
	content
	likes_count
	category_id
	author_id

GET --> DONE
/api/like
header:
	jwt
	post_id

GET --> DONE
/api/dislike
header:
	jwt
	post_id

POST --> DONE
/api/comment
headers:
    jwt
body:
	comment
	post_id

POST --> DONE
/api/uncomment
headers:
    jwt
body:
	post_id


GET
/api/getcommentsforpost
headers:
    post_id

GET
/api/removepost
header:
	jwt
	post_id

GET
/api/getpostsforauthorbychrono
header:
    author_id

GET
/api/getpostsforauthorbylikes
header:
    author_id

GET
/api/getlikesforpost
header:
    post_id

'''