from django.db import models
from django.contrib.auth.models import User


# user will be registered, usershowname is display name
class InstaUser(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    user_showname = models.CharField(null=False, max_length=20)
    user_img =  models.ImageField(null=True, upload_to='upload', max_length=None)
    user_email = models.EmailField(max_length=254)
    user_detail = models.CharField(null=False, max_length=100)

    def __str__(self):
        return self.user_showname

# post will be assigned to particular user, , auto create date and likes will increase by views, one per user
class Posts(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(null=True, upload_to='upload', max_length=None)
    post_caption = models.CharField(max_length=100)
    post_created = models.DateTimeField(auto_now_add=True)
    post_likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.post_user)

# cooment will select which post, user auto get from view and date auto and data will be comment
class Comments(models.Model):
    comment_data = models.TextField(null=False)
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_data



'''
class saved_post(models.Model):
    saved_user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_posts = models.ManyToManyField(posts)

    def __str__(self):
        return self.saved_user
'''