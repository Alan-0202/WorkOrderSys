

from django.conf.urls import url, include

from .views import idc_list
from . import views
# urlpatterns = [
#
#     url(r'^idcs/$', idc_list)
# ]



# urlpatterns = [
#     url("^$", idc_list),
#     url("^idcs/$", views.IdcList.as_view(), name="idc_list_Use_ApiView"),
#     url("^idcs/(?P<pk>[0-9]+)/$", views.IdcDetail.as_view(), name="idc_detail")
# ]



# For ViewSet
# from rest_framework.routers import  DefaultRouter
#
# route = DefaultRouter()
# route.register("idcs", views.IdcViewset_v7)
# urlpatterns = [
#     url(r'^', include(route.urls))
# ]

from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register("idcs", views.IdcViewset_v1)

urlpatterns = [
    url(r'^', include(route.urls))
]