from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import Product,Category,Profile

class SignupForm(UserCreationForm):
   
   class Meta:
       model=User
      
       
       fields=('username','email', 'password1','password2')
    

class LoginForm(forms.ModelForm):
    
    class Meta:
        model =User 
        fields = ("username","password")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =('cate','name','description','price','p_state','p_city','p_img','p_img1','p_img2',)

class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields =("c_name",)

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =('cate','name','description','price','p_state','p_city','p_img','p_img1','p_img2',)



class ProfileForm(UserCreationForm):
    class Meta:
        model=Profile
        fields =('user','pic','bio','location','dob')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = (
                 'email',
                 'first_name',
                 'last_name'
                )

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =('bio','location','dob',"pic")