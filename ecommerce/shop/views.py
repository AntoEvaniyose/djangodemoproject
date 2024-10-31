from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def allcategories(request):
    c=Category.objects.all()
    context={'cat':c}
    return render(request,'category.html',context)

def allproducts(request,p):                 #here p receives the category id
    c=Category.objects.get(id=p)            #reads a particular category object using id
    p=Product.objects.filter(category=c)    #reads all products under a particular category object
    context={'cat':c,'product':p}
    return render(request,'product.html',context)

def productdetail(request,p):
    k=Product.objects.get(id=p)
    context={'pro':k}
    return render(request,'detail.html',context)

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            u.save()
        else:
            return HttpResponse("Passwords are not same")
        return redirect('shop:login')
    return render(request,'register.html')

def user_login(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:categories')
        else:
            messages.error(request,"Invalid credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:categories')

def add_categories(request):
    if(request.method=="POST"):
        cn=request.POST['cn']
        d=request.POST['d']
        i=request.FILES['i']

        c=Category.objects.create(name=cn,desc=d,image=i)
        c.save()
        return redirect('shop:categories')
    return render(request,'addcategories.html')

def add_products(request):
    if(request.method=="POST"):
        pn=request.POST['pn']
        d=request.POST['d']
        p=request.POST['p']
        s=request.POST['s']
        cn=request.POST['cn']   #reads the category name from form field
        m=request.FILES['m']

        cat=Category.objects.get(name=cn)   #category objects/record matching with category name cn

        c=Product.objects.create(name=pn,desc=d,image=m,price=p,stock=s,category=cat) #assigns each value to product fields
        c.save()
        return redirect('shop:categories')
    return render(request,'addproducts.html')

def addstock(request,p):
    k=Product.objects.get(id=p)

    if(request.method=="POST"):     #after form submission
        k.stock=request.POST['s']
        k.save()
        return redirect('shop:categories')
    context={'pro':k}
    return render(request,'addstock.html',context)






