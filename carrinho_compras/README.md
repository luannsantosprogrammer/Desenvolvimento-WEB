# Carrinho Compras
App Django Full Stack que gerencia compras no mercado

> Esse app em Django serve como um gerenciador de compras onde o usuário pode adicionar antes ou durante as compra seus itens, tendo como retorno além do armazenamento, o calculo total.


## Models:
> No arquivo Models utilizei a ferramenta de criação de autentificação de usuário do Django e inseri como argumento na variável **client** em um **ForeignKey**.
> As variavel **name_product**,**price** e **amount** são schemas que serão preenchidos pelo usuário.
> A função **total_product** é o calculo do preço x quantidade.


`


    from django.db import models
    from django.contrib.auth.models import User
    
    
    class BuyModel(models.Model):
        client = models.ForeignKey(User, on_delete=models.CASCADE)
        name_product = models.CharField(max_length=100, verbose_name="Nome do Produto")
        price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name="Preço unitário",)
        amount = models.IntegerField(verbose_name="Quantidade")
    
    
        def total_product(self):
            return self.price * self.amount
    
        def __str__(self):
            return self.name_product
`

## Forms:
> No arquivo forms foi desenvolvido os campos de formulário de criação de login do usuário e POST dos itens para o "carrinho" .
> **CreateUserForm** herda o objeto **UserCreationForm** do Django e deste modo o fields são escolhidos para exibição do formulário
> O **BuyForms** herda de **forms** e consequentemente criei os fields para inserir os itens no carrinho

`

    from django.contrib.auth.models import User
    from django.contrib.auth.forms import UserCreationForm
    from django import forms
    from .models import BuyModel
    
    
    class CreateUserForm(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'password1', 'password2']
    
    
    class BuyForms(forms.ModelForm):
        class Meta:
            model = BuyModel
            fields = ["name_product", "price", "amount"]
`

## Urls:
> Essas são as urls do projeto

`

    from django.urls import path
    from . import views
    
    
    urlpatterns = [
     path("",views.login_user,name="login"),
     path("create_user/",views.create_user,name="create_user"),
     path("logout_user/",views.logout_user,name="logout_user"),
     path("delete_item/<int:id>/",views.delete_item,name="delete_item"),
     path("buy/",views.buy,name="buy"),
    ]

`

## Views:

> No arquivo views, desenvolvi as seguintes funções:
  1. **create_user**: instancio a classe de autentificação e criação de usuário e renderizo na página da rota **create_user**. Nesta mesma função criei a validação da criação do usuário.
  2. **login_user**: essa é a página inicial. É renderizada tanto como homepage quanto após a criação do usuário.
  3. **logout_user** : serve para que o usuário saia da autentificação. Nesta função, já começo a trabalhar com **@login_required** para permissão.
  4. **buy**: essa é a página onde o usuário irá gerenciar seus itens de compra. Os verbos CREATE e READ, fiz questão de adiciona-los em uma mesma página para tornar mais dinamica a aplicação.
  5. **delete_item** : esse método servirá para o verbo DELETE do CRUD


`

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

`


## Templates e Sctatics:

> Os templates e statics possuem arquivos html e css para cada rota da aplicação. Assim a manutenção se torna mais rápida e autentica.
![teste](templates_statics)


