from django.shortcuts import render
#from .forms import SignUpForm

def sign_up(request):
    form = 1
    context = {
                "form":form,
            }
    return render(request,"accounts/sign_up.html",context)
