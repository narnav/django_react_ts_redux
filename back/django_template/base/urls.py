from django.urls import path
from .views import *
from . import views 

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.register ),
    path('test/',views.test ),
    path('mymodel/', views.MyModelView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:pk>/', views.CategoryView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('products/<int:pk>/', views.ProductView.as_view()),
    path('mymodel/<int:pk>/', views.MyModelView.as_view()),
]
# data - OK
# authentication - OK
# upload files (image)