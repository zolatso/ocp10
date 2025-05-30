from rest_framework import serializers
from users.models import User, Contributor

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email','age','can_be_contacted','can_data_be_shared']
        

class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['user','project']
