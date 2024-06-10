from django.shortcuts import render,redirect
from .forms import SignupForm,ChangeUserData
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from cars.models import Order

# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                return redirect('login')
        
        else:
            signup_form = SignupForm()
    
        return render(request,'signup.html',{'form':signup_form})
    else:
        return redirect('homepage')

class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'Logged In Successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Logged In information Incorrect')
        return super().form_invalid(form)
    
@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'profile.html',{'orders':orders})

@login_required
def editProfile(request):
    if request.method == 'POST':
        profile_form = ChangeUserData(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('homepage')
    else:
        profile_form = ChangeUserData(instance = request.user)
    return render(request,'edit_profile.html',{'form':profile_form})

def UserLogout(request):
    logout(request)
    return redirect('homepage')