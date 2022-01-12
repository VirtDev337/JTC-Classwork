from django.db import models
import datetime as dt


# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    img_link = models.URLField()
    title =  models.CharField(max_length = 255)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    
    @property
    def responses(self):
        return Comment.objects.filter(post = self)
class Comment(models.Model):
    comment_id = models.AutoField(primary_key = True)
    created = models.DateTimeField(auto_now_add =  True)
    comment = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", default = 1, on_delete = models.CASCADE)
    author = models.CharField(max_length = 255, default = 'Guest')
    
    def __str__(self):
        return self.comment