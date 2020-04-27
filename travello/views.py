from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
    #return render(request,'index.html',{'dest1':dest1,'dest2':dest2,'dest3':dest3}), we could have done this
    #also but it will take lots of time if we have large number of objects.