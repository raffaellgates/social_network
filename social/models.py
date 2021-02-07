from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=80)
    email = models.EmailField()
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=12)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(Profile, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
        
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='commet', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name