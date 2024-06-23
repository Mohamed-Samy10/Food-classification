from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['image','username','first_name','last_name','phone_number','gender','age','weight','height','email', 'password']
        extra_kwargs = {'password': {'write_only': True},
                        'gender': {'required': True},
                        'age': {'required': True},
                        'weight': {'required': True},
                        'height': {'required': True},
                        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','phone_number','gender','age','weight','height','email','image']