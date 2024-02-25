from django.shortcuts import render

from myapp.models import contact, register


# Create your views here.

def real(request):
    return render(request, "index.html")

def aboutpage(request):
    return render(request, "about.html")

def registerdata(request):
    return render(request, "register.html")

def contactpage(request):
    return render(request, "contact.html")

def storedata(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        comment = request.POST.get("comment")

        insertdata = contact(fname=fname, lname=lname, email=email, comment=comment)
        insertdata.save()

        return render(request, "index.html")
    return render(request, "contact.html")

def registerdata(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        cpwd = request.POST.get("cpwd")

        insertdata = register(Name=Name, email=email, pwd=pwd, cpwd=cpwd)
        insertdata.save()

        return render(request, "index.html")
    return render(request, "register.html")