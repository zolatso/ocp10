from rest_framework import serializers
from users.models import User, Contributor
from resources.models import Project

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
    

class ContributorSerializer(serializers.ModelSerializer):
    # 'user' is read-only because it will be automatically set to request.user
    # during creation. Clients should not provide a user ID for this field.
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'date_joined']
        read_only_fields = ['date_joined'] # This field is auto_now_add

    def validate(self, data):
        """
        Custom validation to ensure the authenticated user is not already
        a contributor to the specified project.
        """
        # The request object is available in serializer context
        request_user = self.context['request'].user
        project = data['project']

        # Check if a Contributor instance already exists for this user and project
        if Contributor.objects.filter(user=request_user, project=project).exists():
            raise serializers.ValidationError(
                {"detail": "You are already a contributor to this project."}
            )
        return data