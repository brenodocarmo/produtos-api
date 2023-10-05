from rest_framework import viewsets

from .models import Group, Product, SubGroup

from .serializers import GroupSerializer, SubGroupSerializer, ProductSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    Exibindo os grupo
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class SubGroupViewSet(viewsets.ModelViewSet):
    """
    Exibindo os SubGrupos
    """
    queryset = SubGroup.objects.all()
    serializer_class = SubGroupSerializer

class ProductViweSet(viewsets.ModelViewSet):
    """
    Exibindo os Produtos
    """
    queryset = Product,object.all()
    serializer_class = ProductSerializer


