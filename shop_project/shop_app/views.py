from django.contrib import messages
from django.shortcuts import render, redirect
from .models import product
from .forms import productfrom


# Create your views here.
def index(request):
    obj=product.objects.all()
    context={
        'products':obj,
    }
    return render(request,'index.html',context)

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        price=request.POST.get('price',)
        stock=request.POST.get('stock',)
        img=request.FILES['img']
        item=product(name=name,desc=desc,price=price,stock=stock,img=img)
        item.save()
        messages.info(request,"Product add Sucessfull")
    return render(request,'add.html')

def detail(request,pro_id):
    item=product.objects.get(id=pro_id)
    print(item.name)
    context={
        'pro':item,
    }
    return render(request,"detail.html",context)

def update(request,pro_id):
    item=product.objects.get(id=pro_id)
    form=productfrom(request.POST or None,request.FILES,instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'item':item})


def delete(request,pro_id):
    if request.method=='POST':
        item=product.objects.get(id=pro_id)
        item.delete()
        return redirect('/')
    return render(request,'delete.html')
