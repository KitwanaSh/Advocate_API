from rest_framework.serializers import ModelSerializer
from .models import Advocates

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocates
        fields = ("username", "bio")