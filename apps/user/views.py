from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets

from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve:
        return the User info, but only one

    List:
        return the list of the user Info
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer