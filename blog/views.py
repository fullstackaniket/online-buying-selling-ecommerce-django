from django.shortcuts import render,redirect,get_object_or_404
from blog.forms import *
from django.contrib.auth.models import User
from blog.models import Product,Category,Profile
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):

    productinfo=Product.objects.all()
    category=Category.objects.all()
    
    query=request.GET.get('s')
    if query:
        productinfo=Product.objects.filter(
            Q(cate__c_name=query)|
            Q(seller__username=query)|
            Q(p_city=query)|
            Q(p_state=query)|
            Q(name__icontains=query)

        )
    
    
    paginator=Paginator(productinfo,8)
    page=request.GET.get('pg')
    productinfo=paginator.get_page(page)


    if request.user.is_authenticated:
        user=Profile.objects.get(user=request.user)
        print(request.user)
        profileinfo=request.user   
        data ={
        'productinfo':productinfo,
        'profileinfo':profileinfo,
        'category':category,
        'user':user,
        }
    else:
        data={
            'productinfo':productinfo,
        
        'category':category,
        
        
        }

    print(data)
    return render(request, 'index.html',data)

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST )
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.dob=form.cleaned_data.get('dob')
            user.save()
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=user.username,password=raw_password)
            auth_login(request,user)
            return redirect('index')
        
    else:
        form=SignupForm()  
    data={
        'form':form,
         }
    return render(request, 'signup.html',data)

def category(request):
    if request.method == 'POST':
        form=CategoryFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form=CategoryFrom()
    data={
        'form':form
    }
    return render(request, 'category.html',data)

def about(request):
    return render(request, 'about.html')



def login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request,user)
            return redirect('index')
    else:
        form=LoginForm(request.POST)
        return render(request,"login.html",{'form':form}) 



# def login(request):
#     if request.method == 'GET':
#         form=UserCreateForm(request.GET)
#         if form.is_valid():
#             user = form.save() 
#             auth_login(request,user)
#             return redirect('index')
#     else:
#         form=UserCreateForm()
#     return render(request,"login.html",{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('index')


def product(request):
    if request.method == 'POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=ProductForm()
    data={
        'form':form
    }
    return render(request, 'product.html',data)

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    userinfo=Profile.objects.filter(user=request.user.id).get()
    product=Product.objects.filter(seller=request.user.id)
    if request.user.is_authenticated:
        user=Profile.objects.get(user=request.user)
    data={
        'userinfo':userinfo,
        'product':product,
        'user':user,
    }

    return render(request, 'profile.html',data)

def sell(request):
    if request.user.is_authenticated:
        user=Profile.objects.get(user=request.user)
        data={
            'user':user,
        }

    return render(request, 'sell.html')

def display(request,pk):
        
        productinfo=Product.objects.filter(pk=pk).get()
        profileinfo=Profile.objects.filter(user=productinfo.seller).get()
        print(productinfo)
        print(profileinfo.pic)
        cate =productinfo.cate
        print(cate)
        category=Category.objects.filter(c_name=cate).get()
        if request.user.is_authenticated:
            user=Profile.objects.get(user=request.user)
        data ={
        'productinfo':productinfo,
        'profileinfo':profileinfo,
        'category':category,
        'user':user
        }
        print(data)
        return render(request, 'display.html',data)


def sell(request,pk):
    if request.user.is_authenticated:
        user=Profile.objects.get(user=request.user)
    salesman=Profile.objects.get(id=pk)
    
    print(salesman)
    data={
        'salesman':salesman,
        'user':user
    }
    return render(request, 'sell.html',data)

# def display1(request,pk):
#     if request.user.is_authenticated:
#         productinfo=Product.objects.get(id=pk)
#         category=Category.objects.get(id=pk)
#         userinfo=Profile.objects.get(user=request.user.username)
#         data ={
#         'productinfo':productinfo,
#         'profileinfo':profileinfo,
#         'category':category,
#         }
#         print(data)
#         return render(request, 'display1.html',data)
#     else:
#         return redirect("index")
def product_edit(request,id):
    product=get_object_or_404(Product,id=id)
    if request.method == "POST":
        form=ProductEditForm(request.POST or None,instance=product)
        if form.is_valid():
            print(form)
            form.save()
            return redirect("profile")
    else:
        form = ProductEditForm(instance=product)
    data ={
        'product':product,
        "form":form,
    }
    return render(request,"product.html",data)

    

def category_edit(request,id):
    pass

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile) 
        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    data = {
        'form':form,
        'profile_form':profile_form
    }
    
    return render(request, 'profileedit.html', data)


