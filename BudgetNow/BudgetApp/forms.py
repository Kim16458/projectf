from django import forms
from .models import Expense, Categories, Budget

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['Category', 'Amount']

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['CategoryName', 'BudgetLimit']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['CategoryName', 'Maximum', 'TimeInMonths']