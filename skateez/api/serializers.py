from rest_framework import serializers
from skateez.models import 	*

class TablaSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Tabla
		fields= ('nombre', 'medida', 'concavo' )

class EjesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ejes
		fields = ('nombre', 'medida', 'altura')