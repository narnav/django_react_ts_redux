from rest_framework import serializers
from .models import Task,Category,Product


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Task.objects.create(**validated_data,user=user)

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    # def create(self, validated_data):
    #     return Category.objects.create(**validated_data)

class ProducSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'