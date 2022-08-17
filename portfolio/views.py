from django.shortcuts import render,redirect
from .models import Person


# Create your views here.
def loadhtml(request):
    return render(request, "index.html")

def savedata (request):
    if request.POST:
        pname = request.POST['Name']
        pemail = request.POST['Email']
        psubject = request.POST['Subject']
        pmessage = request.POST['Message']
        obj = Person(Name=pname, Email=pemail, Subject=psubject, Message=pmessage)
        obj.save()
    return redirect('/#')    
