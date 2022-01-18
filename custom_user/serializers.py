from asyncore import write
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'is_active',
                  'is_staff',
                  'is_admin',
                  )
        extra_kwargs = {'password': {'write_only': True,'style':{'input_type':'password'}}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            #password =validated_data['password])
            #return user
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

    # def update(self, instance, validated_data):
    #     if 'password' in validated_data:
    #         password=validated.pop('password')
    #         instance.set_password(password)
    #     return super().update(instance, validated_data)
