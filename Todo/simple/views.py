from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Newdata
from .serializers import NewdataSerializer
from simple import forms

def goto(request):
    return render(request,'simple/index.html')
# Create your views here.
class studentlist(APIView):
    def get(self,request):
        print(request.GET)
        if 'delete' in request.GET:
            delitem=Newdata.objects.get(id=request.GET['delete'])
            delitem.delete()
            return HttpResponseRedirect('/student/')
            #return HttpResponseRedirect('/student/')
        # if(request.method=='Delete'):
            # print("Maa ki chit")
        li=Newdata.objects.all()
        serializer=NewdataSerializer(li,many=True)
        return render(request,'simple/base.html',{'studentlist':serializer.data})
    def post(self,request):
        form=forms.Newform(request.POST)
        print('aagya')
        print(form.data)
        print(request.POST)

        if( 'update' in request.POST):
            i=int(form.data['update'])
            str=form.data['Task']
            if(len(str)>0):
                Newdata.objects.filter(pk=i).update(Task=str)
                return HttpResponseRedirect('/student/')
            #li=Newdata.objects.all()
            #serializer=NewdataSerializer(li,many=True)

        elif(form.is_valid()):
            print('valid h bhai')
            form.save(commit=True)
            li=Newdata.objects.all()
            serializer=NewdataSerializer(li,many=True)
        # return render(request,'simple/base.html',{'studentlist':serializer.data})
            return HttpResponseRedirect('/student/')
