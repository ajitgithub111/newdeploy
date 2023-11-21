from rest_framework import serializers

from .models import jiomodel


class jioser(serializers.ModelSerializer):
    class Meta:
        model=jiomodel
        fields="__all__"