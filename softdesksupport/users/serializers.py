from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','age','can_be_contacted','can_data_be_shared']

        
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'age', 'can_be_contacted', 'can_data_be_shared']

    def validate(self, data):
        age = data.get('age')
        if age is not None and age < 15:
            raise serializers.ValidationError({"age": "You must be at least 15 years old to register."})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
