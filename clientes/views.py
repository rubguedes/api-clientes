from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # Adicionando um filtro na api
    # filters.OrderingFilter - adiciona o filtro de acordo com os campos selecionados em ordering_filters
    # filters.SearchFilter - adiciona o filtro de busca de acordo com os campos selecionados em search_fields
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # Selecionando quais serão os campos utilizados para a ordenação
    ordering_fields = ['nome', 'id']
    # Selecionando quais serão os campos utilizados para a busca
    search_fields = ['nome', 'id', 'cpf', 'rg']
    # Busca exata de clientes que são ativos ou não
    filterset_fields = ['ativo']