from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()

    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again!")
            return redirect('home')
    else:        
        return render(request, 'website/home.html', {'records': records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully register user")
            return redirect('home')
    else: 
        form = SignUpForm()
        return render(request, 'website/register.html', {'form': form})
    
    return render(request, 'website/register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'website/record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You must logged in to view record')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()

        messages.success(request, 'Succesfully delete the record')
        return redirect('home')
    else:
        messages.success(request, 'You must logged in to view record')
        return redirect('home')

def add_record(request):
    pass