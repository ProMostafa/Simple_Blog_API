from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=models.TextField()
    image=models.ImageField(upload_to='Images',blank=True,null=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Author: {} , Aritcle Title: {}".format(self.author,self.title)
    


COMMENT_STATUS=(('Like','Like'),('Angry','Angry'),('Dislike','Dislike'),('Funny','Funny'),('Love','Love'))
USERS=(('Authanticated User','Authanticated User'),('Anonymous User','Anonymous User'))
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    # Make null=True for Handling anonymous user in fornt end when display comments on post
    # for now make  fields that indicator anonymous user or Authanticated User make a comment # for showing only in browsable API
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    make_comment=models.CharField(choices=USERS,default='Anonymous User',max_length=20)
    comment=models.CharField(max_length=255)
    status=models.CharField(choices=COMMENT_STATUS,default='Like',max_length=8)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {} , commment {} , on post {}".format(self.user,self.comment,self.post)

