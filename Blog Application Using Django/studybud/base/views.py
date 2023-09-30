from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from .models import Room,User,Message
from .forms import RoomForm

# Create your views here.
# def homeapp(request):
#     return HttpResponse("App Home Page")
# rooms = [   # 1
#     {'id':1, 'name':'Jayesh'},
#     {'id':2, 'name':'Piyush'},
#     {'id':3, 'name':'Vinayak'},
#     {'id':4, 'name': 'Bharat'}
# ]

# def homeapp(request):  # 1
#     context = {'rooms':rooms}
#     return render(request,'base/home.html',context)

# def roomapp(request,pk):  # 1
#     room = None
#     for i in rooms:
#         if i['id']==int(pk):
#             room = i
#     context = {'room':room}
#     return render(request,'base/room.html',context)

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password') 
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User doesn't exist")
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        # else:
        #     messages.error(request,"username or password doest not match")
    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'something went wrong.')
    return render(request, 'base/login_register.html',{'page':page,'form':form})
    
def homeapp(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Room.objects.all()
    context = {'rooms':rooms,'topics':topics, 'room_count':room_count}
    return render(request,'base/home.html',context)

def roomapp(request,pk):
    room = Room.objects.get(id=pk)
    message_room = room.message_set.all().order_by('-created')
    if request.method == "POST":
        message = Message.objects.create(
            user = request.user,
            room = room,
            text = request.POST.get('comment')
        )
        return redirect('room', pk=room.id)
    context = {'room':room,"message_room":message_room}
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        print(request.POST)
    context = {'form':form}
    return render(request, 'base/room_form.html',context)

@login_required(login_url='login')
def deleteroom(request,pk):
    room = Room.objects.get(id=pk)
    if request.user!=room.host:
        return HttpResponse('You are not allowed here!!!')
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html',{'obj':room})

@login_required(login_url='login')
def updateroom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user!=room.host:
        return HttpResponse('You are not allowed here!!!')
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html',context)

