from rest_framework import serializers
from escola.models import Estudante,Curso

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields =['id','nome','email','cpf','dt_nascimento','celular']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        exclude = []