from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# Create your views here.

@login_required(login_url='/auth/')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect('auth_view')