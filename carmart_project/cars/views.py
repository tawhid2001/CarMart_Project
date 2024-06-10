from django.shortcuts import render,redirect
from django.views.generic import DetailView
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from .models import Car,Order
from django.contrib import messages
from . import forms

# Create your views here.

class DetailsCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'details.html'

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        comment_form = forms.CommentForm(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = self.object
            new_comment.user = request.user
            new_comment.save()
            return redirect('details',id=self.object.id)
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = models.Comment.objects.filter(car=car)
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@login_required
def buy_car(request,car_id):
    car = Car.objects.get(pk=car_id)

    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user,car=car,quantity=1)
        messages.success(request,f"You have successfully purchased {car.name}")
        return redirect('profile')
    else:
        messages.error(request,f'Sorry,{car.name} is out of stock')

    return render(request,'details.html')
