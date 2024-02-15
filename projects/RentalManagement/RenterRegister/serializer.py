from rest_framework import serializers
class renterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 50)
    phone = serializers.IntegerField()
    password = serializers.CharField(max_length = 50)
    room = serializers.IntegerField()
    price = serializers.IntegerField()
    