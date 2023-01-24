# from django.http import HttpResponse
# from django.views import View
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.models import User
from .serializers import TaskSerializer,CategorySerializer,ProducSerializer
from .models import Task,Category,Product


from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

# //////////test method
@api_view(['GET'])
def test(req):
    return Response("<h1>welcome to my project -  server a live</h1>")


# model crud
# @permission_classes([IsAuthenticated])
class CategoryView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of MyModel objects
        """
        if (pk > -1):
            my_model = Category.objects.get(id=pk)
            serializer = CategorySerializer(my_model)
        else:
            my_model = Category.objects.all()
            serializer = CategorySerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        # usr =request.user
        # print(usr)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Category.objects.get(pk=pk)
        serializer = CategorySerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Category.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# model crud
# @permission_classes([IsAuthenticated])
class ProductView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request,pk=-1):
        """
        Handle GET requests to return a list of MyModel objects
        """
        if (pk > -1):
            my_model = Product.objects.filter(category=pk)
            serializer = ProducSerializer(my_model, many=True)
        else:
            my_model = Product.objects.all()
            serializer = ProducSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        # usr =request.user
        # print(usr)
        serializer = ProducSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Product.objects.get(pk=pk)
        serializer = ProducSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# model crud
@permission_classes([IsAuthenticated])
class MyModelView(APIView):
    """
    This class handle the CRUD operations for MyModel
    """
    def get(self, request):
        """
        Handle GET requests to return a list of MyModel objects
        """
        my_model = request.user.task_set.all()
        serializer = TaskSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new Task object
        """
        # usr =request.user
        # print(usr)
        serializer = TaskSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """
        Handle PUT requests to update an existing Task object
        """
        my_model = Task.objects.get(pk=pk)
        serializer = TaskSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Handle DELETE requests to delete a Task object
        """
        my_model = Task.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ////////////////////////////////login /register
# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# register
@api_view(['POST'])
def  register(req):
    username=req.data["username"]
    password=req.data["password"]
    # create a new user (encrypt password)
    try:
        User.objects.create_user(username=username,password=password)
    except:
        return Response("error")    
    return Response(f"{username} registered")
 