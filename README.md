# WorkOrderSys
For Devops Prac.  Use, Django and Vue

# restframework advanced method

urls.py:
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register("idcs", views.IdcViewset_v1)

urlpatterns = [
    url(r'^', include(route.urls))
]


views.py:
from rest_framework import viewsets
class IdcViewset_v1(viewsets.ModelViewSet):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

______________________________v1


------------------------For User API-----------------------------------
# Use the Django auth_user
 command: "dbshell" and desc auth_user;
 
## Create Users 
command: "shell"  -> "from django.contrib.auth.models import User"

```angular2html
def create_user(name):
    for i in range(1,20):
        username = "{}-{}".format(name, i)

        User.objects.create__user(username, "{}@alan.com", "1234")

        User.objects.create__user(username, "{}@alan.com".format(name), "1234")
```

add_user_api
        
 Invode: create_user(name)

 
