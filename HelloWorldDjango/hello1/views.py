from django.shortcuts import render
from django.shortcuts import HttpResponse
from hello1 import models


# Create your views here.

def index(request):
    # return HttpResponse("hello world!")
    # return render(request,"index.html")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
    return render(request, "index.html")


# user_list = [
# 	{"user":"liuhao","pw":"123456"},
# 	{"user":"liyang","pw":"654321"},
# ];
def userList(request):
    print("route userList")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # user = {"user":username,"pw":password}
        # user_list.append(user)
        print(username, password)
        # add
        models.UserInfo.objects.create(user=username, pw=password)
    # get
    user_list = models.UserInfo.objects.all()

    return render(request, "index2.html", {"data": user_list})
