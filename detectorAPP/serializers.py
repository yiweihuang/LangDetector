from rest_framework import serializers

class DetectorAppSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   lang = serializers.CharField()
