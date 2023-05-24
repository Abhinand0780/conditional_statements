from django.shortcuts import render

# Create your views here.
def condi(request):
    d={'a':1000,'b':100}
    return render(request,'condi.html',d)
