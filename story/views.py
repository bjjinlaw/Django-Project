from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model



User = get_user_model()
# Create your views here.

def home(request):
    return render(request, "home.html")

def dash(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html",)
    else:
        return HttpResponseRedirect(reverse("user:login"))
    
def matches(request):
    users=User.objects.exclude(id=request.user.id)
    context = {
        'users': users,
    }

    return render(request, "matches.html",context)