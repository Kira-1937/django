from django.shortcuts import render
from .forms import ExplorinForm
from .models import *

def Form(request):
      formdata=ExplorinForm()
      if request.method=='POST':
       formdtata=ExplorinForm(request.POST)
      if formdtata.is_valid():
        formdtata.save()

        context={
          'formdata':formdtata
        }
        return render(request,"form.html",context)


def Table(request):
    form=product.objects.all()

    context={
     'form':form
      }

    return render(request,"table.html",context)