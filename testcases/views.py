from rest_framework import viewsets
from .models import TestCase
from .serializers import TestCaseSerializer

class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all().order_by('id')
    serializer_class = TestCaseSerializer
