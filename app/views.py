from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.
class cbv_page(TemplateView):
    template_name='cbv_page.html'



class cbv_form(TemplateView):
    template_name='cbv_form.html'


    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='hari'
        context['age']=23
        
        return context
class cbv_form(TemplateView):
    template_name='cbv_form.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(** kwargs)
        context['form']=student()
        return context
        

    def post(self,request):
        form_data=student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
