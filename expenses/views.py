from django.shortcuts import render
#from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'expenses/index.html')

def add_expenses(request):
    return render(request,'expenses/add_expenses.html')

