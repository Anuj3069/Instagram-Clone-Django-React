from rest_framework import serializers
from Instagram_App.models import InstaUser,  Posts, Comments

#serializer for Posts model
class PostsSerializer(serializers.ModelSerializer):
    #xyzneeded in this = anyserializer(many=True, read_only=True)

    class Meta:
        model = Posts
        #exclude = ['anyfeild']   if one wishes to exclude
        fields = "__all__"


#serializer for InstaUser model
class InstaUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstaUser
        
        fields = "__all__"


#serializer for Comments model
class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"