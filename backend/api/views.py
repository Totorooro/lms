from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, UserSerializer, LogoutSerializer
from rest_framework_simplejwt.views import TokenBlacklistView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class LoginView(generics.GenericAPIView):
    """
    Представление для обработки входа пользователя.
    """
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)


class LogoutView(TokenBlacklistView):
    """
    Представление для logout.
    """
    serializer_class = LogoutSerializer
    permission_classes = [AllowAny]