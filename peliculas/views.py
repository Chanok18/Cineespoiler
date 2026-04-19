from rest_framework import viewsets
from .models import Pelicula, Genero
from .serializers import PeliculaSerializer, GeneroSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import CustomPagination

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    pagination_class = CustomPagination
    
class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

    filterset_fields = ['genero']
    search_fields = ['titulo']

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genero']

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer