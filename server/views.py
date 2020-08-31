from rest_framework import viewsets, generics
from .serializer import TimeSeriesSerializer
from .models import Zykluszeiten

class TimeSeriesViewSet(viewsets.ModelViewSet):
# class TimeSeriesViewSet(generics.ListAPIView, viewsets.GenericViewSet):
    queryset = Zykluszeiten.objects.all()
    serializer_class = TimeSeriesSerializer