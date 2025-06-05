from users.models import User, Contributor
from users.serializers import UserSerializer, UserRegistrationSerializer, ContributorSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsStaffOrOwner, IsProjectAuthorOrSelfContributor

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwner]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        # Non-staff users can only retrieve/manage their own account
        return User.objects.filter(pk=user.pk)


class UserRegistrationView(APIView):
    permission_classes = [AllowAny] # Allow anyone to register

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ContributorViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    # Apply IsAuthenticated first, then your custom permission
    permission_classes = [IsAuthenticated, IsProjectAuthorOrSelfContributor]

    def perform_create(self, serializer):
        """
        Override perform_create to automatically set the 'user' field
        to the authenticated user making the request.
        """
        # The serializer's validate method has already checked for uniqueness
        # and that the project exists.
        serializer.save(user=self.request.user)

    # No need to override perform_destroy for basic deletion.
    # The permission class will handle authorization for deletion.
    

    
