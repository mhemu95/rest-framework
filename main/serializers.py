from rest_framework import serializers
from .models import Student, Category, Book
from django.contrib.auth.models import User     # imported for token authentication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    # Hash user password
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        # this is for object level validation(2)
        def validate(self, data):

            if data['age'] < 18:
                raise serializers.ValidationError({'error': 'Age can not be less than 18'})

            if data['name']:
                for n in data['name']:
                    if n.isdigit():
                        raise serializers.ValidationError({'error': 'name can not contain digit'})

            if data['father_name']:
                for n in data['father_name']:
                    if n.isdigit():
                        raise serializers.ValidationError({'error': "father's name can not contain digit"})

            else:
                return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ['name', 'category']
        # depth = 1
