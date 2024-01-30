from rest_framework import  serializers
from .models import NomaUser

class NomaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NomaUser
        fields = '__all__'
