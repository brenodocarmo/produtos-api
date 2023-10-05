from rest_framework import serializers

from .models import Group, SubGroup, Product


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializers: Seria uma forma que realizar um filtro
    dos campos que desejamos exibir atraves da API
    """
    class Meta:
        model = Group
        fields = [
            'cod_gpr', 
            'desc_gpr', 
            'situ_gpr'
        ]


class SubGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubGroup
        fields = [
            'cod_sbg', 
            'desc_sbg', 
            'situ_sgb',
            'group_f'
        ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'