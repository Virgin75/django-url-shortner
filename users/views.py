from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate
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
            print(user)
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
            print(user)
            return render(request, "users/signup.html", {'form': form})
