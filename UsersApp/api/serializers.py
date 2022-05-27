from UsersApp.models import CustomUser
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    confirmPassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # is_active = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirmPassword']#, 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    # def get_is_active(self, obj):
    #     return False
    
    def save(self):
        password = self.validated_data['password']
        confirmPassword = self.validated_data['confirmPassword']

        # if password matches
        if password != confirmPassword:
            raise serializers.ValidationError({'error': 'password and confirmPassword should be same'})
        
        # if email exists
        if CustomUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists'})
        
        account = CustomUser(email=self.validated_data['email'], is_active=False)
        account.set_password(password)
        account.save()

        return account


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['password', 'last_login']
        