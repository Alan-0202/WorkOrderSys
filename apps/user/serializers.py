from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    """
    Serializer For User
    """

    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()