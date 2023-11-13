from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from women.serializers import Women_Serializer
from .models import Women, Category
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.


# просмотр всех данных
class Women_API_List(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = Women_Serializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


#  обновление данных
class Women_API_Update(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = Women_Serializer
    permission_classes = (IsOwnerOrReadOnly,)


# crud dannix
class Women_API_Destroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = Women_Serializer
    permission_classes = (IsAdminOrReadOnly,)


# class Women_View_Set(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = Women_Serializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)

#     @action(methods=["get"], detail=True)
#     def category(self, request, pk):
#         cats = Category.objects.get(pk=pk)
#         return Response({"cats": cats.name})


# class Women_API_View(APIView):
#     def get(self, request):
#         w = Women.objects.all().values()
#         return Response({"posts": Women_Serializer(w, many=True).data})

#     def post(self, request):
#         serializer = Women_Serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"post": serializer.data})

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = Women_Serializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({"post": serializer.data})

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Delete not allowed"})

#         return Response({"post": "delete post" + str(pk)})


# class Women_API_View(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
