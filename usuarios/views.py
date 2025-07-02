from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

# Vista para listar y crear usuarios
class UsuarioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para obtener, actualizar y eliminar un usuario
class UsuarioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer