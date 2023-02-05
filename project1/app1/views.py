from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(http_method_names = ['POST','GET', 'PUT', 'DELETE'])
def first_api(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        if data:
            return Response(data = data)
        data = {'details':'please provide some data with post request'}
        return Response(data = data)
    if request.method == 'PUT':
        data = request.data
        if data:
            return Response(data = data)
        data = {'details':'please provide some data with put request'}
        return Response(data = data)
    data = {'details':'this is first api second day'}
    return Response(data = data)

class SecondAPI(APIView):
    def get(self, request):
        return Response(data = {'details': 'this is class based view'})
    
    def post(self, request):
        return Response(data = {'DETAILS': 'THIS IS POST METHOD CLASS BASED VIEW'})

    def put(self, request):
        return Response(data = {'deatils': ' his is put method class based view'})

    def delete(self, request):
        return Response(data = {'details': ' this is delete method class based view'})

class ThirdApi(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(data = serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            print(obj.pk)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

class fetchperticular(APIView):
    def get(self, request, pk=None):
    #    try:
    #        obj = Post.objects.get(pk = pk)
    #         serializer = PostSerializer(obj)
    #         return Response(data=serializer.data)
    #     except Post.DoesNotExist:
    #        data = {'deatils':'Data not found'}
    #        return Response(data=data)
           obj =  get_object_or_404(Post, pk = pk)
           serializer = PostSerializer(obj)
           return Response(data=serializer.data)
    def put(self, request, pk=None):
        obj = get_object_or_404(Post, pk = pk)
        serializer = PostSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def patch(self, request, pk=None):
        obj = get_object_or_404(Post, pk = pk)
        serializer = PostSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def delete(self, request, pk=None):
        obj = get_object_or_404(Post, pk = pk)
        obj.delete()
        return Response(data={'details':'no data'})




