from django.shortcuts import render


from rest_framework import generics
from rest_framework.response import Response
from custom_user import serializers, models

# class CustomUserViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.CustomUserSerializer
#     queryset = models.CustomUser.objects.all()

class RegisterApi(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": serializers.UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )