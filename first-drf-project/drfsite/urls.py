"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from women.views import (
    Women_API_Update,
    Women_API_List,
    # Women_API_Detail_View,
    # Women_View_Set,
    Women_API_Destroy,
)
from rest_framework import routers


# class My_Custom_Router(routers.SimpleRouter):
#     routes = [
#         routers.Route(
#             url=r"^{prefix}$",
#             mapping={"get": "list"},
#             name="{basename}-list",
#             detail=False,
#             initkwargs={"suffix": "List"},
#         ),
#         routers.Route(
#             url=r"^{prefix}/{lookup}$",
#             mapping={"get": "retrieve"},
#             name="{basename}-detail",
#             detail=True,
#             initkwargs={"suffix": "Detail"},
#         ),
#     ]


# router = My_Custom_Router()
# router.register(r"women", Women_View_Set, basename="women")
# print(router.urls)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
    path("api/v1/women/", Women_API_List.as_view()),
    path("api/v1/women/<int:pk>/", Women_API_Update.as_view()),
    path("api/v1/womendelete/<int:pk>/", Women_API_Destroy.as_view()),
    # # path("api/v1/", include(router.urls))
    # path("api/v1/womenlist/", Women_View_Set.as_view({"get": "list"})),
    # path("api/v1/womenlist/<int:pk>/", Women_View_Set.as_view({"put": "update"})),
]
