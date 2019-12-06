from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, RetrieveDestroyAPIView, ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.
from .permissions import *
from .models import *
from .serializers import *
from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    name = "login"

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    name = "sign-up"

class UserList(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-list"


class UserDetail(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminOrUserOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "user-detail"


class CategorieList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminOrReadOnly]
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    name = "categorie-list"

    filter_fields = ('title',)
    search_fields = ('^description',)
    ordering_fields = ('pk', 'title')

class CategorieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminOrReadOnly]
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    name = "categorie-detail"


class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "post-list"

    filter_fields = ('title', 'categorie', 'owner')
    search_fields = ('^description',)
    ordering_fields = ('pk', 'title')

    def post(self, request, *args, **kwargs):
        owner = reverse('user-detail',args=[request.user.id],request=request)
        request.data['owner'] = str(owner)
        return super().post(request, *args, **kwargs)

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminOrOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "post-detail"

    def put(self, request, *args, **kwargs):
        owner = reverse('user-detail',args=[Post.objects.get(pk=kwargs['pk']).owner.id],request=request)
        request.data['owner'] = str(owner)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        owner = reverse('user-detail',args=[Post.objects.get(pk=kwargs['pk']).owner.id],request=request)
        request.data['owner'] = str(owner)
        return super().patch(request, *args, **kwargs)

class PartList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    name = "part-list"

    filter_fields = ('title', 'post')
    search_fields = ('^title',)
    ordering_fields = ('pk', 'title')

    def post(self, request, *args, **kwargs):
        post_id = int(request.data['post'].split('/')[-1])
        try :
            post = Post.objects.get(pk=post_id)
        except:
            return Response({'error':"This Post does not exist "},status = status.HTTP_404_NOT_FOUND)
        if post.owner != request.user:
            return Response({'error':"You can't add Part to a Post you don't own "},status = status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)

class PartDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminOrPostOwnerOrReadOnly]
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    name = "part-detail"

    def put(self, request, *args, **kwargs):
        post = reverse('post-detail',args=[Part.objects.get(pk=kwargs['pk']).post.id],request=request)
        request.data['post'] = str(post)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        post = reverse('post-detail',args=[Part.objects.get(pk=kwargs['pk']).post.id],request=request)
        request.data['post'] = str(post)
        return super().patch(request, *args, **kwargs)

class StepList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    name = "step-list"

    filter_fields = ('title', 'part')
    search_fields = ('^title',)
    ordering_fields = ('pk', 'title')

    def post(self, request, *args, **kwargs):
        part_id = int(request.data['part'].split('/')[-1])
        try :
            part = Part.objects.get(pk=part_id)
        except:
            return Response({'error':"This Part does not exist "},status = status.HTTP_404_NOT_FOUND)
        if part.post.owner != request.user:
            return Response({'error':"You can't add Steps to a Part you don't own the Post "},status = status.HTTP_401_UNAUTHORIZED)
        return super().post(request, *args, **kwargs)

class StepDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminOrPartOwnerOrReadOnly]
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    name = "step-detail"

    def put(self, request, *args, **kwargs):
        part = reverse('part-detail',args=[Step.objects.get(pk=kwargs['pk']).part.id],request=request)
        request.data['part'] = str(part)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        part = reverse('part-detail',args=[Step.objects.get(pk=kwargs['pk']).part.id],request=request)
        request.data['part'] = str(part)
        return super().put(request, *args, **kwargs)

class CommentList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = "comment-list"

    filter_fields = ('title', 'post', 'owner')
    search_fields = ('^title',)
    ordering_fields = ('pk', 'title')

    def post(self, request, *args, **kwargs):
        owner = reverse('user-detail',args=[request.user.id],request=request)
        request.data['owner'] = str(owner)
        return super().post(request, *args, **kwargs)

class CommentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAdminOrOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = "comment-detail"

    def put(self, request, *args, **kwargs):
        owner = reverse('user-detail',args=[Comment.objects.get(pk=kwargs['pk']).owner.id],request=request)
        request.data['owner'] = str(owner)
        post = reverse('post-detail',args=[Comment.objects.get(pk=kwargs['pk']).post.id],request=request)
        request.data['post'] = str(post)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        owner = reverse('user-detail',args=[Comment.objects.get(pk=kwargs['pk']).owner.id],request=request)
        request.data['owner'] = str(owner)
        post = reverse('post-detail',args=[Comment.objects.get(pk=kwargs['pk']).post.id],request=request)
        request.data['post'] = str(post)
        return super().patch(request, *args, **kwargs)


class ApiRoot(GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            "signup": reverse(UserCreate.name, request=request),
            "login": reverse(MyTokenObtainPairView.name, request=request),
            "user": reverse(UserList.name, request=request),
            "categorie": reverse(CategorieList.name, request=request),
            "post": reverse(PostList.name, request=request),
            "part": reverse(PartList.name, request=request),
            "step": reverse(StepList.name, request=request),
            "comment": reverse(CommentList.name, request=request),
        }, status=status.HTTP_200_OK)
