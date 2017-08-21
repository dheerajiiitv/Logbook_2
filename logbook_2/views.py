from django.http import HttpResponse,request,HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .models import MeetingDetails
from .models import StudDetails
from .models import Students

# Create your views here.
def index(request):
    print("Hello")
    return render(request, 'logbook_2/index.html')

def new_entry(request):
    if(request.method == "POST"):
        dt= request.POST['dt']
        st = request.POST['st']
        et = request.POST['et']
        objjective = request.POST['obj']
        entry = MeetingDetails(date=dt,start_time=st,end_time=et,today_objective=objjective)
        entry.save()
        st = Students.objects.all()
        for s in st:
            idq = str(s.id)
            if(request.POST.get(idq,"Not present") == "on"):
                sq = "ob"+idq
                ob = request.POST[sq]
                student=StudDetails(name=s,objective=ob,present=True,date=dt)
                student.save()

        return HttpResponseRedirect("/logbook/")
    else:
        students = Students.objects.all()
        return render(request,'logbook_2/add.html',{'students':students})


def past_entry(request):
    data = MeetingDetails.objects.order_by('-date')
    students = StudDetails.objects.all()
    return render(request,'logbook_2/entries.html',{'data':data,'students':students})

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        id = request.POST['id']
        student = Students(name=name,id=id)
        student.save()
        return HttpResponseRedirect('/logbook/')

    else:
        return render(request,'logbook_2/add_student.html')


