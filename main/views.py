from django.shortcuts import render,HttpResponse,redirect
import string,random
from main.forms import shorten
from main.models import path
from django.urls import resolve

# Create your views here.
def home(request):
    form=shorten(request.POST)
    # fo=path.objects.exclude(url="h")
    if request.method=="POST":
        # while(assign(form)):
        ran= assign(form)
        full= "127.0.0.1:8000/" + ran
        return render(request,"result.html",{'full':full})
    else:
        return render(request,"main.html",{'form':form})

def assign(form):
    # global ran
    ran=random_generator()
    check=path.objects.filter(url_short=ran)
    if check:
        return True
    else:
        temp=form.save(commit=False)
        temp.url_short=ran
        temp.save()
        return ran

def random_generator(size=5, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase ):
    return ''.join(random.choice(chars) for x in range(size))

def redir(request,shrt):
    form=path.objects.filter(url_short=shrt)
    if form:
        temp=form[0].url
        return redirect(temp)
    else:
        return HttpResponse("Invalid Url,Check again")