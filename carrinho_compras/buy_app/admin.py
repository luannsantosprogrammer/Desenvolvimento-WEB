from django.contrib import admin
from .models import BuyModel


class BuyAdmin(admin.ModelAdmin):
    list_display = ("client","name_product", "price", "amount")
    list_filter = ("name_product","price","amount")


admin.site.register(BuyModel,BuyAdmin)
