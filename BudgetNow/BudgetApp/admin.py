from django.contrib import admin
from .models import Categories, Expense, Budget

# Register your models here.

admin.site.register(Categories)
admin.site.register(Expense)
admin.site.register(Budget)



