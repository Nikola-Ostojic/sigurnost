from rest_framework.generics import ListAPIView, RetrieveAPIView
from priroda.models import Priroda
from .serializers import PrirodaSerializer

class PrirodaListView(ListAPIView):
    queryset = Priroda.objects.all()
    serializer_class = PrirodaSerializer

class PrirodaDetailView(RetrieveAPIView):
    queryset = Priroda.objects.all()
    serializer_class = PrirodaSerializer

