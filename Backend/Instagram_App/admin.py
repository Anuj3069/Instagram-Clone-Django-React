from django.contrib import admin
from .models import Posts, InstaUser , Comments
# Register your models here.

admin.site.register(Posts)
admin.site.register(InstaUser)
admin.site.register(Comments)
#admin.site.register(saved_post)