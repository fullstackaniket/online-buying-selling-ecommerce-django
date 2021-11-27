"""rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup',views.signup, name='signup'),
    path('about',views.about, name='about'),
    path('category',views.category, name='category'),
    path('logout',views.logout, name='logout'),
    path('contact',views.contact, name='contact'),
    path('product',views.product, name='product'),
    path('profile',views.profile, name='profile'),
    path('login',auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    #path('login',auth_views.LoginView.as_view(), name="login"),
    path('display/<int:pk>',views.display, name='display'),
    # path('display1/<int:pk>',views.display1, name='display1'),
    path('sell/<int:pk>',views.sell, name='sell'),
    path('product_edit/<int:id>',views.product_edit, name='product_edit'),
    path('category_edit',views.category_edit, name='category_edit'),
    path('profile_edit',views.profile_edit, name='profile_edit'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)