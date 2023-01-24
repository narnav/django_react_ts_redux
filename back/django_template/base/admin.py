from django.contrib import admin

# Register your models here.
from .models import Task,Product,Category
 
admin.site.register(Task)
admin.site.register(Product)
admin.site.register(Category)
