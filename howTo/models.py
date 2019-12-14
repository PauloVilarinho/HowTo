from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Categorie(models.Model):
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()



class Post(models.Model):
    image = models.FileField(null=True)
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    categorie =  models.ForeignKey(Categorie,
                                    on_delete=models.CASCADE,
                                    related_name="posts")
    owner = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="posts")


class Part(models.Model):
    title = models.CharField(max_length=255)
    post = models.ForeignKey(Post,
                                on_delete=models.CASCADE,
                                related_name="parts")

class Step(models.Model):
    image = models.FileField(null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    part = models.ForeignKey(Part,
                                on_delete=models.CASCADE,
                                related_name="steps")

class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="comments")
    post = models.ForeignKey(Post,
                                on_delete=models.CASCADE,
                                related_name="comments")
