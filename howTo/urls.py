from django.urls import path, include
from .views import *


urlpatterns = [

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
]
