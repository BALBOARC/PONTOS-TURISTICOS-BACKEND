from rest_framework import viewsets
from enderecos.models import Endereco
from enderecos.api.serializers import EnderecoSerializer



class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    