from rest_framework import viewsets
from avaliacoes.models import Avaliacao
from avaliacoes.api.serializers import AvaliacaoSerializer



class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    