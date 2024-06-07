from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'CPF':'CPF inválido'})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'NOME':'Somente letras'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"RG":'O campo RG precisa ter 9 dígitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"CELULAR":'Formato de celular inválido. Modelo válido: 11 91234-1234'})

        return data