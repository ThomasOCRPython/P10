from asyncore import write
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'username',
                #   'is_active',
                #   'is_staff',
                #   'is_admin',
                  )
        extra_kwargs = {'password': {'write_only': True,'style':{'input_type':'password'}}}

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )

    # def create(self, validated_data):
    #     user = CustomUser.objects.create(
    #         email=validated_data["email"],
    #         first_name=validated_data["first_name"],
    #         last_name=validated_data["last_name"],
    #         #password =validated_data['password])
    #         #return user
    #     )

    #     user.set_password(validated_data["password"])
        
    #     return user

    # def update(self, instance, validated_data):
    #     if 'password' in validated_data:
    #         password=validated.pop('password')
    #         instance.set_password(password)
    #     return super().update(instance, validated_data)
