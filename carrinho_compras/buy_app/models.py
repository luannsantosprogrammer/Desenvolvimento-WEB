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
