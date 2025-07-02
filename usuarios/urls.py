from django.urls import path
from .views import UsuarioListCreateAPIView, UsuarioRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UsuarioListCreateAPIView.as_view(), name='usuario-list-create'),
    path('<int:pk>/', UsuarioRetrieveUpdateDestroyAPIView.as_view(), name='usuario-detail'),
]