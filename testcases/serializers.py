from rest_framework import serializers
from .models import TestCase

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__' # Or specify a tuple of fields: ('id', 'title', 'description', ...)
