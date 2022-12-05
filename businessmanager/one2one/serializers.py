from rest_framework import serializers
from one2one.models import Project, Okr, One2One


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'created_at')


class One2OneSerializer(serializers.ModelSerializer):
    class Meta:
        model = One2One
        fields = fields = ('id', 'title', 'created_at', 'project')


class OkrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okr
        fields = ('')
