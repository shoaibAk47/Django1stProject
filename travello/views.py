from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')     #the data name is passed in json format or dictionary
    #intitally it was return render(request,'home.html')