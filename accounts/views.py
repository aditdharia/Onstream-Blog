from django.shortcuts import render
from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout
)
from .forms import userLoginForm,userRegisterForm
from django.shortcuts import redirect


def index(request):
    return render(request,"index.html",{})
# Create your views here.
def login_view(request):
    title="login"
    form=userLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username="username",password="password")
        login(request,user)
        return redirect("/")

    return render(request,"login.html",{"form":form,"title":title})


def register_view(request):
    title="Register"
    form=userRegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=username,password=password)
        login(request,user)
        return redirect("/")
    context={"form":form,"title":title}
    return render(request,"register.html",context)



def logout_view(request):
    logout(request)
    return redirect("/")
    return render(request,"login.html",{})