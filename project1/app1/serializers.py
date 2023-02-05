from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=20)
    content = serializers.CharField(max_length=20)

    def create(self, validated_data):
        #title = validated_data.get('title')
        #content = validated_data.get('content')
        #p = Post(title=title, content=content)
        #p.save()
        #return p 
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
        