from django.contrib import admin
from blog.models import Category,Profile,Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Product)