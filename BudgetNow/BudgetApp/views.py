from django.shortcuts import render, redirect
from .models import Categories, Expense, Budget
from .forms import ExpenseForm, CategoriesForm, BudgetForm
from django.db.models import Q, Sum

# Create your views here.
def index(request):
    expenses = Expense.objects.all()
    total = Expense.objects.aggregate(Sum('Amount'))
    categories = Categories.objects.all()
    budget = Budget.objects.all()
    return render(request, 'templates/index.html', {'expenses': expenses, 'total':total,  'categories':Categories, 'budget':Budget})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

def edit_expense(request):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'BudgetApp/edit_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('index')
    return render(request, 'BudgetApp/delete_expense.html', {'expense': expense})

def search_expenses(request):
    query = request.GET.get('q')
    results = Expense.objects.filter(Q(Category__icontains=query) | Q(Amount__icontains=query))
    return render(request, 'BudgetApp/search_expenses.html', {'results': results})

def view_expenses(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'BudgetApp/view_expenses.html', {'expense': expense})

def add_category(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriesForm()
    return render(request, 'BudgetApp/add_category.html', {'form': form})

def edit_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == 'POST':
        form = CategoriesForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriesForm(instance=category)
    return render(request, 'BudgetApp/edit_category.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, 'BudgetApp/delete_category.html', {'category': category})

def view_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'BudgetApp/view_category.html', {'category': category})


def insert_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BudgetForm()
    return render(request, 'BudgetApp/insert_budget.html', {'form': form})

def update_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'BudgetApp/update_budget.html', {'form': form})

def check_budget(request, pk):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            category = expense.category
            total_spent = Expense.objects.filter(category=category).aggregate(Sum('Amount'))['Amount__sum'] or 0

            if  total_spent + expense.Amount > Budget.Amount:
                return render(request, 'BudgetApp/check_budget.html', {'form': form, 'exceeded': True, 'notification':'You have exceeded the budget limit for category'}) 
    else:
        form = BudgetForm()
    return render(request, 'BudgetApp/check_budget.html', {'form': form})
