from rest_framework import serializers
from .models import *


class UserDisplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']

class CategorieDisplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = ['url','title','childs']

class StepDisplaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Step
        fields = ['url','title','description']

class PartDisplaySerializer(serializers.HyperlinkedModelSerializer):
    steps = StepDisplaySerializer(many=True,read_only=True)
    class Meta:
        model = Part
        fields = ['url','title','steps']

class PostDisplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['url','title']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostDisplaySerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username','email','posts']

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    childs = CategorieDisplaySerializer(many=True,read_only=True)
    posts = PostDisplaySerializer(many=True,read_only=True)
    class Meta:
        model = Categorie
        fields = ['url','title','description','childs','posts']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    parts = PartDisplaySerializer(many=True,read_only=True)
    categorie = CategorieDisplaySerializer(read_only=True)
    owner = UserDisplaySerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['url','title','description','owner','categorie','parts']

class PartSerializer(serializers.HyperlinkedModelSerializer):
    steps = StepDisplaySerializer(many=True,read_only=True)
    post = PostDisplaySerializer(read_only=True)
    class Meta:
        model = Part
        fields = ['url','title','steps','post']

class StepSerializer(serializers.HyperlinkedModelSerializer):
    part = PartDisplaySerializer(read_only=True)
    class Meta:
        model = Step
        fields = ['url','title','description','part']
