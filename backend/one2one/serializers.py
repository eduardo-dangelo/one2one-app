from rest_framework import serializers
from one2one.models import Workspace, Okr, One2One


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('id', 'title', 'created_at')


class One2OneSerializer(serializers.ModelSerializer):
    class Meta:
        model = One2One
        fields = fields = ('id', 'title', 'created_at', 'workspace')


class OkrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okr
        fields = ('')
