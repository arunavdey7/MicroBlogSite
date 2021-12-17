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

# Create your views here.
SECRET = 'JGJDLKZUENIBVE61749456'

@api_view(['POST'])
def register_author(request):
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

@api_view(['GET'])
def get_author_info(request):
    token = request.headers['token']
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        author = Authors.objects.get(email = payload['email'])
        if(author != None):
            return Response({'success': True,
                         'author_info': {
                             'first_name': author.first_name,
                             'last_name': author.last_name,
                             'email': author.email,
                             'bio': author.bio,
                             'profile_pic': author.profile_pic
                         }
                        })
        else:
            return Response({
                'success': False,
                'message': 'No such user found'
            })
    except Exception as err_msg:
        return Response({
                'success': False,
                'message': str(err_msg)
            })


