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

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name="post-detail")

    class Meta:
        model = Categorie
        fields = ['url','id','title','description','posts']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    parts = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name="part-detail")
    class Meta:
        model = Post
        fields = ['url','id','title','description','owner','categorie','parts']

class PartSerializer(serializers.HyperlinkedModelSerializer):
    steps = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name="steps-detail")
    class Meta:
        model = Part
        fields = ['url','id','title','steps','post']

class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ['url','id','title','description','part']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url','id','post','owner','text']
