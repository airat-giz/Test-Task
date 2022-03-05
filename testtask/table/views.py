from rest_framework import generics
from .serializers import TableSerializer
from .models import Table


class TableList(generics.ListCreateAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
