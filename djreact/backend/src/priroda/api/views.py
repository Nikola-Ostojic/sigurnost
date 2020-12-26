# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )

# class PrirodaListView(ListAPIView):
#     queryset = Priroda.objects.all()
#     serializer_class = PrirodaSerializer

# class PrirodaDetailView(RetrieveAPIView):
#     queryset = Priroda.objects.all()
#     serializer_class = PrirodaSerializer

# class PrirodaCreateView(CreateAPIView):
#     queryset = Priroda.objects.all()
#     serializer_class = PrirodaSerializer

# class PrirodaDeleteView(DestroyAPIView):
#     queryset = Priroda.objects.all()
#     serializer_class = PrirodaSerializer

# class PrirodaUpdateView(UpdateAPIView):
#     queryset = Priroda.objects.all()
#     serializer_class = PrirodaSerializer

from priroda.models import Priroda
from .serializers import PrirodaSerializer

from rest_framework import viewsets

class PrirodaViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PrirodaSerializer
    queryset = Priroda.objects.all()