from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from rolepermissions.roles import assign_role,get_user_roles
from .form import Form_add_user
from rolepermissions.admin import roles 


def user_add(request):

    if request.method == 'POST':
        form = Form_add_user(request.POST)

        print(form.as_p)

        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST.get('name'),
                email=request.POST.get('email'),
                password=request.POST.get('password')
            )
            user.save()
            assign_role(user,'funcionario')
            return redirect(user_list)
        else:
            return HttpResponse('ouve um erro ao criar usuario!')
    
    form = Form_add_user()
    return render(request, "user_add.html", {"form": form})

def user_rem(request,id):
        user = User.objects.get(id=id)
        user.delete()
        users = User.objects.all()
        return render(request, "user_index.html",{"users":users})


def user_update(request):
    pass

def user_list(request):
        users = User.objects.all()
      
        return render(request, "user_index.html",{"users":users})
