from django.urls import path, include
from .views import *
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('documentation', schema_view),

    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('login', MyTokenObtainPairView.as_view(), name=MyTokenObtainPairView.name),
    path('signup', UserCreate.as_view(), name=UserCreate.name),

    path('user', UserList.as_view(), name=UserList.name),
    path('user/<int:pk>', UserDetail.as_view(), name=UserDetail.name),

    path('categorie', CategorieList.as_view(), name=CategorieList.name),
    path('categorie/<int:pk>', CategorieDetail.as_view(), name=CategorieDetail.name),

    path('post', PostList.as_view(), name=PostList.name),
    path('post/<int:pk>', PostDetail.as_view(), name=PostDetail.name),

    path('part', PartList.as_view(), name=PartList.name),
    path('part/<int:pk>', PartDetail.as_view(), name=PartDetail.name),

    path('step', StepList.as_view(), name=StepList.name),
    path('step/<int:pk>', StepDetail.as_view(), name=StepDetail.name),

    path('comment', CommentList.as_view(), name=CommentList.name),
    path('comment/<int:pk>', CommentDetail.as_view(), name=CommentDetail.name),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
