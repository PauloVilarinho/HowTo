from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'username','email','posts']

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url','id','post','owner','text']

class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ['url','id','title','description','part']

class PartSerializer(serializers.HyperlinkedModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    class Meta:
        model = Part
        fields = ['url','id','title','steps','post']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    parts = PartSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['url','id','title','description','owner','categorie','parts','comments']

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Categorie
        fields = ['url','id','title','description','posts']
