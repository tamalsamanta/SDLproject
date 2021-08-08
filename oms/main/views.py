from django.shortcuts import render
from .models import table
# from django.http import HttpResponse
# from django.db import connection

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def menu(request):
    
    if request.method == 'POST':
        Table = table()
        Table.name = request.POST.get('name')
        Table.number = request.POST.get('number')
        
        #local vars
        num1 = request.POST.get('burgerQ')
        num2 = request.POST.get('pattiesQ')
        num3 = request.POST.get('pizzaQ')
        num4 = request.POST.get('maggiQ')
        
        items = []
        if num1 != '0':
            items.append("Burger")
            items.append(num1)
        if num2 != '0':
            items.append("Pattice")
            items.append(num2)
        if num3 != '0':
            items.append("Pizza")
            items.append(num3)
        if num4 != '0':
            items.append("Maggi")
            items.append(num4)

        print(items)

        Table.items = items

        total = (float(num1)*59.99)+(float(num2)*12)+(float(num3)*99.99)+(float(num4)*35)
        print(total)

        Table.price = total
        Table.save()
    
    context = {}
    return render(request, 'menu.html', context)

def test(request):
    
    tables = table.objects.raw("SELECT * FROM main_table")

    context = {
        'table': tables,
    }
    return render (request, 'sample.html', context)

def sample(request):

    num = request.POST.get('num')

    context = {
        'table': table.objects.all(),
        'num': num,
        'title': "Show Orders"
    }
    return render(request, 'bill.html', context)