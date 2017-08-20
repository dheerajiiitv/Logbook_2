from django.http import HttpResponse,request
from django.shortcuts import render
from .models import MeetingDetails
from .models import StudDetails
from .models import Students

# Create your views here.
def index(request):
    print("Hello")
    return render(request, 'logbook_2/index.html')

def new_entry(request):



def past_entry(request):
    data = MeetingDetails.objects.order_by('-date')
    students = StudDetails.objects.all()
    return render(request,'logbook_2/entries.html',{'data':data,'students':students})


