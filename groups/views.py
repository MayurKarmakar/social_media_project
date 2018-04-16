from django.shortcuts import render,get_object_or_404
from . import models
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import IntegrityError
# Create your views here.
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
class CreateGroup(LoginRequiredMixin,generic.CreateView):
    model = models.Group
    fields = ('name','description')
class SingleGroup(generic.DetailView):
    model = models.Group
class ListGroup(generic.ListView):
    model = models.Group
class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(models.Group,slug=self.kwargs.get('slug'))
        try:
            models.GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,'You, already a member!')
        else:
            messages.success(self.request,'You are a member now!')
        return super().get(request,*args,**kwargs)
class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})
    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,"You aren't a member of this group!")
        else:
            membership.delete()
            messages.success(self.request,"You left the Group.")
        return super().get(request,*args,**kwargs)
