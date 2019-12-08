from rest_framework import viewsets
from .Serializer import EntrySerializer
from .models import Entry

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
