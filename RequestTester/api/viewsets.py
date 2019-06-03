from rest_framework import viewsets, mixins, status
from .serializers import PersonSerializer
from myapp.models import Person
class PersonViewsets(mixins.ListModelMixin,
                    mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer