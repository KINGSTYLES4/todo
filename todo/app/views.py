from django.shortcuts import render
from app.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO':EUFO , 'EPFO':EPFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST)
        if UFDO.is_valid() and PFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()
            return HttpResponseRedirect(reverse('login'))
        return HttpResponse('Invalid Data')
    return render(request,'register.html',d)

def login(request):
    return render(request,'login.html')