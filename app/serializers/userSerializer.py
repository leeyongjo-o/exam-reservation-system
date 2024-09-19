from rest_framework import serializers

from app.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'is_admin')
        read_only_fields = ('is_admin',)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
