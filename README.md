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

