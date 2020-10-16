#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions # IsAuthenticatedOrReadOnly # IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse



class PontoTuristicoViewSet(viewsets.ModelViewSet):
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['nome', 'descricao']
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao']
    # lookup_field = 'id'
    permission_classes = [DjangoModelPermissions]
    authentication_classes = [TokenAuthentication]
               
    def get_queryset(self):
        queryset = PontoTuristico.objects.all()
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        
        if id is not None:
            queryset = queryset.filter(id__iexact=id)

        if nome is not None:
            queryset = queryset.filter(nome__iexact=nome)
        
        if descricao is not None:
            queryset = queryset.filter(descricao__iexact=descricao)
        
        return queryset
          
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
        
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
        
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
        
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
        # return super(PontoTuristicoViewSet, self).denunciar(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
        # return super(PontoTuristicoViewSet, self).teste(request, *args, **kwargs)
    
    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('Ok')
        