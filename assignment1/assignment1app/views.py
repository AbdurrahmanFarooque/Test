from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout as logouts

from assignment1 import settings

from . models import User, Gallery
from . form import RegisterForm, LoginForm, UpdateForm, ChangepasswordForm
from django.core.mail import send_mail
def index(request):
          return render(request, 'index.html')
          

def login(request):
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        email_cleaned = form.cleaned_data['email']
                        password_cleaned = form.cleaned_data['Password']
                        try:
                                user = User.objects.get(email=email_cleaned)
                                if not user:
                                        messages.warning(request, 'email does not exist')
                                        return redirect('/login')
                                elif password_cleaned != user.password:
                                        messages.warning(request, 'password is incorrect')
                                        return redirect('/login')
                                else:
                                        messages.success(request, 'Success')
                                        return redirect('/home/%s' % user.id)
                        except:
                                messages.warning(request, 'email or password incorrect')
                                return redirect('/login')
        else:
                form = LoginForm()
        return render(request, 'login.html', {'form': form})


def home(request, id):
        user = User.objects.get(id=id)
        return render(request, 'home.html', {'user': user})


def register(request):
        if request.method == 'POST':
                form = RegisterForm(request.POST, request.FILES)
                if form.is_valid():
                        name_cleaned = form.cleaned_data['name']
                        age_cleaned = form.cleaned_data['age']
                        place_cleaned = form.cleaned_data['place']
                        photo_cleaned = form.cleaned_data['photo']
                        email_cleaned = form.cleaned_data['email']
                        password_cleaned = form.cleaned_data['Password']
                        confirmpassword_cleaned = form.cleaned_data['ConfirmPassword']

                        user = User.objects.filter(email=email_cleaned).exists()
                        if user:
                                messages.warning(request, 'email already exists')
                                return redirect('/login')
                        elif password_cleaned != confirmpassword_cleaned:
                                messages.warning(request, 'passwrod missmatch')
                        else:
                                tab = User(name=name_cleaned, age=age_cleaned, place=place_cleaned, photo=photo_cleaned, email=email_cleaned, password=password_cleaned)
                                tab.save()                               
                                messages.success(request, 'data saved')
                                return redirect('/')
        else:
                form = RegisterForm()
        return render(request, 'register.html', {'form': form})
          

def update(request, id):
        user = User.objects.get(id=id)
        if request.method == 'POST':
                form = UpdateForm(request.POST or None, instance=user)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Success')
                        return redirect('/home/%s' % user.id)
        else:
                form = UpdateForm(instance=user)
        return render(request, 'update.html', {'user': user, 'form': form})


def logout(request):
        logouts(request)
        messages.success(request, 'logged out')
        return redirect('/')


def delete(request, id):
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request, 'Account Deleted')
        return redirect('/')


def changepassword(request, id):
        user = User.objects.get(id=id)
        if request.method == 'POST':
                form = ChangepasswordForm(request.POST or None)
                if form.is_valid:
                        oldpassword_cleaned = form.cleaned_data['OldPassword']
                        newpassword_cleaned = form.cleaned_data['NewPassword']
                        confirmpassword_cleaned = form.cleaned_data['ConfirmPassword']
                        
                        if oldpassword_cleaned != user.password:
                                messages.warning(request, 'old password is incorrect')
                                return redirect('/changepassword/%s' % user.id)
                        elif oldpassword_cleaned == newpassword_cleaned:
                                messages.warning(request, 'new passowrd is identical to old password')
                                return redirect('/changepassword/%s' % user.id)
                        elif newpassword_cleaned != confirmpassword_cleaned:
                                messages.warning(request, 'new password and confirm password are different')
                                return redirect('/changepassword/%s' % user.id)
                        else:
                                user.password=newpassword_cleaned
                                user.save()
                                messages.success(request, 'password changed')
        else:
                form = ChangepasswordForm()
                return render(request, 'changepassword.html', {'user': user, 'form': form})                       


def details(request, id):
        gallery = Gallery.objects.get(id=id)      
        return render(request, 'details.html', {'gallery': gallery})  


def gallery(request):
        gallery = Gallery.objects.all()
        return render(request, 'gallery.html', {'gallery': gallery})