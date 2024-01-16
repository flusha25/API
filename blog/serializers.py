from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from .models import Blog

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    #password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User neeeot found.')
        data['user'] = user
        return data
    


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
            model = Blog
            fields = "__all__"