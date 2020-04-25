from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name="maldives"
    dest1.desc="I will go here some day"
    dest1.price="300"
    dest1.img="destination_1.jpg"

    dest2=Destination()
    dest2.name="bali"
    dest2.desc="I will go here some other day"
    dest2.price="890"
    dest2.img="destination_8.jpg"

    dest3=Destination()
    dest3.name="las vegas"
    dest3.desc="I will go not here some day"
    dest3.price="370"
    dest3.img="destination_9.jpg"


    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})
    #return render(request,'index.html',{'dest1':dest1,'dest2':dest2,'dest3':dest3}), we could have done this
    #also but it will take lots of time if we have large number of objects.