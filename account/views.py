from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db import transaction

from django.http import HttpResponse


from account.models import User
from account.forms import UserForm, UserCreateForm, UserLoginForm
# Create your views here.

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('main_site')
        else:
            form = UserLoginForm()
            return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('main_site')
        else:
            form = UserLoginForm(request.POST)
            print(request.POST)
            # for item in dir(form):
            #     print(item, form.__dict__.get(item))
            if form.is_valid():
                cleaned_data = form.clean()
                username = cleaned_data['username']
                password = cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect('main_site')
                else:
                    return redirect('login')
            else:
                return render(request, 'account/login.html', {'form': form})
                    
        
class Signup(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, "account/signup.html", {"form": form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            cleaned_data = form.clean()
            username = cleaned_data['username']
            password = cleaned_data['password1']
            email = cleaned_data['email']
            user = User.objects.create(username=username)
            user.email = email
            user.password = password
            user.save()
            transaction.commit()
        else:
            return render(request, "account/signup.html", {"form": form})

        return redirect("main_page")

class Logout(View):
    def get(self, request):
        pass
    def post(self, request):
        User

class UserCreateTeam(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class UserCreateOrg(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


