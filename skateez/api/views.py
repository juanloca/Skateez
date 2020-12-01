
from rest_framework import viewsets
from skateez.api.serializers import *
from skateez.models import *
from skateez.views import *

class TablaViewSet(viewsets.ModelViewSet):

	queryset = Tabla.objects.all()

	serializer_class = TablaSerializer

class EjesViewSet(viewsets.ModelViewSet):

	queryset = Ejes.objects.all()
	serializer_class = EjesSerializer
