from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import BuyModel
from .form import BuyForms,CreateUserForm

#criação de usuário
def create_user(request):

    form = CreateUserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")
        
    return render(request,"create_user.html", {"form":form})

#login do usuário
def login_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect("buy")

    return render(request,"login.html")


@login_required
def logout_user(request):
    logout(request)
    return redirect("/")


@login_required
def buy(request):
    form = BuyForms(request.POST or None)
    itens = BuyModel.objects.filter(client=request.user)
    
    if request.method == "POST":
        if form.is_valid():
            item = form.save(commit=False)
            item.client = request.user
            item.save()
            return redirect("buy")
        
    return render(request,"buy.html",{"form":form, "itens":itens})

@login_required
def delete_item(request,id):
    item = get_object_or_404(BuyModel,id=id,client=request.user)

    if request.method == "POST":
        item.delete()
        return redirect("buy")
    return render(request,"delete_item.html")