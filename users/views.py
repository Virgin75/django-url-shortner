from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import get_user_model


from .forms import LoginForm, SignupForm

class LogInView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {'form': form})

    def post(self, request):
        # create a form instance and populate it with data from the request:
        form = LoginForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['username'], 
                        password=form.cleaned_data['password'])
            
            if user is not None:
                login(request, user)
                return redirect('/shorten', user=user)
            else:
                #error cant login
                messages.add_message(request, messages.ERROR, 'Cannot login with the provided credentials.')
        messages.add_message(request, messages.ERROR, 'Form data is invalid.')
        return render(request, "users/login.html", {'form': form})



class SignUpView(View):

    def get(self, request):
        form = SignupForm()
        return render(request, "users/signup.html", {'form': form})

    def post(self, request):
        # create a form instance and populate it with data from the request:
        form = SignupForm(data=request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            user = get_user_model().objects.create_user(
                    email=form.cleaned_data['email'], 
                    password=form.cleaned_data['password1'])
           
            if user is not None:
                login(request, user)
                return redirect('/shorten', user=user)

        messages.add_message(request, messages.ERROR, 'Form data is invalid.')
        return render(request, "users/signup.html", {'form': form})

class LogOutView(View):

    def get(self, request):
        logout(request)
        return render(request, 'users/loggedout.html')
